""" data.py by 100451170 & 100451258 """


# ! Definición de las variables
# Estructura de las variables:
# ? alumno = [id, ciclo, conflictividad, movilidad, id_hermano]
    # ? id = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...] -> id del alumno
    # ? ciclo = [1, 2] -> 1: 1º ciclo, 2: 2º ciclo
    # ? conflictividad = [C, X] -> C: conflictivo, X: no conflictivo
    # ? movilidad = [R,X] -> R: movilidad reducida, X: sin movilidad reducida
    # ? id_hermano = [1, 2, 3, 4...] -> 0: no tiene hermano

# ! Estructura del tablero (autobús):
# Nota: C=chofer, P=puerta, *=pasillo
# !     C  C  * P  P
# ?     1  2  * 3  4  -> 0
#       5  6  * 7  8  -> 1
#       9  10 * 11 12 -> 2
# ?     13 14 * 15 16 -> 3
# !     P  P  * P  P
# ?     17 18 * 19 20 -> 4
#       21 22 * 23 24 -> 5
#       25 26 * 27 28 -> 6
#       29 30 * 31 32 -> 7


# ! Nota: no se considera ni el pasillo, ni el chófer ni las puertas como parte de la solución
# ! Esto se debe a que no se impone ninguna restricción sobre estos, pero se tendrán en cuenta

dominio_movilidad_reducida = [(0,0), (0,1), (0,2), (0,3), (3,0), (3,1), (3,2), (3,3),
                              (4,0), (4,1), (4,2), (4,3)]
# Nota: son las posiciones: (fila, columna) de los alumnos con movilidad reducida (asientos)
# 1, 2, 3, 4, 13, 14, 15, 16, 17, 18, 19, 20

dominio_sin_movilidad_reducida = [(1,0), (1,1), (1,2), (1,3), (2,0), (2,1), (2,2), (2,3),
                                  (5,0), (5,1), (5,2), (5,3), (6,0), (6,1), (6,2), (6,3),
                                  (7,0), (7,1), (7,2), (7,3)]
# Nota: son las posiciones de los alumnos sin movilidad reducida (asientos)
# 5, 6, 7, 8, 9, 10, 11, 12, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32

dominio_primer_ciclo = [(0,0), (0,1), (0,2), (0,3), (1,0), (1,1), (1,2), (1,3), (2,0),
                        (2,1), (2,2), (2,3), (3,0), (3,1), (3,2), (3,3)]
# Nota: son las posiciones de los alumnos del primer ciclo (asientos)
# 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16

dominio_segundo_ciclo = [(4,0), (4,1), (4,2), (4,3), (5,0), (5,1), (5,2), (5,3), (6,0),
                         (6,1), (6,2), (6,3), (7,0), (7,1), (7,2), (7,3)]
# Nota: son las posiciones de los alumnos del segundo ciclo (asientos)
# 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32
