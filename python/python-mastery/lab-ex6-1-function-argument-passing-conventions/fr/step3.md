# Amélioration de la représentation des objets

Notre classe `Structure` est utile pour créer et accéder aux objets. Cependant, elle n'a actuellement pas un bon moyen de se représenter sous forme de chaîne de caractères. Lorsque vous affichez un objet ou le visualisez dans l'interpréteur Python, vous souhaitez voir un affichage clair et informatif. Cela vous aide à comprendre de quoi l'objet est constitué et quelles sont ses valeurs.

## Comprendre la représentation des objets en Python

En Python, il existe deux méthodes spéciales utilisées pour représenter les objets de différentes manières. Ces méthodes sont importantes car elles vous permettent de contrôler la façon dont vos objets sont affichés.

- `__str__` - Cette méthode est utilisée par la fonction `str()` et la fonction `print()`. Elle fournit une représentation lisible par l'homme de l'objet. Par exemple, si vous avez un objet `Stock`, la méthode `__str__` pourrait retourner quelque chose comme "Stock: GOOG, 100 shares at $490.1".
- `__repr__` - Cette méthode est utilisée par l'interpréteur Python et la fonction `repr()`. Elle donne une représentation plus technique et non ambiguë de l'objet. L'objectif de `__repr__` est de fournir une chaîne de caractères qui peut être utilisée pour recréer l'objet. Par exemple, pour un objet `Stock`, elle pourrait retourner "Stock('GOOG', 100, 490.1)".

Ajoutons une méthode `__repr__` à notre classe `Structure`. Cela facilitera le débogage de notre code car nous pourrons clairement voir l'état de nos objets.

## Implémentation d'une bonne représentation

Maintenant, vous devez mettre à jour votre fichier `structure.py`. Vous allez ajouter la méthode `__repr__` à la classe `Structure`. Cette méthode créera une chaîne de caractères représentant l'objet d'une manière qui peut être utilisée pour le recréer.

```python
def __repr__(self):
    """
    Return a representation of the object that can be used to recreate it.
    Example: Stock('GOOG', 100, 490.1)
    """
    # Get the class name
    cls_name = type(self).__name__

    # Get all the field values
    values = [getattr(self, name) for name in self._fields]

    # Format the fields and values
    args_str = ', '.join(repr(value) for value in values)

    # Return the formatted string
    return f"{cls_name}({args_str})"
```

Voici ce que cette méthode fait étape par étape :

1. Elle obtient le nom de la classe en utilisant `type(self).__name__`. Cela est important car il vous indique de quel type d'objet vous avez affaire.
2. Elle récupère toutes les valeurs des champs de l'instance. Cela vous donne les données que l'objet contient.
3. Elle crée une représentation sous forme de chaîne de caractères avec le nom de la classe et les valeurs. Cette chaîne de caractères peut être utilisée pour recréer l'objet.

## Test de la représentation améliorée

Testons notre implémentation améliorée. Créez un nouveau fichier appelé `test_repr.py`. Ce fichier créera quelques instances de nos classes et affichera leurs représentations.

```python
# test_repr.py
from structure import Stock, Point, Date

# Create instances
s = Stock('GOOG', 100, 490.1)
p = Point(3, 4)
d = Date(2023, 11, 9)

# Print the representations
print(repr(s))
print(repr(p))
print(repr(d))

# Direct printing also uses __repr__ in the interpreter
print(s)
print(p)
print(d)
```

Pour exécuter le test, ouvrez votre terminal et entrez la commande suivante :

```bash
python3 test_repr.py
```

Vous devriez voir la sortie suivante :

```
Stock('GOOG', 100, 490.1)
Point(3, 4)
Date(2023, 11, 9)
Stock('GOOG', 100, 490.1)
Point(3, 4)
Date(2023, 11, 9)
```

Cette sortie est beaucoup plus informative que précédemment. Lorsque vous voyez `Stock('GOOG', 100, 490.1)`, vous savez immédiatement de quoi l'objet est constitué. Vous pourriez même copier cette chaîne de caractères et l'utiliser pour recréer l'objet dans votre code.

## L'avantage d'une bonne représentation

Une bonne implémentation de `__repr__` est très utile pour le débogage. Lorsque vous examinez des objets dans l'interpréteur ou les enregistrez pendant l'exécution du programme, une représentation claire facilite l'identification rapide des problèmes. Vous pouvez voir l'état exact de l'objet et comprendre ce qui peut ne pas fonctionner.
