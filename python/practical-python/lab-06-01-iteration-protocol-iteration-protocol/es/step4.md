# Ejercicio 6.1: Iteración ilustrada

Crea la siguiente lista:

```python
a = [1,9,4,25,16]
```

Itera manualmente sobre esta lista. Llama a `__iter__()` para obtener un iterador y llama al método `__next__()` para obtener elementos sucesivos.

```python
>>> i = a.__iter__()
>>> i
<listiterator object at 0x64c10>
>>> i.__next__()
1
>>> i.__next__()
9
>>> i.__next__()
4
>>> i.__next__()
25
>>> i.__next__()
16
>>> i.__next__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>>
```

La función integrada `next()` es un atajo para llamar al método `__next__()` de un iterador. Prueba a usarla en un archivo:

```python
>>> f = open('portfolio.csv')
>>> f.__iter__()    # Nota: Esto devuelve el archivo mismo
<_io.TextIOWrapper name='portfolio.csv' mode='r' encoding='UTF-8'>
>>> next(f)
'name,shares,price\n'
>>> next(f)
'"AA",100,32.20\n'
>>> next(f)
'"IBM",50,91.10\n'
>>>
```

Sigue llamando a `next(f)` hasta que llegues al final del archivo. Observa lo que sucede.
