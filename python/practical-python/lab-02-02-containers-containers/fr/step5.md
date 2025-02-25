# Construction de dictionnaires

Exemple de création d'un dictionnaire à partir de zéro.

```python
prices = {} # Dictionnaire initialement vide

# Insérez de nouveaux éléments
prices['GOOG'] = 513.25
prices['CAT'] = 87.22
prices['IBM'] = 93.37
```

Un exemple de remplissage du dictionnaire à partir du contenu d'un fichier.

```python
prices = {} # Dictionnaire initialement vide

with open('prices.csv', 'rt') as f:
    for line in f:
        row = line.split(',')
        prices[row[0]] = float(row[1])
```

Remarque : Si vous essayez cela avec le fichier `prices.csv`, vous constaterez que cela fonctionne presque - il y a une ligne vide à la fin qui provoque une erreur. Vous devrez trouver un moyen de modifier le code pour prendre cela en compte (voir l'exercice 2.6).
