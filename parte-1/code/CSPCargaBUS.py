#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" importing libraries """
from constraint import *

# Importamos los modulos necesarios
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
lista_alumnos = read.read("parte-1/CSP-tests/test1/test1.txt")


# Al final los alumnos solo puede pertenecer al ciclo 1 o al ciclo 2
# Por tanto, carece de sentido añadir más dominios
# Guardaremos los elementos relevantes de cada alumno en un array, así:
# No habrá tanto coste computacional como el acceso repetido a un array de arrays grande

def id_alumno(estudiante):
    """ Añadimos el id del alumno a la lista de id's """
    alumnos_id.append(estudiante[0])


def ciclo_alumno(estudiante):
    """ Obtenemos el ciclo al que pertenece el alumno y le asignamos el dominio """
    if estudiante[1] == '1':
        # Añadimos el alumno a la lista de alumnos del primer ciclo
        alumnos_primer_ciclo.append(estudiante[0])
        return dominio_primer_ciclo
    alumnos_segundo_ciclo.append(estudiante[0])
    return dominio_segundo_ciclo


def movilidad_alumno(estudiante, dom):
    """ Si el alumno tiene movilidad reducida, le asignamos el resultado del dominio """
    if estudiante[3] == 'R':
        # Creamos un nuevo dominio de la conjunción del dominio activo y el de movilidad reducida
        alumnos_movilidad_reducida.append(estudiante[0])
        return [x for x in dom if x in dominio_movilidad_reducida]
    return dom


def conflictivo(estudiante):
    """ Si el alumno es conflictivo, lo añadimos a la lista de conflictivos """
    if estudiante[2] == 'C':
        alumnos_conflictivos.append(estudiante[0])


def hermano(estudiante):
    """ Si el alumno tiene hermanos, los añadimos a la lista de hermanos """
    if estudiante[4] != '0':
        # Añadimos un array con el id del alumno y el id de su hermano
        alumnos_hermanos.append([estudiante[0], estudiante[4]])


for i, alumno in enumerate(lista_alumnos):
    print(f'alumno{i+1}', alumno)
    dominio = []

    # Comprobamos si el alumno pertenece al primer ciclo o al segundo ciclo
    dominio = ciclo_alumno(alumno)

    # Si el alumno tiene movilidad reducida, acotamos sus asientos
    dominio = movilidad_alumno(alumno, dominio)
    print(f'dominio{i+1}', dominio)

    # Si el alumno es conflictivo, lo añadimos a la lista de conflictivos
    conflictivo(alumno)

    # Si el alumno tiene hermanos, los añadimos a la lista de hermanos
    hermano(alumno)
    print(f'hermanos{i+1}', alumnos_hermanos)

    print(f'estudiante{alumno[0]}', dominio)
    problem.addVariable(f'{alumno[0]}', dominio)


# ! RESTRICCIONES

# ? 1. Todo el alumnado tiene que tener asignado un asiento y solo uno
problem.addConstraint(AllDifferentConstraint())


# ? 2. Alumnos con movilidad reducida, libre el asiento de al lado
def mov_reducida(posicion_alumnoR, posicion_alumnoX):
    """ Si un alumno tiene movilidad reducida, asiento de al lado libre """
    # Tendremos que tener en cuenta si el alumno está o no al lado del pasillo
    # También tendremos que tener en cuenta el eje j (columnas)
    # Casos posibles:
    # a. El alumno con mov.reducida está en el lateral izquierdo
    # b. El alumno está pegado al pasillo (izquierda)
    # c. El alumno está pegado al pasillo (derecha)
    # d. El alumno con mov.reducida está en el lateral derecho
    if ((posicion_alumnoR[1] == 0 and (posicion_alumnoR[1]+1 == posicion_alumnoX[1])) and
            (posicion_alumnoR[0] == posicion_alumnoX[0])) or \
        ((posicion_alumnoR[1] == 1 and (posicion_alumnoR[1]-1 == posicion_alumnoX[1])) and
            (posicion_alumnoR[0] == posicion_alumnoX[0])) or \
        ((posicion_alumnoR[1] == 2 and (posicion_alumnoR[1]+1 == posicion_alumnoX[1])) and
            (posicion_alumnoR[0] == posicion_alumnoX[0])) or \
        ((posicion_alumnoR[1] == 3 and (posicion_alumnoR[1]-1 == posicion_alumnoX[1])) and
            (posicion_alumnoR[0] == posicion_alumnoX[0])):
        return False
    return True


