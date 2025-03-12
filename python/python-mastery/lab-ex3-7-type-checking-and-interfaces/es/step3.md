# Creación de clases de plantilla de algoritmo

En este paso, vamos a utilizar clases base abstractas para implementar un patrón de método plantilla. El objetivo es reducir la duplicación de código en la funcionalidad de análisis de archivos CSV. La duplicación de código puede dificultar el mantenimiento y la actualización de tu código. Al utilizar el patrón de método plantilla, podemos crear una estructura común para nuestro código de análisis de CSV y permitir que las subclases manejen los detalles específicos.

## Comprender el patrón de método plantilla

El patrón de método plantilla es un patrón de diseño de comportamiento. Es como un plano para un algoritmo. En un método, define la estructura general o el "esqueleto" de un algoritmo. Sin embargo, no implementa completamente todos los pasos. En lugar de eso, pospone algunos de los pasos a las subclases. Esto significa que las subclases pueden redefinir ciertas partes del algoritmo sin cambiar su estructura general.

En nuestro caso, si miras el archivo `reader.py`, notarás que las funciones `read_csv_as_dicts()` y `read_csv_as_instances()` tienen mucho código similar. La principal diferencia entre ellas es cómo crean registros a partir de las filas del archivo CSV. Al utilizar el patrón de método plantilla, podemos evitar escribir el mismo código varias veces.

## Agregar la clase base CSVParser

Comencemos agregando una clase base abstracta para nuestro análisis de CSV. Abre el archivo `reader.py`. Agregaremos la clase base abstracta `CSVParser` justo en la parte superior del archivo, después de las declaraciones de importación.

```python
# reader.py
import csv
from abc import ABC, abstractmethod

class CSVParser(ABC):
    def parse(self, filename):
        records = []
        with open(filename) as f:
            rows = csv.reader(f)
            headers = next(rows)
            for row in rows:
                record = self.make_record(headers, row)
                records.append(record)
        return records

    @abstractmethod
    def make_record(self, headers, row):
        pass
```

Esta clase `CSVParser` sirve como una plantilla para el análisis de CSV. El método `parse` contiene los pasos comunes para leer un archivo CSV, como abrir el archivo, obtener los encabezados y recorrer las filas. La lógica específica para crear un registro a partir de una fila se abstrae en el método `make_record()`. Dado que es un método abstracto, cualquier clase que herede de `CSVParser` debe implementar este método.

## Implementar las clases de analizador concretas

Ahora que tenemos nuestra clase base, necesitamos crear las clases de analizador concretas. Estas clases implementarán la lógica específica de creación de registros.

```python
class DictCSVParser(CSVParser):
    def __init__(self, types):
        self.types = types

    def make_record(self, headers, row):
        return { name: func(val) for name, func, val in zip(headers, self.types, row) }

class InstanceCSVParser(CSVParser):
    def __init__(self, cls):
        self.cls = cls

    def make_record(self, headers, row):
        return self.cls.from_row(row)
```

La clase `DictCSVParser` se utiliza para crear registros como diccionarios. Toma una lista de tipos en su constructor. El método `make_record` utiliza estos tipos para convertir los valores de la fila y crear un diccionario.

La clase `InstanceCSVParser` se utiliza para crear registros como instancias de una clase. Toma una clase en su constructor. El método `make_record` llama al método `from_row` de esa clase para crear una instancia a partir de la fila.

## Refactorizar las funciones originales

Ahora, refactoricemos las funciones originales `read_csv_as_dicts()` y `read_csv_as_instances()` para utilizar estas nuevas clases.

```python
def read_csv_as_dicts(filename, types):
    '''
    Read a CSV file into a list of dictionaries with appropriate type conversion.
    '''
    parser = DictCSVParser(types)
    return parser.parse(filename)

def read_csv_as_instances(filename, cls):
    '''
    Read a CSV file into a list of instances of a class.
    '''
    parser = InstanceCSVParser(cls)
    return parser.parse(filename)
```

Estas funciones refactorizadas tienen la misma interfaz que las originales. Pero internamente, utilizan las nuevas clases de analizador que acabamos de crear. De esta manera, hemos separado la lógica común de análisis de CSV de la lógica específica de creación de registros.

## Probar tu implementación

Veamos si nuestro código refactorizado funciona correctamente. Crea un archivo llamado `test_reader.py` y agrega el siguiente código a él.

```python
import reader
import stock

# Test the refactored read_csv_as_instances function
portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
print("First stock:", portfolio[0])

# Test the refactored read_csv_as_dicts function
portfolio_dicts = reader.read_csv_as_dicts('portfolio.csv', [str, int, float])
print("First stock as dict:", portfolio_dicts[0])

# Test direct use of a parser
parser = reader.DictCSVParser([str, int, float])
portfolio_dicts2 = parser.parse('portfolio.csv')
print("First stock from direct parser:", portfolio_dicts2[0])
```

Para ejecutar la prueba, abre tu terminal y ejecuta el siguiente comando:

```bash
python test_reader.py
```

Deberías ver una salida similar a esta:

```
First stock: Stock('AA', 100, 32.2)
First stock as dict: {'name': 'AA', 'shares': 100, 'price': 32.2}
First stock from direct parser: {'name': 'AA', 'shares': 100, 'price': 32.2}
```

Si ves esta salida, significa que tu código refactorizado está funcionando correctamente. Tanto las funciones originales como el uso directo de los analizadores están produciendo los resultados esperados.
