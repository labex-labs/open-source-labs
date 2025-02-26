# En panne de bus

Le fichier `ctabus.csv` est un fichier CSV contenant les données quotidiennes de la fréquentation des bus de l'Autorité de transport en commun de Chicago (CTA) du 1er janvier 2001 au 31 août 2013. Il contient environ 577 000 lignes de données. Utilisez Python pour afficher quelques lignes de données pour voir à quoi cela ressemble :

```python
>>> f = open('/home/labex/project/ctabus.csv')
>>> next(f)
'route,date,daytype,rides\n'
>>> next(f)
'3,01/01/2001,U,7354\n'
>>> next(f)
'4,01/01/2001,U,9288\n'
>>>
```

Il y a 4 colonnes de données.

- route : Colonne 0. Le nom de la ligne de bus.
- date : Colonne 1. Une chaîne de caractères de date au format MM/DD/YYYY.
- daytype : Colonne 2. Un code de type de jour (U = dimanche / fête, A = samedi, W = jour ouvrable)
- rides : Colonne 3. Nombre total de passagers (entier)

La colonne `rides` enregistre le nombre total de personnes qui sont montées dans un bus sur cette ligne le jour donné. Ainsi, dans l'exemple, 7354 personnes ont pris le bus numéro 3 le 1er janvier 2001.
