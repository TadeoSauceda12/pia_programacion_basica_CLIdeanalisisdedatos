 #Pia de Tadeo Sauceda Flores por que su equipo no se puso deacuerdo
import pandas as pd
import matplotlib.pyplot as plt
import os


def cargar_csv(ruta_csv):
    """Carga un archivo CSV y valida su contenido."""
    if not os.path.exists(ruta_csv):
        print(f"\n El archivo '{ruta_csv}' no existe.")
        return None
    
def cargar_archivo_csv(path_archivo):
    """Carga y valida el archivo CSV."""
    if not os.path.exists(path_archivo):
        print("El archivo no existe.")
        return None
    try:
        df = pd.read_csv(path_archivo)
        # Validar columnas requeridas
        columnas_requeridas = {"fecha", 'monto', 'categoria'}
        if not columnas_requeridas.issubset(df.columns):
            print("El archivo no contiene las columnas necesarias: fecha, monto, categoria")
            return None
        return df
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return None

def analizar_ingresos(df):
    """Analiza ingresos totales, mayor y menor."""
    ingresos_totales = df['monto'].sum()
    ingreso_mayor = df['monto'].max()
    ingreso_menor = df['monto'].min()

    print("=== INFORME DE INGRESOS ===")
    print(f"Ingreso total: ${ingresos_totales}")
    print(f"Ingreso mayor: ${ingreso_mayor}")
    print(f"Ingreso menor: ${ingreso_menor}")

    return ingresos_totales, ingreso_mayor, ingreso_menor

def graficar_por_categoria(df, nombre_archivo='ingresos_por_categoria.png'):
    """Genera una gráfica de pastel por categoría."""
    resumen = df.groupby('categoria')['monto'].sum()
    plt.figure(figsize=(8, 6))
    resumen.plot(kind='pie', autopct='%1.1f%%')
    plt.title("Distribución de ingresos por categoría")
    plt.ylabel("")  # Quita etiqueta del eje Y
    plt.tight_layout()
    plt.savefig(nombre_archivo)
    plt.close()
    print(f"Gráfica guardada como {nombre_archivo}")


def graficar_por_dia(df):
    """Genera una gráfica de barras de montos por día."""
    try:
        # Asegurarse de que la columna 'Fecha' está en formato datetime
        df["fecha"] = pd.to_datetime(df["fecha"], errors='coerce', dayfirst=True)
        df = df.dropna(subset=["fecha", "monto"])

        # Agrupar por día y sumar montos
        resumen_diario = df.groupby(df["fecha"].dt.date)["monto"].sum()

        # Crear gráfico de barras
        resumen_diario.plot(kind='bar', figsize=(10, 5), color="skyblue")
        plt.title("Montos por Día")
        plt.xlabel("Fecha")
        plt.ylabel("Monto Total")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig("Grafica de Barras.png")
        plt.show()
        print("Gráfica guardada como Grafica de Barras.png ")

    except Exception as e:
        print(f" No se pudo generar la gráfica diaria: {e}")


def convertir_a_excel(df, nombre_archivo='ingresos_convertido.xlsx'):
    """Convierte el DataFrame a un archivo Excel."""
    try:
        df.to_excel(nombre_archivo, index=False)
        print(f"Archivo convertido y guardado como '{nombre_archivo}'")
    except Exception as e:
        print(f"No se pudo convertir a Excel: {e}")

def ordenar_por_fecha(df, descendente=False):
    """Ordena el DataFrame por la columna 'Fecha'."""
    try:
        df['fecha'] = pd.to_datetime(df['fecha'], format="%d/%m/%Y")
        df_ordenado = df.sort_values(by='fecha', ascending=not descendente)
        print("\nDatos ordenados por fecha:")
        print(df_ordenado)
        return df_ordenado
    except Exception as e:
        print(f"No se pudo ordenar por fecha: {e}")
        return df
def ordenar_por_monto(df, descendente=True):
    """Ordena el DataFrame por la columna 'Monto'."""
    try:
        df_ordenado = df.sort_values(by='monto', ascending=not descendente)
        print("\nDatos ordenados por monto:")
        print(df_ordenado)
        return df_ordenado
    except Exception as e:
        print(f"No se pudo ordenar por monto: {e}")
        return df
def guardar_como_csv(df, nombre_archivo="ingresos_ordenados.csv"):
    """Guarda el DataFrame en un nuevo archivo CSV."""
    try:
        df.to_csv(nombre_archivo, index=False, encoding='utf-8-sig')
        print(f"\nArchivo guardado exitosamente como: {nombre_archivo}")
    except Exception as e:
        print(f"Error al guardar el archivo CSV: {e}")


#ruta_csv = "ing.csv"
def main():
    ruta_csv= input("ingrese el nombre del archivo csv: ")
    df_ingresos = cargar_archivo_csv(ruta_csv)
    if df_ingresos is not None:
        analizar_ingresos(df_ingresos)
        graficar_por_categoria(df_ingresos)
        graficar_por_dia(df_ingresos)
        convertir_a_excel(df_ingresos)
        # Pregunta al usuario si quiere ordenar
        eleccion = input("\n¿Deseas ordenar los datos por (1) Fecha o (2) Monto? (0 para omitir): ")

        if eleccion == '1':
            orden_fecha = input("¿Orden descendente? (s/n): ").lower() == 's'
            df_ordenado = ordenar_por_fecha(df_ingresos, descendente=orden_fecha)
            guardar = input("\n¿Deseas guardar este archivo ordenado como un nuevo CSV? (s/n): ").lower()
            if guardar == 's':
                nombre = input("Indica el nombre para el nuevo archivo (sin .csv): ")
                guardar_como_csv(df_ordenado, nombre + ".csv")
        elif eleccion == '2':
            orden_monto = input("¿Orden descendente (mayor a menor)? (s/n): ").lower() == 's'
            df_ordenado = ordenar_por_monto(df_ingresos, descendente=orden_monto)
            guardar = input("\n¿Deseas guardar este archivo ordenado como un nuevo CSV? (s/n): ").lower()
            if guardar == 's':
                nombre = input("Indica el nombre para el nuevo archivo (sin .csv): ")
                guardar_como_csv(df_ordenado, nombre + ".csv")

if __name__ == "__main__":
    main()