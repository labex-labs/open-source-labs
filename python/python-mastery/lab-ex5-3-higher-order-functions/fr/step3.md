# Refactorisation des fonctions existantes

Maintenant, nous avons créé une fonction de haut niveau appelée `convert_csv()`. Les fonctions de haut niveau sont des fonctions qui peuvent prendre d'autres fonctions comme arguments ou renvoyer des fonctions en résultat. Ce sont des concepts puissants en Python qui nous aident à écrire un code plus modulaire et réutilisable. Dans cette section, nous allons utiliser cette fonction de haut niveau pour refactoriser les fonctions originales `csv_as_dicts()` et `csv_as_instances()`. La refactorisation est le processus de restructuration d'un code existant sans changer son comportement externe, dans le but d'améliorer sa structure interne, par exemple en éliminant la duplication de code.

Commençons par ouvrir le fichier `reader.py` dans l'éditeur WebIDE. Nous allons mettre à jour les fonctions comme suit :

1. Tout d'abord, nous allons remplacer la fonction `csv_as_dicts()`. Cette fonction est utilisée pour convertir des lignes de données CSV en une liste de dictionnaires. Voici le nouveau code :

```python
def csv_as_dicts(lines, types, *, headers=None):
    '''
    Convert lines of CSV data into a list of dictionaries
    '''
    def dict_converter(headers, row):
        return {name: func(val) for name, func, val in zip(headers, types, row)}

    return convert_csv(lines, dict_converter, headers=headers)
```

Dans ce code, nous définissons une fonction interne `dict_converter` qui prend `headers` et `row` comme arguments. Elle utilise une compréhension de dictionnaire pour créer un dictionnaire où les clés sont les noms des en - têtes et les valeurs sont le résultat de l'application de la fonction de conversion de type correspondante aux valeurs de la ligne. Ensuite, nous appelons la fonction `convert_csv()` avec la fonction `dict_converter` comme argument.

2. Ensuite, nous allons remplacer la fonction `csv_as_instances()`. Cette fonction est utilisée pour convertir des lignes de données CSV en une liste d'instances d'une classe donnée. Voici le nouveau code :

```python
def csv_as_instances(lines, cls, *, headers=None):
    '''
    Convert lines of CSV data into a list of instances
    '''
    def instance_converter(headers, row):
        return cls.from_row(row)

    return convert_csv(lines, instance_converter, headers=headers)
```

Dans ce code, nous définissons une fonction interne `instance_converter` qui prend `headers` et `row` comme arguments. Elle appelle la méthode de classe `from_row` de la classe donnée `cls` pour créer une instance à partir de la ligne. Ensuite, nous appelons la fonction `convert_csv()` avec la fonction `instance_converter` comme argument.

Après avoir refactorisé ces fonctions, nous devons les tester pour nous assurer qu'elles fonctionnent toujours comme prévu. Pour ce faire, nous allons exécuter les commandes suivantes dans un interpréteur Python :

```bash
cd ~/project
python3 -i reader.py
```

La commande `cd ~/project` change le répertoire de travail actuel pour le répertoire `project`. La commande `python3 -i reader.py` exécute le fichier `reader.py` en mode interactif, ce qui signifie que nous pouvons continuer à exécuter du code Python après que le fichier ait terminé son exécution.

Une fois l'interpréteur Python ouvert, nous allons exécuter le code suivant pour tester les fonctions refactorisées :

```python
# Define a simple Stock class for testing
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @classmethod
    def from_row(cls, row):
        return cls(row[0], int(row[1]), float(row[2]))

    def __repr__(self):
        return f'Stock({self.name}, {self.shares}, {self.price})'

# Test csv_as_dicts
with open('portfolio.csv') as f:
    portfolio_dicts = csv_as_dicts(f, [str, int, float])
print("First dictionary:", portfolio_dicts[0])

# Test csv_as_instances
with open('portfolio.csv') as f:
    portfolio_instances = csv_as_instances(f, Stock)
print("First instance:", portfolio_instances[0])
```

Dans ce code, nous définissons tout d'abord une simple classe `Stock` pour les tests. La méthode `__init__` initialise les attributs d'une instance `Stock`. La méthode de classe `from_row` crée une instance `Stock` à partir d'une ligne de données CSV. La méthode `__repr__` fournit une représentation sous forme de chaîne de caractères de l'instance `Stock`.

Ensuite, nous testons la fonction `csv_as_dicts()` en ouvrant le fichier `portfolio.csv` et en le passant à la fonction avec une liste de fonctions de conversion de type. Nous affichons le premier dictionnaire de la liste résultante.

Enfin, nous testons la fonction `csv_as_instances()` en ouvrant le fichier `portfolio.csv` et en le passant à la fonction avec la classe `Stock`. Nous affichons la première instance de la liste résultante.

Si tout fonctionne correctement, vous devriez voir une sortie similaire à ceci :

```
First dictionary: {'name': 'AA', 'shares': 100, 'price': 32.2}
First instance: Stock(AA, 100, 32.2)
```

Cette sortie indique que nos fonctions refactorisées fonctionnent correctement. Nous avons éliminé avec succès la duplication de code tout en conservant la même fonctionnalité.

Pour quitter l'interpréteur Python, vous pouvez taper `exit()` ou appuyer sur Ctrl + D.
