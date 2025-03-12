# Application de l'inspection de fonction dans les classes

Maintenant, nous allons utiliser ce que nous avons appris sur l'inspection de fonction pour améliorer une implémentation de classe. L'inspection de fonction nous permet de regarder à l'intérieur des fonctions et de comprendre leur structure, comme les paramètres qu'elles prennent. Dans ce cas, nous l'utiliserons pour rendre notre code de classe plus efficace et moins sujet aux erreurs. Nous allons modifier une classe `Structure` afin qu'elle puisse détecter automatiquement les noms de champs à partir de la signature de la méthode `__init__`.

## Comprendre la classe Structure

Le fichier `structure.py` contient une classe `Structure`. Cette classe agit comme une classe de base, ce qui signifie que d'autres classes peuvent en hériter pour créer des objets de données structurées. Actuellement, pour définir les attributs des objets créés à partir de classes héritant de `Structure`, nous devons définir une variable de classe `_fields`.

Ouvrons le fichier dans l'éditeur. Nous utiliserons la commande suivante pour naviguer jusqu'au répertoire du projet :

```bash
cd ~/project
```

Une fois que vous avez exécuté cette commande, vous pouvez trouver et afficher la classe `Structure` existante dans le fichier `structure.py` dans l'IDE Web.

## Création d'une classe Stock

Créons une classe `Stock` qui hérite de la classe `Structure`. L'héritage signifie que la classe `Stock` aura toutes les fonctionnalités de la classe `Structure` et pourra également ajouter les siennes. Nous allons ajouter le code suivant à la fin du fichier `structure.py` :

```python
class Stock(Structure):
    _fields = ('name', 'shares', 'price')

    def __init__(self, name, shares, price):
        self._init()
```

Cependant, il y a un problème avec cette approche. Nous devons définir à la fois le tuple `_fields` et la méthode `__init__` avec les mêmes noms de paramètres. Cela est redondant car nous écrivons essentiellement les mêmes informations deux fois. Si nous oublions de mettre à jour l'un lorsque nous modifions l'autre, cela peut entraîner des erreurs.

## Ajout d'une méthode de classe set_fields

Pour résoudre ce problème, nous allons ajouter une méthode de classe `set_fields` à la classe `Structure`. Cette méthode détectera automatiquement les noms de champs à partir de la signature de `__init__`. Voici le code que nous devons ajouter à la classe `Structure` :

```python
@classmethod
def set_fields(cls):
    # Get the signature of the __init__ method
    import inspect
    sig = inspect.signature(cls.__init__)

    # Get parameter names, skipping 'self'
    params = list(sig.parameters.keys())[1:]

    # Set _fields attribute on the class
    cls._fields = tuple(params)
```

Cette méthode utilise le module `inspect`, qui est un outil puissant en Python pour obtenir des informations sur des objets tels que des fonctions et des classes. Tout d'abord, elle obtient la signature de la méthode `__init__`. Ensuite, elle extrait les noms des paramètres, mais ignore le paramètre `self` car `self` est un paramètre spécial dans les classes Python qui fait référence à l'instance elle - même. Enfin, elle définit la variable de classe `_fields` avec ces noms de paramètres.

## Modification de la classe Stock

Maintenant que nous avons la méthode `set_fields`, nous pouvons simplifier notre classe `Stock`. Remplacez le code précédent de la classe `Stock` par le suivant :

```python
class Stock(Structure):
    def __init__(self, name, shares, price):
        self._init()

# Call set_fields to automatically set _fields from __init__
Stock.set_fields()
```

De cette façon, nous n'avons pas à définir manuellement le tuple `_fields`. La méthode `set_fields` s'en chargera pour nous.

## Test de la classe modifiée

Pour nous assurer que notre classe modifiée fonctionne correctement, nous allons créer un script de test simple. Créez un nouveau fichier appelé `test_structure.py` et ajoutez le code suivant :

```python
from structure import Stock

def test_stock():
    # Create a Stock object
    s = Stock(name='GOOG', shares=100, price=490.1)

    # Test string representation
    print(f"Stock representation: {s}")

    # Test attribute access
    print(f"Name: {s.name}")
    print(f"Shares: {s.shares}")
    print(f"Price: {s.price}")

    # Test attribute modification
    s.shares = 50
    print(f"Updated shares: {s.shares}")

    # Test attribute error
    try:
        s.share = 50  # Misspelled attribute
        print("Error: Did not raise AttributeError")
    except AttributeError as e:
        print(f"Correctly raised: {e}")

if __name__ == "__main__":
    test_stock()
```

Ce script de test crée un objet `Stock`, teste sa représentation sous forme de chaîne de caractères, accède à ses attributs, modifie un attribut et essaie d'accéder à un attribut mal orthographié pour vérifier s'il lève l'erreur correcte.

Pour exécuter le script de test, utilisez la commande suivante :

```bash
python3 test_structure.py
```

Vous devriez voir un résultat similaire à ceci :

```
Stock representation: Stock('GOOG',100,490.1)
Name: GOOG
Shares: 100
Price: 490.1
Updated shares: 50
Correctly raised: No attribute share
```

## Comment cela fonctionne

1. La méthode `set_fields` utilise `inspect.signature()` pour obtenir les noms de paramètres de la méthode `__init__`. Cette fonction nous donne des informations détaillées sur les paramètres de la méthode `__init__`.
2. Elle définit ensuite automatiquement la variable de classe `_fields` en fonction de ces noms de paramètres. Ainsi, nous n'avons pas à écrire les mêmes noms de paramètres à deux endroits différents.
3. Cela élimine le besoin de définir manuellement à la fois `_fields` et `__init__` avec des noms de paramètres correspondants. Cela rend notre code plus facilement maintenable car si nous modifions les paramètres dans la méthode `__init__`, `_fields` sera mis à jour automatiquement.

Cette approche utilise l'inspection de fonction pour rendre notre code plus facilement maintenable et moins sujet aux erreurs. C'est une application pratique des capacités d'introspection de Python, qui nous permettent d'examiner et de modifier des objets à l'exécution.
