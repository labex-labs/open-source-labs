# Création d'une fonction de haut niveau (Higher-Order Function)

En Python, une fonction de haut niveau est une fonction qui peut prendre une autre fonction comme argument. Cela permet une plus grande flexibilité et une meilleure réutilisation du code. Maintenant, créons une fonction de haut niveau appelée `convert_csv()`. Cette fonction gérera les opérations communes de traitement des données CSV, tout en vous permettant de personnaliser la manière dont chaque ligne du CSV est convertie en un enregistrement.

Ouvrez le fichier `reader.py` dans l'éditeur WebIDE. Nous allons ajouter une fonction qui prendra un itérable de données CSV, une fonction de conversion et, éventuellement, des en - têtes de colonnes. La fonction de conversion sera utilisée pour transformer chaque ligne du CSV en un enregistrement.

Voici le code de la fonction `convert_csv()`. Copiez - le et collez - le dans votre fichier `reader.py` :

```python
def convert_csv(lines, conversion_func, *, headers=None):
    '''
    Convert lines of CSV data using the provided conversion function

    Args:
        lines: An iterable containing CSV data
        conversion_func: A function that takes headers and a row and returns a record
        headers: Column headers (optional). If None, the first row is used as headers

    Returns:
        A list of records as processed by conversion_func
    '''
    records = []
    rows = csv.reader(lines)
    if headers is None:
        headers = next(rows)
    for row in rows:
        record = conversion_func(headers, row)
        records.append(record)
    return records
```

Analysons ce que fait cette fonction. Tout d'abord, elle initialise une liste vide appelée `records` pour stocker les enregistrements convertis. Ensuite, elle utilise la fonction `csv.reader()` pour lire les lignes de données CSV. Si aucun en - tête n'est fourni, elle prend la première ligne comme en - tête. Pour chaque ligne suivante, elle applique la `conversion_func` pour convertir la ligne en un enregistrement et l'ajoute à la liste `records`. Enfin, elle renvoie la liste d'enregistrements.

Maintenant, nous avons besoin d'une simple fonction de conversion pour tester notre fonction `convert_csv()`. Cette fonction prendra les en - têtes et une ligne et convertira la ligne en un dictionnaire en utilisant les en - têtes comme clés.

Voici le code de la fonction `make_dict()`. Ajoutez également cette fonction à votre fichier `reader.py` :

```python
def make_dict(headers, row):
    '''
    Convert a row to a dictionary using the provided headers
    '''
    return dict(zip(headers, row))
```

La fonction `make_dict()` utilise la fonction `zip()` pour associer chaque en - tête à sa valeur correspondante dans la ligne, puis crée un dictionnaire à partir de ces paires.

Testons ces fonctions. Ouvrez un interpréteur Python en exécutant les commandes suivantes dans le terminal :

```bash
cd ~/project
python3 -i reader.py
```

L'option `-i` dans la commande `python3` lance l'interpréteur Python en mode interactif et importe le fichier `reader.py`, afin que nous puissions utiliser les fonctions que nous venons de définir.

Dans l'interpréteur Python, exécutez le code suivant pour tester nos fonctions :

```python
# Open the CSV file
lines = open('portfolio.csv')

# Convert to a list of dictionaries using our new function
result = convert_csv(lines, make_dict)

# Print the result
print(result)
```

Ce code ouvre le fichier `portfolio.csv`, utilise la fonction `convert_csv()` avec la fonction de conversion `make_dict()` pour convertir les données CSV en une liste de dictionnaires, puis affiche le résultat.

Vous devriez voir une sortie similaire à ceci :

```
[{'name': 'AA', 'shares': '100', 'price': '32.20'}, {'name': 'IBM', 'shares': '50', 'price': '91.10'}, {'name': 'CAT', 'shares': '150', 'price': '83.44'}, {'name': 'MSFT', 'shares': '200', 'price': '51.23'}, {'name': 'GE', 'shares': '95', 'price': '40.37'}, {'name': 'MSFT', 'shares': '50', 'price': '65.10'}, {'name': 'IBM', 'shares': '100', 'price': '70.44'}]
```

Cette sortie montre que notre fonction de haut niveau `convert_csv()` fonctionne correctement. Nous avons créé avec succès une fonction qui prend une autre fonction comme argument, ce qui nous permet de changer facilement la manière dont les données CSV sont converties.

Pour quitter l'interpréteur Python, vous pouvez taper `exit()` ou appuyer sur Ctrl + D.
