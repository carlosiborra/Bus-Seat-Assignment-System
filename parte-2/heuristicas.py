""" Archivo para calcular el las distintas heurísticas """

# Importamos las librerías necesarias
import re


def select_heuristic(heuristic: int, cola_restante) -> callable:
    """ Función que devuelve la heurística seleccionada """
    if heuristic == 1:
        return heuristica1(cola_restante)
    elif heuristic == 2:
        return heuristica2(cola_restante)
    elif heuristic == 3:
        return heuristica3(cola_restante)
    elif heuristic == 4:
        return heuristica4(cola_restante)
    elif heuristic == 5:
        return heuristica5(cola_restante)
    else:
        return heuristica1(cola_restante)


def heuristica1(cola_restante) -> callable:
    """ Función heurística que devuelve 1 para forzar fuerza bruta y por tanto aplicar Dijkstra """
    if cola_restante == []:
        return 0
    return 1


def heuristica2(cola_restante) -> callable:
    """ Función heurística que devuelve el número de alumnos que quedan por subir al autobús """
    return len(cola_restante)


def heuristica3(cola_restante) -> callable:
    """ Función heurística que aplica un coste de 2 a los alumnos que tienen movilidad reducida """
    # Además, los alumnos conflictivos tienen un coste de 0.5 y así se fomenta que suban los últimos
    conflictivos, reducida, normales = 0, 0, 0
    # Prevalece el coste de alumnos conflictivos, ya que si hay un alumno conflictivo y de mov. red
    # se le aplica el coste de conflictivo; esto es, para forzar que se suban lo más tarde posible
    for alumno in cola_restante:
        if re.match(r'\d*C\w', alumno[0]):
            conflictivos += 1
        elif re.match(r'\d*\wR', alumno[0]):
            reducida += 1
        else:
            normales += 1
    coste = 0.5*conflictivos + 2*reducida + normales
    print(
        f'Conflictivos: {conflictivos}, Reducida: {reducida},  Normales: {normales}, Coste: {coste}')
    return coste


def heuristica4(cola_restante) -> callable:
    """ Función heurística que aplica un coste de 2 a los alumnos que tienen movilidad reducida """
    # Los conflictivos tienen un coste de 0.1 y así se fomenta que suban los últimos
    conflictivos, reducida, normales = 0, 0, 0
    # Prevalece el coste de alumnos conflictivos, ya que si hay un alumno conflictivo y de mov. red
    # se le aplica el coste de conflictivo; esto es, para forzar que se suban lo más tarde posible
    for alumno in cola_restante:
        if re.match(r'\d*C\w', alumno[0]):
            conflictivos += 1
        elif re.match(r'\d*\wR', alumno[0]):
            reducida += 1
        else:
            normales += 1
    coste = 0.1*conflictivos + 2*reducida + normales
    print(
        f'Conflictivos: {conflictivos}, Reducida: {reducida},  Normales: {normales}, Coste: {coste}')
    return coste


def heuristica5(cola_restante) -> callable:
    """ Función heurística que aplica un coste de 2 a los alumnos que tienen movilidad reducida """
    # Los conflictivos tienen un coste de 0.9, para hacer de esta heurística más informada,
    # pese que no forzará de tanto que estos suban los últimos al bus
    conflictivos, reducida, normales = 0, 0, 0
    # Prevalece el coste de alumnos conflictivos, ya que si hay un alumno conflictivo y de mov. red
    # se le aplica el coste de conflictivo; esto es, para forzar que se suban lo más tarde posible
    for alumno in cola_restante:
        if re.match(r'\d*C\w', alumno[0]):
            conflictivos += 1
        elif re.match(r'\d*\wR', alumno[0]):
            reducida += 1
        else:
            normales += 1
    coste = 0.9*conflictivos + 2*reducida + normales
    print(
        f'Conflictivos: {conflictivos}, Reducida: {reducida},  Normales: {normales}, Coste: {coste}')
    return coste
