# Exercice 3.7 : Sélectionner un délimiteur de colonne différent

Bien que les fichiers CSV soient assez courants, il est également possible que vous rencontriez un fichier utilisant un séparateur de colonne différent, tel qu'un tabulation ou un espace. Par exemple, le fichier `portfolio.dat` ressemble à ceci :

```csv
name shares price
"AA" 100 32.20
"IBM" 50 91.10
"CAT" 150 83.44
"MSFT" 200 51.23
"GE" 95 40.37
"MSFT" 50 65.10
"IBM" 100 70.44
```

La fonction `csv.reader()` permet de spécifier un délimiteur de colonne différent comme suit :

```python
rows = csv.reader(f, delimiter=' ')
```

Modifiez votre fonction `parse_csv()` dans `/home/labex/project/fileparse_3.7.py` de sorte qu'elle permette également de changer le délimiteur.

Par exemple :

```python
>>> portfolio = parse_csv('/home/labex/project/portfolio.dat', types=[str, int, float], delimiter=' ')
>>> portfolio
[{'name': 'AA','shares': 100, 'price': 32.2}, {'name': 'IBM','shares': 50, 'price': 91.1}, {'name': 'CAT','shares': 150, 'price': 83.44}, {'name': 'MSFT','shares': 200, 'price': 51.23}, {'name': 'GE','shares': 95, 'price': 40.37}, {'name': 'MSFT','shares': 50, 'price': 65.1}, {'name': 'IBM','shares': 100, 'price': 70.44}]
>>>
```
