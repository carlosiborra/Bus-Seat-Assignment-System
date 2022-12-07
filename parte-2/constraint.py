""" Archivo para calcular ciertas restricciones """

# Importamos las librerías necesarias
import re

# ! Los alumnos con movilidad reducida tardan 3 veces más en subir al autobús


def mov_reducida_final(cola_bus, len_restantes) -> bool:
    """ Función que devuelve una lista con los alumnos con movilidad reducida """
    # Comprobamos si el último alumno de la lista es con movilidad reducida
    # Si el alumno es el ultimo de la lista abierta, False
    print(cola_bus[-1][0])
    if re.match(r'\d\wR', cola_bus[-1][0]) and len_restantes == 0:
        print('Movilidad reducida final')
        return True
    return False


# ! Dos alumnos con movilidad reducida no pueden ir seguidos
def mov_reducida_seguidos(cola_bus) -> bool:
    """ Función que devuelve una lista con los alumnos con movilidad reducida """
    # Comprobamos si el último alumno de la lista es con movilidad reducida
    # Lo comprobamos mediante el uso de expresiones regulares
    if re.match(r'\d\wR', cola_bus[-1][0]) and re.match(r'\d\wR', cola_bus[-2][0]):
        return True
    return False


# ! Infile test
# cola = [['4XX', 2], ['3XX', 21], ['2XR', 18], ['1XR', 20]]
# open_list = [['5XX', 3]]
# print(mov_reducida_final(cola, len(open_list)))
# print(mov_reducida_seguidos(cola))
