# Preparación

En el Ejercicio 4.3, creaste una serie de clases `Validator` para realizar diferentes tipos de comprobaciones de tipo y valor. Por ejemplo:

```python
>>> from validate import Integer
>>> Integer.check(1)
>>> Integer.check('hello')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "validate.py", line 21, in check
    raise TypeError(f'Expected {cls.expected_type}')
TypeError: Expected <class 'int'>
>>>
```

Podrías usar los validadores en funciones de la siguiente manera:

```python
>>> def add(x, y):
        Integer.check(x)
        Integer.check(y)
        return x + y

>>>
```

En este ejercicio, vamos a avanzar un paso más.
