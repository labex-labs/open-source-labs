# Conversión de Fila

Una característica que falta en la clase `Structure` es un método `from_row()` que le permita trabajar con el código anterior de lectura de CSV. Vamos a corregir eso. Da a la clase `Structure` una variable de clase `_types` y el siguiente método de clase:

```python
# structure.py

class Structure:
    _types = ()
 ...
    @classmethod
    def from_row(cls, row):
        rowdata = [ func(val) for func, val in zip(cls._types, row) ]
        return cls(*rowdata)
 ...
```

Modifica el decorador `@validate_attributes` para que examine los diferentes validadores para un atributo `expected_type` y lo use para llenar la variable `_types` anterior.

Una vez que hayas hecho esto, deberías poder hacer cosas como esta:

```python
>>> s = Stock.from_row(['GOOG', '100', '490.1'])
>>> s
Stock('GOOG', 100, 490.1)
>>> import reader
>>> port = reader.read_csv_as_instances('portfolio.csv', Stock)
>>>
```
