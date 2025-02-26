# Capturer les exceptions

Au lieu de planter sur des données erronées, modifiez le code pour émettre un message d'avertissement à la place. Le résultat final devrait être une liste des lignes qui ont été converties avec succès. Par exemple :

```python
>>> port = read_csv_as_dicts('missing.csv', types=[str, int, float])
Row 4: Bad row: ['C', '', '53.08']
Row 7: Bad row: ['DIS', '50', 'N/A']
Row 8: Bad row: ['GE', '', '37.23']
Row 13: Bad row: ['INTC', '', '21.84']
Row 17: Bad row: ['MCD', '', '51.11']
Row 19: Bad row: ['MO', '', '70.09']
Row 22: Bad row: ['PFE', '', '26.40']
Row 26: Bad row: ['VZ', '', '42.92']
>>> len(port)
20
>>>
```

Note : Apporter ce changement peut être un peu difficile en raison de votre utilisation précédente de la fonction intégrée `map()`. Vous devrez peut-être abandonner cette approche car il n'y a pas de manière simple de capturer et de gérer les exceptions dans `map()`.
