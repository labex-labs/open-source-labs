# Generadores

Un generador es una función que define una iteración.

```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1
```

Por ejemplo:

```python
>>> for x in countdown(10):
...   print(x, end=' ')
...
10 9 8 7 6 5 4 3 2 1
>>>
```

Un generador es cualquier función que utiliza la declaración `yield`.

El comportamiento de los generadores es diferente al de una función normal. Llamar a una función generadora crea un objeto generador. No ejecuta inmediatamente la función.

```python
def countdown(n):
    # Added a print statement
    print('Counting down from', n)
    while n > 0:
        yield n
        n -= 1
```

```python
>>> x = countdown(10)
# There is NO PRINT STATEMENT
>>> x
# x is a generator object
<generator object at 0x58490>
>>>
```

La función solo se ejecuta en la llamada a `__next__()`.

```python
>>> x = countdown(10)
>>> x
<generator object at 0x58490>
>>> x.__next__()
Counting down from 10
10
>>>
```

`yield` produce un valor, pero suspende la ejecución de la función. La función se reanuda en la siguiente llamada a `__next__()`.

```python
>>> x.__next__()
9
>>> x.__next__()
8
```

Cuando el generador finalmente devuelve, la iteración lanza un error.

```python
>>> x.__next__()
1
>>> x.__next__()
Traceback (most recent call last):
File "<stdin>", line 1, in? StopIteration
>>>
```

_Observación: Una función generadora implementa el mismo protocolo de bajo nivel que utiliza la instrucción for en listas, tuplas, diccionarios, archivos, etc._
