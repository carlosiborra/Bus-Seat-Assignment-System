#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" importing libraries """
import re


dict_posiciones = {'4XR': 2, '3XR': 16, '2XR': 18, '1XR': 20}


class Estado():
    """ Clase de los nodos para el algoritmo A* """

    def __init__(self, padre=None, identifier=None, g=0, h=0):
        """Constructor de la clase nodo"""
        self.identifier = identifier
        self.conflict = conflict
        self.reduc = reduc
        self.padre = padre
        self.heur = g
        self.coste = h
        self.coste_f = self.coste + self.heur  # f(n) = g(n) + h(n)


def heuristica1(estado, alumno, open_list, closed_list) -> callable:
    """ Función heurística que devuelve el número de alumnos que quedan por subir al autobús """
    return len(open_list)


def heuristica2(estado) -> callable:
    """ Función heurística que devuelve el número de alumnos que quedan por subir al autobús """
    return len(estado)


def heuristica(heuristica, estado, alumno, open_list, closed_list) -> callable:
    """ Función heurística que devuelve el número de alumnos que no están en su asiento """
    if heuristica == 1:
        return heuristica1(estado, alumno, open_list, closed_list)
    return heuristica2(estado)


def coste(estado, alumno, open_list, closed_list) -> callable:
    """ Función que calcula el coste de un nodo """
    # ? Es decir, tiene en cuenta las distintas restricciones al subir x alumno al autobús
    print(estado, alumno)
    estado.append(alumno)  # Añadimos el alumno al estado
    print(estado)
    lista_costes = []
    id_conflictivos = []
    multiplicador = 1

    print(lista_costes, multiplicador, id_conflictivos)

    # TODO: Lo mismo hay que sacarlo fuera de los costes per se
    # ! Dos alumnos con movilidad reducida no pueden ir seguidos ni al final
    if mov_reducida_seguidos(estado) or mov_reducida_final(estado, len(open_list)):
        print('ERROR: Movilidad reducida seguida o al final')
        return None  # No se puede añadir el alumno

    # ! Recorremos la lista de alumnos para calcular el coste total
    for i, alumno in enumerate(estado):

        # Calculamos el número de conflc. con menor id y calculamos el multiplicador
        id_alumno = re.findall(r'\d', estado[i])[0]

        if len(id_conflictivos) > 0 and sum(i < id_alumno for i in id_conflictivos) > 0:
            print(2 * sum(i < id_alumno for i in id_conflictivos))
            multiplicador = 2 * sum(i < id_alumno for i in id_conflictivos)
        else:
            multiplicador = 1

        # ? Si el alumno es de mov. reducida, el coste es el triple
        if re.match(r'\d[XC]R', estado[i]):
            # ? Si el alumno anterior es conflictivo, el coste es el doble
            if i > 0 and re.match(r'\dCX', estado[i-1]):
                lista_costes.append(3 * (2 * multiplicador))
            else:
                lista_costes.append(3 * multiplicador)

        # ? Si el alumno no es de mov. reducida coste normal
        if re.match(r'\d[XC]X', estado[i]):
            # ? Si el alumno anterior es con movilidad reducida, no tiene coste
            if i > 0 and re.match(r'\d[XC]R', estado[i-1]):
                lista_costes.append(0)
            # ? Si el alumno anterior es conflictivo, el coste es el doble
            elif i > 0 and re.match(r'\dCX', estado[i-1]):
                lista_costes.append(2 * multiplicador)
            # ? Si no, se suma el coste del alumno
            else:
                lista_costes.append(1 * multiplicador)

        # ? Si hay un alumno conflictivo, el coste del alumno anterior y siguiente es el doble
        if i > 0 and re.match(r'\dC[XR]', estado[i]):
            lista_costes[i-1] = lista_costes[i-1] * 2

        # ? Si el alumno es conflictivo, lo añadimos a la lista de conflictivos
        if re.match(r'\dC[XR]', estado[i]):
            id_conflictivos.append(id_alumno)

        print(lista_costes, multiplicador, id_conflictivos)

    return sum(lista_costes)


