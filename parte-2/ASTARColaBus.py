#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" importing libraries """
import sys
import time

# Importamos las listas para poder obtener los datos del archivo
# El diccionario de un archivo .prob de un path
# Otra función para parsear el resultado de la función anterior a una lista
from readParse import parse_result
from costeG import coste
from constraint import mov_reducida_final, mov_reducida_seguidos
from heuristicas import select_heuristic
from writeResult import write_solution, write_statistics
from comprobaciones import comprobar_estado


# ? Antes de nada, obtenemos el argumento (path) pasado por consola
def command_prompt():
    """ Obtenemos el argumento (path) pasado por consola """
    if len(sys.argv) < 3 or len(sys.argv) > 3:
        print("Error: Se necesita un argumento (el path al test) y un tipo de heurística (1 o 2)")
        sys.exit(1)
    return sys.argv[1], sys.argv[2]


# ! -------------------------------------------------------------------
# ! CLASE DE LOS DISTINTOS ESTADOS de A*
# ! -------------------------------------------------------------------
class Estado():
    """ Clase de los nodos para el algoritmo A* """

    def __init__(self, padre: object, cola_bus: list, cola_total: list, heuristica: int):
        """ Constructor de la clase nod """
        print("\nCREACIÓN ESTADO:")
        self.padre = padre
        self.cola_bus = cola_bus
        print("Cola del bus:", self.cola_bus)
        self.cola_restante = restantes(self.cola_bus, cola_total)
        print("Alumnos restantes:", self.cola_restante)
        # Calulamos los costes
        print("\nCOSTES DEL ESTADO:")
        self.coste_g = coste(self.cola_bus)
        print("Coste g(n):", self.coste_g)
        self.coste_h = select_heuristic(heuristica, self.cola_restante)
        print("Coste h(n):", self.coste_h)
        self.coste_f = self.coste_g + self.coste_h  # f(n) = g(n) + h(n)
        print("Coste f(n):", self.coste_f)

    def __eq__(self, estado):
        """ Función que compara si dos estados son iguales """
        # Dos estados son iguales si la cola bus son iguales
        if self.cola_bus == estado.cola_bus:
            return True
        return False


def restantes(cola_bus, cola_total) -> list:
    """ Función que devuelve una lista con los alumnos que faltan por subir al autobús """
    if cola_bus is None:
        return cola_total
    return [alumno for alumno in cola_total if alumno not in cola_bus]


def is_goal(estado) -> bool:
    """Función que determina si un estado es meta en base a la heurística"""
    if estado.coste_h == 0:
        print("\nESTADO META, coste heurístico es 0:", estado.cola_bus)
        return True
    return False


def expandir(estado, cola_total, heuristica_sel: int) -> list:
    """ Función que consigue los estados posibles de expansión en base a un estado """
    if len(estado.cola_bus) > 1 and (mov_reducida_seguidos(estado.cola_bus) or mov_reducida_final(estado.cola_bus, len(estado.cola_restante))):
        print('ERROR: Movilidad reducida seguida o al final')
        return []  # No se han añadido hijos ya que no se puede seguir por esta rama
    else:
        hijos = []
        for elem in estado.cola_restante:
            cola_nueva = estado.cola_bus + [elem]
            nuevo_estado = Estado(estado, cola_nueva,
                                  restantes(cola_nueva, cola_total), heuristica_sel)
            hijos.append(nuevo_estado)
        return hijos


def esta_en_lista(estado1, lista) -> bool:
    """Función que determina si un estado1 está en la lista determinada"""
    for estado2 in lista:
        if estado1 == estado2:
            return True
        return False


