#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" importing libraries """
import sys
from random import randint
from constraint import *


# Importamos los modulos necesarios
import data
from read import read_input
from write import write_result
from functions import ciclo_alumno, movilidad_alumno
from functions import conflictivo, hermano
from functions import obtain_sol


# ? Antes de nada, obtenemos el argumento (path) pasado por consola
def command_prompt():
    """ Obtenemos el argumento (path) pasado por consola """
    if len(sys.argv) < 2 or len(sys.argv) > 2:
        print("Error: Se necesita un argumento (el path al test)")
        sys.exit(1)
    return f"{sys.argv[1]}"


# ? Leemos el archivo .csv y lo guardamos en un array de arrays
# Los path pueden estar en formato ./parte-1/CSP-tests/alumnos00 o .\\parte1\\CSP-tests\\alumnos00
def read_path(path="./parte-1/CSP-tests/alumnos00") -> list:
    """ Leemos el archivo .csv y lo guardamos en una lista de listas """
    return read_input(path)

# Guardamos como variable el array de arrays
lista_alumnos = read_path(str(command_prompt()))

# Definición de una variable3 como nuestro problema de CSP
problem = Problem()

# Importamos las listas con los dominios de las variables
dominio_movilidad_reducida = data.dominio_movilidad_reducida
dominio_sin_movilidad_reducida = data.dominio_sin_movilidad_reducida
dominio_primer_ciclo = data.dominio_primer_ciclo
dominio_segundo_ciclo = data.dominio_segundo_ciclo

# TODO: eliminar las listas no usadas
# Creamos listas donde se almacenarán las variables (alumnos)
alumnos_movilidad_reducida = []
alumnos_segundo_ciclo = []
alumnos_primer_ciclo = []
alumnos_conflictivos = []
alumnos_hermanos = []


# ! -------------------------------------------------------------------
# ! CREAMOS LAS VARIABLES
# ! -------------------------------------------------------------------

# Se llamarán a las funciones anteriores para ir restringiendo los dominios

for i, alumno in enumerate(lista_alumnos):
    print(f'alumno{i+1}', alumno)
    dominio = []

    # Comprobamos si el alumno pertenece al primer ciclo o al segundo ciclo
    # Si el alumno tiene hermanos, entonces puede que vayan juntos en otro ciclo
    dominio = ciclo_alumno(lista_alumnos, alumno,
                           alumnos_primer_ciclo, alumnos_segundo_ciclo)

    # Si el alumno tiene movilidad reducida, acotamos sus asientos
    dominio = movilidad_alumno(alumno, dominio, alumnos_movilidad_reducida)

    # Si el alumno es conflictivo, lo añadimos a la lista de conflictivos
    conflictivo(alumno, alumnos_conflictivos)

    # Si el alumno tiene hermanos, los añadimos a la lista de hermanos
    hermano(alumno, alumnos_hermanos)

    print(f'estudiante{alumno[0]}', dominio)
    problem.addVariable(f'{alumno[0]}', dominio)


print(f"\nAlumnos primer ciclo: {alumnos_primer_ciclo}")
print(f"Alumnos segundo ciclo: {alumnos_segundo_ciclo}")
print(f"Alumnos con mov. reducida: {alumnos_movilidad_reducida}")
print(f"Alumnos conflictivos: {alumnos_conflictivos}")
print(f"Alumnos hermanos: {alumnos_hermanos}\n")


# ! -------------------------------------------------------------------
# ! CREAMOS LAS RESTRICCIONES
# ! -------------------------------------------------------------------

# Separamos la creación de las restricciones en funciones para facilitar su lectura y mantenimiento

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
# Y en caso de que sobrasen asientos de mov. reducida, podrían sentarse alumnos sin mov. reducida


# ? 4. Alumnos conflictivos no pueden setarse cerca de ningun otro conflictivo ni con mov reducida
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
        # Si son dos alumnos conflictivos o uno es conflictivo y el otro mov.reducida
        # Excepto si son hermanos, que no han de cumplir estas restricciones
        if ((alumnoA[0] in alumnos_conflictivos and alumnoB[0] in alumnos_conflictivos) or
                (alumnoA[0] in alumnos_conflictivos and alumnoB[0] in alumnos_movilidad_reducida) or
                (alumnoA[0] in alumnos_movilidad_reducida and alumnoB[0] in alumnos_conflictivos)) and \
                (alumnoA[0] != alumnoB[0]) and \
                ((alumnoA[4] != alumnoB[0]) and (alumnoB[4] != alumnoA[0])):
            print(
                f'Conflictividad {alumnoA[0]}, {alumnoB[0]}, {alumnos_conflictivos}')
            problem.addConstraint(
                conflictivos, (f'{alumnoA[0]}', f'{alumnoB[0]}'))


