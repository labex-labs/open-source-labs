# Défi d'analyse de données

Dans le dernier laboratoire, vous avez écrit du code pour lire des données au format CSV relatives à l'Autorité de transport en commun de Chicago. Par exemple, vous pouvez récupérer les données sous forme de dictionnaires comme ceci :

```python
>>> import readrides
>>> rows = readrides.read_rides_as_dicts('/home/labex/project/ctabus.csv')
>>>
```

Il serait dommage de faire tout ce travail et de ne rien faire avec les données.

Dans cet exercice, votre tâche est la suivante : écrire un programme pour répondre aux quatre questions suivantes :

1. Combien de lignes de bus existent à Chicago?

2. Combien de personnes ont pris le bus numéro 22 le 2 février 2011? Et pour n'importe quelle ligne à n'importe quelle date de votre choix?

3. Quel est le nombre total de trajets effectués sur chaque ligne de bus?

4. Quelles sont les cinq lignes de bus ayant enregistré la plus forte augmentation de la fréquentation sur dix ans, de 2001 à 2011?

Vous êtes libre d'utiliser n'importe quelle technique pour répondre aux questions ci-dessus, pourvu qu'elle fasse partie de la bibliothèque standard de Python (c'est-à-dire les types de données intégrés, les modules de bibliothèque standard, etc.).
