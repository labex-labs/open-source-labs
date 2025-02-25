# Exercice 1.32 : Utilisation d'une fonction de bibliothèque

Python est livré avec une large bibliothèque standard de fonctions utiles. Une bibliothèque qui pourrait être utile ici est le module `csv`. Vous devriez l'utiliser chaque fois que vous devez travailler avec des fichiers de données au format CSV. Voici un exemple de son utilisation :

```python
>>> import csv
>>> f = open('portfolio.csv')
>>> rows = csv.reader(f)
>>> headers = next(rows)
>>> headers
['name','shares', 'price']
>>> for row in rows:
        print(row)

['AA', '100', '32.20']
['IBM', '50', '91.10']
['CAT', '150', '83.44']
['MSFT', '200', '51.23']
['GE', '95', '40.37']
['MSFT', '50', '65.10']
['IBM', '100', '70.44']
>>> f.close()
>>>
```

Une des bonnes choses du module `csv` est qu'il gère une variété de détails de bas niveau tels que les guillemets et la division appropriée par des virgules. Dans la sortie ci-dessus, vous remarquerez qu'il a enlevé les guillemets doubles des noms dans la première colonne.

Modifiez votre programme `pcost.py` de sorte qu'il utilise le module `csv` pour le parsing et essayez d'exécuter les exemples précédents.
