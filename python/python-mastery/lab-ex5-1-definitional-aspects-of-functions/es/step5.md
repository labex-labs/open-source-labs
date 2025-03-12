# Agregando sugerencias de tipo

En Python 3.5 y versiones posteriores, se admiten las sugerencias de tipo (type hints). Las sugerencias de tipo son una forma de indicar los tipos de datos esperados de variables, parámetros de función y valores de retorno en tu código. No cambian cómo se ejecuta el código, pero hacen que el código sea más legible y pueden ayudar a detectar ciertos tipos de errores antes de que el código se ejecute realmente. Ahora, agreguemos sugerencias de tipo a nuestras funciones de lectura de archivos CSV.

1. Abre el archivo `reader.py` y actualízalo para incluir sugerencias de tipo:

```python
# reader.py

import csv
from typing import List, Callable, Dict, Any, Type, Optional, TextIO, Iterator, TypeVar

# Define a generic type for the class parameter
T = TypeVar('T')

def csv_as_dicts(lines: Iterator[str],
                types: List[Callable[[str], Any]],
                headers: Optional[List[str]] = None) -> List[Dict[str, Any]]:
    '''
    Parse CSV data from an iterable into a list of dictionaries

    Args:
        lines: An iterable producing CSV lines
        types: List of type conversion functions for each column
        headers: Optional list of column names. If None, first row is used as headers

    Returns:
        List of dictionaries with data from the CSV lines
    '''
    records: List[Dict[str, Any]] = []
    rows = csv.reader(lines)

    if headers is None:
        # Use the first row as headers if none provided
        headers = next(rows)

    for row in rows:
        record = { name: func(val)
                  for name, func, val in zip(headers, types, row) }
        records.append(record)
    return records

def csv_as_instances(lines: Iterator[str],
                    cls: Type[T],
                    headers: Optional[List[str]] = None) -> List[T]:
    '''
    Parse CSV data from an iterable into a list of class instances

    Args:
        lines: An iterable producing CSV lines
        cls: Class to create instances from
        headers: Optional list of column names. If None, first row is used as headers

    Returns:
        List of class instances with data from the CSV lines
    '''
    records: List[T] = []
    rows = csv.reader(lines)

    if headers is None:
        # Skip the first row if no headers provided
        next(rows)

    for row in rows:
        record = cls.from_row(row)
        records.append(record)
    return records

def read_csv_as_dicts(filename: str,
                     types: List[Callable[[str], Any]],
                     headers: Optional[List[str]] = None) -> List[Dict[str, Any]]:
    '''
    Read CSV data into a list of dictionaries with optional type conversion

    Args:
        filename: Path to the CSV file
        types: List of type conversion functions for each column
        headers: Optional list of column names. If None, first row is used as headers

    Returns:
        List of dictionaries with data from the CSV file
    '''
    with open(filename) as file:
        return csv_as_dicts(file, types, headers)

def read_csv_as_instances(filename: str,
                         cls: Type[T],
                         headers: Optional[List[str]] = None) -> List[T]:
    '''
    Read CSV data into a list of class instances

    Args:
        filename: Path to the CSV file
        cls: Class to create instances from
        headers: Optional list of column names. If None, first row is used as headers

    Returns:
        List of class instances with data from the CSV file
    '''
    with open(filename) as file:
        return csv_as_instances(file, cls, headers)
```

Comprendamos los cambios clave que hemos realizado en el código:

1. Importamos tipos del módulo `typing`. Este módulo proporciona un conjunto de tipos que podemos usar para definir sugerencias de tipo. Por ejemplo, `List`, `Dict` y `Optional` son tipos de este módulo.
2. Agregamos una variable de tipo genérico `T` para representar el tipo de clase. Una variable de tipo genérico nos permite escribir funciones que pueden trabajar con diferentes tipos de manera segura en términos de tipos.
3. Agregamos sugerencias de tipo a todos los parámetros de función y valores de retorno. Esto hace claro qué tipos de argumentos espera una función y qué tipo de valor devuelve.
4. Usamos tipos de contenedores adecuados como `List`, `Dict` y `Optional`. `List` representa una lista, `Dict` representa un diccionario y `Optional` indica que un parámetro puede tener un cierto tipo o ser `None`.
5. Usamos `Callable` para las funciones de conversión de tipo. `Callable` se utiliza para indicar que un parámetro es una función que se puede llamar.
6. Usamos el genérico `T` para expresar que `csv_as_instances` devuelve una lista de instancias de la clase pasada. Esto ayuda al IDE y otras herramientas a entender el tipo de los objetos devueltos.

7. Ahora, creemos un archivo de prueba simple para asegurarnos de que todo siga funcionando correctamente:

```python
# test_types.py

import reader
import stock

# The functions should work exactly as before
portfolio = reader.read_csv_as_dicts('portfolio.csv', [str, int, float])
print("First item:", portfolio[0])

# But now we have better type checking and IDE support
stock_portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
print("\nFirst stock:", stock_portfolio[0])

# We can see that stock_portfolio is a list of Stock objects
# This helps IDEs provide better code completion
first_stock = stock_portfolio[0]
print(f"\nName: {first_stock.name}")
print(f"Shares: {first_stock.shares}")
print(f"Price: {first_stock.price}")
print(f"Value: {first_stock.shares * first_stock.price}")
```

3. Ejecuta el script de prueba desde la terminal:

```bash
python test_types.py
```

La salida debería ser similar a:

```
First item: {'name': 'AA', 'shares': 100, 'price': 32.2}

First stock: Stock('AA', 100, 32.2)

Name: AA
Shares: 100
Price: 32.2
Value: 3220.0
```

Las sugerencias de tipo no cambian cómo se ejecuta el código, pero ofrecen varios beneficios:

1. Ofrecen mejor soporte del IDE con finalización de código. Cuando usas un IDE como PyCharm o VS Code, puede usar las sugerencias de tipo para sugerir los métodos y atributos correctos para tus variables.
2. Proporcionan una documentación más clara sobre los tipos de parámetros y valores de retorno esperados. Solo con mirar la definición de la función, puedes saber qué tipos de argumentos espera y qué tipo de valor devuelve.
3. Permiten usar verificadores de tipo estáticos como mypy para detectar errores temprano. Los verificadores de tipo estáticos analizan tu código sin ejecutarlo y pueden encontrar errores relacionados con los tipos antes de ejecutar el código.
4. Mejoran la legibilidad y mantenibilidad del código. Cuando tú u otros desarrolladores vuelvan al código más tarde, es más fácil entender lo que está haciendo el código.

En una base de código grande, estos beneficios pueden reducir significativamente los errores y hacer que el código sea más fácil de entender y mantener.

**Nota:** Las sugerencias de tipo son opcionales en Python, pero se utilizan cada vez más en el código profesional. Bibliotecas como las de la biblioteca estándar de Python y muchos paquetes de terceros populares ahora incluyen sugerencias de tipo extensas.
