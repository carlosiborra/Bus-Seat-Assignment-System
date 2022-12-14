#!/bin/sh
# ? Forma inicial de ejecutar el sh: $ sh ./parte-1/CSP-calls.sh
# python ./parte-2/ASTARColaBus.py ./parte-2/ASTAR-tests/alumnos.prob 1
# orden: rel_path ASTARColaBus.py - rel_path alumnos.prob - ID de la heuristica

# ? Alumnos00: un alumno normal -> posee solución de bajo coste
# python ./parte-2/ASTARColaBus.py ./parte-2/ASTAR-tests/alumnos00.prob 1
# python ./parte-2/ASTARColaBus.py ./parte-2/ASTAR-tests/alumnos00.prob 2
# python ./parte-2/ASTARColaBus.py ./parte-2/ASTAR-tests/alumnos00.prob 3
# python ./parte-2/ASTARColaBus.py ./parte-2/ASTAR-tests/alumnos00.prob 4
# python ./parte-2/ASTARColaBus.py ./parte-2/ASTAR-tests/alumnos00.prob 5

# ? Alumnos01: un alumno reducido -> no debe haber solución (final)
# python ./parte-2/ASTARColaBus.py ./parte-2/ASTAR-tests/alumnos01.prob 1
# python ./parte-2/ASTARColaBus.py ./parte-2/ASTAR-tests/alumnos01.prob 2
# python ./parte-2/ASTARColaBus.py ./parte-2/ASTAR-tests/alumnos01.prob 3
# python ./parte-2/ASTARColaBus.py ./parte-2/ASTAR-tests/alumnos01.prob 4
# python ./parte-2/ASTARColaBus.py ./parte-2/ASTAR-tests/alumnos01.prob 5

# ? Alumnos02: dos alumnos reducidos -> no debe haber solución (final y seguidos)
# python ./parte-2/ASTARColaBus.py ./parte-2/ASTAR-tests/alumnos02.prob 1
# python ./parte-2/ASTARColaBus.py ./parte-2/ASTAR-tests/alumnos02.prob 2
# python ./parte-2/ASTARColaBus.py ./parte-2/ASTAR-tests/alumnos02.prob 3
# python ./parte-2/ASTARColaBus.py ./parte-2/ASTAR-tests/alumnos02.prob 4
# python ./parte-2/ASTARColaBus.py ./parte-2/ASTAR-tests/alumnos02.prob 5

# ? Alumnos03: dos alumnos reducidos y uno normal -> más R que X + C - > no debe haber solución (final)
# python ./parte-2/ASTARColaBus.py ./parte-2/ASTAR-tests/alumnos03.prob 1
# python ./parte-2/ASTARColaBus.py ./parte-2/ASTAR-tests/alumnos03.prob 2
# python ./parte-2/ASTARColaBus.py ./parte-2/ASTAR-tests/alumnos03.prob 3
# python ./parte-2/ASTARColaBus.py ./parte-2/ASTAR-tests/alumnos03.prob 4
# python ./parte-2/ASTARColaBus.py ./parte-2/ASTAR-tests/alumnos03.prob 5

# ? Alumnos04: dos alumnos normales y uno reducido -> más X + C que R -> solución de bajo coste
# python ./parte-2/ASTARColaBus.py ./parte-2/ASTAR-tests/alumnos04.prob 1
# python ./parte-2/ASTARColaBus.py ./parte-2/ASTAR-tests/alumnos04.prob 2
# python ./parte-2/ASTARColaBus.py ./parte-2/ASTAR-tests/alumnos04.prob 3
# python ./parte-2/ASTARColaBus.py ./parte-2/ASTAR-tests/alumnos04.prob 4
# python ./parte-2/ASTARColaBus.py ./parte-2/ASTAR-tests/alumnos04.prob 5

