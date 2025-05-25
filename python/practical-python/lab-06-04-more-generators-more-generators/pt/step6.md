# Exercício 6.15: Simplificação de código

Expressões geradoras são frequentemente uma substituição útil para pequenas funções geradoras. Por exemplo, em vez de escrever uma função como esta:

```python
def filter_symbols(rows, names):
    for row in rows:
        if row['name'] in names:
            yield row
```

Você poderia escrever algo como isto:

```python
rows = (row for row in rows if row['name'] in names)
```

Modifique o programa `ticker.py` para usar expressões geradoras conforme apropriado.
