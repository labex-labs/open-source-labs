# Comprendiendo el contexto

En ejercicios anteriores, es posible que hayas encontrado código que lee archivos CSV y almacena los datos en diversas estructuras de datos. El propósito de este código es tomar los datos de texto sin procesar de un archivo CSV y convertirlos en objetos de Python más útiles, como diccionarios o instancias de clase. Esta conversión es esencial porque nos permite trabajar con los datos de una manera más estructurada y significativa dentro de nuestros programas de Python.

El patrón típico para leer archivos CSV suele seguir una estructura específica. Aquí tienes un ejemplo de una función que lee un archivo CSV y convierte cada fila en un diccionario:

```python
import csv

def read_csv_as_dicts(filename, types):
    records = []
    with open(filename) as file:
        rows = csv.reader(file)
        headers = next(rows)
        for row in rows:
            record = { name: func(val)
                       for name, func, val in zip(headers, types, row) }
            records.append(record)
    return records
```

Analicemos cómo funciona esta función. En primer lugar, importa el módulo `csv`, que proporciona funcionalidades para trabajar con archivos CSV en Python. La función toma dos parámetros: `filename`, que es el nombre del archivo CSV a leer, y `types`, que es una lista de funciones utilizadas para convertir los datos de cada columna al tipo de dato adecuado.

Dentro de la función, se inicializa una lista vacía llamada `records` para almacenar los diccionarios que representan cada fila del archivo CSV. Luego, se abre el archivo utilizando la declaración `with`, que asegura que el archivo se cierre correctamente después de ejecutar el bloque de código. La función `csv.reader` se utiliza para crear un iterador que lee cada fila del archivo CSV. Se asume que la primera fila son los encabezados, por lo que se recupera utilizando la función `next`.

A continuación, la función itera sobre las filas restantes del archivo CSV. Para cada fila, crea un diccionario utilizando una comprensión de diccionario. Las claves del diccionario son los encabezados de las columnas, y los valores son el resultado de aplicar la función de conversión de tipo correspondiente de la lista `types` al valor de la fila. Finalmente, el diccionario se agrega a la lista `records`, y la función devuelve la lista de diccionarios.

Ahora, veamos una función similar que lee datos de un archivo CSV en instancias de clase:

```python
def read_csv_as_instances(filename, cls):
    records = []
    with open(filename) as file:
        rows = csv.reader(file)
        headers = next(rows)
        for row in rows:
            record = cls.from_row(row)
            records.append(record)
    return records
```

Esta función es similar a la anterior, pero en lugar de crear diccionarios, crea instancias de una clase. La función toma dos parámetros: `filename`, que es el nombre del archivo CSV a leer, y `cls`, que es la clase cuyas instancias se crearán.

Dentro de la función, sigue una estructura similar a la función anterior. Inicializa una lista vacía llamada `records` para almacenar las instancias de clase. Luego, abre el archivo, lee los encabezados y itera sobre las filas restantes. Para cada fila, llama al método `from_row` de la clase `cls` para crear una instancia de la clase utilizando los datos de la fila. La instancia se agrega a la lista `records`, y la función devuelve la lista de instancias.

En este laboratorio, refactorizaremos estas funciones para hacerlas más flexibles y robustas. También exploraremos el sistema de sugerencias de tipo (type hinting) de Python, que nos permite especificar los tipos esperados de los parámetros y valores de retorno de nuestras funciones. Esto puede hacer que nuestro código sea más legible y fácil de entender, especialmente para otros desarrolladores que puedan trabajar con nuestro código.

Comencemos creando un archivo `reader.py` y agregando estas funciones iniciales a él. Asegúrate de probar estas funciones para garantizar que funcionen correctamente antes de pasar a los siguientes pasos.