# Creamos las restricciones de movilidad reducida
for i, alumnoA in enumerate(lista_alumnos):
    for j, alumnoB in enumerate(lista_alumnos):
        # print(f'({alumnoA[0]},{alumnoB[0]})')
        # TODO: tiene sentido que sean dos if o por el contrario es mejor ejecutar un elif?
        # TODO: Lo mismo no hace falta separar los dos if
        # Si el alumno movilidad reducida es el A, B no puede sentarse a su lado
        if (alumnoA[0] in alumnos_movilidad_reducida) and (alumnoA[0] != alumnoB[0]):
            # print(f'A {alumnoA[0]}, {alumnoB[0]}, {alumnos_movilidad_reducida}')
            problem.addConstraint(
                mov_reducida, (f'{alumnoA[0]}', f'{alumnoB[0]}'))
        # Si el alumno con movilidad reducida es el B, A no puede sentarse a su lado
        if (alumnoB[0] in alumnos_movilidad_reducida) and (alumnoA[0] != alumnoB[0]):
            # print(f'B {alumnoA[0]}, {alumnoB[0]}, alumnos con mov.reducida: {alumnos_movilidad_reducida}')
            problem.addConstraint(
                mov_reducida, (f'{alumnoB[0]}', f'{alumnoA[0]}'))


# ? 3. Un asiento de personas con mov reducida, si no hay, pueden personas sin mov reducida
# Ya se hace ya que los los alumnos sin mov. reducida -> dominio con todos los asientos de su ciclo


# ? 4. Alumnos conflictivos no pueden setarse cerca de ningun otro conflictivo ni de mov reducida
# TODO: No se tienen en cuenta las puertas, no? según lo visto en el enunciado
# Cuando se dice cerca, es que no pueden estar alrededor de ellos
def conflictivos(posicion_alumnoA, posicion_alumnoB):
    """ Si un alumno tiene movilidad reducida, asiento de al lado libre """
    # No habrá ninguno alrededor de ellos, siguiendo el orden:
    # Arriba izda, arriba, arriba dcha, izda, dcha, abajo izda, abajo, abajo dcha
    if (posicion_alumnoA[0]-1, posicion_alumnoA[1]-1) == posicion_alumnoB or \
            (posicion_alumnoA[0]-1, posicion_alumnoA[1]) == posicion_alumnoB or \
            (posicion_alumnoA[0]-1, posicion_alumnoA[1]+1) == posicion_alumnoB or \
            (posicion_alumnoA[0], posicion_alumnoA[1]-1) == posicion_alumnoB or \
            (posicion_alumnoA[0], posicion_alumnoA[1]+1) == posicion_alumnoB or \
            (posicion_alumnoA[0]+1, posicion_alumnoA[1]-1) == posicion_alumnoB or \
            (posicion_alumnoA[0]+1, posicion_alumnoA[1]) == posicion_alumnoB or \
            (posicion_alumnoA[0]+1, posicion_alumnoA[1]+1) == posicion_alumnoB:
        return False
    return True


# Creamos las restricciones de conflictividad
for i, alumnoA in enumerate(lista_alumnos):
    for j, alumnoB in enumerate(lista_alumnos):
        # TODO: tiene sentido que sean dos if o por el contrario es mejor ejecutar un elif?
        # Si son dos alumnos conflictivos o uno es conflictivo y el otro mov.reducida
        if ((alumnoA[0] in alumnos_conflictivos and alumnoB[0] in alumnos_conflictivos) or
                (alumnoA[0] in alumnos_conflictivos and alumnoB[0] in alumnos_movilidad_reducida) or
                (alumnoA[0] in alumnos_movilidad_reducida and alumnoB[0] in alumnos_conflictivos)) and \
                (alumnoA[0] != alumnoB[0]):
            print(
                f'Conflictividad {alumnoA[0]}, {alumnoB[0]}, {alumnos_conflictivos}')
            problem.addConstraint(
                conflictivos, (f'{alumnoA[0]}', f'{alumnoB[0]}'))


# ! DEVOLVEMOS LAS SOLUCIONES
# Obtenemos una solución
# TODO: hay que transformar e insertar en otro archivo la solución
# ! ha de impimirse en el formato: {’3XX’: 11, ’1CX’: 12,
# ! ’6XX’: 15, ’5XX’: 16, ’8XR’: 18, ’4CR’: 20, ’2XX’: 31, ’7CX’: 32}
solution = problem.getSolution()
print(solution)
# Obtenemos todas las soluciones
# solutions = problem.getSolutions()
# print(solutions)

# TODO: meter las funciones de las restricciones en el archivo de constraints.py


#  NOTA, PARA QUE FUNCIONE LA RESTRICCION DE LOS HERMANOS, SOLO TENDREMOS QUE AÑADIRLOS COMO RESTRICCIONES EN LOS IF DE LAS DEMAS RESTRICCIONES
