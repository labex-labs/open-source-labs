# Ejemplo de registro

Consideremos una función.

```python
def add(x, y):
    return x + y
```

Ahora, consideremos la función con un poco de registro agregado.

```python
def add(x, y):
    print('Calling add')
    return x + y
```

Ahora una segunda función también con un poco de registro.

```python
def sub(x, y):
    print('Calling sub')
    return x - y
```
