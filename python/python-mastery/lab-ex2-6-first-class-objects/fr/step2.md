# Création d'une fonction utilitaire de parsing

Créez un nouveau fichier `reader.py`. Dans ce fichier, définissez une fonction utilitaire `read_csv_as_dicts()` qui lit un fichier de données CSV dans une liste de dictionnaires où l'utilisateur spécifie les conversions de type pour chaque colonne.

Voici comment cela devrait fonctionner :

```python
>>> import reader
>>> portfolio = reader.read_csv_as_dicts('portfolio.csv', [str,int,float])
>>> for s in portfolio:
         print(s)

{'name': 'AA','shares': 100, 'price': 32.2}
{'name': 'IBM','shares': 50, 'price': 91.1}
{'name': 'CAT','shares': 150, 'price': 83.44}
{'name': 'MSFT','shares': 200, 'price': 51.23}
{'name': 'GE','shares': 95, 'price': 40.37}
{'name': 'MSFT','shares': 50, 'price': 65.1}
{'name': 'IBM','shares': 100, 'price': 70.44}
>>>
```

Ou, si vous vouliez lire les données CTA :

```python
>>> rows = reader.read_csv_as_dicts('ctabus.csv', [str,str,str,int])
>>> len(rows)
577563
>>> rows[0]
{'daytype': 'U', 'route': '3', 'rides': 7354, 'date': '01/01/2001'}
>>>
```
