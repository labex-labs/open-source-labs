# Devolviendo valores

La instrucción `return` devuelve un valor

```python
def square(x):
    return x * x
```

Si no se da un valor de retorno o falta la instrucción `return`, se devuelve `None`.

```python
def bar(x):
    statements
    return

a = bar(4)      # a = None

# O

def foo(x):
    statements  # No `return`

b = foo(4)      # b = None
```
