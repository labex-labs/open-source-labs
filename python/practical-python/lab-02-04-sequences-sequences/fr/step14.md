# Exercice 2.15 : Un exemple pratique de `enumerate()`

Rappelez-vous que le fichier `missing.csv` contient des données pour un portefeuille d'actions, mais a quelques lignes avec des données manquantes. En utilisant `enumerate()`, modifiez votre programme `pcost.py` de sorte qu'il affiche un numéro de ligne avec le message d'avertissement lorsqu'il rencontre des données incorrectes.

```python
>>> cost = portfolio_cost('/home/labex/project/missing.csv')
Ligne 4: Impossible de convertir : ['MSFT', '', '51.23']
Ligne 7: Impossible de convertir : ['IBM', '', '70.44']
>>>
```

Pour ce faire, vous devrez modifier quelques parties de votre code.

```python
...
for rowno, row in enumerate(rows, start=1):
    try:
     ...
    except ValueError:
        print(f'Ligne {rowno} : Mauvaise ligne : {row}')
```
