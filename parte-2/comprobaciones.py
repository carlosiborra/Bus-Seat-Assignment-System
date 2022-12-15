""" Archivo con la función de comprobación de resultados admisibles y admisibles"""


def comprobar_estado(estado):
    """ Función que comprueba la validez de una heurística """
    coste_ruta_f, coste_ruta_g, coste_ruta_h = [], [], []

    i = True
    while i:
        coste_ruta_g.append(estado.coste_g)
        coste_ruta_h.append(estado.coste_h)
        coste_ruta_f.append(estado.coste_f)
        # print(estado.coste_g, estado.coste_h, estado.coste_f)
        if estado.padre is None:
            i = False
        estado = estado.padre

    # Si f(n) != g(n) + h(n) no es admisible
    if round(sum(coste_ruta_f), 2) != round((sum(coste_ruta_g) + sum(coste_ruta_h)), 2):
        return "ERROR: suma de costes no es correcta"

    # Si h(n) > h(n') no es admisible"
    for i in range(len(coste_ruta_h)-1):
        if coste_ruta_h[i] > coste_ruta_h[i+1]:
            return "ERROR: heurística no es admisible"

    # Si h(n) > g(n), no es admisible, en caso de estar en el estado meta
    
    return "Heurística y costes admisibles"
