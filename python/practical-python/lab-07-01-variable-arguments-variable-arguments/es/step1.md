# Argumentos variables posicionales (\*args)

Una función que acepta _cualquier número_ de argumentos se dice que utiliza argumentos variables. Por ejemplo:

```python
def f(x, *args):
  ...
```

Llamada a la función.

```python
f(1,2,3,4,5)
```

Los argumentos adicionales se pasan como una tupla.

```python
def f(x, *args):
    # x -> 1
    # args -> (2,3,4,5)
```
