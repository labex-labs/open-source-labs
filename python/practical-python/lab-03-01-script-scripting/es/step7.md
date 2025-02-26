# Estilo de abajo hacia arriba

Las funciones se tratan como bloques de construcción. Los bloques más pequeños/simples van primero.

```python
# myprogram.py
def foo(x):
  ...

def bar(x):
  ...
    foo(x)          # Definido anteriormente
  ...

def spam(x):
  ...
    bar(x)          # Definido anteriormente
  ...

spam(42)            # El código que utiliza las funciones aparece al final
```

Las funciones posteriores se basan en las funciones anteriores. Una vez más, esto solo es un punto de estilo. Lo único que importa en el programa anterior es que la llamada a `spam(42)` vaya al final.
