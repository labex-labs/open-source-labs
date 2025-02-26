# Exercice 3.9 : Capturer des exceptions

La fonction `parse_csv()` que vous avez écrite est utilisée pour traiter le contenu complet d'un fichier. Cependant, dans le monde réel, il est possible que les fichiers d'entrée soient corrompus, manquants ou contiennent des données sales. Essayez cet exemple :

```python
>>> portfolio = parse_csv('missing.csv', types=[str, int, float])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "fileparse.py", line 36, in parse_csv
    row = [func(val) for func, val in zip(types, row)]
ValueError: invalid literal for int() with base 10: ''
>>>
```

Modifiez la fonction `parse_csv()` pour capturer toutes les exceptions `ValueError` générées pendant la création d'un enregistrement et afficher un message d'avertissement pour les lignes qui ne peuvent pas être converties.

Le message devrait inclure le numéro de ligne et des informations sur la raison pour laquelle la conversion a échoué. Pour tester votre fonction, essayez de lire le fichier `missing.csv` ci-dessus. Par exemple :

```python
>>> portfolio = parse_csv('missing.csv', types=[str, int, float])
Ligne 4: Impossible de convertir ['MSFT', '', '51.23']
Ligne 4: Raison : invalid literal for int() with base 10: ''
Ligne 7: Impossible de convertir ['IBM', '', '70.44']
Ligne 7: Raison : invalid literal for int() with base 10: ''
>>>
>>> portfolio
[{'name': 'AA','shares': 100, 'price': 32.2}, {'name': 'IBM','shares': 50, 'price': 91.1}, {'name': 'CAT','shares': 150, 'price': 83.44}, {'name': 'GE','shares': 95, 'price': 40.37}, {'name': 'MSFT','shares': 50, 'price': 65.1}]
>>>
```
