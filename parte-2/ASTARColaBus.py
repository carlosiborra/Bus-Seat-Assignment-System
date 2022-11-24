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

# TODO: REESCUCHAR AUDIO A* DE 5 min (EL OTRO ES DE SCP) Y VER NOTION Y EL PSEUDOCÓDIGO DE A* PARA IR CREANDO EL PROGRAMA
# TODO: Mirar problema del viajante de comercio (TSP) para ver si se puede aplicar a este problema


# AGENTE VIAJERO: Se debe visitar solo 1 vez cada nodo y todos los nodos deben ser visitados, volviendo al nodo inicial
# Ruta con coste menor acumulado 
# link interesante: https://knuth.uca.es/moodle/mod/page/view.php?id=3417

# Factor de ramificación > 10

class nodo():
    def __init__(self, id, estado, padre, heuristica, coste):
        """Constructor de la clase nodo"""
        self.id = id 	
        self.padre = padre
        self.heur = heuristica
        self.coste_acum = coste # f(n) = g(n) + h(n)
        # TODO: añadir variables del nodo que hace que sea inequívoco
    
    def __eq__(self, otro):
        """Compara dos nodos -> para poder saber si se ha expandido o no. No se compara ni el coste ni el valor h ni el nodo padre"""
        return ((self.id == otro.id))
 

def heuristica(estado):
    """Función heurística que devuelve el número de alumnos que no están en su asiento"""
    

def expandir(nodo):
    """Función que devuelve una lista de nodos hijos de un nodo dado + su coste de expansión?"""

def es_meta(estado):
    """Función que devuelve True si el estado es meta y False en caso contrario (heurística = 0)"""

def esta_en_cola(cola, nodo):
    """Función que devuelve True si un nodo está en una cola y False en caso contrario"""

def a_estrella(open, closed, finish, init_state):
    
    """
    Función que implementa el algoritmo A*
    idea: Ordenar por coste 
    (sort()), ya que en a estrella las, listas han de estar ordenadas de menor a mayor 
    e ir haciendo pop(0) para ir sacando el de menor coste
    cuidado!: Se pueden añadir nodos iguales pero con costes diferentes, comprobar siempre!
    """

# Variables globales
nodos_gen = 0
nodos_expand = 0
estado_inicial = [] # Cola vacía, y los alumnos obtenidos de la parte 1 se usarán para irlos metiendo en la cola
open_list = [estado_inicial]
closed_list = []
finish = False

