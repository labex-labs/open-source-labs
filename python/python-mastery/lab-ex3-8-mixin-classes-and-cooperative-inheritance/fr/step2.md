# Implémentation de classes mixin pour le formatage

Dans cette étape, nous allons apprendre les classes mixin. Les classes mixin sont une technique très utile en Python. Elles vous permettent d'ajouter des fonctionnalités supplémentaires aux classes sans modifier leur code d'origine. C'est très pratique car cela aide à maintenir votre code modulaire et facile à gérer.

## Qu'est-ce que les classes mixin ?

Une classe mixin est un type spécial de classe. Son but principal est de fournir une fonctionnalité qui peut être héritée par une autre classe. Cependant, une classe mixin n'est pas destinée à être utilisée seule. Vous ne créez pas directement une instance d'une classe mixin. Au lieu de cela, vous l'utilisez pour ajouter des fonctionnalités spécifiques à d'autres classes de manière contrôlée et prévisible. C'est une forme d'héritage multiple, où une classe peut hériter de plusieurs classes parentes.

Maintenant, implémentons deux classes mixin dans notre fichier `tableformat.py`. Tout d'abord, ouvrez le fichier dans l'éditeur. Vous pouvez le faire en exécutant les commandes suivantes dans votre terminal :

```bash
cd ~/project
code tableformat.py
```

Une fois le fichier ouvert, ajoutez les définitions de classe suivantes à la fin du fichier, mais avant toute fonction existante.

```python
class ColumnFormatMixin:
    formats = []
    def row(self, rowdata):
        rowdata = [(fmt % d) for fmt, d in zip(self.formats, rowdata)]
        super().row(rowdata)
```

Cette classe `ColumnFormatMixin` fournit une fonctionnalité de formatage des colonnes. La variable de classe `formats` est une liste qui contient des codes de format. Ces codes sont utilisés pour formater les données de chaque colonne. La méthode `row()` prend les données de la ligne, applique les codes de format à chaque élément de la ligne, puis transmet les données de la ligne formatée à la classe parente en utilisant `super().row(rowdata)`.

Ensuite, ajoutez une autre classe mixin qui fait apparaître les en-têtes de tableau en majuscules :

```python
class UpperHeadersMixin:
    def headings(self, headers):
        super().headings([h.upper() for h in headers])
```

Cette classe `UpperHeadersMixin` transforme le texte des en-têtes en majuscules. Elle prend la liste des en-têtes, convertit chaque en-tête en majuscules, puis transmet les en-têtes modifiés à la méthode `headings()` de la classe parente en utilisant `super().headings()`.

## Utilisation des classes mixin

Testons nos nouvelles classes mixin. Nous allons exécuter un peu de code Python pour voir comment elles fonctionnent.

```python
python3 -c "
from tableformat import TextTableFormatter, ColumnFormatMixin, portfolio, print_table

class PortfolioFormatter(ColumnFormatMixin, TextTableFormatter):
    formats = ['%s', '%d', '%0.2f']

formatter = PortfolioFormatter()
print_table(portfolio, ['name','shares','price'], formatter)
"
```

Lorsque vous exécutez ce code, vous devriez voir une sortie bien formatée. La colonne des prix aura un nombre cohérent de décimales grâce au formatage fourni par la classe `ColumnFormatMixin`.

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

Maintenant, essayons la classe `UpperHeadersMixin`. Exécutez le code suivant :

```python
python3 -c "
from tableformat import TextTableFormatter, UpperHeadersMixin, portfolio, print_table

class PortfolioFormatter(UpperHeadersMixin, TextTableFormatter):
    pass

formatter = PortfolioFormatter()
print_table(portfolio, ['name','shares','price'], formatter)
"
```

Ce code devrait afficher les en-têtes en majuscules.

```
      NAME     SHARES      PRICE
---------- ---------- ----------
        AA        100       32.2
       IBM         50       91.1
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50       65.1
       IBM        100      70.44
```

## Comprendre l'héritage coopératif

Remarquez que dans nos classes mixin, nous utilisons `super().method()`. Cela s'appelle "héritage coopératif". Dans l'héritage coopératif, chaque classe dans la chaîne d'héritage travaille ensemble. Lorsqu'une classe appelle `super().method()`, elle demande à la classe suivante dans la chaîne d'exécuter sa partie de la tâche. De cette façon, une chaîne de classes peut ajouter chacune son propre comportement au processus global.

L'ordre d'héritage est très important. Lorsque nous définissons `class PortfolioFormatter(ColumnFormatMixin, TextTableFormatter)`, Python cherche d'abord les méthodes dans `ColumnFormatMixin`, puis dans `TextTableFormatter`. Donc, lorsque `super().row()` est appelé dans `ColumnFormatMixin`, il fait référence à `TextTableFormatter.row()`.

Nous pouvons même combiner les deux mixins. Exécutez le code suivant :

```python
python3 -c "
from tableformat import TextTableFormatter, ColumnFormatMixin, UpperHeadersMixin, portfolio, print_table

class PortfolioFormatter(ColumnFormatMixin, UpperHeadersMixin, TextTableFormatter):
    formats = ['%s', '%d', '%0.2f']

formatter = PortfolioFormatter()
print_table(portfolio, ['name','shares','price'], formatter)
"
```

Ce code nous donnera à la fois des en-têtes en majuscules et des nombres formatés.

```
      NAME     SHARES      PRICE
---------- ---------- ----------
        AA        100      32.20
       IBM         50      91.10
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50      65.10
       IBM        100      70.44
```

Dans l'étape suivante, nous allons rendre ces mixins plus faciles à utiliser en améliorant la fonction `create_formatter()`.
