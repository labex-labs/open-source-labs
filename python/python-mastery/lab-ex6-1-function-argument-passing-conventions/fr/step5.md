# Refonte de la classe Stock

Maintenant que nous avons une classe de base `Structure` bien définie, il est temps de refaire notre classe `Stock`. En utilisant cette classe de base, nous pouvons simplifier notre code et le rendre plus organisé. La classe `Structure` fournit un ensemble de fonctionnalités communes que nous pouvons réutiliser dans notre classe `Stock`, ce qui est un grand atout pour la maintenance et la lisibilité du code.

## Création de la nouvelle classe Stock

Commençons par créer un nouveau fichier nommé `stock.py`. Ce fichier contiendra notre classe `Stock` refaite. Voici le code que vous devez placer dans le fichier `stock.py` :

```python
# stock.py
from structure import Structure

class Stock(Structure):
    _fields = ('name', 'shares', 'price')

    @property
    def cost(self):
        """
        Calculate the cost as shares * price
        """
        return self.shares * self.price

    def sell(self, nshares):
        """
        Sell a number of shares
        """
        self.shares -= nshares
```

Analysons ce que fait cette nouvelle classe `Stock` :

1. Elle hérite de la classe `Structure`. Cela signifie que la classe `Stock` peut utiliser toutes les fonctionnalités fournies par la classe `Structure`. L'un des avantages est que nous n'avons pas besoin d'écrire nous - mêmes une méthode `__init__` car la classe `Structure` s'occupe automatiquement de l'affectation des attributs.
2. Nous définissons `_fields`, qui est un tuple spécifiant les attributs de la classe `Stock`. Ces attributs sont `name`, `shares` et `price`.
3. La propriété `cost` est définie pour calculer le coût total du stock. Elle multiplie le nombre de `shares` par le `price`.
4. La méthode `sell` est utilisée pour réduire le nombre de parts. Lorsque vous appelez cette méthode avec un nombre de parts à vendre, elle soustrait ce nombre du nombre actuel de parts.

## Test de la nouvelle classe Stock

Pour nous assurer que notre nouvelle classe `Stock` fonctionne comme prévu, nous devons créer un fichier de test. Créons un fichier nommé `test_stock.py` avec le code suivant :

```python
# test_stock.py
from stock import Stock

# Create a stock
s = Stock('GOOG', 100, 490.1)

# Check the attributes
print(f"Stock: {s}")
print(f"Name: {s.name}")
print(f"Shares: {s.shares}")
print(f"Price: {s.price}")
print(f"Cost: {s.cost}")

# Sell some shares
print("\nSelling 20 shares...")
s.sell(20)
print(f"Shares after selling: {s.shares}")
print(f"Cost after selling: {s.cost}")

# Try to set an invalid attribute
print("\nTrying to set an invalid attribute:")
try:
    s.prices = 500  # Invalid attribute (should be 'price')
    print("This should not print")
except AttributeError as e:
    print(f"Error correctly caught: {e}")
```

Dans ce fichier de test, nous importons d'abord la classe `Stock` depuis le fichier `stock.py`. Ensuite, nous créons une instance de la classe `Stock` avec le nom 'GOOG', 100 parts et un prix de 490.1. Nous affichons les attributs du stock pour vérifier s'ils sont correctement définis. Après cela, nous vendons 20 parts et affichons le nouveau nombre de parts et le nouveau coût. Enfin, nous essayons de définir un attribut invalide `prices` (il devrait s'agir de `price`). Si notre classe `Stock` fonctionne correctement, elle devrait lever une erreur `AttributeError`.

Pour exécuter le test, ouvrez votre terminal et entrez la commande suivante :

```bash
python3 test_stock.py
```

La sortie attendue est la suivante :

```
Stock: Stock('GOOG', 100, 490.1)
Name: GOOG
Shares: 100
Price: 490.1
Cost: 49010.0

Selling 20 shares...
Shares after selling: 80
Cost after selling: 39208.0

Trying to set an invalid attribute:
Error correctly caught: No attribute prices
```

## Exécution de tests unitaires

Si vous avez des tests unitaires provenant d'exercices précédents, vous pouvez les exécuter sur votre nouvelle implémentation. Dans votre terminal, entrez la commande suivante :

```bash
python3 teststock.py
```

Notez que certains tests peuvent échouer. Cela peut être parce qu'ils attendent des comportements ou des méthodes spécifiques que nous n'avons pas encore implémentées. Ne vous inquiétez pas ! Nous continuerons à construire sur cette base dans les exercices suivants.

## Revue de nos progrès

Prenons un moment pour revoir ce que nous avons accompli jusqu'à présent :

1. Nous avons créé une classe de base `Structure` réutilisable. Cette classe :
   - Gère automatiquement l'affectation des attributs, ce qui nous évite d'écrire beaucoup de code répétitif.
   - Fournit une bonne représentation sous forme de chaîne de caractères, facilitant l'affichage et le débogage de nos objets.
   - Restreint les noms d'attributs pour éviter les erreurs, ce qui rend notre code plus robuste.

2. Nous avons refait notre classe `Stock`. Elle :
   - Hérite de la classe `Structure` pour réutiliser la fonctionnalité commune.
   - Ne définit que les champs et les méthodes spécifiques au domaine, ce qui garde la classe ciblée et propre.
   - A une conception claire et simple, facilitant sa compréhension et sa maintenance.

Cette approche présente plusieurs avantages pour notre code :

- Il est plus facilement maintenable car il y a moins de répétition. Si nous devons changer quelque chose dans la fonctionnalité commune, nous n'avons besoin de le changer que dans la classe `Structure`.
- Il est plus robuste grâce aux meilleures vérifications d'erreurs fournies par la classe `Structure`.
- Il est plus lisible car les responsabilités de chaque classe sont claires.

Dans les exercices suivants, nous continuerons à construire sur cette base pour créer un système de gestion de portefeuille d'actions plus sophistiqué.
