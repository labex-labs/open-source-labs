# Un generador simple

Si alguna vez te encuentras queriendo personalizar la iteración, siempre debes pensar en funciones generadoras. Son fáciles de escribir: simplemente crea una función que realice la lógica de iteración deseada y utilice `yield` para emitir valores.

Por ejemplo, prueba este generador que te permite iterar sobre un rango de números con pasos fraccionarios (algo que no es soportado por la función `range()` incorporada):

```python
>>> def frange(start,stop,step):
        while start < stop:
            yield start
            start += step

>>> for x in frange(0, 2, 0.25):
        print(x, end=' ')

0 0.25 0.5 0.75 1.0 1.25 1.5 1.75
>>>
```

Iterar sobre un generador es una operación única. Por ejemplo, esto es lo que pasa si intentas iterar dos veces:

```python
>>> f = frange(0, 2, 0.25)
>>> for x in f:
        print(x, end=' ')

0 0.25 0.5 0.75 1.0 1.25 1.5 1.75
>>> for x in f:
        print(x, end=' ')

>>>
```

Si quieres iterar sobre la misma secuencia, debes recrear el generador llamando a `frange()` nuevamente. Alternativamente, podrías empaquetar todo en una clase:

```python
>>> class FRange:
        def __init__(self, start, stop, step):
            self.start = start
            self.stop = stop
            self.step = step
        def __iter__(self):
            n = self.start
            while n < self.stop:
                yield n
                n += self.step

>>> f = FRange(0, 2, 0.25)
>>> for x in f:
        print(x, end=' ')

0 0.25 0.5 0.75 1.0 1.25 1.5 1.75
>>> for x in f:
        print(x, end=' ')

0 0.25 0.5 0.75 1.0 1.25 1.5 1.75
>>>
```
