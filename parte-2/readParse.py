""" read.py by 100451170 & 100451258 """

def parse_result(path: str) -> None:
    """ Obtiene el diccionario de la solución """
    print("\nOBTENIENDO LISTA DE LOS ALUMNOS:")
    with open(path, "r", encoding="utf8") as file:
        result = (file.read())
        # parseamos el resultado a diccionario
        return parse_list(parse_input(result))

def parse_input(result: str) -> dict:
    """ Parsea el resultado a un diccionario """
    # El contenido a parsear a diccionario es un string
    # Con formato: {'4XR': 2, '3XR': 16, '2XR': 18, '1XR': 20}
    # Se parsea a diccionario
    # Se elimina el primer y último carácter
    result = result[1:-1]
    # Se separa por comas
    result = result.split(",")
    # Se crea un diccionario vacío
    result_dict = {}
    # Se recorre la lista
    for i in result:
        # Se separa por :
        i = i.split(":")
        # Se añade al diccionario
        result_dict[i[0].strip()[1:-1]] = int(i[1].strip())
    return result_dict

def parse_list(dictionary: dict) -> list:
    """ Parsea el diccionario a una lista """
    # El diccionario tiene el formato: {'4XR': 2, '3XR': 16, '2XR': 18, '1XR': 20}
    # Se parsea a lista con el formato: [[key, value], [key, value], [key, value], [key, value]]
    # Se crea una lista vacía
    result_list = []
    # Se recorre el diccionario
    for key, value in dictionary.items():
        # Se añade a la lista
        result_list.append([key, value])
    return result_list

# ! Infile test
# path = 'ASTAR-tests\\alumnos00.prob'
# print(parse_result(path))