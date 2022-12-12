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
from restricciones import mov_reducida_final, mov_reducida_seguidos
from heuristicas import select_heuristic
from writeResult import write_solution, write_statistics
from comprobaciones import comprobar_estado
from utils import esta_en_lista, restantes, is_goal


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
        self.padre = padre
        self.cola_bus = cola_bus
        print(f'\n    SE CREA ESTADO HIJO con cola del bus: {self.cola_bus}')
        self.cola_restante = restantes(self.cola_bus, cola_total)
        print("        Alumnos restantes:", self.cola_restante)
        # Calulamos los costes
        self.coste_g = coste(self.cola_bus)
        self.coste_h = select_heuristic(heuristica, self.cola_restante)
        self.coste_f = self.coste_g + self.coste_h  # f(n) = g(n) + h(n)
        print(
            f"        Costes del estado hijo: coste g(n): {self.coste_g}, coste h(n): {self.coste_h}, coste f(n): {self.coste_f}")

    def __eq__(self, estado):
        """ Función que compara si dos estados son iguales """
        # Dos estados son iguales si la cola bus son iguales
        if self.cola_bus == estado.cola_bus:
            return True
        return False


def expandir(estado, cola_total, heuristica_sel: int) -> list:
    """ Función que consigue los estados posibles de expansión en base a un estado """
    hijos = []
    for elem in estado.cola_restante:
        if mov_reducida_final(estado.cola_bus + [elem], estado.cola_restante):
            print(
                f'\n    NO SE CREA ESTADO HIJO con cola del bus: {estado.cola_bus + [elem]}')
            print('        ERROR: movilidad reducida final:')
            continue

        elif mov_reducida_seguidos(estado.cola_bus + [elem]):
            print(
                f'\n    NO SE CREA ESTADO HIJO con cola del bus: {estado.cola_bus + [elem]}')
            print('        ERROR: movilidad reducida seguidos:')
            continue

        cola_nueva = estado.cola_bus + [elem]
        nuevo_estado = Estado(estado, cola_nueva,
                              restantes(cola_nueva, cola_total), heuristica_sel)
        hijos.append(nuevo_estado)
    if not hijos:
        print('\n    NOTA: este estado no tenía hijos válidos')
        return False
    return hijos


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
    while not goal and open_list:
        # print("Lista abierta:", open_list)
        # print("Lista cerrada:", closed_list)
        estado_actual = open_list.pop(0)
        print(
            f'\nESTADO SELECCIONADO: {estado_actual.cola_bus}, {estado_actual.coste_f}')
        # ! Comprobamos si el estado actual es meta
        if is_goal(estado_actual):
            print(goal)
            # ! Además, se para el cronómetro -> tiempo que ha tardado el algoritmo
            tiempo_total = time.time() - start_time
            # ! Se llega al estado meta
            goal = True

        # ! Si no es meta, se expande
        else:
            # ! Metemos el estado actual en la lista cerrada
            closed_list.append(estado_actual)

            hijos = expandir(estado_actual, cola_total, heuristica_sel)
            if not hijos:
                continue
            else:
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
        if open_list:
            open_list.sort(key=lambda x: (x.coste_f, x.coste_h))
            # ! Imprimimos los costes f de los nodos de la lista abierta
            # print("\nCOSTES F tras ORDENACIÓN:")
            # print(
            #     f'Costes f de la lista abierta: \n{[elem.coste_f for elem in open_list]}')

    # ! Si se ha llegado al estado meta, se imprimen los resultados

    # ! Imprimimos la lista abierta (solo cola de bus)
    print('\n\nTERMINADA LA EJECUCIÓN DEL ALGORITMO')
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
        print("Heurística seleccionada:", heuristica_sel)
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
        write_solution(heuristica_sel, cola_total,
                       output, str(command_prompt()[0]))
        # ! Exportamos las estadísticas a un fichero
        write_statistics(heuristica_sel, estadisticas,
                         str(command_prompt()[0]))

    # ! Si la lista abierta está vacía, se ha llegado al final sin encontrar una solución
    else:
        # len(open_list) == 0:
        print("\nFRACASO: no se ha encontrado una solución\n")
        return None


# ! La función a_estrella se llama desde el main
def main():
    """ Función principal del programa """
    # Obtenemos el path del fichero y la heurística a utilizar desde la consola
    path = str(command_prompt()[0])
    heuristica_sel = int(command_prompt()[1])
    # Obtenemos la cola total del fichero al que apunta el path
    cola_total = parse_result(path)
    print('\n----------------------------------------')
    print('\nCREANDO ESTADO INICIAL...')
    print(f'Heurística seleccionada: {heuristica_sel}\n{cola_total}')
    # Creamos el estado inicial
    estado_inicial = Estado(None, [], cola_total, heuristica_sel)
    # Llamamos a la función a_estrella y le pasamos el estado inicial y la cola total
    a_estrella(estado_inicial, cola_total, heuristica_sel)


if __name__ == '__main__':
    # Llamamos a la función principal
    main()
