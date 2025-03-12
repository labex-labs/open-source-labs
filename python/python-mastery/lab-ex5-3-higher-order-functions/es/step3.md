# Refactorización de funciones existentes

Ahora, hemos creado una función de orden superior llamada `convert_csv()`. Las funciones de orden superior son funciones que pueden tomar otras funciones como argumentos o devolver funciones como resultados. Son un concepto poderoso en Python que puede ayudarnos a escribir código más modular y reutilizable. En esta sección, usaremos esta función de orden superior para refactorizar las funciones originales `csv_as_dicts()` y `csv_as_instances()`. La refactorización es el proceso de reorganizar el código existente sin cambiar su comportamiento externo, con el objetivo de mejorar su estructura interna, como eliminar la duplicación de código.

Comencemos abriendo el archivo `reader.py` en el WebIDE. Actualizaremos las funciones de la siguiente manera:

1. Primero, reemplazaremos la función `csv_as_dicts()`. Esta función se utiliza para convertir líneas de datos CSV en una lista de diccionarios. Aquí está el nuevo código:

```python
def csv_as_dicts(lines, types, *, headers=None):
    '''
    Convert lines of CSV data into a list of dictionaries
    '''
    def dict_converter(headers, row):
        return {name: func(val) for name, func, val in zip(headers, types, row)}

    return convert_csv(lines, dict_converter, headers=headers)
```

En este código, definimos una función interna `dict_converter` que toma `headers` y `row` como argumentos. Utiliza una comprensión de diccionario para crear un diccionario donde las claves son los nombres de los encabezados y los valores son el resultado de aplicar la función de conversión de tipo correspondiente a los valores de la fila. Luego, llamamos a la función `convert_csv()` con la función `dict_converter` como argumento.

2. A continuación, reemplazaremos la función `csv_as_instances()`. Esta función se utiliza para convertir líneas de datos CSV en una lista de instancias de una clase dada. Aquí está el nuevo código:

```python
def csv_as_instances(lines, cls, *, headers=None):
    '''
    Convert lines of CSV data into a list of instances
    '''
    def instance_converter(headers, row):
        return cls.from_row(row)

    return convert_csv(lines, instance_converter, headers=headers)
```

En este código, definimos una función interna `instance_converter` que toma `headers` y `row` como argumentos. Llama al método de clase `from_row` de la clase `cls` dada para crear una instancia a partir de la fila. Luego, llamamos a la función `convert_csv()` con la función `instance_converter` como argumento.

Después de refactorizar estas funciones, debemos probarlas para asegurarnos de que sigan funcionando como se espera. Para hacer esto, ejecutaremos los siguientes comandos en una shell de Python:

```bash
cd ~/project
python3 -i reader.py
```

El comando `cd ~/project` cambia el directorio de trabajo actual al directorio `project`. El comando `python3 -i reader.py` ejecuta el archivo `reader.py` en modo interactivo, lo que significa que podemos continuar ejecutando código Python después de que el archivo haya terminado de ejecutarse.

Una vez abierta la shell de Python, ejecutaremos el siguiente código para probar las funciones refactorizadas:

```python
# Define a simple Stock class for testing
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @classmethod
    def from_row(cls, row):
        return cls(row[0], int(row[1]), float(row[2]))

    def __repr__(self):
        return f'Stock({self.name}, {self.shares}, {self.price})'

# Test csv_as_dicts
with open('portfolio.csv') as f:
    portfolio_dicts = csv_as_dicts(f, [str, int, float])
print("First dictionary:", portfolio_dicts[0])

# Test csv_as_instances
with open('portfolio.csv') as f:
    portfolio_instances = csv_as_instances(f, Stock)
print("First instance:", portfolio_instances[0])
```

En este código, primero definimos una clase `Stock` simple para pruebas. El método `__init__` inicializa los atributos de una instancia de `Stock`. El método de clase `from_row` crea una instancia de `Stock` a partir de una fila de datos CSV. El método `__repr__` proporciona una representación en cadena de la instancia de `Stock`.

Luego, probamos la función `csv_as_dicts()` abriendo el archivo `portfolio.csv` y pasándolo a la función junto con una lista de funciones de conversión de tipo. Imprimimos el primer diccionario de la lista resultante.

Finalmente, probamos la función `csv_as_instances()` abriendo el archivo `portfolio.csv` y pasándolo a la función junto con la clase `Stock`. Imprimimos la primera instancia de la lista resultante.

Si todo está funcionando correctamente, deberías ver una salida similar a la siguiente:

```
First dictionary: {'name': 'AA', 'shares': 100, 'price': 32.2}
First instance: Stock(AA, 100, 32.2)
```

Esta salida indica que nuestras funciones refactorizadas están funcionando correctamente. Hemos eliminado con éxito la duplicación de código mientras mantenemos la misma funcionalidad.

Para salir de la shell de Python, puedes escribir `exit()` o presionar Ctrl+D.
