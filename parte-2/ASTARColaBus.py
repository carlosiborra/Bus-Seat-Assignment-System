#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" importing libraries """


# Importamos las listas para poder obtener los datos del archivo
# El diccionario de un archivo .prob de un path
# Otra función para parsear el resultado de la función anterior a una lista

# TODO: Añadir las funciones externas necesarias para que funcione A* -> parsear_resultado, coste, mov_red_seguidos, mov_red_final, etc
# TODO: Añadir cola_total sacado del resultado de la parte 1


def heuristica1(cola_restante) -> callable:
    """ Función heurística que devuelve el número de alumnos que quedan por subir al autobús """
    return len(cola_restante)


class Estado():
    """ Clase de los nodos para el algoritmo A* """

    def __init__(self, padre=None, cola_bus: list = [], cola_total: list = []):
        """Constructor de la clase nodo"""
        self.padre = padre
        self.cola_bus = cola_bus
        self.cola_restante = restantes(self.cola_bus, cola_total)
        self.coste_h = heuristica1(self.cola_restante)
        self.coste_g = coste(self.cola_bus)
        self.coste_f = self.coste_g + self.coste_h  # f(n) = g(n) + h(n)

    def __eq__(self, other):
        """ Función que compara dos nodos """
        return self.cola_restante == other.cola_restante


def restantes(cola_bus, cola_total) -> list:
    """ Función que devuelve una lista con los alumnos que faltan por subir al autobús """
    if cola_bus is None:
        return cola_total
    return [alumno for alumno in cola_total if alumno not in cola_bus]


def is_goal(estado) -> bool:
    """Función que determina si un estado es meta en base a la heurística"""
    if (estado.coste_h == 0):
        return True
    else:
        return False


def expandir(estado, cola_total) -> list:
    """ Función que consigue los estados posibles de expansión en base a un estado """
    if len(estado.cola_bus) > 1 and (mov_reducida_seguidos(estado.cola_bus) or mov_reducida_final(estado.cola_bus, len(estado.cola_restante))):
        print('ERROR: Movilidad reducida seguida o al final')
        return []  # No se han añadido hijos ya que no se puede seguir por esta rama
    else:
        hijos = []
        for elem in estado.cola_restante:
            cola_nueva = estado.cola_bus + [elem]
            nuevo_estado = Estado(estado, cola_nueva,
                                  restantes(cola_nueva, cola_total))
            hijos.append(nuevo_estado)
        return hijos


def esta_en_lista(estado, lista) -> bool:
    """Función que determina si un estado está en la lista determinada"""
    for state in lista:
        if estado == state:
            return True
        else:
            return False


def a_estrella(estado_inicial, cola_total):
    """ Función que implementa el algoritmo A* """
    ####  variables iniciales  ####
    nodes_gen = 1                   # Número de nodos generados
    # Metemos en la lista abierta el estado inicial
    open_list = [estado_inicial]  # Lista abierta con los nodos a expandir
    closed_list = []                # Lista de nodos espandidos
    goal = False                    # Variable que indica si se ha llegado al estado meta

    ####  bucle de ejecución de A*  ####
    while (not goal or len(open_list) >= 0):
        estado_actual = open_list.pop()
        if is_goal(estado_actual):
            goal = True
            break
        else:
            hijos = expandir(estado_actual, cola_total)
            if not hijos:
                continue
            else:
                closed_list.append(estado_actual)
                # Se compara por todos los hijos
                for elem in hijos:
                    if not esta_en_lista(elem, closed_list):
                        if not esta_en_lista(elem, open_list):
                            open_list.append(elem)
                            nodes_gen += 1
                        else:
                            op_l_cpy = open_list.copy()
                            for elem2 in op_l_cpy:
                                if elem2 == elem:
                                    if elem2.coste_f > elem.coste_f:
                                        open_list.remove(elem2)
                                        open_list.append(elem)
                                        nodes_gen += 1
                                else:
                                    continue
                    else:
                        continue

    if goal:
        print("Solución encontrada")
        print("Nodos generados: ", nodes_gen)
        print("Nodos expandidos: ", len(closed_list))
        print("Coste Total: ", estado_actual.coste_f)
        print(f"Ruta: {estado_actual.cola_bus[-1][0]}")
        while estado_actual.padre is not None:
            print(estado_actual.cola_bus[-1][0])
            estado_actual = estado_actual.padre
    else:
        print("Solución no encontrada")


# La función a_estrella se llama desde el main
def main():
    """ Función principal del programa """

    path = 'ASTAR-tests\\alumnos00.prob'
    estado_inicial = Estado(None, [], cola_total)
    a_estrella(estado_inicial, cola_total)


if __name__ == '__main__':
    main()  # Llamamos a la función principal


# ! Llamamos a la función para sacar el diccionario de la cola de alumnos del archivo
