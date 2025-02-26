# Todo es un objeto

Números, cadenas, listas, funciones, excepciones, clases, instancias, etc. son todos objetos. Esto significa que todos los objetos que se pueden nombrar se pueden pasar como datos, colocar en contenedores, etc., sin ninguna restricción. No hay _especiales_ tipos de objetos. A veces se dice que todos los objetos son "de primer clase".

Un ejemplo simple:

```python
>>> import math
>>> items = [abs, math, ValueError ]
>>> items
[<built-in function abs>,
  <module'math' (builtin)>,
  <type 'exceptions.ValueError'>]
>>> items[0](-45)
45
>>> items[1].sqrt(2)
1.4142135623730951
>>> try:
        x = int('not a number')
    except items[2]:
        print('Failed!')
Failed!
>>>
```

Aquí, `items` es una lista que contiene una función, un módulo y una excepción. Puedes usar directamente los elementos de la lista en lugar de los nombres originales:

```python
items[0](-45)       # abs
items[1].sqrt(2)    # math
except items[2]:    # ValueError
```

Con gran poder viene gran responsabilidad. Simplemente porque puedas hacer eso no significa que debas.

En este conjunto de ejercicios, examinamos algunos de los poderes que derivan de los objetos de primer clase.
