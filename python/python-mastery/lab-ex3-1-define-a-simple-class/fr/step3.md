# Mise en forme et affichage des données du portefeuille

Dans cette étape, nous allons créer une fonction qui nous aidera à afficher les données du portefeuille dans un tableau bien organisé. Un portefeuille est une collection d'actions, et il est important de présenter ces données de manière claire et lisible. C'est là que la fonction `print_portfolio(portfolio)` entre en jeu. Cette fonction prendra un portefeuille en entrée et l'affichera dans un tableau avec des en-têtes et un alignement approprié.

## Mise en forme de chaînes de caractères en Python

En Python, il existe plusieurs façons de formater des chaînes de caractères. La mise en forme de chaînes est une compétence cruciale car elle vous permet de présenter les données de manière plus organisée et conviviale.

- L'opérateur `%` est un style plus ancien de mise en forme de chaînes. C'est comme un modèle où vous pouvez insérer des valeurs à des endroits spécifiques dans une chaîne.
- La méthode `str.format()` est une autre façon. Elle offre plus de flexibilité et une syntaxe plus propre pour formater des chaînes.
- Les f - strings sont une fonctionnalité introduite en Python 3.6 et versions ultérieures. Elles sont très pratiques car elles vous permettent d'intégrer des expressions à l'intérieur de littéraux de chaînes.

Pour cet exercice, nous utiliserons l'opérateur `%`. Il est particulièrement utile lorsque vous souhaitez créer des colonnes de largeur fixe, ce qui est exactement ce dont nous avons besoin pour notre tableau de portefeuille.

## Instructions d'implémentation

1. Tout d'abord, ouvrez le fichier `stock.py` dans votre éditeur. S'il est déjà ouvert, c'est parfait. C'est dans ce fichier que nous allons écrire notre fonction `print_portfolio`.

2. Une fois le fichier ouvert, recherchez le commentaire `# TODO: Add print_portfolio(portfolio) function here`. Ce commentaire est un marqueur qui nous indique où ajouter notre nouvelle fonction.

3. En dessous de ce commentaire, ajoutez la fonction suivante :

```python
def print_portfolio(portfolio):
    """
    Print the portfolio data in a nicely formatted table.

    Args:
        portfolio (list): A list of Stock objects
    """
    # Print the header row
    print('%10s %10s %10s' % ('name', 'shares', 'price'))

    # Print a separator line
    print('-' * 10 + ' ' + '-' * 10 + ' ' + '-' * 10)

    # Print each stock in the portfolio
    for stock in portfolio:
        print('%10s %10d %10.2f' % (stock.name, stock.shares, stock.price))
```

Cette fonction imprime d'abord la ligne d'en-tête du tableau, puis une ligne de séparation, et enfin, elle parcourt chaque action du portefeuille et imprime ses détails de manière formatée.

4. Après avoir ajouté la fonction, enregistrez le fichier. Vous pouvez le faire en appuyant sur `Ctrl+S` ou en sélectionnant "File > Save" dans le menu. Enregistrer le fichier garantit que vos modifications sont conservées.

5. Maintenant, nous devons tester notre fonction. Créez un nouveau fichier appelé `test_print.py`. Ce fichier sera notre script de test. Ajoutez le code suivant :

```python
# test_print.py
from stock import read_portfolio, print_portfolio

# Read the portfolio from the CSV file
portfolio = read_portfolio('portfolio.csv')

# Print the portfolio as a formatted table
print_portfolio(portfolio)
```

Ce script importe les fonctions `read_portfolio` et `print_portfolio` à partir du fichier `stock.py`. Il lit ensuite les données du portefeuille à partir d'un fichier CSV et utilise notre fonction `print_portfolio` nouvellement créée pour les afficher.

6. Enfin, exécutez le script de test. Ouvrez votre terminal et entrez la commande suivante :

```bash
python3 test_print.py
```

Si tout fonctionne correctement, vous devriez voir une sortie comme celle-ci :

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

Cette sortie confirme que votre fonction `print_portfolio` fonctionne comme prévu. Elle met en forme et affiche les données du portefeuille dans un tableau avec des en-têtes et des colonnes alignées, ce qui facilite la lecture.

## Comprendre la mise en forme de chaînes de caractères

Examinons de plus près comment fonctionne la mise en forme de chaînes de caractères dans la fonction `print_portfolio`.

- `%10s` est utilisé pour formater une chaîne. Le `10` indique la largeur du champ, et le `s` signifie chaîne. Il aligne la chaîne à droite dans un champ de largeur 10.
- `%10d` est pour formater un entier. Le `10` est la largeur du champ, et `d` représente un entier. Il aligne également l'entier à droite dans un champ de largeur 10.
- `%10.2f` est utilisé pour formater un nombre à virgule flottante. Le `10` est la largeur du champ, et le `.2` spécifie que nous voulons afficher le nombre à virgule flottante avec 2 décimales. Il aligne le nombre à virgule flottante à droite dans un champ de largeur 10.

Cette mise en forme garantit que toutes les colonnes de notre tableau sont correctement alignées, ce qui rend la sortie beaucoup plus facile à lire et à comprendre.
