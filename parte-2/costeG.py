""" Archivo para calcular el coste G (de S a N) """

# Importamos las librerías necesarias
import re


def coste(cola_bus) -> callable:
    """ Función que calcula el coste de un nodo """
    # Creamos las variables necesarias
    lista_costes = []
    id_conflictivos = []
    multiplicador = 1

    # print(lista_costes, multiplicador, id_conflictivos)

    # Previamente al expandir se han comprobado ciertas condiciones
    # Esto es, no pueden ir ni seguidos ni al final

    # ! Recorremos la lista de alumnos para calcular el coste total
    if cola_bus is None:
        return 0

    for i, alumno in enumerate(cola_bus):

        # ? Calculamos el número de conflc. con menor id y calculamos el multiplicador
        # print(cola_bus[i][0], cola_bus[i][1])
        posicion = cola_bus[i][1]

        if len(id_conflictivos) > 0 and sum(i < posicion for i in id_conflictivos) > 0:
            # print(2 * sum(i < posicion for i in id_conflictivos))
            multiplicador = 2 * sum(i < posicion for i in id_conflictivos)
        else:
            multiplicador = 1

        # ? Si el alumno es de mov. reducida, el coste es el triple
        if re.match(r'\d[XC]R', cola_bus[i][0]):
            # ? Si el alumno anterior es conflictivo, el coste es el doble
            if i > 0 and re.match(r'\dCX', cola_bus[i-1][0]):
                lista_costes.append(3 * (2 * multiplicador))
            else:
                lista_costes.append(3 * multiplicador)

        # ? Si el alumno no es de mov. reducida coste normal
        if re.match(r'\d[XC]X', cola_bus[i][0]):
            # ? Si el alumno anterior es con movilidad reducida, no tiene coste
            if i > 0 and re.match(r'\d[XC]R', cola_bus[i-1][0]):
                lista_costes.append(0)
            # ? Si el alumno anterior es conflictivo, el coste es el doble
            elif i > 0 and re.match(r'\dCX', cola_bus[i-1][0]):
                lista_costes.append(2 * multiplicador)
            # ? Si no, se suma el coste del alumno
            else:
                lista_costes.append(1 * multiplicador)

        # ? Si hay un alumno conflictivo, el coste del alumno anterior y siguiente es el doble
        if i > 0 and re.match(r'\dC[XR]', cola_bus[i][0]):
            lista_costes[i-1] = lista_costes[i-1] * 2

        # ? Si el alumno es conflictivo, lo añadimos a la lista de conflictivos
        if re.match(r'\dC[XR]', cola_bus[i][0]):
            id_conflictivos.append(posicion)

        # print(lista_costes, multiplicador, id_conflictivos)

    # print(lista_costes, multiplicador, id_conflictivos)
    return sum(lista_costes)

# ! Infile test
# cola_bus = [['4XX', 2], ['3CX', 21], ['2XX', 18], ['1XX', 20]]
# print(coste(cola_bus))
