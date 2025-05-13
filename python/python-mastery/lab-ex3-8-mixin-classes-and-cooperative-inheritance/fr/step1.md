# Comprendre le problème avec le formatage des colonnes

Dans cette étape, nous allons examiner une limitation de notre implémentation actuelle du formatage de tableau. Nous examinerons également certaines solutions possibles à ce problème.

Tout d'abord, comprenons ce que nous allons faire. Nous allons ouvrir l'éditeur VSCode et examiner le fichier `tableformat.py` dans le répertoire du projet. Ce fichier est important car il contient le code qui nous permet de formater des données tabulaires de différentes manières, comme en texte, CSV ou HTML.

Pour ouvrir le fichier, nous utiliserons les commandes suivantes dans le terminal. La commande `cd` change le répertoire vers le répertoire du projet, et la commande `code` ouvre le fichier `tableformat.py` dans VSCode.

```bash
cd ~/project
touch tableformat.py
```

Lorsque vous ouvrez le fichier, vous remarquerez que plusieurs classes sont définies. Ces classes jouent différents rôles dans le formatage des données du tableau.

- `TableFormatter` : Il s'agit d'une classe de base abstraite. Elle possède des méthodes qui sont utilisées pour formater les en-têtes et les lignes du tableau. Considérez-la comme un modèle pour les autres classes de formatage.
- `TextTableFormatter` : Cette classe est utilisée pour afficher le tableau en format texte brut.
- `CSVTableFormatter` : Elle est responsable du formatage des données du tableau au format CSV (Comma-Separated Values - Valeurs séparées par des virgules).
- `HTMLTableFormatter` : Cette classe formate les données du tableau au format HTML.

Il existe également une fonction `print_table()` dans le fichier. Cette fonction utilise les classes de formatage que nous venons de mentionner pour afficher les données tabulaires.

Maintenant, voyons comment ces classes fonctionnent. Dans votre répertoire `/home/labex/project`, créez un nouveau fichier nommé `step1_test1.py` en utilisant votre éditeur ou la commande `touch`. Ajoutez le code Python suivant :

```python
# step1_test1.py
from tableformat import print_table, TextTableFormatter, portfolio

formatter = TextTableFormatter()
print("--- Running Step 1 Test 1 ---")
print_table(portfolio, ['name', 'shares', 'price'], formatter)
print("-----------------------------")
```

Enregistrez le fichier et exécutez-le depuis votre terminal :

```bash
python3 step1_test1.py
```

Après avoir exécuté le script, vous devriez voir une sortie similaire à celle-ci :

```
--- Running Step 1 Test 1 ---
      name     shares      price
---------- ---------- ----------
        AA        100       32.2
       IBM         50       91.1
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50       65.1
       IBM        100      70.44
-----------------------------
```

Maintenant, trouvons le problème. Remarquez que les valeurs dans la colonne `price` ne sont pas formatées de manière cohérente. Certaines valeurs ont une décimale, comme 32.2, tandis que d'autres en ont deux, comme 51.23. Dans les données financières, nous voulons généralement que le formatage soit cohérent.

Voici à quoi nous voulons que la sortie ressemble :

```
      name     shares      price
---------- ---------- ----------
        AA        100      32.20
       IBM         50      91.10
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50      65.10
       IBM        100      70.44
```

Une façon de résoudre ce problème est de modifier la fonction `print_table()` pour accepter des spécifications de format. Voyons comment cela fonctionne _sans_ réellement modifier `tableformat.py`. Créez un nouveau fichier nommé `step1_test2.py` avec le contenu suivant. Ce script redéfinit la fonction `print_table` localement à des fins de démonstration.

```python
# step1_test2.py
from tableformat import TextTableFormatter

# Re-define Stock and portfolio locally for this example
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

portfolio = [
    Stock('AA', 100, 32.20), Stock('IBM', 50, 91.10), Stock('CAT', 150, 83.44),
    Stock('MSFT', 200, 51.23), Stock('GE', 95, 40.37), Stock('MSFT', 50, 65.10),
    Stock('IBM', 100, 70.44)
]

# Define a modified print_table locally
def print_table_modified(records, fields, formats, formatter):
    formatter.headings(fields)
    for r in records:
        # Apply formats to the original attribute values
        rowdata = [(fmt % getattr(r, fieldname))
                   for fieldname, fmt in zip(fields, formats)]
        # Pass the already formatted strings to the formatter's row method
        formatter.row(rowdata)

print("--- Running Step 1 Test 2 ---")
formatter = TextTableFormatter()
# Note: TextTableFormatter.row expects strings already formatted for width.
# This example might not align perfectly yet, but demonstrates passing formats.
print_table_modified(portfolio,
                     ['name', 'shares', 'price'],
                     ['%10s', '%10d', '%10.2f'], # Using widths
                     formatter)
print("-----------------------------")

```

Exécutez ce script :

```bash
python3 step1_test2.py
```

Cette approche démontre le passage de formats, mais la modification de `print_table` a un inconvénient : la modification de l'interface de la fonction pourrait casser le code existant qui utilise la version originale.

Une autre approche consiste à créer un formateur personnalisé par sous-classement (subclassing). Nous pouvons créer une nouvelle classe qui hérite de `TextTableFormatter` et redéfinir (override) la méthode `row()`. Créez un fichier `step1_test3.py` :

```python
# step1_test3.py
from tableformat import TextTableFormatter, print_table, portfolio

class PortfolioFormatter(TextTableFormatter):
    def row(self, rowdata):
        # Example: Add a prefix to demonstrate overriding
        # Note: The original lab description's formatting example had data type issues
        # because print_table sends strings to this method. This is a simpler demo.
        print("> ", end="") # Add a simple prefix to the line start
        super().row(rowdata) # Call the parent method

print("--- Running Step 1 Test 3 ---")
formatter = PortfolioFormatter()
print_table(portfolio, ['name', 'shares', 'price'], formatter)
print("-----------------------------")
```

Exécutez le script :

```bash
python3 step1_test3.py
```

Cette solution fonctionne pour démontrer le sous-classement, mais la création d'une nouvelle classe pour chaque variation de formatage n'est pas pratique. De plus, vous êtes lié à la classe de base dont vous héritez (ici, `TextTableFormatter`).

Dans l'étape suivante, nous explorerons une solution plus élégante utilisant les classes mixin.
