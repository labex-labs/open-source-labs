# Comprendre le contexte

Dans les exercices précédents, vous avez peut - être rencontré du code qui lit des fichiers CSV et stocke les données dans diverses structures de données. Le but de ce code est de prendre les données textuelles brutes d'un fichier CSV et de les convertir en objets Python plus utiles, tels que des dictionnaires ou des instances de classe. Cette conversion est essentielle car elle nous permet de travailler avec les données de manière plus structurée et significative dans nos programmes Python.

Le modèle typique pour lire des fichiers CSV suit souvent une structure spécifique. Voici un exemple de fonction qui lit un fichier CSV et convertit chaque ligne en un dictionnaire :

```python
import csv

def read_csv_as_dicts(filename, types):
    records = []
    with open(filename) as file:
        rows = csv.reader(file)
        headers = next(rows)
        for row in rows:
            record = { name: func(val)
                       for name, func, val in zip(headers, types, row) }
            records.append(record)
    return records
```

Analysons le fonctionnement de cette fonction. Tout d'abord, elle importe le module `csv`, qui fournit des fonctionnalités pour travailler avec les fichiers CSV en Python. La fonction prend deux paramètres : `filename`, qui est le nom du fichier CSV à lire, et `types`, qui est une liste de fonctions utilisées pour convertir les données de chaque colonne en le type de données approprié.

À l'intérieur de la fonction, elle initialise une liste vide appelée `records` pour stocker les dictionnaires représentant chaque ligne du fichier CSV. Elle ouvre ensuite le fichier à l'aide de l'instruction `with`, qui garantit que le fichier est correctement fermé après l'exécution du bloc de code. La fonction `csv.reader` est utilisée pour créer un itérateur qui lit chaque ligne du fichier CSV. On suppose que la première ligne est l'en - tête, donc elle est récupérée à l'aide de la fonction `next`.

Ensuite, la fonction itère sur les lignes restantes du fichier CSV. Pour chaque ligne, elle crée un dictionnaire à l'aide d'une compréhension de dictionnaire. Les clés du dictionnaire sont les en - têtes de colonne, et les valeurs sont le résultat de l'application de la fonction de conversion de type correspondante de la liste `types` à la valeur de la ligne. Enfin, le dictionnaire est ajouté à la liste `records`, et la fonction retourne la liste de dictionnaires.

Maintenant, regardons une fonction similaire qui lit les données d'un fichier CSV dans des instances de classe :

```python
def read_csv_as_instances(filename, cls):
    records = []
    with open(filename) as file:
        rows = csv.reader(file)
        headers = next(rows)
        for row in rows:
            record = cls.from_row(row)
            records.append(record)
    return records
```

Cette fonction est similaire à la précédente, mais au lieu de créer des dictionnaires, elle crée des instances d'une classe. La fonction prend deux paramètres : `filename`, qui est le nom du fichier CSV à lire, et `cls`, qui est la classe dont les instances seront créées.

À l'intérieur de la fonction, elle suit une structure similaire à la fonction précédente. Elle initialise une liste vide appelée `records` pour stocker les instances de classe. Elle ouvre ensuite le fichier, lit les en - têtes et itère sur les lignes restantes. Pour chaque ligne, elle appelle la méthode `from_row` de la classe `cls` pour créer une instance de la classe à l'aide des données de la ligne. L'instance est ensuite ajoutée à la liste `records`, et la fonction retourne la liste d'instances.

Dans ce laboratoire, nous allons refactoriser ces fonctions pour les rendre plus flexibles et robustes. Nous allons également explorer le système d'indication de type (type hinting) de Python, qui nous permet de spécifier les types attendus des paramètres et des valeurs de retour de nos fonctions. Cela peut rendre notre code plus lisible et plus facile à comprendre, en particulier pour les autres développeurs qui pourraient travailler avec notre code.

Commençons par créer un fichier `reader.py` et y ajouter ces fonctions initiales. Assurez - vous de tester ces fonctions pour vous assurer qu'elles fonctionnent correctement avant de passer aux étapes suivantes.