# ? 5. Alumnos hermanos han de sentarse juntos
# Cuando decimos juntos, hay que tener en cuenta el pasillo, situado entre el j 1 y el j 2
# Si un alumno esta en la columna 1, el otro no puede estar en la 2
def hermanos(posicion_alumnoA, posicion_alumnoB):
    """ Si dos alumnos son hermanos, tienen que sentarse juntos """
    if (posicion_alumnoA[0] == posicion_alumnoB[0]) and \
            (posicion_alumnoA[1] == posicion_alumnoB[1]-1 or
             posicion_alumnoA[1] == posicion_alumnoB[1]+1) and \
            (posicion_alumnoA[1]+1, posicion_alumnoB[1]) != 2 and \
            (posicion_alumnoB[1]+1, posicion_alumnoA[1]) != 2 and \
            (posicion_alumnoA[1]-1, posicion_alumnoB[1]) != 1 and \
            (posicion_alumnoB[1]-1, posicion_alumnoA[1]) != 1:
        return True
    return False


# Si uno de ellos tuvise mov reducida, deberían estar en el mismo ciclo, no asientos contiguos
def hermanos_reducida(posicion_alumnoA, posicion_alumnoB):
    """ Si dos alumnos son hermanos, tienen que sentarse en el mismo ciclo """
    if (posicion_alumnoA[0] <= 3 and posicion_alumnoB[0] <= 3) or \
            (posicion_alumnoA[0] >= 4 and posicion_alumnoB[0] >= 4):
        return True
    return False


# Si tienen != ciclos, constraint para que el mayor esté al lado del pasillo
def hermanos_pasillo(posicion_hermano_mayor):
    """ Si dos hermanos, != ciclos, el mayor (alumno entrante) debe estar pegado al pasillo """
    # El mayor ha de estar en la columna 1 o 2 (pegado al pasillo)
    # Que el menor haya de estar al lado del mayor en la (ventana), lo hace el constraint hermanos
    if posicion_hermano_mayor[1] == 1 or posicion_hermano_mayor[1] == 2:
        return True
    return False


# Creamos las restricciones de los hermanos
for i, alumnoA in enumerate(lista_alumnos):
    for j, alumnoB in enumerate(lista_alumnos):
        # Si son dos alumnos hermanos y no son el mismo, irán juntos
        if ((alumnoA[4] == alumnoB[0]) and (alumnoB[4] == alumnoA[0])) and \
                (alumnoA[0] != alumnoB[0]):
            print(
                f'Hermanos {alumnoA[0]}, {alumnoB[0]}, {alumnos_hermanos}')
            # Si uno de ellos tiene movilidad reducida, se sientan en el mismo ciclo
            if (alumnoA[0] in alumnos_movilidad_reducida) or\
                    (alumnoB[0] in alumnos_movilidad_reducida):
                problem.addConstraint(
                    hermanos_reducida, (f'{alumnoA[0]}', f'{alumnoB[0]}'))

            # Si no, han de estar juntos
            else:
                problem.addConstraint(
                    hermanos, (f'{alumnoA[0]}', f'{alumnoB[0]}'))

                # Si tienen != ciclos, constraint para que el mayor esté al lado del pasillo
                # Siempre que no hayan hermanos de mov. reducida
                if alumnoA[1] != alumnoB[1]:
                    # Si el mayor es el alumno A (este pertece al ciclo 2)
                    if alumnoA[1] > alumnoB[1]:
                        problem.addConstraint(
                            hermanos_pasillo, (f'{alumnoA[0]}'))
                    # Si el alumno B es el mayor (este pertece al ciclo 2)
                    else:
                        problem.addConstraint(
                            hermanos_pasillo, (f'{alumnoB[0]}'))


# ! -------------------------------------------------------------------
# ! EXPORTAMOS LAS SOLUCIONES
# ! -------------------------------------------------------------------

# Obtenemos una solución
# Creamos una función para para cambiar el formato de la solución
# {’3XX’: 11, ’1CX’: 12, ’6XX’: 15, ’5XX’: 16, ’8XR’: 18, ’4CR’: 20, ’2XX’: 31, ’7CX’: 32}

# Obtenemos todas las soluciones posibles y su número
soluciones = problem.getSolutions()
num_soluciones = len(soluciones)
res_num_soluciones = f"Número de soluciones: {num_soluciones}"
print(f"\nNúmero de soluciones: {num_soluciones}")

# Obtenemos tres soluciones distintas y aleatorias de todas las soluciones posibles
# Parseamos todas las soluciones y las guardamos (obtain_sol llama a la función parse_solution)
# Hacer que se guarden las 3 variables
rand_sol = obtain_sol(lista_alumnos, soluciones, num_soluciones)

# Función para exportar el resultado
# Esta ha de tener el mismo path y nombre pero acabado en .output
write_result(str(command_prompt()) + '.output', res_num_soluciones, rand_sol)
