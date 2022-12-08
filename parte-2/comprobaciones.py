""" Archivo con la función de comprobación de resultados admisibles """


def comprobar_estado(estado):
    """ Función que comprueba si la heurística es admisible """
    coste_ruta_f, coste_ruta_g, coste_ruta_h = [], [], []

    while estado.padre is not None:
        coste_ruta_g.append(estado.coste_g)
        coste_ruta_h.append(estado.coste_h)
        coste_ruta_f.append(estado.coste_f)
        estado = estado.padre

    # Si f(n) != g(n) + h(n) no es admisible
    if sum(coste_ruta_f) != sum(coste_ruta_g) + sum(coste_ruta_h):
        return "ERROR: suma de costes no es correcta"

    # Si h(n) > h(n') no es admisible
    for i in range(len(coste_ruta_h)-1):
        if coste_ruta_h[i] > coste_ruta_h[i+1]:
            return "ERROR: heurística no es admisible (A)"

    # Si h(n) > g(n), no es admisible, en caso de estar en el estado meta
    if sum(coste_ruta_h) > sum(coste_ruta_g):
        return "ERROR: heurística no es admisible (B)"

    return "Heurística y costes admisibles"
