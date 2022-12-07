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

    def __init__(self, padre=None, cola_bus: list = [], cola_total: list = [], heuristica: int = 1):
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


# ! -------------------------------------------------------------------
# ! AGORITMO A*
# ! -------------------------------------------------------------------
def a_estrella(estado_inicial, cola_total):
    """ Función que implementa el algoritmo A* """
    # ! Iniciamos el conómetro
    start_time = time.time()
    # ! Inicializamos las variables
    nodes_gen = 1  # Número de nodos generados
    # Metemos en la lista abierta el estado inicial
    print("Estado inicial:", estado_inicial.cola_bus)
    open_list = [estado_inicial]  # Lista abierta con los nodos a expandir
    closed_list = []  # Lista de nodos espandidos
    goal = False  # Variable que indica si se ha llegado al estado meta

    ####  bucle de ejecución de A*  ####
    while (not goal or len(open_list) >= 0):
        # print("Lista abierta:", open_list)
        # print("Lista cerrada:", closed_list)
        estado_actual = open_list.pop()
        print("Estado actual:", estado_actual.cola_bus)
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

        # ! Ordenamos la lista abierta por coste f e imprimimos
        # TODO: ¿Porque cuando se pone reverse Trie cambia tanto? de 11 a 34
        open_list.sort(key=lambda x: x.coste_f, reverse=False)
        # ! Imprimimos los costest f de los nodos de la lista abierta
        print("\nCOSTES F:")
        print("Costes f de la lista abierta:", [
              elem.coste_f for elem in open_list])

    # ! Si se ha llegado al estado meta, se imprimen los resultados
    if goal:
        print("\nRESULTADOS:")
        output = estado_actual.cola_bus
        estadisticas = [] 
        coste_ruta = 0
        ruta_seguida = []
        while estado_actual.padre is not None:
            ruta_seguida.append(estado_actual.cola_bus[-1][0])
            coste_ruta += estado_actual.coste_f
            estado_actual = estado_actual.padre
        # Calculamos el tiempo que ha tardado el algoritmo
        tiempo_total = time.time() - start_time
        estadisticas.append(tiempo_total)
        print("Tiempo total:", tiempo_total)
        # Coste total de la ruta encontrada
        # Coste total = sumatorio de todos los costes f de los estados seguidos de la ruta
        estadisticas.append(coste_ruta)
        print("Coste Total:", coste_ruta)
        # Nodos generados
        estadisticas.append(nodes_gen)
        print("Longitud del plan:", nodes_gen)
        # Nodos expandidos
        estadisticas.append(len(closed_list))
        print("Nodos expandidos:", len(closed_list))
        # Imprimimos el plan (ruta seguida), orden inverso, de padre a hijo
        print("Ruta seguida:")
        for i in ruta_seguida:
            print(i)

        # ! Exportamos la solución a un fichero
        write_solution(output, cola_total, str(command_prompt()[0]))
        # ! Exportamos las estadísticas a un fichero
        write_statistics(estadisticas, str(command_prompt()[0]))

    else:
        print("Solución no encontrada")


# La función a_estrella se llama desde el main
def main():
    """ Función principal del programa """
    # Obtenemos el path del fichero y la heurística a utilizar desde la consola
    path = str(command_prompt()[0])
    heuristica_sel = str(command_prompt()[1])
    # Obtenemos la cola total del fichero al que apunta el path
    cola_total = parse_result(path)
    print(cola_total)
    print("\nCREANDO ESTADO INICIAL")
    # Estado: (padre, cola_bus, cola_total, heuristica_seleccionada)
    # Creamos el estado inicial
    estado_inicial = Estado(None, [], cola_total, heuristica_sel)
    # Llamamos a la función a_estrella y le pasamos el estado inicial y la cola total
    a_estrella(estado_inicial, cola_total)


if __name__ == '__main__':
    # Llamamos a la función principal
    main()
