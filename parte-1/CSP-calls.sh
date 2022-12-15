#!/bin/sh
# ? Forma inicial de ejecutar el sh: $ sh ./parte-1/CSP-calls.sh
# NOTA: se recomienda comentar parte de los tests para no saturar la consola
# Además cada test tiene su propósito y por ende se recomienda ejecutarlos por separado

# ! Test con solo 1 alumno, 16 soluciones posibles (ciclo 1 y 2)
# Nota: se ve como alumnos C y X puedan ser asignados a asientos de mov. reducida
# ? 00. Un alumno normal ciclo 1 -> Válido 16 posibles soluciones
python ./parte-1/CSPCargaBUS.py ./parte-1/CSP-tests/alumnos00
# ? 01. Un alumno normal, ciclo 2 -> Válido 16 posibles soluciones
python ./parte-1/CSPCargaBUS.py ./parte-1/CSP-tests/alumnos01
# ? 02. Un alumno conflictivo, ciclo 1 -> Válido 16 posibles soluciones
python ./parte-1/CSPCargaBUS.py ./parte-1/CSP-tests/alumnos02
# ? 03. Un alumno conflictivo, ciclo 2 -> Válido 16 posibles soluciones
python ./parte-1/CSPCargaBUS.py ./parte-1/CSP-tests/alumnos03


# ! Caso excepcional
# ? 04. Test de id de alumnos duplicados - Inválido
python ./parte-1/CSPCargaBUS.py ./parte-1/CSP-tests/alumnos04


# ! Tests de alumnos conflictivos (válidos e inválidos)
# ? 05. Tests de 5 alumnos conflictivos - Inválido
python ./parte-1/CSPCargaBUS.py ./parte-1/CSP-tests/alumnos05
# ? 06. Test de 5 alumnos conflictivos y mov. reducida - Inválido
python ./parte-1/CSPCargaBUS.py ./parte-1/CSP-tests/alumnos06
# ? 07. Test de mezcla de 5 alumnos conflictivos y mov. reducida - Inválido
python ./parte-1/CSPCargaBUS.py ./parte-1/CSP-tests/alumnos07

# ? 08. Test de 4 alumnos conflictivos es el máximo - Válido
python ./parte-1/CSPCargaBUS.py ./parte-1/CSP-tests/alumnos08
# ? 09. Test de 4 alumnos conflictivos y mov. reducida, ciclo 1 - Válido
python ./parte-1/CSPCargaBUS.py ./parte-1/CSP-tests/alumnos09
# ? 10. Test de 2 conflictivos y 2 de movilidad reducida - Válido
python ./parte-1/CSPCargaBUS.py ./parte-1/CSP-tests/alumnos10


# ! Test de movilidad reducida
# ? 11. 4 alumnos de mov. reducida ciclo 1 - Válido
python ./parte-1/CSPCargaBUS.py ./parte-1/CSP-tests/alumnos11
# ? 12. 2 alumnos de mov. reducida ciclo 2 - Válido
python ./parte-1/CSPCargaBUS.py ./parte-1/CSP-tests/alumnos12

# ? 13. 5 alumnos de mov. reducida ciclo 1 - Inválido
python ./parte-1/CSPCargaBUS.py ./parte-1/CSP-tests/alumnos13
# ? 14. 3 alumnos de mov. reducida ciclo 2 - Inválido
python ./parte-1/CSPCargaBUS.py ./parte-1/CSP-tests/alumnos14

# ? 15. 2 alumnos mov. red. y 1 alumno normal ciclo 2 - Válido
# 96 soluciones posibles al ser 16-4 (pos. normal) * 2^3
python ./parte-1/CSPCargaBUS.py ./parte-1/CSP-tests/alumnos15


# ! Test para el funcionamiento de los alumnos hermanos
# ? 16. Hermanos en el mismo ciclo 1 - Válido
python ./parte-1/CSPCargaBUS.py ./parte-1/CSP-tests/alumnos16
# ? 17. Hermanos en el mismo ciclo 2 - Válido
python ./parte-1/CSPCargaBUS.py ./parte-1/CSP-tests/alumnos17
# ? 18. Hermanos en diferentes ciclos (irán al ciclo 1), 8 soluciones - Válido
# Se observa como el mayor (1) va al asiento pegado al pasillo
python ./parte-1/CSPCargaBUS.py ./parte-1/CSP-tests/alumnos18
# ? 19. Hermanos en diferentes ciclos (irán al ciclo 1), 8 soluciones - Válido
# Se observa como el mayor (2) va al asiento pegado al pasillo
python ./parte-1/CSPCargaBUS.py ./parte-1/CSP-tests/alumnos19
# ? 20. Dos hermanos conflictivos - Válido
python ./parte-1/CSPCargaBUS.py ./parte-1/CSP-tests/alumnos20
# ? 21. Hermanos conflictivos en diferentes ciclos (irán al ciclo 1), 8 soluciones - Válido
# Se observa como el mayor (1) va al asiento pegado al pasillo
python ./parte-1/CSPCargaBUS.py ./parte-1/CSP-tests/alumnos21
# ? 22. Hermanos conflictivos en diferentes ciclos (irán al ciclo 1), 8 soluciones - Válido
# Se observa como el mayor (2) va al asiento pegado al pasillo
python ./parte-1/CSPCargaBUS.py ./parte-1/CSP-tests/alumnos22
# ? 23. Un hermano conflictivo y un hermano normal - Válido
python ./parte-1/CSPCargaBUS.py ./parte-1/CSP-tests/alumnos23
# ? 24. Dos hermanos conflictivos y 3 alumnos conflictivos - Válido
# Tener 5 conflictivos a la vez ahora es posible al ir dos hermanos juntos
python ./parte-1/CSPCargaBUS.py ./parte-1/CSP-tests/alumnos24

# ? 25. Dos hermanos conflictivos y 4 alumnos conflictivos - Inválido
python ./parte-1/CSPCargaBUS.py ./parte-1/CSP-tests/alumnos25

# ? 26. Un hermano de mov reducida y el otro normal, distinto ciclo - Válido
python ./parte-1/CSPCargaBUS.py ./parte-1/CSP-tests/alumnos26
# ? 27. Dos hermanos de mov reducida y distinto ciclo - Válido
python ./parte-1/CSPCargaBUS.py ./parte-1/CSP-tests/alumnos27
# ? 28. Dos hermanos de mov reducida y conflictivos, distinto ciclo - Válido
python ./parte-1/CSPCargaBUS.py ./parte-1/CSP-tests/alumnos28
# ? 29. Varios hermanos - Válido
python ./parte-1/CSPCargaBUS.py ./parte-1/CSP-tests/alumnos29


# ! Test de longitud mayor para ver como se comporta el algoritmo y su eficiencia
# ? 30. Test de ejemplo del enunciado - Válido
python ./parte-1/CSPCargaBUS.py ./parte-1/CSP-tests/alumnos30
# ? 31. Varios hermanos con diferentes cualidades - Válido
python ./parte-1/CSPCargaBUS.py ./parte-1/CSP-tests/alumnos31
# ? 32. Tests de prueba - Válido
python ./parte-1/CSPCargaBUS.py ./parte-1/CSP-tests/alumnos32
# ? 33. Tests de prueba - Válido
python ./parte-1/CSPCargaBUS.py ./parte-1/CSP-tests/alumnos33