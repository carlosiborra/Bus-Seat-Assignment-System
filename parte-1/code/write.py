""" write.py by 100451170 & 100451258 """

# Se pretende devolver una solución al archivo indicado en el formato txt
# Se exporta en .txt ya que los diccionarios de las soluciones el .csv lo escribe con comillas
# o solo escribe las keys, lo cual no sigue el formato de la solución deseado

# Crear un nuevo archivo .output con los resultados
# Si el archivo ya existe, sobreescribirlo
def write_result(path: str, num_sol: str, rand_sol) -> None:
    """ Escribe el archivo en el path especificado con los resultados (num_sol y rand_sol) """
    with open(path, "w", encoding="utf8") as file:
        file.write(num_sol + "\n")
        for sol in rand_sol:
            file.write(f"{sol}\n")