# ! -------------------------------------------------------------------
# ! ALGORITMO A*
# ! -------------------------------------------------------------------
def a_estrella(estado_inicial, cola_total, heuristica_sel):
    """ Función que implementa el algoritmo A* """
    # ! Iniciamos el conómetro
    start_time = time.time()
    # ! Inicializamos las variables
    # Metemos en la lista abierta el estado inicial
    print("Estado inicial:", estado_inicial.cola_bus)
    open_list = []  # Lista abierta con los nodos a expandir
    closed_list = []  # Lista de nodos expandidos
    goal = False  # Variable que indica si se ha llegado al estado meta

    # Añadimos el estado inicial a la lista abierta
    open_list.append(estado_inicial)

    # ! Bucle de ejecución de A*
    while (not goal or len(open_list) >= 0):
        # print("Lista abierta:", open_list)
        # print("Lista cerrada:", closed_list)
        estado_actual = open_list.pop(0)
        print(
            f'Estado actual: {estado_actual.cola_bus}, {estado_actual.coste_h}')

        # ! Comprobamos si el estado actual es meta
        if is_goal(estado_actual):
            # ! Añadimos el estado meta a la lista cerrada
            closed_list.append(estado_actual)
            # ! Además, se para el cronómetro -> tiempo que ha tardado el algoritmo
            tiempo_total = time.time() - start_time
            # ! Se llega al estado meta
            goal = True
            break

        # ! Si no es meta, se expande
        else:
            hijos = expandir(estado_actual, cola_total, heuristica_sel)
            if not hijos:
                continue
            else:
                closed_list.append(estado_actual)
                # Se añaden los hijos a la lista abierta
                # Primero, comprobamos si están en la lista cerrada
                for state1 in hijos:
                    # Se recorren los hijos del estado actual
                    # Comprobamos si está en la lista cerrada -> Se descarta
                    if not esta_en_lista(state1, closed_list):
                        # No está en la lista cerrada
                        # Comprobamos si está en la lista abierta
                        if not esta_en_lista(state1, open_list):
                            # Si no está en la lista abierta, se mete
                            open_list.append(state1)
                        else:
                            # Si está en la lista abierta, comprobamos si el coste f es menor
                            open_list_copy = open_list.copy()
                            # Comprobamos si el estado nuevo es mejor que el anterior
                            for state2 in open_list_copy:
                                if state1 == state2:
                                    if state1.coste_f < state2.coste_f:
                                        print("Se ha encontrado un estado mejor")
                                        print("Estado anterior:", state2.cola_bus,
                                              "estado nuevo:", state1.cola_bus)
                                        state2 = state1
                                        # Eliminamos el estado anterior de la lista abierta
                                        open_list.remove(state2)
                                        open_list.append(state1)
                                    else:
                                        continue
                                else:
                                    continue
                    else:
                        continue

        # ! Ordenamos la lista abierta por coste f e imprimimos
        # ! En caso de que haya empate, se ordena por coste h
        open_list.sort(key=lambda x: (x.coste_f, x.coste_h))
        # ! Imprimimos los costest f de los nodos de la lista abierta
        # print("\nCOSTES F tras ORDENACIÓN:")
        # print(
        #     f'Costes f de la lista abierta: \n{[elem.coste_f for elem in open_list]}')
        # # ! Imprimimos la lista abierta (solo cola de bus)
        # print("\nLISTA ABIERTA:")
        # print([elem.cola_bus for elem in open_list])
        # # ! Imprimimos la lista cerrada (solo cola de bus)
        # print("\nLISTA CERRADA:")
        # print([elem.cola_bus for elem in closed_list])

    # ! Si se ha llegado al estado meta, se imprimen los resultados

    # ! Imprimimos la lista abierta (solo cola de bus)
    print("\nLISTA ABIERTA:")
    print([elem.cola_bus for elem in open_list])
    # ! Imprimimos la lista cerrada (solo cola de bus)
    print("\nLISTA CERRADA:")
    print([elem.cola_bus for elem in closed_list])

    # ! SE HA LLEGADO AL ESTADO META
    if goal:
        print("\nRESULTADOS:")

        # ! Antes de nada, podemos comprobar si el resultado y coste es admisible
        print(comprobar_estado(estado_actual))
        coste_total = estado_actual.coste_f
        output = estado_actual.cola_bus
        estadisticas, ruta_seguida = [], []
        ruta_seguida = []
        i = True
        while i:
            if estado_actual.padre is None:
                ruta_seguida.append(None)
            else:
                ruta_seguida.append(estado_actual.cola_bus[-1][0])
            if estado_actual.padre is None:
                i = False
            estado_actual = estado_actual.padre

        # ! Obtención de las estadísticas
        # Tiempo total
        estadisticas.append(tiempo_total)
        print("Tiempo total:", tiempo_total)
        # Coste total de la ruta encontrada es el coste f del estado meta
        # sería lo mismo que el coste g ya que no hay coste h en el estado meta
        estadisticas.append(coste_total)
        print("Coste Total:", coste_total)
        # Nodos generados -> nodos en la lista abierta + nodos en la lista cerrada
        long_plan = len(open_list) + len(closed_list)
        estadisticas.append(long_plan)
        print("Longitud del plan:", long_plan)
        # Nodos expandidos -> nodos lista cerrada
        estadisticas.append(len(closed_list))
        print("Nodos expandidos:", len(closed_list))
        # Imprimimos el plan (ruta seguida), orden inverso, de padre a hijo
        print("Distribución seguida:")
        print(ruta_seguida[::-1])

        # ! Exportamos la solución a un fichero
        write_solution(cola_total, output, str(command_prompt()[0]))
        # ! Exportamos las estadísticas a un fichero
        write_statistics(estadisticas, str(command_prompt()[0]))

    else:
        print("Solución no encontrada")


# La función a_estrella se llama desde el main
def main():
    """ Función principal del programa """
    # Obtenemos el path del fichero y la heurística a utilizar desde la consola
    path = str(command_prompt()[0])
    heuristica_sel = int(command_prompt()[1])
    print('heuristica_sel', heuristica_sel)
    # Obtenemos la cola total del fichero al que apunta el path
    cola_total = parse_result(path)
    print(cola_total)
    print("\nCREANDO ESTADO INICIAL...")
    # Estado: (padre, cola_bus, cola_total, heuristica_seleccionada)
    # Creamos el estado inicial
    estado_inicial = Estado(None, [], cola_total, heuristica_sel)
    # Llamamos a la función a_estrella y le pasamos el estado inicial y la cola total
    a_estrella(estado_inicial, cola_total, heuristica_sel)


if __name__ == '__main__':
    # Llamamos a la función principal
    main()
