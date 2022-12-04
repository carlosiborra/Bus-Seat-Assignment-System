""" functions.py by 100451170 & 100451258 """
from random import randint
import data

# Importamos las listas con los dominios de las variables
dominio_primer_ciclo = data.dominio_primer_ciclo
dominio_segundo_ciclo = data.dominio_segundo_ciclo
dominio_movilidad_reducida = data.dominio_movilidad_reducida
# Se podría importar lista_alumnos pero daría un error de importación circular

# ! -------------------------------------------------------------------
# ! FUNCIONES PARA LA GENERACIÓN DE DOMINIOS
# ! -------------------------------------------------------------------

# Al final los alumnos solo puede pertenecer al ciclo 1 o al ciclo 2
# Por tanto, carece de sentido añadir más dominios si ya se restringirá mas adelante
# No habrá tanto coste computacional como el acceso repetido a un array de arrays grande


def ciclo_alumno(lista_alumnos, estudiante, alumnos_primer_ciclo, alumnos_segundo_ciclo) -> list:
    """ Obtenemos el ciclo al que pertenece el alumno y le asignamos el dominio """
    # Si los hermanos están en distintos ciclos, se irán al ciclo 1
    if estudiante[4] != '0' and lista_alumnos[int(estudiante[4])-1][1] != estudiante[1]:
        alumnos_primer_ciclo.append(estudiante[0])
        return dominio_primer_ciclo
    # En cambio, si no tienen hermanos o estos tienen el mismo ciclo, se irán a su ciclo
    if estudiante[1] == '1':
        # Añadimos el alumno a la lista de alumnos del primer ciclo
        alumnos_primer_ciclo.append(estudiante[0])
        return dominio_primer_ciclo
    alumnos_segundo_ciclo.append(estudiante[0])
    return dominio_segundo_ciclo


def movilidad_alumno(estudiante, dom, alumnos_movilidad_reducida) -> list:
    """ Si el alumno tiene movilidad reducida, le asignamos el resultado del dominio """
    if estudiante[3] == 'R':
        # Creamos un nuevo dominio de la conjunción del dominio activo y el de movilidad reducida
        alumnos_movilidad_reducida.append(estudiante[0])
        return [x for x in dom if x in dominio_movilidad_reducida]
    return dom


def conflictivo(estudiante, alumnos_conflictivos):
    """ Si el alumno es conflictivo, lo añadimos a la lista de conflictivos """
    if estudiante[2] == 'C':
        alumnos_conflictivos.append(estudiante[0])


def hermano(estudiante, alumnos_hermanos):
    """ Si el alumno tiene hermanos, los añadimos a la lista de hermanos """
    if estudiante[4] != '0':
        # Añadimos un array con el id del alumno y el id de su hermano
        alumnos_hermanos.append([estudiante[0], estudiante[4]])


# ! -------------------------------------------------------------------
# ! FUNCIONES PARA LAS SOLUCIONES FINALES
# ! -------------------------------------------------------------------


def obtain_sol(lista_alumnos, soluciones, solucion_init, num_soluciones):
    """ Obtenemos 10 soluciones distintas y aleatorias (9) del total de las soluciones """
    rand_sol = []
    # La primera solución será la dada por get_solution 
    solucion_pars = parse_sol(lista_alumnos, solucion_init)
    rand_sol.append(solucion_pars)
    print(f"Solución particular {0}: {solucion_pars}")
    for i in range(9):
        # Pasamos el len de soluciones como parámetro para no repetir cálculos innecesarios
        solucion = soluciones[randint(0, num_soluciones-1)]
        solucion_pars = parse_sol(lista_alumnos, solucion)
        rand_sol.append(solucion_pars)
        print(f"Solución aleatoria {i+1}:  {solucion_pars}")
    return rand_sol


def parse_sol(lista_alumnos, solucion_in):
    """ Parseamos la solución para que sea de la forma: {'3XX': (1, 1), '1CX': (1, 2), ...} """
    # Creamos un diccionario vacío
    solution_parsed = {}
    # Recorremos el diccionario e insertamos sus tuplas
    try:
        for key, value in solucion_in.items():
            # Cambiamos la key al formato: '3CR'
            key = key + str(lista_alumnos[int(key)-1][2]) +\
                str(lista_alumnos[int(key)-1][3])
            # El ciclo 1 va de la posición 1 a la 16, el ciclo 2 de la 17 a la 32
            posicion = value[0]*4 + (value[1]+1)
            solution_parsed[key] = posicion
        # Ordenamos el diccionario por la posición
        solution_parsed = dict(
            sorted(solution_parsed.items(), key=lambda item: item[1]))
        return solution_parsed
    except Exception as exception:
        print(f'No hay solución: {exception}')
        return "{None}"
