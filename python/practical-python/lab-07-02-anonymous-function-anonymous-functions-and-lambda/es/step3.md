# Lambda: Funciones anónimas

Utiliza una función lambda en lugar de crear la función. En nuestro ejemplo de clasificación anterior.

```python
portfolio.sort(key=lambda s: s['name'])
```

Esto crea una función _sin nombre_ que evalúa una _única_ expresión. El código anterior es mucho más corto que el código inicial.

```python
def stock_name(s):
    return s['name']

portfolio.sort(key=stock_name)

# vs lambda
portfolio.sort(key=lambda s: s['name'])
```
