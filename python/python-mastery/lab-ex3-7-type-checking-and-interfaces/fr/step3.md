# Création de classes de modèle d'algorithme

Dans cette étape, nous allons utiliser des classes de base abstraites pour implémenter le modèle de méthode de gabarit (template method pattern). L'objectif est de réduire la duplication de code dans la fonctionnalité d'analyse de fichiers CSV. La duplication de code peut rendre votre code plus difficile à maintenir et à mettre à jour. En utilisant le modèle de méthode de gabarit, nous pouvons créer une structure commune pour notre code d'analyse de CSV et laisser les sous - classes gérer les détails spécifiques.

## Comprendre le modèle de méthode de gabarit

Le modèle de méthode de gabarit est un modèle de conception comportemental. C'est comme un plan pour un algorithme. Dans une méthode, il définit la structure globale ou le "squelette" d'un algorithme. Cependant, il n'implémente pas entièrement toutes les étapes. Au lieu de cela, il reporte certaines étapes aux sous - classes. Cela signifie que les sous - classes peuvent redéfinir certaines parties de l'algorithme sans changer sa structure globale.

Dans notre cas, si vous regardez le fichier `reader.py`, vous remarquerez que les fonctions `read_csv_as_dicts()` et `read_csv_as_instances()` ont beaucoup de code similaire. La principale différence entre elles est la façon dont elles créent des enregistrements à partir des lignes du fichier CSV. En utilisant le modèle de méthode de gabarit, nous pouvons éviter d'écrire le même code plusieurs fois.

## Ajout de la classe de base CSVParser

Commençons par ajouter une classe de base abstraite pour notre analyse de CSV. Ouvrez le fichier `reader.py`. Nous allons ajouter la classe de base abstraite `CSVParser` tout en haut du fichier, juste après les instructions d'importation.

```python
# reader.py
import csv
from abc import ABC, abstractmethod

class CSVParser(ABC):
    def parse(self, filename):
        records = []
        with open(filename) as f:
            rows = csv.reader(f)
            headers = next(rows)
            for row in rows:
                record = self.make_record(headers, row)
                records.append(record)
        return records

    @abstractmethod
    def make_record(self, headers, row):
        pass
```

Cette classe `CSVParser` sert de modèle pour l'analyse de CSV. La méthode `parse` contient les étapes communes pour lire un fichier CSV, comme ouvrir le fichier, obtenir les en - têtes et itérer sur les lignes. La logique spécifique pour créer un enregistrement à partir d'une ligne est abstraite dans la méthode `make_record()`. Étant donné qu'il s'agit d'une méthode abstraite, toute classe qui hérite de `CSVParser` doit implémenter cette méthode.

## Implémentation des classes de parseur concrètes

Maintenant que nous avons notre classe de base, nous devons créer les classes de parseur concrètes. Ces classes implémenteront la logique spécifique de création d'enregistrements.

```python
class DictCSVParser(CSVParser):
    def __init__(self, types):
        self.types = types

    def make_record(self, headers, row):
        return { name: func(val) for name, func, val in zip(headers, self.types, row) }

class InstanceCSVParser(CSVParser):
    def __init__(self, cls):
        self.cls = cls

    def make_record(self, headers, row):
        return self.cls.from_row(row)
```

La classe `DictCSVParser` est utilisée pour créer des enregistrements sous forme de dictionnaires. Elle prend une liste de types dans son constructeur. La méthode `make_record` utilise ces types pour convertir les valeurs de la ligne et créer un dictionnaire.

La classe `InstanceCSVParser` est utilisée pour créer des enregistrements sous forme d'instances d'une classe. Elle prend une classe dans son constructeur. La méthode `make_record` appelle la méthode `from_row` de cette classe pour créer une instance à partir de la ligne.

## Refactorisation des fonctions originales

Maintenant, refactorisons les fonctions originales `read_csv_as_dicts()` et `read_csv_as_instances()` pour utiliser ces nouvelles classes.

```python
def read_csv_as_dicts(filename, types):
    '''
    Read a CSV file into a list of dictionaries with appropriate type conversion.
    '''
    parser = DictCSVParser(types)
    return parser.parse(filename)

def read_csv_as_instances(filename, cls):
    '''
    Read a CSV file into a list of instances of a class.
    '''
    parser = InstanceCSVParser(cls)
    return parser.parse(filename)
```

Ces fonctions refactorisées ont la même interface que les originales. Mais en interne, elles utilisent les nouvelles classes de parseur que nous venons de créer. De cette façon, nous avons séparé la logique d'analyse de CSV commune de la logique spécifique de création d'enregistrements.

## Test de votre implémentation

Vérifions si notre code refactorisé fonctionne correctement. Créez un fichier nommé `test_reader.py` et ajoutez le code suivant.

```python
import reader
import stock

# Test the refactored read_csv_as_instances function
portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
print("First stock:", portfolio[0])

# Test the refactored read_csv_as_dicts function
portfolio_dicts = reader.read_csv_as_dicts('portfolio.csv', [str, int, float])
print("First stock as dict:", portfolio_dicts[0])

# Test direct use of a parser
parser = reader.DictCSVParser([str, int, float])
portfolio_dicts2 = parser.parse('portfolio.csv')
print("First stock from direct parser:", portfolio_dicts2[0])
```

Pour exécuter le test, ouvrez votre terminal et exécutez la commande suivante :

```bash
python test_reader.py
```

Vous devriez voir une sortie similaire à celle - ci :

```
First stock: Stock('AA', 100, 32.2)
First stock as dict: {'name': 'AA', 'shares': 100, 'price': 32.2}
First stock from direct parser: {'name': 'AA', 'shares': 100, 'price': 32.2}
```

Si vous voyez cette sortie, cela signifie que votre code refactorisé fonctionne correctement. Les fonctions originales et l'utilisation directe des parseurs produisent tous les résultats attendus.
