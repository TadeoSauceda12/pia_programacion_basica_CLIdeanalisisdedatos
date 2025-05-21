import csv
import random
from datetime import datetime, timedelta

def generar_csv(path_archivo, num_filas=10):
    encabezados = ['fecha', 'monto', 'categoria']
    categorias = ['comida', 'transporte', 'salud', 'entretenimiento', 'otros']
    with open(path_archivo, mode='w', newline='', encoding='utf-8') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(encabezados)

        for _ in range(num_filas):
            dias_aleatorios = random.randint(0, 365 * 3)
            fecha = (datetime.today() - timedelta(days=dias_aleatorios)).strftime('%d/%m/%Y')
            monto = round(random.uniform(1.0, 1000.0), 2)
            categoria = random.choice(categorias)
            escritor.writerow([fecha, monto, categoria])
    print(f"Archivo generado exitosamente en: {path_archivo}")
generar_csv("datos_ejemplo.csv", num_filas=20)

