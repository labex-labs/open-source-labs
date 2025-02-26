# Utilisation de base de la mémoire pour le texte

Déterminons une base pour la mémoire nécessaire pour travailler avec ce fichier de données. Tout d'abord, redémarrez Python et essayez une expérience très simple consistant simplement à ouvrir le fichier et à stocker ses données dans une seule chaîne de caractères :

```python
>>> # --- RESTART
>>> import tracemalloc
>>> f = open('ctabus.csv')
>>> tracemalloc.start()
>>> data = f.read()
>>> len(data)
12361039
>>> current, peak = tracemalloc.get_traced_memory()
>>> current
12369664
>>> peak
24730766
>>>
```

Vos résultats peuvent varier légèrement, mais vous devriez constater une utilisation de mémoire actuelle dans la plage de 12 Mo avec un pic de 24 Mo.

Que se passe-t-il si vous lisez tout le fichier dans une liste de chaînes de caractères à la place? Redémarrez Python et essayez ceci :

```python
>>> # --- RESTART
>>> import tracemalloc
>>> f = open('/home/labex/project/ctabus.csv')
>>> tracemalloc.start()
>>> lines = f.readlines()
>>> len(lines)
577564
>>> current, peak = tracemalloc.get_traced_memory()
>>> current
45828030
>>> peak
45867371
>>>
```

Vous devriez constater que l'utilisation de mémoire augmente considérablement, dans la plage de 40 à 50 Mo. Question à réfléchir : quelle pourrait être la source de cette surcharge supplémentaire?
