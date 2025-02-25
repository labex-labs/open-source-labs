# Iteración sobre una secuencia

El bucle `for` itera sobre los elementos de una secuencia.

```python
>>> s = [1, 4, 9, 16]
>>> for i in s:
...     print(i)
...
1
4
9
16
>>>
```

En cada iteración del bucle, obtienes un nuevo elemento con el que trabajar. Este nuevo valor se coloca en la variable de iteración. En este ejemplo, la variable de iteración es `x`:

```python
for x in s:         # `x` es una variable de iteración
  ...statements
```

En cada iteración, el valor anterior de la variable de iteración se sobrescribe (si existe). Después de que el bucle finalice, la variable conserva el último valor.
