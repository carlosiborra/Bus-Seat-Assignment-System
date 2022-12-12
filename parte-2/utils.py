""" Archivo que contiene las funciones necesarias para hacer a A* funcionar """


def esta_en_lista(estado1, lista) -> bool:
    """Función que determina si un estado 1 está en la lista determinada"""
    for estado2 in lista:
        if estado1 == estado2:
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
