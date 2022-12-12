""" Archivo para escribir los resultados en un archivo de texto """

# Importamos las librerías necesarias
from readParse import parse_dict


def write_solution(heuristica, input_dict: dict, output_dict: dict, path):
    """ Función que escribe los resultados en un archivo de texto """
    # Quitamos la extensión del path (.prob) y le añadimos la extensión .output
    # Abrimos el archivo de texto
    with open(path[:-5] + f'-{heuristica}' + '.output', 'w', encoding='UTF8') as file:
        # Escribimos los resultados
        in_dict = parse_dict(input_dict)
        out_dict = parse_dict(output_dict)
        file.write(f'INICIAL: {in_dict}\nFINAL: {out_dict}')
        print("\nSOLUCIÓN AL PROBLEMA:")
        print(f'INICIAL: {in_dict}\nFINAL: {out_dict}')


def write_statistics(heuristica, input_dict: list, path):
    """ Función que escribe los las estadísticas en un archivo de texto """
    # Quitamos la extensión del path (.prob) y le añadimos la extensión .stat
    # Abrimos el archivo de texto
    with open(path[:-5] + f'-{heuristica}' + '.stat', 'w', encoding='UTF8') as file:
        # Escribimos los resultados
        print("\nESTADÍTICAS DE LA EJECUCIÓN:")
        file.write(f'Tiempo total: {input_dict[0]}\nCoste Total: {input_dict[1]}\
                   \nLongitud del plan: {input_dict[2]}\nNodos expandidos: {input_dict[3]}')
        print(f'Tiempo total: {input_dict[0]}\nCoste Total: {input_dict[1]}\
                   \nLongitud del plan: {input_dict[2]}\nNodos expandidos: {input_dict[3]}')
