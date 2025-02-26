# Exercice 4.9 : Meilleure sortie pour l'affichage d'objets

Modifiez l'objet `Stock` que vous avez défini dans `stock.py` de sorte que la méthode `__repr__()` produise une sortie plus utile. Par exemple :

```python
>>> goog = stock.Stock('GOOG', 100, 490.1)
>>> goog
Stock('GOOG', 100, 490.1)
>>>
```

Voyez ce qui se passe lorsque vous lisez un portefeuille d'actions et que vous visualisez la liste résultante après avoir effectué ces modifications. Par exemple :

```python
>>> import report
>>> portfolio = report.read_portfolio('portfolio.csv')
>>> portfolio
... voir ce que la sortie est...
>>>
```
