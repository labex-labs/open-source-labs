# Copias superficiales

Las listas y los diccionarios tienen métodos para copiar.

```python
>>> a = [2,3,[100,101],4]
>>> b = list(a) # Hacer una copia
>>> a is b
False
```

Es una nueva lista, pero los elementos de la lista se comparten.

```python
>>> a[2].append(102)
>>> b[2]
[100,101,102]
>>>
>>> a[2] is b[2]
True
>>>
```

Por ejemplo, la lista interna `[100, 101, 102]` se está compartiendo. Esto se conoce como una copia superficial. Aquí está una representación.

![Copia superficial](../assets/shallow.png)