# ! Los alumnos con movilidad reducida tardan 3 veces más en subir al autobús
def mov_reducida_final(estado, len_open_list) -> bool:
    """ Función que devuelve una lista con los alumnos con movilidad reducida """
    # Comprobamos si el último alumno de la lista es con movilidad reducida
    # Si el alumno es el ultimo de la lista abierta, False
    if re.match(r'\d\wR', estado[-1]) and len_open_list == 0:
        print('Movilidad reducida final')
        return True
    return False


# ! Dos alumnos con movilidad reducida no pueden ir seguidos
def mov_reducida_seguidos(estado) -> bool:
    """ Función que devuelve una lista con los alumnos con movilidad reducida """
    # Comprobamos si el último alumno de la lista es con movilidad reducida
    # Lo comprobamos mediante el uso de expresiones regulares
    if re.match(r'\d\wR', estado[-1]) and re.match(r'\d\wR', estado[-2]):
        return True
    return False


def a_estrella(estado_inicial: list):
    """
    Función que implementa el algoritmo A*
    idea: Ordenar por coste
    (sort()), ya que en a estrella las, listas han de estar ordenadas de menor a mayor 
    e ir haciendo pop(0) para ir sacando el de menor coste
    cuidado!: Se pueden añadir nodos iguales pero con costes diferentes, comprobar siempre!
    """
    ###  Creación de las variables globales  ###
    # Añadimos a la open list el estado incial, que no tiene padre y es una lista vacía de ids, el nodo inicial dndn se
    open_list = Estado(None, [], 0, 0)
    closed_list = []                # Lista de nodos expandidos
    # decision_list = []            # Lista de nodos que van a competir en cada iteración por acabar en la closed list
    goal = False                    # Variable que indica si se ha llegado al estado meta

    # Creamos el nodo inicial
    nodo_inicial = Estado(None, closed_list, 0, heuristica(open_list))

    while (not goal or len(open_list) >= 0):
        nodo_actual = open_list.pop(0)
        for elem in open_list:
            if elem.coste < nodo_actual.coste_f:
                nodo_actual = elem

        if is_goal(nodo_actual):
            goal = True
            break
        else:
            closed_list.append(nodo_actual)
            # Se compara por todos los hijos
            for elem in nodo_actual.expandir():
                if not esta_en_cola(closed_list, elem):
                    if not esta_en_cola(open_list, elem):
                        open_list.append(elem)
                    else:
                        for elem2 in open_list:
                            if elem2 == elem:
                                if elem2.coste_f > elem.coste_f:
                                    open_list.remove(elem2)
                                    open_list.append(elem)
                else:
                    continue

    if goal:
        print("Solución encontrada")
        print("Nodos generados: ", nodos_gen)
        print("Nodos expandidos: ", nodos_expand)
        print("Coste: ", nodo_actual.coste_f)
        print("Ruta: ", nodo_actual.id)
        while nodo_actual.padre is not None:
            nodo_actual = nodo_actual.padre
            print("Ruta: ", nodo_actual.id)


# La función a_estrella se llama desde el main
def main():
    """ Función principal del programa """
    # # Inicialización
    # estado_inicial = open_list[0]
    # nodo_inicial = Nodo(0, estado_inicial, None, heuristica(estado_inicial), 0)
    # open_list.append(nodo_inicial)
    estado_anterior = Estado(None, ['3XR', '2XR'], 8, 10)
    estado_actual = Estado(estadoAnterior,  ['3XR', '2XR', '1XR'], 10, 15)
    open_list = []
    coste_g = coste(closed_list, '4XX', open_list, closed_list)
    coste_h = heuristica(1, closed_list, '4XX', open_list, closed_list)
    coste_f = coste_g + coste_h
    print(f'{coste_f}={coste_g}+{coste_h}')


if __name__ == '__main__':
    main()  # Llamamos a la función principal
