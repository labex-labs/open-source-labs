# Implémentation de la vérification de type avec des descripteurs

Dans cette étape, nous allons créer une classe `Stock` qui utilise des descripteurs pour la vérification de type. Mais d'abord, comprenons ce que sont les descripteurs. Les descripteurs sont une fonctionnalité très puissante en Python. Ils vous donnent le contrôle sur la manière dont les attributs sont accédés dans les classes.

Les descripteurs sont des objets qui définissent comment les attributs sont accédés sur d'autres objets. Ils le font en implémentant des méthodes spéciales comme `__get__`, `__set__`, et `__delete__`. Ces méthodes permettent aux descripteurs de gérer la manière dont les attributs sont récupérés, définis et supprimés. Les descripteurs sont très utiles pour implémenter la validation, la vérification de type et les propriétés calculées. Par exemple, vous pouvez utiliser un descripteur pour vous assurer qu'un attribut est toujours un nombre positif ou une chaîne de caractères d'un certain format.

Le fichier `validate.py` contient déjà des classes de validation (`String`, `PositiveInteger`, `PositiveFloat`). Nous pouvons utiliser ces classes pour valider les attributs de notre classe `Stock`.

Maintenant, créons notre classe `Stock` avec des descripteurs.

1. Tout d'abord, ouvrez le fichier `stock.py` dans votre éditeur.

2. Une fois le fichier ouvert, remplacez le contenu de l'espace réservé par le code suivant :

```python
# stock.py

from structure import Structure
from validate import String, PositiveInteger, PositiveFloat

class Stock(Structure):
    _fields = ('name', 'shares', 'price')
    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares

# Create an __init__ method based on _fields
Stock.create_init()
```

Analysons ce que fait ce code. Le tuple `_fields` définit les attributs de la classe `Stock`. Ce sont les noms des attributs que nos objets `Stock` auront.

Les attributs `name`, `shares` et `price` sont définis comme des objets descripteurs. Le descripteur `String()` garantit que l'attribut `name` est une chaîne de caractères. Le descripteur `PositiveInteger()` s'assure que l'attribut `shares` est un entier positif. Et le descripteur `PositiveFloat()` garantit que l'attribut `price` est un nombre à virgule flottante positif.

La propriété `cost` est une propriété calculée. Elle calcule le coût total du stock en fonction du nombre d'actions et du prix par action.

La méthode `sell` est utilisée pour réduire le nombre d'actions. Lorsque vous appelez cette méthode avec un nombre d'actions à vendre, elle soustrait ce nombre de l'attribut `shares`.

La ligne `Stock.create_init()` crée dynamiquement une méthode `__init__` pour notre classe. Cette méthode nous permet de créer des objets `Stock` en passant les valeurs des attributs `name`, `shares` et `price`.

3. Après avoir ajouté le code, enregistrez le fichier. Cela garantira que vos modifications sont enregistrées et peuvent être utilisées lorsque vous exécutez les tests.

4. Exécutons maintenant les tests pour vérifier votre implémentation. Tout d'abord, changez de répertoire pour vous rendre dans le répertoire `~/project` en exécutant la commande suivante :

```bash
cd ~/project
```

Ensuite, exécutez les tests en utilisant la commande suivante :

```bash
python3 teststock.py
```

Si votre implémentation est correcte, vous devriez voir une sortie similaire à celle-ci :

```
.........
----------------------------------------------------------------------
Ran 9 tests in 0.001s

OK
```

Cette sortie signifie que tous les tests sont réussis. Les descripteurs valident avec succès les types de chaque attribut !

Essayons de créer un objet `Stock` dans l'interpréteur Python. Tout d'abord, assurez-vous d'être dans le répertoire `~/project`. Ensuite, exécutez la commande suivante :

```bash
cd ~/project
python3 -c "from stock import Stock; s = Stock('GOOG', 100, 490.1); print(s); print(f'Cost: {s.cost}')"
```

Vous devriez voir la sortie suivante :

```
Stock('GOOG', 100, 490.1)
Cost: 49010.0
```

Vous avez implémenté avec succès des descripteurs pour la vérification de type ! Améliorons maintenant ce code.
