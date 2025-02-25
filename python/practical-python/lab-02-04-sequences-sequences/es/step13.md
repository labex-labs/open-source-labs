# Ejercicio 2.14: Más operaciones con secuencias

Experimenta interactivamente con algunas de las operaciones de reducción de secuencias.

```python
>>> data = [4, 9, 1, 25, 16, 100, 49]
>>> min(data)
1
>>> max(data)
100
>>> sum(data)
204
>>>
```

Intenta iterar sobre los datos.

```python
>>> for x in data:
        print(x)

4
9
...
>>> for n, x in enumerate(data):
        print(n, x)

0 4
1 9
2 1
...
>>>
```

A veces, los principiantes usan la instrucción `for`, `len()` y `range()` en algún fragmento de código horrible que parece haber salido de las profundidades de un programa C oxidado.

```python
>>> for n in range(len(data)):
        print(data[n])

4
9
1
...
>>>
```

¡No lo hagas! No solo hace que les duela la vista a todos, es ineficiente en memoria y es mucho más lento. Simplemente usa un bucle `for` normal si quieres iterar sobre datos. Usa `enumerate()` si por alguna razón necesitas el índice.
