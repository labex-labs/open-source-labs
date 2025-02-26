# Aplicación de las validaciones

Modifica la clase `ValidatedFunction` para que aplique las comprobaciones de valores adjuntadas a través de las anotaciones de funciones. Por ejemplo:

```python
>>> def add(x: Integer, y:Integer):
        return x + y
>>> add = ValidatedFunction(add)
>>> add(2,3)
5
>>> add('two','three')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "validate.py", line 67, in __call__
    self.func.__annotations__[name].check(val)
  File "validate.py", line 21, in check
    raise TypeError(f'Expected {cls.expected_type}')
TypeError: expected <class 'int'>
>>>>
```

Pista: Para hacer esto, experimenta con la vinculación de firmas. Utiliza el método `bind()` de los objetos `Signature` para vincular los argumentos de la función a los nombres de argumentos. Luego, cruza esta información con el atributo `__annotations__` para obtener las diferentes clases de validadores.

Tien en cuenta que estás creando un objeto que parece una función, pero en realidad no lo es. Hay algo de magia ocurriendo detrás de escena.