# ? Alumnos05: tres alumnos reducidos y 2 conflictivos -> más R que X+C -> no debe haber solución (final)
# python ./parte-2/ASTARColaBus.py ./parte-2/ASTAR-tests/alumnos05.prob 1
# python ./parte-2/ASTARColaBus.py ./parte-2/ASTAR-tests/alumnos05.prob 2
# python ./parte-2/ASTARColaBus.py ./parte-2/ASTAR-tests/alumnos05.prob 3
# python ./parte-2/ASTARColaBus.py ./parte-2/ASTAR-tests/alumnos05.prob 4
# python ./parte-2/ASTARColaBus.py ./parte-2/ASTAR-tests/alumnos05.prob 5

# ? Alumnos06: un alumno reducido y uno normal -> solución de bajo coste
# python ./parte-2/ASTARColaBus.py ./parte-2/ASTAR-tests/alumnos06.prob 1
# python ./parte-2/ASTARColaBus.py ./parte-2/ASTAR-tests/alumnos06.prob 2
# python ./parte-2/ASTARColaBus.py ./parte-2/ASTAR-tests/alumnos06.prob 3
# python ./parte-2/ASTARColaBus.py ./parte-2/ASTAR-tests/alumnos06.prob 4
# python ./parte-2/ASTARColaBus.py ./parte-2/ASTAR-tests/alumnos06.prob 5

# ? Alumnos07: un alumno reducido y uno conflictivo -> solución de mayor coste que Alumnos06
# python ./parte-2/ASTARColaBus.py ./parte-2/ASTAR-tests/alumnos07.prob 1
# python ./parte-2/ASTARColaBus.py ./parte-2/ASTAR-tests/alumnos07.prob 2
# python ./parte-2/ASTARColaBus.py ./parte-2/ASTAR-tests/alumnos07.prob 3
# python ./parte-2/ASTARColaBus.py ./parte-2/ASTAR-tests/alumnos07.prob 4
# python ./parte-2/ASTARColaBus.py ./parte-2/ASTAR-tests/alumnos07.prob 5

# ! ZONA CONFLICTIVIDAD  ->  ÚTIL PARA VER DIFERENCIAS ENTRE HEURÍSTICAS, se observa la debilidad de la nuestra

# ? Alumnos08: un alumno conflictivo -> solución de bajo coste
# python ./parte-2/ASTARColaBus.py ./parte-2/ASTAR-tests/alumnos08.prob 1
# python ./parte-2/ASTARColaBus.py ./parte-2/ASTAR-tests/alumnos08.prob 2
# python ./parte-2/ASTARColaBus.py ./parte-2/ASTAR-tests/alumnos08.prob 3
# python ./parte-2/ASTARColaBus.py ./parte-2/ASTAR-tests/alumnos08.prob 4
# python ./parte-2/ASTARColaBus.py ./parte-2/ASTAR-tests/alumnos08.prob 5

# ? Alumnos09: dos alumnos conflictivos -> solución de mayor coste que Alumnos08
# python ./parte-2/ASTARColaBus.py ./parte-2/ASTAR-tests/alumnos09.prob 1
# python ./parte-2/ASTARColaBus.py ./parte-2/ASTAR-tests/alumnos09.prob 2
# python ./parte-2/ASTARColaBus.py ./parte-2/ASTAR-tests/alumnos09.prob 3
# python ./parte-2/ASTARColaBus.py ./parte-2/ASTAR-tests/alumnos09.prob 4
# python ./parte-2/ASTARColaBus.py ./parte-2/ASTAR-tests/alumnos09.prob 5

# ? Alumnos10: tres alumnos conflictivos -> solución de mayor coste que Alumnos09
# python ./parte-2/ASTARColaBus.py ./parte-2/ASTAR-tests/alumnos10.prob 1
# python ./parte-2/ASTARColaBus.py ./parte-2/ASTAR-tests/alumnos10.prob 2
# python ./parte-2/ASTARColaBus.py ./parte-2/ASTAR-tests/alumnos10.prob 3
# python ./parte-2/ASTARColaBus.py ./parte-2/ASTAR-tests/alumnos10.prob 4
# python ./parte-2/ASTARColaBus.py ./parte-2/ASTAR-tests/alumnos10.prob 5

