# Projet de défi spécial

Dans l'exercice 2.5, nous avons créé une classe `RideData` qui stockait toutes les données du bus en colonnes, mais présentait en fait les données à un utilisateur sous forme d'une séquence de dictionnaires. Cela a économisé beaucoup de mémoire grâce à diverses formes de magie.

Pouvez-vous généraliser cette idée? Plus précisément, pouvez-vous créer une fonction générique `read_csv_as_columns()` qui fonctionne comme ceci :

```python
>>> data = read_csv_as_columns('ctabus.csv', types=[str, str, str, int])
>>> data
<__main__.DataCollection object at 0x102b45048>
>>> len(data)
577563
>>> data[0]
{'route': '3', 'date': '01/01/2001', 'daytype': 'U', 'rides': 7354}
>>> data[1]
{'route': '4', 'date': '01/01/2001', 'daytype': 'U', 'rides': 9288}
>>> data[2]
{'route': '6', 'date': '01/01/2001', 'daytype': 'U', 'rides': 6048}
>>>
```

Cette fonction est censée être générique - vous pouvez lui donner n'importe quel fichier et une liste des types de colonnes et elle lira les données. Les données sont lues dans une classe `DataCollection` qui stocke les données en colonnes à l'intérieur. Les données apparaissent sous forme d'une séquence de dictionnaires lorsqu'elles sont accessibles cependant.

Essayez d'utiliser cette fonction avec le truc d'internement de chaînes dans la dernière partie. Combien de mémoire faut-il pour stocker toutes les données de trajet maintenant? Pouvez-vous toujours utiliser cette fonction avec votre code d'analyse CTA antérieur?

## Note :

Complétez la fonction `read_csv_as_columns()` dans le fichier `colreader.py`.
