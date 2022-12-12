""" Archivo para calcular las restricciones """

# Importamos las librerías necesarias
import re


# ! Los alumnos con movilidad reducida tardan 3 veces más en subir al autobús
def mov_reducida_final(cola_bus, cola_restante) -> bool:
    """ Función que devuelve una lista con los alumnos con movilidad reducida """
    # Comprobamos si el último alumno de la lista es con movilidad reducida

    # Antes de nada debemos comprobar que la cola del bus no está vacía, si lo estuviese
    # E intentamos meter uno de movilidad reducida, nos daría error, ya que sería
    # el último y no habría ninguno
    # Es importante recordar que la cola restante no está actualizada todavía, por ello == 1
    if len(cola_bus) > 0 and re.match(r'\d*\wR', cola_bus[-1][0]) and len(cola_restante) == 1:
        print('Movilidad reducida final')
        return True
    return False


# ! Dos alumnos con movilidad reducida no pueden ir seguidos
def mov_reducida_seguidos(cola_bus) -> bool:
    """ Función que devuelve una lista con los alumnos con movilidad reducida """
    # Comprobamos si el último alumno de la lista es con movilidad reducida
    # Lo comprobamos mediante el uso de expresiones regulares

    if len(cola_bus) > 1 and re.match(r'\d*\wR', cola_bus[-1][0]) and \
            re.match(r'\d\wR', cola_bus[-2][0]):
        print('Movilidad reducida seguidos')
        return True
    return False


# ! Infile test
# cola = []
# open_list = [['5XR', 3]]
# print(mov_reducida_final(cola, open_list))
# print(mov_reducida_seguidos(cola))
