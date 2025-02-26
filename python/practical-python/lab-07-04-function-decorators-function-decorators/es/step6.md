# Ejercicio 7.10: Un decorador para medir el tiempo

Si defines una función, su nombre y módulo se almacenan en los atributos `__name__` y `__module__`. Por ejemplo:

```python
>>> def add(x,y):
        return x+y

>>> add.__name__
'add'
>>> add.__module__
'__main__'
>>>
```

En un archivo `timethis.py`, escribe una función decoradora `timethis(func)` que envuelva una función con una capa adicional de lógica que imprime cuánto tiempo tarda en ejecutarse una función. Para hacer esto, rodearás la función con llamadas de medición del tiempo como esta:

```python
start = time.time()
r = func(*args,**kwargs)
end = time.time()
print('%s.%s: %f' % (func.__module__, func.__name__, end-start))
```

Aquí hay un ejemplo de cómo debería funcionar tu decorador:

```python
>>> from timethis import timethis
>>> @timethis
def countdown(n):
    while n > 0:
        n -= 1

>>> countdown(10000000)
__main__.countdown : 0.076562
>>>
```

Discusión: Este decorador `@timethis` se puede colocar delante de cualquier definición de función. Por lo tanto, es posible que lo uses como una herramienta de diagnóstico para el ajuste de rendimiento.
