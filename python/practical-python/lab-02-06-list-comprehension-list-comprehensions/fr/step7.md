# Exercice 2.20 : Réductions de séquence

Calculez le coût total du portefeuille en utilisant une seule instruction Python.

```python
>>> portfolio = read_portfolio('portfolio.csv')
>>> cost = sum([ s['shares'] * s['price'] for s in portfolio ])
>>> cost
44671.15
>>>
```

Une fois que vous avez fait cela, montrez comment vous pouvez calculer la valeur actuelle du portefeuille en utilisant une seule instruction.

```python
>>> value = sum([ s['shares'] * prices[s['name']] for s in portfolio ])
>>> value
28686.1
>>>
```

Les deux opérations ci-dessus sont des exemples de map-réduction. La compréhension de liste effectue une opération sur chaque élément de la liste.

```python
>>> [ s['shares'] * s['price'] for s in portfolio ]
[3220.0000000000005, 4555.0, 12516.0, 10246.0, 3835.1499999999996, 3254.9999999999995, 7044.0]
>>>
```

La fonction `sum()` effectue ensuite une réduction sur le résultat :

```python
>>> sum(_)
44671.15
>>>
```

Avec ces connaissances, vous êtes maintenant prêt à lancer une startup de big data.
