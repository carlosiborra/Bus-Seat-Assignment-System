# HyO. Práctica 2 por 100451170 y 100451258

Proyecto 2 la asignatura "Heurística y Optimización" del grado de ingeniería informática, curso 3, cuatrimestre 1. Universidad Carlos III de Madrid.
`<br/><br/>`

## Requisitos

- Se recomienda usar Python 3.10.8
- Se recomienda usar un entorno virtual para instalar las dependencias
- Instalar las dependencias (en requirements.txt)
  `<br/><br/>`

## Notas a leer

- Para entrar en el virtualenv (venv):

  - Windows: `venv\Scripts\activate.bat`
  - Linux: `source venv/bin/activate`
  - O simplemente añadir un nuevo terminal en VSCode y seleccionar el entorno virtual.
- Para instalar las dependencias (una vez dentro del venv):

  - `pip install -r requirements.txt`
- Para ver correctamente el color de los comentarios (!, ?, * ...) en el código, instalar la extensión "Better Comments" en VSCode.
- Para poder ejecutarlo correctamente, debemos ejecutar el archivo desde un Bash (el de git mismamente) (en VSCode, añadir un nuevo terminal y seleccionar bash). Si no, no funcionará correctamente.
  `<br/>`De todas maneras, se puede ejecutar desde Linux (recomendado).`<br/>` Imágen de ejemplo de ejecución (*con el comando sh ./parte-1/code/CSP-calls.sh*):`<br/>`
  ![1669374620519](image/README/1669374620519.png)
  `<br/><br/>`

## TODO's

### Parte 1 - TODO's

- [X] Crear el repositorio
- [X] Crear el README.md
- [X] Crear el .gitignore
- [X] Crear el venv
- [X] Crear el requirements.txt
- [X] Externalizar las funciones
- [X] Crear la restricción de los hermanos
- [X] Crear la restricción de los hermanos
- [X] Crear la función write al archivo de salida
- [X] Sacar 3 soluciones DISTINTAS y ALEATORIAS
- [X] Crear el archivo .sh para ejecutar el código
- [X] Eliminar variables (listas) no usadas
- [X] CREAR 15 TESTS ESPECÍFICOS, CHECK BOUNDARIES !!
- [X] SACAR TODO DE LA CARPETA CODE, REORDENAR !!
  `<br/>`

### Parte 2 - TODO's

- [X] Eliminar duplicados
- [X] Añadir las funciones externas necesarias para que funcione A*
- [X] Añadir cola_total sacado del resultado de la parte 1
- [X] Crear heuríticas nuevas, más eficientes; estaría bien que fueran mínimo 3
  - [X] Crear heurística 1
  - [X] Crear heurística 2
  - [X] Crear heurística 3
- [X] Exportar el resultado de la parte 2
  - [X] Estadísticas
  - [X] Resultados
- [X] CREAR 15 TESTS ESPECÍFICOS, CHECK BOUNDARY VALUES !!
- [X] Automatizar la comprobación de la validez de las soluciones, costes y heurísticas
- [X] Comentar mejor el A*
  `<br/><br/>`

## Dudas a responder

### Parte 1 - Dudas

- [X] ¿Se debe seguir de forma estricta la distribución de los ficheros?
- [X] ¿Se puede usar el bus con posición vertical? Es más eficiente que el horizontal (que aparece en el pdf).
- [X] ¿Es necesario usar X, C y R's en las estructuras de las tuplas?
- [X] ¿Cuentan las puertas y el chofer como posiciones del bus? (de la misma forma que el pasillo no lo hace)
- [X] ¿Se han de crear listas externas o es irrelevante, tema de velocidad, optimización...?
- [X] ¿Afectan las pertas a los alumnos conflictivos (entre ciclo 1 y 2)? o ¿siguen tienendo que dejar espacio con otro conflictivos sin contar las puertas?
- [X] ¿Se puede usar el formato de path: *python ./parte-1/code/CSPCargaBUS.py ./parte-1/CSP-tests/alumnos00*?
- [X] ¿Ha de ser la primera solución aleatoria también o la primera que se lanza? Ahora mismo los 3 resultados son aleatorios.
- [X] Tamaño y longitud de los tests, complejidad, etc.
- [X] Forma de exportar los resultados
- [X] ¿Si hay un alumno de movilidad reducida en 2, puede sentarse otro en 3?
  `<br/>`

### Parte 2 - Dudas

- [X] ¿El formato de los test debe ser las soluciones anteriores, con el num total y las aleatorias?
- [X] Si un alumno tiene delante un conflictivo y encima este tiene menor id, ¿se multiplica x4?
- [X] Se coge como archivo test un predet. o uno de la parte 1?
- [X] Resto de dudas no formuladas ya resultas
- [X] Si no se encuentra solución, ¿se deben exportar las estadísticas?
  `<br/><br/>`
