# Lambda : Fonctions anonymes

Utilisez une fonction lambda au lieu de créer une fonction. Dans notre exemple de tri précédent.

```python
portfolio.sort(key=lambda s: s['name'])
```

Cela crée une fonction _sans nom_ qui évalue une _seule_ expression. Le code ci-dessus est beaucoup plus court que le code initial.

```python
def stock_name(s):
    return s['name']

portfolio.sort(key=stock_name)

# vs lambda
portfolio.sort(key=lambda s: s['name'])
```
