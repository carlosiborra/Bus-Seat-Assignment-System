""" Archivo para escribir los resultados en un archivo de texto """

# Importamos las librerías necesarias
from readParse import parse_dict


def write_solution(input_dict: dict, output_dict: dict, path):
    """ Función que escribe los resultados en un archivo de texto """
    # Quitamos la extensión del path (.prob) y le añadimos la extensión .output
    # Abrimos el archivo de texto
    with open(path[:-5] + '.output', 'w', encoding='UTF8') as file:
        # Escribimos los resultados
        in_dict = parse_dict(input_dict)
        out_dict = parse_dict(output_dict)
        file.write(f'INICIAL: {in_dict}\nFINAL: {out_dict}')
        print("\nSOLUCIÓN AL PROBLEMA:")
        print(f'INICIAL: {in_dict}\nFINAL: {out_dict}')
