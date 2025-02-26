# Expresiones Generadoras

Una versión generadora de una comprensión de lista.

```python
>>> a = [1,2,3,4]
>>> b = (2*x for x in a)
>>> b
<generator object at 0x58760>
>>> for i in b:
...   print(i, end=' ')
...
2 4 6 8
>>>
```

Diferencias con las Comprensiones de Lista.

- No construye una lista.
- El único propósito útil es la iteración.
- Una vez consumido, no se puede reutilizar.

Sintaxis general.

```python
(<expression> for i in s if <conditional>)
```

También puede servir como argumento de función.

```python
sum(x*x for x in a)
```

Se puede aplicar a cualquier iterable.

```python
>>> a = [1,2,3,4]
>>> b = (x*x for x in a)
>>> c = (-x for x in b)
>>> for i in c:
...   print(i, end=' ')
...
-1 -4 -9 -16
>>>
```

El principal uso de las expresiones generadoras es en código que realiza algún cálculo sobre una secuencia, pero solo utiliza el resultado una vez. Por ejemplo, eliminar todos los comentarios de un archivo.

```python
f = open('somefile.txt')
lines = (line for line in f if not line.startswith('#'))
for line in lines:
  ...
f.close()
```

Con los generadores, el código se ejecuta más rápido y utiliza poco memoria. Es como un filtro aplicado a un flujo.
