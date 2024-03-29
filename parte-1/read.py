""" read.py by 100451170 & 100451258 """

# Importamos la librería csv
import csv

def read_input(path: str) -> list:
    """ Lee el archivo .csv y devuelve una lista de listas con los datos de los alumnos """
    with open(path, newline='', encoding="utf8") as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        data = []
        for row in reader:
            data.append(row)
    return data
