""" write.py by 100451170 & 100451258 """

# Se pretende devolver una solución al archivo indicado en el formato indicado
import csv

# Crear un nuevo archivo .csv con los resultados
def write(path: str, data: list) -> None:
    """ Escribe en el archivo .csv la solución obtenida """
    with open(path, 'w', newline='', encoding="utf8") as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        for row in data:
            writer.writerow(row)
