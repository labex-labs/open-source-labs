# Exercice 3.6 : Travailler sans en-têtes

Certains fichiers CSV ne contiennent pas d'informations d'en-tête. Par exemple, le fichier `prices.csv` ressemble à ceci :

```csv
"AA",9.22
"AXP",24.85
"BA",44.85
"BAC",11.27
...
```

Modifiez la fonction `parse_csv()` dans `/home/labex/project/fileparse_3.6.py` de sorte qu'elle puisse fonctionner avec de tels fichiers en créant une liste de tuples à la place. Par exemple :

```python
>>> prices = parse_csv('/home/labex/project/prices.csv', types=[str,float], has_headers=False)
>>> prices
[('AA', 9.22), ('AXP', 24.85), ('BA', 44.85), ('BAC', 11.27), ('C', 3.72), ('CAT', 35.46), ('CVX', 66.67), ('DD', 28.47), ('DIS', 24.22), ('GE', 13.48), ('GM', 0.75), ('HD', 23.16), ('HPQ', 34.35), ('IBM', 106.28), ('INTC', 15.72), ('JNJ', 55.16), ('JPM', 36.9), ('KFT', 26.11), ('KO', 49.16), ('MCD', 58.99), ('MMM', 57.1), ('MRK', 27.58), ('MSFT', 20.89), ('PFE', 15.19), ('PG', 51.94), ('T', 24.79), ('UTX', 52.61), ('VZ', 29.26), ('WMT', 49.74), ('XOM', 69.35)]
>>>
```

Pour apporter ces modifications, vous devrez modifier le code de sorte que la première ligne de données ne soit pas interprétée comme une ligne d'en-tête. De plus, vous devrez vous assurer de ne pas créer de dictionnaires car il n'y a plus de noms de colonnes pour servir de clés.
