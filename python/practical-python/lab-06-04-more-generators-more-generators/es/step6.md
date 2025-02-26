# Ejercicio 6.15: Simplificación del código

Las expresiones generadoras a menudo son un reemplazo útil de pequeñas funciones generadoras. Por ejemplo, en lugar de escribir una función como esta:

```python
def filter_symbols(rows, names):
    for row in rows:
        if row['name'] in names:
            yield row
```

Podría escribir algo como esto:

```python
rows = (row for row in rows if row['name'] in names)
```

Modifique el programa `ticker.py` para usar expresiones generadoras en la medida de lo posible.
