# Création d'une fonction utilitaire pour le traitement de fichiers CSV

Maintenant que nous comprenons comment les objets de première classe de Python peuvent nous aider dans la conversion de données, nous allons créer une fonction utilitaire réutilisable. Cette fonction lira les données d'un fichier CSV et les transformera en une liste de dictionnaires. C'est une opération très utile car les fichiers CSV sont couramment utilisés pour stocker des données tabulaires, et les convertir en une liste de dictionnaires facilite la manipulation des données en Python.

## Création de l'utilitaire de lecture de fichiers CSV

Tout d'abord, ouvrez le WebIDE. Une fois ouvert, accédez au répertoire du projet et créez un nouveau fichier nommé `reader.py`. Dans ce fichier, nous allons définir une fonction qui lit les données d'un fichier CSV et applique des conversions de type. Les conversions de type sont importantes car les données dans un fichier CSV sont généralement lues sous forme de chaînes de caractères, mais nous pouvons avoir besoin de différents types de données comme des entiers ou des nombres à virgule flottante pour un traitement ultérieur.

Ajoutez le code suivant à `reader.py` :

```python
import csv

def read_csv_as_dicts(filename, types):
    """
    Read a CSV file into a list of dictionaries, converting each field according
    to the types provided.

    Parameters:
    filename (str): Name of the CSV file to read
    types (list): List of type conversion functions for each column

    Returns:
    list: List of dictionaries representing the CSV data
    """
    records = []
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        headers = next(rows)  # Get the column headers

        for row in rows:
            # Apply type conversions to each value in the row
            converted_row = [func(val) for func, val in zip(types, row)]

            # Create a dictionary mapping headers to converted values
            record = dict(zip(headers, converted_row))
            records.append(record)

    return records
```

Cette fonction ouvre d'abord le fichier CSV spécifié. Elle lit ensuite les en-têtes du fichier CSV, qui sont les noms des colonnes. Ensuite, elle parcourt chaque ligne du fichier. Pour chaque valeur dans la ligne, elle applique la fonction de conversion de type correspondante de la liste `types`. Enfin, elle crée un dictionnaire où les clés sont les en-têtes de colonne et les valeurs sont les données converties, et ajoute ce dictionnaire à la liste `records`. Une fois que toutes les lignes ont été traitées, elle retourne la liste `records`.

## Test de la fonction utilitaire

Testons notre fonction utilitaire. Tout d'abord, ouvrez un terminal et lancez l'interpréteur Python en tapant :

```bash
python3
```

Maintenant que nous sommes dans l'interpréteur Python, nous pouvons utiliser notre fonction pour lire les données du portefeuille. Les données du portefeuille sont contenues dans un fichier CSV qui contient des informations sur les actions, telles que le nom de l'action, le nombre de parts et le prix.

```python
import reader
portfolio = reader.read_csv_as_dicts('portfolio.csv', [str, int, float])
for record in portfolio[:3]:  # Show the first 3 records
    print(record)
```

Lorsque vous exécutez ce code, vous devriez voir une sortie similaire à :

```
{'name': 'AA', 'shares': 100, 'price': 32.2}
{'name': 'IBM', 'shares': 50, 'price': 91.1}
{'name': 'CAT', 'shares': 150, 'price': 83.44}
```

Cette sortie montre les trois premiers enregistrements des données du portefeuille, avec les types de données correctement convertis.

Essayons également notre fonction avec les données des bus CTA. Les données des bus CTA sont contenues dans un autre fichier CSV qui contient des informations sur les itinéraires de bus, les dates, les types de jour et le nombre de trajets.

```python
rows = reader.read_csv_as_dicts('ctabus.csv', [str, str, str, int])
print(f"Total rows: {len(rows)}")
print("First row:", rows[0])
```

La sortie devrait être quelque chose comme :

```
Total rows: 577563
First row: {'route': '3', 'date': '01/01/2001', 'daytype': 'U', 'rides': 7354}
```

Cela montre que notre fonction peut gérer différents fichiers CSV et appliquer les conversions de type appropriées.

Pour quitter l'interpréteur Python, tapez :

```python
exit()
```

Vous avez maintenant créé une fonction utilitaire réutilisable qui peut lire n'importe quel fichier CSV et appliquer les conversions de type appropriées. Cela démontre la puissance des objets de première classe de Python et comment ils peuvent être utilisés pour créer un code flexible et réutilisable.
