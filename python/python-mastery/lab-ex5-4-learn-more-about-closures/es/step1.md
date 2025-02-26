# Los closures como estructura de datos

Una posible utilización de los closures es como herramienta para la encapsulación de datos. Prueba este ejemplo:

```python
def counter(value):
    def incr():
        nonlocal value
        value += 1
        return value

    def decr():
        nonlocal value
        value -= 1
        return value

    return incr, decr
```

Este código define dos funciones internas que manipulan un valor. Prueba:

```python
>>> up, down = counter(0)
>>> up()
1
>>> up()
2
>>> up()
3
>>> down()
2
>>> down()
1
>>>
```

Observa cómo no hay ninguna definición de clase aquí. Además, tampoco hay una variable global. Sin embargo, las funciones `up()` y `down()` están manipulando un valor "detrás de escena". Es bastante mágico.
