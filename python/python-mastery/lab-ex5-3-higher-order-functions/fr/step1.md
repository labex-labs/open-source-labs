# Comprendre la duplication de code

Commençons par examiner le code actuel dans le fichier `reader.py`. En programmation, examiner le code existant est une étape importante pour comprendre le fonctionnement des choses et identifier les domaines d'amélioration. Vous pouvez ouvrir le fichier `reader.py` dans l'éditeur WebIDE. Il existe deux façons de le faire. Vous pouvez cliquer sur le fichier dans l'explorateur de fichiers, ou vous pouvez exécuter les commandes suivantes dans le terminal. Ces commandes permettent d'abord de naviguer jusqu'au répertoire du projet, puis d'afficher le contenu du fichier `reader.py`.

```bash
cd ~/project
cat reader.py
```

Lorsque vous examinez le code, vous remarquerez qu'il y a deux fonctions. Les fonctions en Python sont des blocs de code qui effectuent une tâche spécifique. Voici les deux fonctions et ce qu'elles font :

1. `csv_as_dicts()` : Cette fonction prend des données CSV et les convertit en une liste de dictionnaires. Un dictionnaire en Python est une collection de paires clé - valeur, qui est utile pour stocker des données de manière structurée.
2. `csv_as_instances()` : Cette fonction prend des données CSV et les convertit en une liste d'instances. Une instance est un objet créé à partir d'une classe, qui est un modèle pour créer des objets.

Maintenant, examinons de plus près ces deux fonctions. Vous verrez qu'elles sont assez similaires. Les deux fonctions suivent les étapes suivantes :

- Tout d'abord, elles initialisent une liste `records` vide. Une liste en Python est une collection d'éléments qui peuvent être de différents types. Initialiser une liste vide signifie créer une liste sans éléments, qui sera utilisée pour stocker les données traitées.
- Ensuite, elles utilisent `csv.reader()` pour analyser (parser) l'entrée. Analyser signifie examiner les données d'entrée pour extraire des informations significatives. Dans ce cas, `csv.reader()` nous aide à lire les données CSV ligne par ligne.
- Elles gèrent les en - têtes de la même manière. Les en - têtes dans un fichier CSV sont la première ligne qui contient généralement les noms des colonnes.
- Après cela, elles parcourent chaque ligne des données CSV. Une boucle est une structure de programmation qui permet d'exécuter un bloc de code plusieurs fois.
- Pour chaque ligne, elles la traitent pour créer un enregistrement. Cet enregistrement peut être soit un dictionnaire, soit une instance, selon la fonction.
- Elles ajoutent (append) l'enregistrement à la liste `records`. Ajouter signifie ajouter un élément à la fin de la liste.
- Enfin, elles renvoient la liste `records`, qui contient toutes les données traitées.

Cette duplication de code pose problème pour plusieurs raisons. Lorsque le code est dupliqué :

- Il devient plus difficile à maintenir. Si vous avez besoin de modifier le code, vous devez apporter la même modification à plusieurs endroits. Cela prend plus de temps et d'efforts.
- Toutes les modifications doivent être implémentées à plusieurs endroits. Cela augmente la probabilité que vous oubliiez de faire la modification à l'un des endroits, entraînant un comportement incohérent.
- Cela augmente également la probabilité d'introduire des bugs. Les bugs sont des erreurs dans le code qui peuvent le faire se comporter de manière inattendue.

La seule différence réelle entre ces deux fonctions est la manière dont elles convertissent une ligne en enregistrement. C'est une situation classique où une fonction de haut niveau (higher - order function) peut être très utile. Une fonction de haut niveau est une fonction qui peut prendre une autre fonction comme argument ou renvoyer une fonction en résultat.

Examinons quelques exemples d'utilisation de ces fonctions pour mieux comprendre leur fonctionnement. Le code suivant montre comment utiliser `csv_as_dicts()` et `csv_as_instances()` :

```python
# Example of using csv_as_dicts
with open('portfolio.csv') as f:
    portfolio = csv_as_dicts(f, [str, int, float])
print(portfolio[0])  # {'name': 'AA', 'shares': 100, 'price': 32.2}

# Example of using csv_as_instances
class Stock:
    @classmethod
    def from_row(cls, row):
        return cls(row[0], int(row[1]), float(row[2]))

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

with open('portfolio.csv') as f:
    portfolio = csv_as_instances(f, Stock)
print(portfolio[0].name, portfolio[0].shares, portfolio[0].price)  # AA 100 32.2
```

Dans l'étape suivante, nous allons créer une fonction de haut niveau pour éliminer cette duplication de code. Cela rendra le code plus facilement maintenable et moins sujet aux erreurs.
