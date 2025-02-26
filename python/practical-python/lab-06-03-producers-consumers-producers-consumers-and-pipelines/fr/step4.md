# Exercice 6.9 : Configuration d'un pipeline plus complexe

Poussez l'idée de pipeline un peu plus loin en effectuant plus d'actions.

```python
>>> from suivre import suivre
>>> import csv
>>> lignes = suivre('stocklog.csv')
>>> lignes_csv = csv.reader(lignes)
>>> for ligne_csv in lignes_csv:
        print(ligne_csv)

['GOOG', '1502.08', '2023-10-01', '09:37.19', '1.83', '1500.25', '1502.08', '1500.25', '731']
['AAPL', '252.33', '2023-10-01', '09:37.19', '1.83', '250.50', '252.33', '250.50', '681']
['GOOG', '1502.09', '2023-10-01', '09:37.21', '1.84', '1500.25', '1502.09', '1500.25', '734']
['AAPL', '252.34', '2023-10-01', '09:37.21', '1.84', '250.50', '252.34', '250.50', '684']
['GOOG', '1502.10', '2023-10-01', '09:37.23', '1.85', '1500.25', '1502.10', '1500.25', '738']
['AAPL', '252.35', '2023-10-01', '09:37.23', '1.85', '250.50', '252.35', '250.50', '688']
...
```

Eh bien, c'est intéressant. Ce que vous voyez ici est que la sortie de la fonction `suivre()` a été acheminée vers la fonction `csv.reader()` et que nous obtenons maintenant une séquence de lignes divisées.
