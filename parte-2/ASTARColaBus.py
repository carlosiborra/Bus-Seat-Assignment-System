# Restricciones:
#  - Los alumnos con movilidad reducida tardan tres veces mas en montar en el autobús que el resto de
# alumnos.
#  - El alumno que se encuentre en la cola justo detras de un alumno con movilidad reducida debera ayudarle
# a subir al autobus, por lo que no puede haber dos alumnos con movilidad reducida uno a continuacion
# del otro ni ocupando la ultima posición en la cola.
#  - Cuando un alumno ayuda a subir a otro con movilidad reducida el tiempo que tardan los dos es el tiempo
# que tarda el alumno con movilidad reducida puesto que suben a la vez.
#  - Un alumno conflictivo duplicará el tiempo necesario para subir al autobús tanto del compañero que se
# encuentre justo delante de él como del compañero que se encuentre justo detrás, de este modo, si un
# alumno conflictivo ayuda a un alumno con movilidad reducida a subir al autobus, el tiempo empleado por
# los dos se duplicara respecto al tiempo que se invertiría si quien ayudase fuese un alumno no conflictivo.
#  - Un alumno conflictivo duplicara el tiempo invertido para subir al autobús de todos aquellos alumnos que,
# encontrándose en la cola después de él, tengan asignados asientos en el autobús con una numeración
# superior a la suya.


# AGENTE VIAJERO: Se debe visitar solo 1 vez cada nodo y todos los nodos deben ser visitados, volviendo al nodo inicial
# Ruta con coste menor acumulado
# link interesante: https://knuth.uca.es/moodle/mod/page/view.php?id=3417

# Factor de ramificación > 10

dict_posiciones = {'4XR': 2, '3XR': 16, '2XR': 18, '1XR': 20}

# Variables
nodos_gen = 0
nodos_expand = 0
# Cola vacía, y los alumnos obtenidos de la parte 1 se usarán para irlos metiendo en la cola


class Nodo():
    """ Clase nodos para el algoritmo A* """

    def __init__(self, padre=None, id=None, g=0, h=0):
        """Constructor de la clase nodo"""
        self.id = id
        self.padre = padre
        self.heur = heuristica
        self.coste = coste
        self.coste_f = self.coste + self.heur  # f(n) = g(n) + h(n)
        # TODO: añadir variables del nodo que hace que sea inequívoco

    def __eq__(self, otro):
        """Compara dos nodos -> para poder saber si se ha expandido o no. No se compara ni el coste ni el valor h ni el nodo padre"""
        return ((self.id == otro.id))


def heuristica(estado):
    """Función heurística que devuelve el número de alumnos que no están en su asiento"""
    # Función heurística que devuelve el número de alumnos que faltan por subir al autobús
    return len(open_list)


def coste(nodo, alumno):
    """Función que calcula el coste de un nodo"""
    # Si el alumno es de movilidad reducido, tarda 3 veces más en subir al autobús
    estado = nodo.id


def expandir(nodo):
    """Función que devuelve una lista de nodos hijos de un nodo dado"""


def is_goal(estado):
    """Función que devuelve True si el estado es meta y False en caso contrario (heurística = 0)"""
    if heuristica(estado) == 0:
        return True
    else:
        return False


def esta_en_cola(cola, nodo):
    """Función que devuelve True si un nodo está en una cola y False en caso contrario"""


def a_estrella(estado_inicial: list):
    """
    Función que implementa el algoritmo A*
    idea: Ordenar por coste
    (sort()), ya que en a estrella las, listas han de estar ordenadas de menor a mayor 
    e ir haciendo pop(0) para ir sacando el de menor coste
    cuidado!: Se pueden añadir nodos iguales pero con costes diferentes, comprobar siempre!
    """
    ###  Creación de las variables globales  ###
    open_list = estado_inicial      # Lista de nodos posibles de expansión
    closed_list = []                # Lista de nodos expandidos
    # decision_list = []            # Lista de nodos que van a competir en cada iteración por acabar en la closed list
    goal = False                    # Variable que indica si se ha llegado al estado meta

    # Creamos el nodo inicial
    nodo_inicial = Nodo(None, closed_list, 0, heuristica(open_list))

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
    """Función principal del programa"""

    # Inicialización
    estado_inicial = open_list[0]
    nodo_inicial = Nodo(0, estado_inicial, None, heuristica(estado_inicial))
    open_list.append(nodo_inicial)
