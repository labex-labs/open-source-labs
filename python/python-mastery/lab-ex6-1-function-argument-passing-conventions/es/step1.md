# Preparación

Vamos a recrear la clase `Stock` desde cero utilizando algunas nuevas técnicas. Asegúrese de tener sus pruebas unitarias del Ejercicio 5.4 a mano. Las necesitará.

Si define una función, probablemente ya sabe que se puede llamar utilizando una combinación de argumentos posicionales o de palabras clave. Por ejemplo:

```python
>>> def foo(x, y, z):
        return x + y + z

>>> foo(1, 2, 3)
6
>>> foo(1, z=3, y=2)
6
>>>
```

También es posible que sepas que se pueden pasar secuencias y diccionarios como argumentos de función utilizando la sintaxis \* y \*\*. Por ejemplo:

```python
>>> args = (1, 2, 3)
>>> foo(*args)
6
>>> kwargs = {'y':2, 'z':3 }
>>> foo(1,**kwargs)
6
>>>
```

Además de eso, se pueden escribir funciones que acepten cualquier número de argumentos posicionales o de palabras clave utilizando la sintaxis \* y \*\*. Por ejemplo:

```python
>>> def foo(*args):
        print(args)

>>> foo(1,2)
(1, 2)
>>> foo(1,2,3,4,5)
(1, 2, 3, 4, 5)
>>> foo()
()
>>>
>>> def bar(**kwargs):
        print(kwargs)

>>> bar(x=1,y=2)
{'y': 2, 'x': 1}
>>> bar(x=1,y=2,z=3)
{'y': 2, 'x': 1, 'z': 3}
>>> bar()
{}
>>>
```

Las funciones con argumentos variables a veces son útiles como una técnica para reducir o simplificar la cantidad de código que necesita escribir. En este ejercicio, exploraremos esa idea para estructuras de datos simples.
