# Adición de funcionalidad de conversión de filas

En programación, a menudo es útil crear instancias de una clase a partir de filas de datos, especialmente cuando se trabaja con datos de fuentes como archivos CSV. En esta sección, agregaremos la capacidad de crear instancias de la clase `Structure` a partir de filas de datos. Lo haremos implementando un método de clase `from_row` en la clase `Structure`.

1. Primero, debes abrir el archivo `structure.py`. Aquí es donde realizaremos los cambios en el código. Utiliza el siguiente comando en tu terminal:

```bash
code ~/project/structure.py
```

2. A continuación, modificaremos la función `validate_attributes`. Esta función es un decorador de clase que extrae instancias de `Validator` y construye automáticamente las listas `_fields` y `_types`. La actualizaremos para que también recopile información de tipos.

```python
def validate_attributes(cls):
    """
    Class decorator that extracts Validator instances
    and builds the _fields and _types lists automatically
    """
    validators = []
    for name, val in vars(cls).items():
        if isinstance(val, Validator):
            validators.append(val)

    # Set _fields based on validator names
    cls._fields = [val.name for val in validators]

    # Set _types based on validator expected_types
    cls._types = [getattr(val, 'expected_type', lambda x: x) for val in validators]

    # Create initialization method
    cls.create_init()

    return cls
```

En esta función actualizada, estamos recopilando el atributo `expected_type` de cada validador y almacenándolo en la variable de clase `_types`. Esto será útil más adelante cuando convertamos los datos de las filas a los tipos correctos.

3. Ahora, agregaremos el método de clase `from_row` a la clase `Structure`. Este método nos permitirá crear una instancia de la clase a partir de una fila de datos, que podría ser una lista o una tupla.

```python
@classmethod
def from_row(cls, row):
    """
    Create an instance from a data row (list or tuple)
    """
    rowdata = [func(val) for func, val in zip(cls._types, row)]
    return cls(*rowdata)
```

Así es cómo funciona este método:

- Toma una fila de datos, que puede estar en forma de lista o tupla.
- Convierte cada valor en la fila al tipo esperado utilizando la función correspondiente de la lista `_types`.
- Luego crea y devuelve una nueva instancia de la clase utilizando los valores convertidos.

4. Después de realizar estos cambios, guarda el archivo `structure.py`. Esto asegura que tus cambios en el código se conserven.

5. Probemos nuestro método `from_row` para asegurarnos de que funcione como se espera. Crearemos una prueba simple utilizando la clase `Stock`. Ejecuta el siguiente comando en tu terminal:

```bash
cd ~/project
python3 -c "from stock import Stock; s = Stock.from_row(['GOOG', '100', '490.1']); print(s); print(f'Cost: {s.cost}')"
```

Deberías ver una salida similar a esta:

```
Stock('GOOG', 100, 490.1)
Cost: 49010.0
```

Observa que los valores de cadena '100' y '490.1' se convirtieron automáticamente a los tipos correctos (entero y flotante). Esto muestra que nuestro método `from_row` está funcionando correctamente.

6. Finalmente, intentemos leer datos de un archivo CSV utilizando nuestro módulo `reader.py`. Ejecuta el siguiente comando en tu terminal:

```bash
cd ~/project
python3 -c "from stock import Stock; import reader; portfolio = reader.read_csv_as_instances('portfolio.csv', Stock); print(portfolio); print(f'Total value: {sum(s.cost for s in portfolio)}')"
```

Deberías ver una salida que muestre las acciones del archivo CSV:

```
[Stock('GOOG', 100, 490.1), Stock('AAPL', 50, 545.75), Stock('MSFT', 200, 30.47)]
Total value: 73444.0
```

El método `from_row` nos permite convertir fácilmente datos CSV en instancias de la clase `Stock`. Cuando se combina con la función `read_csv_as_instances`, tenemos una forma poderosa de cargar y trabajar con datos estructurados.
