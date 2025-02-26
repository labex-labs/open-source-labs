# Exercice 2.25 : Création de dictionnaires

Souvenez-vous de la manière dont la fonction `dict()` peut facilement créer un dictionnaire si vous avez une séquence de noms de clés et de valeurs? Créons un dictionnaire à partir des en-têtes de colonne :

```python
>>> headers
['name','shares', 'price']
>>> converted
['AA', 100, 32.2]
>>> dict(zip(headers, converted))
{'price': 32.2, 'name': 'AA','shares': 100}
>>>
```

Bien sûr, si vous maîtrisez les compréhensions de liste, vous pouvez effectuer toute la conversion d'un seul coup en utilisant une compréhension de dictionnaire :

```python
>>> { name: func(val) for name, func, val in zip(headers, types, row) }
{'price': 32.2, 'name': 'AA','shares': 100}
>>>
```
