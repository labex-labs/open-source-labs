# Tubería básica de generadores con datos CSV

En este paso, aprenderemos cómo crear una tubería de procesamiento básica utilizando generadores. Pero primero, entendamos qué son los generadores. Los generadores son un tipo especial de iterador en Python. A diferencia de los iteradores normales que pueden cargar todos los datos en memoria a la vez, los generadores generan valores a demanda. Esto es extremadamente útil cuando se trabaja con grandes flujos de datos porque ahorra memoria. En lugar de tener que almacenar todo el conjunto de datos en memoria, el generador produce valores uno por uno según los necesites.

## Comprender los generadores

Un generador es esencialmente una función que devuelve un iterador. Cuando iteras sobre este iterador, produce una secuencia de valores. La forma en que se escribe una función generadora es similar a una función normal, pero hay una diferencia clave. En lugar de usar la declaración `return`, una función generadora utiliza la declaración `yield`. La declaración `yield` tiene un comportamiento único. Pausa la función y guarda su estado actual. Cuando se solicita el siguiente valor, la función continúa desde donde se detuvo. Esto permite que el generador produzca valores de forma incremental sin tener que comenzar desde el principio cada vez.

## Usar la función `follow()`

La función `follow()` que creaste anteriormente funciona de manera similar al comando Unix `tail -f`. El comando `tail -f` monitorea continuamente un archivo en busca de nuevo contenido, y lo mismo hace la función `follow()`. Ahora, usémosla para crear una simple tubería de procesamiento.

### Paso 1: Abrir una nueva ventana de terminal

Primero, abre una nueva ventana de terminal en el WebIDE. Puedes hacerlo yendo a `Terminal → New Terminal`. Esta nueva terminal será donde ejecutaremos nuestros comandos de Python.

### Paso 2: Iniciar una shell interactiva de Python

Una vez que la nueva terminal esté abierta, inicia una shell interactiva de Python. Puedes hacerlo ingresando el siguiente comando en la terminal:

```bash
python3
```

La shell interactiva de Python te permite ejecutar código de Python línea por línea y ver los resultados inmediatamente.

### Paso 3: Importar la función `follow` y configurar la tubería

Ahora, importaremos la función `follow` y configuraremos una tubería básica para leer los datos de las acciones. En la shell interactiva de Python, ingresa el siguiente código:

```python
>>> from follow import follow
>>> import csv
>>> lines = follow('stocklog.csv')
>>> rows = csv.reader(lines)
>>> for row in rows:
...     print(row)
...
```

Esto es lo que hace cada línea:

- `from follow import follow`: Esto importa la función `follow` del módulo `follow`.
- `import csv`: Esto importa el módulo `csv`, que se utiliza para leer y escribir archivos CSV en Python.
- `lines = follow('stocklog.csv')`: Esto llama a la función `follow` con el nombre de archivo `stocklog.csv`. La función `follow` devuelve un generador que produce nuevas líneas a medida que se agregan al archivo.
- `rows = csv.reader(lines)`: La función `csv.reader()` toma las líneas generadas por la función `follow` y las analiza en filas de datos CSV.
- El bucle `for` itera a través de estas filas y las imprime una por una.

### Paso 4: Verificar la salida

Después de ejecutar el código, deberías ver una salida similar a esta (tus datos variarán):

```
['BA', '98.35', '6/11/2007', '09:41.07', '0.16', '98.25', '98.35', '98.31', '158148']
['AA', '39.63', '6/11/2007', '09:41.07', '-0.03', '39.67', '39.63', '39.31', '270224']
['XOM', '82.45', '6/11/2007', '09:41.07', '-0.23', '82.68', '82.64', '82.41', '748062']
['PG', '62.95', '6/11/2007', '09:41.08', '-0.12', '62.80', '62.97', '62.61', '454327']
...
```

Esta salida indica que has creado exitosamente una tubería de datos. La función `follow()` genera líneas del archivo, y luego estas líneas se pasan a la función `csv.reader()`, que las analiza en filas de datos.

Si has visto suficiente salida, puedes detener la ejecución presionando `Ctrl+C`.

## ¿Qué está pasando?

Desglosemos lo que está sucediendo en esta tubería:

1. `follow('stocklog.csv')` crea un generador. Este generador sigue el archivo `stocklog.csv` y produce nuevas líneas a medida que se agregan al archivo.
2. `csv.reader(lines)` toma las líneas generadas por la función `follow` y las analiza en datos de filas CSV. Entiende la estructura de los archivos CSV y divide las líneas en valores individuales.
3. Luego, el bucle `for` itera a través de estas filas, imprimiendo cada una. Esto te permite ver los datos en un formato legible.

Este es un ejemplo simple de una tubería de procesamiento de datos utilizando generadores. En los siguientes pasos, construiremos tuberías más complejas y útiles.
