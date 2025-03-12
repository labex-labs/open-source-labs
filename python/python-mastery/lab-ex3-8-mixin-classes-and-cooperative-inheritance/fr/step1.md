# Comprendre le problème de formatage des colonnes

Dans cette étape, nous allons examiner une limitation de notre implémentation actuelle de formatage de tableaux. Nous allons également étudier quelques solutions possibles à ce problème.

Tout d'abord, comprenons ce que nous allons faire. Nous allons ouvrir l'éditeur VSCode et regarder le fichier `tableformat.py` dans le répertoire du projet. Ce fichier est important car il contient le code qui nous permet de formater des données tabulaires de différentes manières, comme en texte brut, au format CSV ou au format HTML.

Pour ouvrir le fichier, nous allons utiliser les commandes suivantes dans le terminal. La commande `cd` change le répertoire pour le répertoire du projet, et la commande `code` ouvre le fichier `tableformat.py` dans VSCode.

```bash
cd ~/project
code tableformat.py
```

Lorsque vous ouvrez le fichier, vous remarquerez qu'il y a plusieurs classes définies. Ces classes jouent différents rôles dans le formatage des données du tableau.

- `TableFormatter` : Il s'agit d'une classe abstraite de base. Elle a des méthodes qui sont utilisées pour formater les en-têtes et les lignes du tableau. Considérez-la comme un modèle pour les autres classes de formateur.
- `TextTableFormatter` : Cette classe est utilisée pour afficher le tableau au format texte brut.
- `CSVTableFormatter` : Elle est responsable du formatage des données du tableau au format CSV (Comma-Separated Values, valeurs séparées par des virgules).
- `HTMLTableFormatter` : Cette classe formate les données du tableau au format HTML.

Il y a également une fonction `print_table()` dans le fichier. Cette fonction utilise les classes de formateur que nous venons de mentionner pour afficher les données tabulaires.

Maintenant, voyons comment ces classes fonctionnent en exécutant un peu de code Python. Ouvrez un terminal et démarrez une session Python. Le code suivant importe les fonctions et les classes nécessaires du fichier `tableformat.py`, crée un objet `TextTableFormatter`, puis utilise la fonction `print_table()` pour afficher les données du portefeuille.

```python
python3 -c "
from tableformat import print_table, TextTableFormatter, portfolio
formatter = TextTableFormatter()
print_table(portfolio, ['name', 'shares', 'price'], formatter)
"
```

Après avoir exécuté le code, vous devriez voir une sortie similaire à ceci :

```
      name     shares      price
---------- ---------- ----------
        AA        100       32.2
       IBM         50       91.1
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50       65.1
       IBM        100      70.44
```

Maintenant, trouvons le problème. Remarquez que les valeurs dans la colonne `price` ne sont pas formatées de manière cohérente. Certaines valeurs ont une décimale, comme 32.2, tandis que d'autres en ont deux, comme 51.23. Dans les données financières, nous voulons généralement que le formatage soit cohérent.

Voici à quoi nous aimerions que la sortie ressemble :

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

Une façon de résoudre ce problème est de modifier la fonction `print_table()` pour qu'elle accepte des spécifications de format. Le code suivant montre comment nous pouvons le faire. Nous définissons une nouvelle fonction `print_table()` qui prend un paramètre supplémentaire `formats`. À l'intérieur de la fonction, nous utilisons ces spécifications de format pour formater chaque valeur de la ligne.

```python
python3 -c "
from tableformat import TextTableFormatter, portfolio

def print_table(records, fields, formats, formatter):
    formatter.headings(fields)
    for r in records:
        rowdata = [(fmt % getattr(r, fieldname))
             for fieldname, fmt in zip(fields, formats)]
        formatter.row(rowdata)

formatter = TextTableFormatter()
print_table(portfolio,
            ['name','shares','price'],
            ['%s','%d','%0.2f'],
            formatter)
"
```

Cette solution fonctionne, mais elle a un inconvénient. Changer l'interface de la fonction peut casser le code existant qui utilise l'ancienne version de la fonction `print_table()`.

Une autre approche consiste à créer un formateur personnalisé en utilisant la sous-classification. Nous pouvons créer une nouvelle classe qui hérite de `TextTableFormatter` et qui remplace la méthode `row()` pour appliquer le formatage souhaité.

```python
python3 -c "
from tableformat import TextTableFormatter, print_table, portfolio

class PortfolioFormatter(TextTableFormatter):
    def row(self, rowdata):
        formats = ['%s','%d','%0.2f']
        rowdata = [(fmt % d) for fmt, d in zip(formats, rowdata)]
        super().row(rowdata)

formatter = PortfolioFormatter()
print_table(portfolio, ['name','shares','price'], formatter)
"
```

Cette solution fonctionne également, mais elle n'est pas très pratique. Chaque fois que nous voulons un formatage différent, nous devons créer une nouvelle classe. Et nous sommes limités au type de formateur spécifique dont nous dérivons, dans ce cas, `TextTableFormatter`.

Dans l'étape suivante, nous allons explorer une solution plus élégante en utilisant les classes mixin.
