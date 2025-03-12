# Comprendiendo los Objetos de Primera Clase en Python

En Python, todo se trata como un objeto. Esto incluye funciones y tipos. ¿Qué significa esto? Bueno, significa que puedes almacenar funciones y tipos en estructuras de datos, pasarlos como argumentos a otras funciones e incluso devolverlos desde otras funciones. Este es un concepto muy poderoso, y lo vamos a explorar utilizando el procesamiento de datos CSV como ejemplo.

## Explorando Tipos de Primera Clase

Primero, comencemos el intérprete de Python. Abre una nueva terminal en el WebIDE y escribe el siguiente comando. Este comando iniciará el intérprete de Python, donde ejecutaremos nuestro código Python.

```bash
python3
```

Cuando trabajamos con archivos CSV en Python, a menudo necesitamos convertir las cadenas que leemos de estos archivos en los tipos de datos adecuados. Por ejemplo, un número en un archivo CSV podría leerse como una cadena, pero queremos usarlo como un entero o un flotante en nuestro código Python. Para hacer esto, podemos crear una lista de funciones de conversión.

```python
coltypes = [str, int, float]
```

Observa que estamos creando una lista que contiene las funciones de tipo reales, no cadenas. En Python, los tipos son objetos de primera clase, lo que significa que podemos tratarlos como cualquier otro objeto. Podemos ponerlos en listas, pasarlos de un lugar a otro y usarlos en nuestro código.

Ahora, leamos algunos datos de un archivo CSV de cartera para ver cómo podemos usar estas funciones de conversión.

```python
import csv
f = open('portfolio.csv')
rows = csv.reader(f)
headers = next(rows)
row = next(rows)
print(row)
```

Cuando ejecutes este código, deberías ver una salida similar a la siguiente. Esta es la primera fila de datos del archivo CSV, representada como una lista de cadenas.

```
['AA', '100', '32.20']
```

A continuación, usaremos la función `zip`. La función `zip` toma múltiples iterables (como listas o tuplas) y empareja sus elementos. La usaremos para emparejar cada valor de la fila con su función de conversión de tipo correspondiente.

```python
r = list(zip(coltypes, row))
print(r)
```

Esto producirá la siguiente salida. Cada par contiene una función de tipo y un valor de cadena del archivo CSV.

```
[(<class 'str'>, 'AA'), (<class 'int'>, '100'), (<class 'float'>, '32.20')]
```

Ahora que tenemos estos pares, podemos aplicar cada función para convertir los valores a sus tipos adecuados.

```python
record = [func(val) for func, val in zip(coltypes, row)]
print(record)
```

La salida mostrará que los valores se han convertido a sus tipos adecuados. La cadena 'AA' sigue siendo una cadena, '100' se convierte en el entero 100 y '32.20' se convierte en el flotante 32.2.

```
['AA', 100, 32.2]
```

También podemos combinar estos valores con sus nombres de columna para crear un diccionario. Un diccionario es una estructura de datos útil en Python que nos permite almacenar pares clave - valor.

```python
record_dict = dict(zip(headers, record))
print(record_dict)
```

La salida será un diccionario donde las claves son los nombres de las columnas y los valores son los datos convertidos.

```
{'name': 'AA', 'shares': 100, 'price': 32.2}
```

Puedes realizar todos estos pasos en una comprensión única. Una comprensión es una forma concisa de crear listas, diccionarios o conjuntos en Python.

```python
result = {name: func(val) for name, func, val in zip(headers, coltypes, row)}
print(result)
```

La salida será el mismo diccionario que antes.

```
{'name': 'AA', 'shares': 100, 'price': 32.2}
```

Cuando hayas terminado de trabajar en el intérprete de Python, puedes salir de él escribiendo el siguiente comando.

```python
exit()
```

Esta demostración muestra cómo el tratamiento de las funciones como objetos de primera clase en Python permite técnicas de procesamiento de datos poderosas. Al poder tratar tipos y funciones como objetos, podemos escribir código más flexible y conciso.
