# Expressions génératrices et fonctions de réduction

Les expressions génératrices sont particulièrement utiles pour alimenter des données dans des fonctions telles que `sum()`, `min()`, `max()`, `any()`, etc. Essayez quelques exemples en utilisant les données du portefeuille précédentes. Remarquez attentivement que ces exemples manquent de crochets carrés supplémentaires (\[\]) qui apparaissaient lorsqu'on utilisait les compréhensions de liste.

```python
>>> from readport import read_portfolio
>>> portfolio = read_portfolio('portfolio.csv')
>>> sum(s['shares']*s['price'] for s in portfolio)
44671.15
>>> min(s['shares'] for s in portfolio)
50
>>> any(s['name'] == 'IBM' for s in portfolio)
True
>>> all(s['name'] == 'IBM' for s in portfolio)
False
>>> sum(s['shares'] for s in portfolio if s['name'] == 'IBM')
150
>>>
```

Voici un usage subtil d'une expression génératrice pour créer des valeurs séparées par des virgules :

```python
>>> s = ('GOOG',100,490.10)
>>> ','.join(s)
... remarquez qu'elle échoue...
>>> ','.join(str(x) for x in s)    # Cela fonctionne
'GOOG,100,490.1'
>>>
```

La syntaxe dans les exemples ci-dessus peut prendre un peu d'habitude, mais le point crucial est que aucune des opérations ne crée jamais une liste complètement remplie de résultats. Cela vous permet d'économiser beaucoup de mémoire. Cependant, vous devez vous assurer de ne pas abuser de la syntaxe.
