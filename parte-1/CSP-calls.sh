#!/bin/sh
# ? Forma inicial de ejecutar el sh: $ sh ./parte-1/CSP-calls.sh
# NOTA: los tests están comentados debido al tamaño y que cada uno comprueba cosas distintas
# Además de que hay tests que fuerzan que de 0 soluciones posibles o errores

# ! Test de solo 1 alumno, 16 soluciones posibles (ciclo 1 y 2)
# Nota: se ve como alumnos C y X puedan ser asignados a asientos de mov. reducida
# ? Un alumno normal ciclo 1 -> Válido 16 posibles soluciones
# python ./parte-1/CSPCargaBUS.py ./parte-1/CSP-tests/alumnos00
# ? Un alumno normal, ciclo 2 -> Válido 16 posibles soluciones
# python ./parte-1/CSPCargaBUS.py ./parte-1/CSP-tests/alumnos01
# ? Un alumno conflictivo, ciclo 1 -> Válido 16 posibles soluciones
# python ./parte-1/CSPCargaBUS.py ./parte-1/CSP-tests/alumnos02
# ? Un alumno conflictivo, ciclo 2 -> Válido 16 posibles soluciones
# python ./parte-1/CSPCargaBUS.py ./parte-1/CSP-tests/alumnos03

# ! Test de boundary conditions que lleven a 0 soluciones posibles
# ? Test de id de alumnos duplicados - Inválido
# python ./parte-1/CSPCargaBUS.py ./parte-1/CSP-tests/alumnos09
# ? Tests de 5 alumnos conflictivos - Inválido
# python ./parte-1/CSPCargaBUS.py ./parte-1/CSP-tests/alumnos04
# ? Test de 5 alumnos conflictivos y mov. reducida - Inválido
# python ./parte-1/CSPCargaBUS.py ./parte-1/CSP-tests/alumnos05
# ? Test de 5 alumnos conflictivos y otros de mov. reducida - Inválido
# python ./parte-1/CSPCargaBUS.py ./parte-1/CSP-tests/alumnos06
# ? Test de 4 alumnos conflictivos es el máximo Válido
# python ./parte-1/CSPCargaBUS.py ./parte-1/CSP-tests/alumnos07
# ? Test de 4 alumnos conflictivos y mov. reducida, ciclo 1 - Válido
# python ./parte-1/CSPCargaBUS.py ./parte-1/CSP-tests/alumnos19
# ?  conflictivos y 2 de movilidad reducida - Válido
# python ./parte-1/CSPCargaBUS.py ./parte-1/CSP-tests/alumnos08

# ! Test de movilidad reducida
# ? 4 alumnos de mov. reducida ciclo 1 - Válido
# python ./parte-1/CSPCargaBUS.py ./parte-1/CSP-tests/alumnos10
# ? 2 alumnos de mov. reducida ciclo 2 - Válido
# python ./parte-1/CSPCargaBUS.py ./parte-1/CSP-tests/alumnos11
# ? 5 alumnos de mov. reducida ciclo 1 - Inválido
# python ./parte-1/CSPCargaBUS.py ./parte-1/CSP-tests/alumnos12
# ? 3 alumnos de mov. reducida ciclo 2 - Inválido
# python ./parte-1/CSPCargaBUS.py ./parte-1/CSP-tests/alumnos13
# ? 2 alumnos mov. red. y 1 alumno normal ciclo 2 - Válido
# 96 soluciones posibles al ser 16-4 (pos. normal) * 2^3
# python ./parte-1/CSPCargaBUS.py ./parte-1/CSP-tests/alumnos14

# ! Test para el funcionamiento de los alumnos hermanos
# ? Hermanos en el mismo ciclo 1 - Válido
# python ./parte-1/CSPCargaBUS.py ./parte-1/CSP-tests/alumnos15
# ? Hermanos en el mismo ciclo 2 - Válido
# python ./parte-1/CSPCargaBUS.py ./parte-1/CSP-tests/alumnos16
# ? Hermanos en diferentes ciclos (irán al ciclo 1), 8 soluciones - Válido
# Se observa como el mayor (1) va al asiento pegado al pasillo
# python ./parte-1/CSPCargaBUS.py ./parte-1/CSP-tests/alumnos17
# ? Hermanos en diferentes ciclos (irán al ciclo 1), 8 soluciones - Válido
# Se observa como el mayor (2) va al asiento pegado al pasillo
# python ./parte-1/CSPCargaBUS.py ./parte-1/CSP-tests/alumnos18
# ? Dos hermanos conflictivos - Válido
# python ./parte-1/CSPCargaBUS.py ./parte-1/CSP-tests/alumnos20
# ? Un hermano conflictivo y un hermano normal - Válido
# python ./parte-1/CSPCargaBUS.py ./parte-1/CSP-tests/alumnos25
# ? Dos hermanos conflictivos y 3 alumnos conflictivos - Válido
# Tener 5 conflictivos a la vez ahora es posible al ir dos hermanos juntos
# python ./parte-1/CSPCargaBUS.py ./parte-1/CSP-tests/alumnos21
# ? Dos hermanos conflictivos y 4 alumnos conflictivos - Inválido
# python ./parte-1/CSPCargaBUS.py ./parte-1/CSP-tests/alumnos22
# ? Un hermano de mov reducida y el otro normal, distinto ciclo - Válido
# python ./parte-1/CSPCargaBUS.py ./parte-1/CSP-tests/alumnos28
# ? Dos hermanos de mov reducida y distinto ciclo - Válido
# python ./parte-1/CSPCargaBUS.py ./parte-1/CSP-tests/alumnos23
# ? Dos hermanos de mov reducida y conflictivos - Válido
# python ./parte-1/CSPCargaBUS.py ./parte-1/CSP-tests/alumnos26
# ? Varios hermanos - Válido
# python ./parte-1/CSPCargaBUS.py ./parte-1/CSP-tests/alumnos24

# ! Test de longitud mayor para ver como se comporta el algoritmo y su eficiencia
# ? Test del enunciado - Válido
# python ./parte-1/CSPCargaBUS.py ./parte-1/CSP-tests/alumnos27
# ? Varios hermanos con diferentes cualidades - Válido
# python ./parte-1/CSPCargaBUS.py ./parte-1/CSP-tests/alumnos29
# ? Tests de prueba - Válidos
# python ./parte-1/CSPCargaBUS.py ./parte-1/CSP-tests/alumnos30
# python ./parte-1/CSPCargaBUS.py ./parte-1/CSP-tests/alumnos31
# python ./parte-1/CSPCargaBUS.py ./parte-1/CSP-tests/alumnos32