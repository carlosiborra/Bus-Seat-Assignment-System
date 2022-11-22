#!/ usr / bin / env python
# -*- coding: utf-8 -*-

""" importing libraries """
from constraint import *

# Importing the necessary modules
import data
import read

# Definición de una variable3 como nuestro problema de CSP
problem = Problem()

# Importamos las listas con los dominios de las variables
dominio_movilidad_reducida = data.dominio_movilidad_reducida
dominio_sin_movilidad_reducida = data.dominio_sin_movilidad_reducida
dominio_primer_ciclo = data.dominio_primer_ciclo
dominio_segundo_ciclo = data.dominio_segundo_ciclo

# Creamos listas donde se almacenarán las variables (alumnos)
alumnos_movilidad_reducida = []
alumnos_segundo_ciclo = []
alumnos_primer_ciclo = []
alumnos_conflictivos = []
alumnos_hermanos = []
alumnos_id = []

# TODO: Lo mismo tenemos que hacer una lista con los id de los alumnos existentes

# Leemos el archivo .csv y lo guardamos en una lista de listas
lista_alumnos = read.read("parte-1/CSP-tests/test0/test0.txt")
