# Ajout d'itérations à des classes personnalisées

Maintenant que vous avez compris les bases des générateurs, nous allons les utiliser pour ajouter des capacités d'itération à des classes personnalisées. En Python, si vous souhaitez rendre une classe itérable, vous devez implémenter la méthode spéciale `__iter__()`. Une classe itérable vous permet de parcourir ses éléments, tout comme vous pouvez parcourir une liste ou un tuple. C'est une fonctionnalité puissante qui rend vos classes personnalisées plus flexibles et plus faciles à utiliser.

## Comprendre la méthode `__iter__()`

La méthode `__iter__()` est une partie cruciale pour rendre une classe itérable. Elle doit retourner un objet itérateur. Un itérateur est un objet sur lequel on peut itérer (parcourir en boucle). Une façon simple et efficace d'y parvenir est de définir `__iter__()` comme une fonction générateur. Une fonction générateur utilise le mot - clé `yield` pour produire une séquence de valeurs une à une. Chaque fois que l'instruction `yield` est rencontrée, la fonction se met en pause et retourne la valeur. La prochaine fois que l'itérateur est appelé, la fonction reprend là où elle s'était arrêtée.

## Modification de la classe Structure

Dans la configuration de ce laboratoire, nous avons fourni une classe de base `Structure`. D'autres classes, comme `Stock`, peuvent hériter de cette classe `Structure`. L'héritage est un moyen de créer une nouvelle classe qui hérite des propriétés et des méthodes d'une classe existante. En ajoutant une méthode `__iter__()` à la classe `Structure`, nous pouvons rendre toutes ses sous - classes itérables. Cela signifie que toute classe qui hérite de `Structure` aura automatiquement la capacité d'être parcourue en boucle.

1. Ouvrez le fichier `structure.py` dans le WebIDE :

```bash
cd ~/project
```

Cette commande change le répertoire de travail actuel pour le répertoire `project` où se trouve le fichier `structure.py`. Vous devez être dans le bon répertoire pour accéder et modifier le fichier.

2. Examinez l'implémentation actuelle de la classe `Structure` :

```python
class Structure(metaclass=StructureMeta):
    _fields = []
    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError(f'Expected {len(self._fields)} arguments')
        for name, val in zip(self._fields, args):
            setattr(self, '_'+name, val)
```

La classe `Structure` a une liste `_fields` qui stocke les noms des attributs. La méthode `__init__()` est le constructeur de la classe. Elle initialise les attributs de l'objet en vérifiant si le nombre d'arguments passés est égal au nombre de champs. Sinon, elle lève une erreur `TypeError`. Sinon, elle définit les attributs à l'aide de la fonction `setattr()`.

3. Ajoutez une méthode `__iter__()` qui produit chaque valeur d'attribut dans l'ordre :

```python
def __iter__(self):
    for name in self._fields:
        yield getattr(self, name)
```

Cette méthode `__iter__()` est une fonction générateur. Elle parcourt la liste `_fields` et utilise la fonction `getattr()` pour obtenir la valeur de chaque attribut. Le mot - clé `yield` retourne ensuite la valeur une par une.

Le fichier `structure.py` complet devrait maintenant ressembler à ceci :

```python
class StructureMeta(type):
    def __new__(cls, name, bases, clsdict):
        fields = clsdict.get('_fields', [])
        for name in fields:
            clsdict[name] = property(lambda self, name=name: getattr(self, '_'+name))
        return super().__new__(cls, name, bases, clsdict)

class Structure(metaclass=StructureMeta):
    _fields = []
    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError(f'Expected {len(self._fields)} arguments')
        for name, val in zip(self._fields, args):
            setattr(self, '_'+name, val)

    def __iter__(self):
        for name in self._fields:
            yield getattr(self, name)
```

Cette classe `Structure` mise à jour dispose maintenant de la méthode `__iter__()`, qui la rend et ses sous - classes itérables.

4. Enregistrez le fichier.
   Après avoir apporté des modifications au fichier `structure.py`, vous devez l'enregistrer pour que les modifications soient appliquées.

5. Testons maintenant la capacité d'itération en créant une instance de `Stock` et en la parcourant en boucle :

```bash
python3 -c "from stock import Stock; s = Stock('GOOG', 100, 490.1); print('Iterating over Stock:'); [print(val) for val in s]"
```

Cette commande crée une instance de la classe `Stock`, qui hérite de la classe `Structure`. Elle parcourt ensuite l'instance à l'aide d'une compréhension de liste et affiche chaque valeur.

Vous devriez voir une sortie comme celle - ci :

```
Iterating over Stock:
GOOG
100
490.1
```

Maintenant, toute classe qui hérite de `Structure` sera automatiquement itérable, et l'itération produira les valeurs d'attribut dans l'ordre défini par la liste `_fields`. Cela signifie que vous pouvez facilement parcourir les attributs de n'importe quelle sous - classe de `Structure` sans avoir à écrire de code supplémentaire pour l'itération.
