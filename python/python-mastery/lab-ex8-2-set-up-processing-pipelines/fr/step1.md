# Configuration d'un pipeline de traitement

Un avantage majeur des générateurs est qu'ils vous permettent de créer des programmes qui configurent des pipelines de traitement - tout comme les tubes sur les systèmes Unix. Expérimentez ce concept en effectuant les étapes suivantes :

```python
>>> from follow import follow
>>> import csv
>>> lines = follow('stocklog.csv')
>>> rows = csv.reader(lines)
>>> for row in rows:
        print(row)

['BA', '98.35', '6/11/2007', '09:41.07', '0.16', '98.25', '98.35', '98.31', '158148']
['AA', '39.63', '6/11/2007', '09:41.07', '-0.03', '39.67', '39.63', '39.31', '270224']
['XOM', '82.45', '6/11/2007', '09:41.07', '-0.23', '82.68', '82.64', '82.41', '748062']
['PG', '62.95', '6/11/2007', '09:41.08', '-0.12', '62.80', '62.97', '62.61', '454327']
...
```

Eh bien, c'est intéressant. Ce que vous voyez ici est que la sortie de la fonction `follow()` a été acheminée vers la fonction `csv.reader()` et que nous obtenons maintenant une séquence de lignes divisées.
