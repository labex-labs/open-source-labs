# Cómo fallan los programas

Python no realiza ninguna comprobación o validación de los tipos o valores de los argumentos de las funciones. Una función funcionará con cualquier dato que sea compatible con las instrucciones de la función.

```python
def add(x, y):
    return x + y

add(3, 4)               # 7
add('Hello', 'World')   # 'HelloWorld'
add('3', '4')           # '34'
```

Si hay errores en una función, aparecen en tiempo de ejecución (como una excepción).

```python
def add(x, y):
    return x + y

>>> add(3, '4')
Traceback (most recent call last):
...
TypeError: unsupported operand type(s) for +:
'int' and 'str'
>>>
```

Para verificar el código, se da una gran importancia a las pruebas (que se abordan más adelante).
