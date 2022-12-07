""" Archivo para calcular el las distintas heurísticas """

def select_heuristic(heuristic: int, cola_restante) -> callable:
    """ Función que devuelve la heurística seleccionada """
    if heuristic == 1:
        return heuristica1(cola_restante)
    elif heuristic == 2:
        return heuristica2(cola_restante)
    elif heuristic == 3:
        return heuristica3(cola_restante)
    else:
        return heuristica1(cola_restante)

def heuristica1(cola_restante) -> callable:
    """ Función heurística que devuelve el número de alumnos que quedan por subir al autobús """
    return len(cola_restante)


def heuristica2(cola_restante) -> callable:
    """ Función heurística que devuelve el número de alumnos que quedan por subir al autobús """
    return len(cola_restante)


def heuristica3(cola_restante) -> callable:
    """ Función heurística que devuelve el número de alumnos que quedan por subir al autobús """
    return len(cola_restante)