# ? Alumnos11: cuatro alumnos conflictivos -> solución de mayor coste que Alumnos10
# python ./parte-2/ASTARColaBus.py ./parte-2/ASTAR-tests/alumnos11.prob 1
# python ./parte-2/ASTARColaBus.py ./parte-2/ASTAR-tests/alumnos11.prob 2
# python ./parte-2/ASTARColaBus.py ./parte-2/ASTAR-tests/alumnos11.prob 3
# python ./parte-2/ASTARColaBus.py ./parte-2/ASTAR-tests/alumnos11.prob 4
# python ./parte-2/ASTARColaBus.py ./parte-2/ASTAR-tests/alumnos11.prob 5

# ? Alumnos12: todo alumnos normales (4 alumnos) -> solución de menor coste que Alumnos11
# python ./parte-2/ASTARColaBus.py ./parte-2/ASTAR-tests/alumnos12.prob 1
# python ./parte-2/ASTARColaBus.py ./parte-2/ASTAR-tests/alumnos12.prob 2
# python ./parte-2/ASTARColaBus.py ./parte-2/ASTAR-tests/alumnos12.prob 3
# python ./parte-2/ASTARColaBus.py ./parte-2/ASTAR-tests/alumnos12.prob 4
# python ./parte-2/ASTARColaBus.py ./parte-2/ASTAR-tests/alumnos12.prob 5

# ? Alumnos13: caso normal de solución de Parte 1 sin conflictivos para mayor velocidad y forzando IDs de 2 dígitos
# python ./parte-2/ASTARColaBus.py ./parte-2/ASTAR-tests/alumnos13.prob 1
# python ./parte-2/ASTARColaBus.py ./parte-2/ASTAR-tests/alumnos13.prob 2
# python ./parte-2/ASTARColaBus.py ./parte-2/ASTAR-tests/alumnos13.prob 3
# python ./parte-2/ASTARColaBus.py ./parte-2/ASTAR-tests/alumnos13.prob 4
# python ./parte-2/ASTARColaBus.py ./parte-2/ASTAR-tests/alumnos13.prob 5

# ? Alumnos14: caso normal #1 de solución de la Parte 1 para comprobar correcto funcionamiento
# Nota: va a tardar mucho tiempo por la cantidad de alumnos que hay
# python ./parte-2/ASTARColaBus.py ./parte-2/ASTAR-tests/alumnos14.prob 1
# python ./parte-2/ASTARColaBus.py ./parte-2/ASTAR-tests/alumnos14.prob 2
# python ./parte-2/ASTARColaBus.py ./parte-2/ASTAR-tests/alumnos14.prob 3
# python ./parte-2/ASTARColaBus.py ./parte-2/ASTAR-tests/alumnos14.prob 4
# python ./parte-2/ASTARColaBus.py ./parte-2/ASTAR-tests/alumnos14.prob 5

# ? Alumnos15: caso normal #2 de la solución de la Parte 1 para comprobar correcto funcionamiento
# python ./parte-2/ASTARColaBus.py ./parte-2/ASTAR-tests/alumnos15.prob 1
# python ./parte-2/ASTARColaBus.py ./parte-2/ASTAR-tests/alumnos15.prob 2
# python ./parte-2/ASTARColaBus.py ./parte-2/ASTAR-tests/alumnos15.prob 3
# python ./parte-2/ASTARColaBus.py ./parte-2/ASTAR-tests/alumnos15.prob 4
# python ./parte-2/ASTARColaBus.py ./parte-2/ASTAR-tests/alumnos15.prob 5

# ? Alumnos16: caso normal #3 de la solución de la Parte 1 para comprobar correcto funcionamiento
# python ./parte-2/ASTARColaBus.py ./parte-2/ASTAR-tests/alumnos16.prob 1
# python ./parte-2/ASTARColaBus.py ./parte-2/ASTAR-tests/alumnos16.prob 2
# python ./parte-2/ASTARColaBus.py ./parte-2/ASTAR-tests/alumnos16.prob 3
# python ./parte-2/ASTARColaBus.py ./parte-2/ASTAR-tests/alumnos16.prob 4
# python ./parte-2/ASTARColaBus.py ./parte-2/ASTAR-tests/alumnos16.prob 5
