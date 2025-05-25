# Lambda: Anonyme Funktionen

Verwenden Sie eine Lambda-Funktion anstelle der Funktion zu erstellen. Im vorherigen Sortierbeispiel.

```python
portfolio.sort(key=lambda s: s['name'])
```

Dies erstellt eine _namenlose_ Funktion, die einen _einzigen_ Ausdruck 计算。Der obige Code ist viel kürzer als der ursprüngliche Code.

```python
def stock_name(s):
    return s['name']

portfolio.sort(key=stock_name)

# vs lambda
portfolio.sort(key=lambda s: s['name'])
```
