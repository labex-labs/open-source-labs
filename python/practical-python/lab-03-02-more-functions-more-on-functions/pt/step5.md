# Retornando Valores (Returning Values)

A instrução `return` retorna um valor.

```python
def square(x):
    return x * x
```

Se nenhum valor de retorno for fornecido ou `return` estiver ausente, `None` é retornado.

```python
def bar(x):
    statements
    return

a = bar(4)      # a = None

# OR
def foo(x):
    statements  # No `return`

b = foo(4)      # b = None
```
