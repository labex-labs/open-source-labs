# Iteración: Protocolo

Considera la instrucción `for`.

```python
for x in obj:
    # instrucciones
```

¿Qué sucede por debajo de los paneles?

```python
_iter = obj.__iter__()        # Obtener el objeto iterador
while True:
    try:
        x = _iter.__next__()  # Obtener el siguiente elemento
        # instrucciones...
    except StopIteration:     # No hay más elementos
        break
```

Todos los objetos que funcionan con el `for-loop` implementan este protocolo de iteración de bajo nivel.

Ejemplo: Iteración manual sobre una lista.

```python
>>> x = [1,2,3]
>>> it = x.__iter__()
>>> it
<listiterator object at 0x590b0>
>>> it.__next__()
1
>>> it.__next__()
2
>>> it.__next__()
3
>>> it.__next__()
Traceback (most recent call last):
File "<stdin>", line 1, in? StopIteration
>>>
```
