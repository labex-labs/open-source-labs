# Ensembles

Les ensembles sont des collections d'éléments uniques et non triés.

```python
tech_stocks = { 'IBM','AAPL','MSFT' }
# Syntaxe alternative
tech_stocks = set(['IBM', 'AAPL', 'MSFT'])
```

Les ensembles sont utiles pour les tests d'appartenance.

```python
>>> tech_stocks
set(['AAPL', 'IBM', 'MSFT'])
>>> 'IBM' in tech_stocks
True
>>> 'FB' in tech_stocks
False
>>>
```

Les ensembles sont également utiles pour éliminer les doublons.

```python
names = ['IBM', 'AAPL', 'GOOG', 'IBM', 'GOOG', 'YHOO']

unique = set(names)
# unique = set(['IBM', 'AAPL','GOOG','YHOO'])
```

Opérations supplémentaires sur les ensembles :

```python
unique.add('CAT')        # Ajoute un élément
unique.remove('YHOO')    # Supprime un élément

s1 = { 'a', 'b', 'c'}
s2 = { 'c', 'd' }
s1 | s2                 # Union d'ensembles { 'a', 'b', 'c', 'd' }
s1 & s2                 # Intersection d'ensembles { 'c' }
s1 - s2                 # Différence d'ensembles { 'a', 'b' }
```

Dans ces exercices, vous commencez à construire l'un des principaux programmes utilisés pour le reste de ce cours. Effectuez votre travail dans le fichier `report.py`.
