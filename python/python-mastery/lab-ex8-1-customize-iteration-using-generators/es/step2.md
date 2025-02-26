# Agregando iteración a objetos

Si has creado una clase personalizada, puedes hacer que soporte iteración definiendo un método especial `__iter__()`. `__iter__()` devuelve un iterador como resultado. Como se mostró en el ejemplo anterior, una forma fácil de hacerlo es definir `__iter__()` como un generador.

En ejercicios anteriores, definiste una clase base `Structure`. Agrega un método `__iter__()` a esta clase que produzca los valores de los atributos en orden. Por ejemplo:

```python
class Structure(metaclass=StructureMeta):
  ...
    def __iter__(self):
        for name in self._fields:
            yield getattr(self, name)
  ...
```

Una vez que hayas hecho esto, deberías poder iterar sobre los atributos de la instancia de la siguiente manera:

```python
>>> from stock import Stock
>>> s = Stock('GOOG', 100, 490.1)
>>> for val in s:
        print(val)
GOOG
100
490.1
>>>
```
