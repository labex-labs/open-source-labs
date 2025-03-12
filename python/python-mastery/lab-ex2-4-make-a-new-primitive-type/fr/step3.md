# Ajout d'opérations mathématiques

Actuellement, notre classe `MutInt` ne prend pas en charge les opérations mathématiques telles que l'addition. En Python, pour activer de telles opérations pour une classe personnalisée, nous devons implémenter des méthodes spéciales. Ces méthodes spéciales sont également connues sous le nom de "méthodes magiques" ou "méthodes dunder" car elles sont entourées de doubles underscores. Ajoutons la fonctionnalité d'addition en implémentant les méthodes spéciales pertinentes pour les opérations arithmétiques.

1. Ouvrez le fichier `mutint.py` dans le WebIDE et mettez - le à jour avec le code suivant :

```python
# mutint.py

class MutInt:
    """
    A mutable integer class that allows its value to be modified after creation.
    """
    __slots__ = ['value']

    def __init__(self, value):
        """Initialize with an integer value."""
        self.value = value

    def __str__(self):
        """Return a string representation for printing."""
        return str(self.value)

    def __repr__(self):
        """Return a developer-friendly string representation."""
        return f'MutInt({self.value!r})'

    def __format__(self, fmt):
        """Support string formatting with format specifications."""
        return format(self.value, fmt)

    def __add__(self, other):
        """Handle addition: self + other."""
        if isinstance(other, MutInt):
            return MutInt(self.value + other.value)
        elif isinstance(other, int):
            return MutInt(self.value + other)
        else:
            return NotImplemented

    def __radd__(self, other):
        """Handle reversed addition: other + self."""
        # For commutative operations like +, we can reuse __add__
        return self.__add__(other)

    def __iadd__(self, other):
        """Handle in-place addition: self += other."""
        if isinstance(other, MutInt):
            self.value += other.value
            return self
        elif isinstance(other, int):
            self.value += other
            return self
        else:
            return NotImplemented
```

Nous avons ajouté trois nouvelles méthodes à la classe `MutInt` :

- `__add__()` : Cette méthode est appelée lorsque l'opérateur `+` est utilisé avec notre objet `MutInt` du côté gauche. À l'intérieur de cette méthode, nous vérifions d'abord si l'opérande `other` est une instance de `MutInt` ou un `int`. Si c'est le cas, nous effectuons l'addition et retournons un nouvel objet `MutInt` avec le résultat. Si l'opérande `other` est autre chose, nous retournons `NotImplemented`. Cela indique à Python d'essayer d'autres méthodes ou de lever une `TypeError`.
- `__radd__()` : Cette méthode est appelée lorsque l'opérateur `+` est utilisé avec notre objet `MutInt` du côté droit. Étant donné que l'addition est une opération commutative (c'est - à - dire que `a + b` est le même que `b + a`), nous pouvons simplement réutiliser la méthode `__add__`.
- `__iadd__()` : Cette méthode est appelée lorsque l'opérateur `+=` est utilisé sur notre objet `MutInt`. Au lieu de créer un nouvel objet, elle modifie l'objet `MutInt` existant et le retourne.

2. Créez un nouveau fichier de test appelé `test_math_ops.py` pour tester ces nouvelles méthodes :

```python
# test_math_ops.py

from mutint import MutInt

# Create MutInt objects
a = MutInt(3)
b = MutInt(5)

# Test regular addition
c = a + b
print(f"a + b = {c}")

# Test addition with int
d = a + 10
print(f"a + 10 = {d}")

# Test reversed addition
e = 7 + a
print(f"7 + a = {e}")

# Test in-place addition
print(f"Before a += 5: a = {a}")
a += 5
print(f"After a += 5: a = {a}")

# Test in-place addition with reference sharing
f = a  # f and a point to the same object
print(f"Before a += 10: a = {a}, f = {f}")
a += 10
print(f"After a += 10: a = {a}, f = {f}")

# Test unsupported operation
try:
    result = a + 3.5  # Adding a float is not supported
    print(f"a + 3.5 = {result}")
except TypeError as e:
    print(f"Error when adding float: {e}")
```

Dans ce fichier de test, nous importons d'abord la classe `MutInt`. Ensuite, nous créons quelques objets `MutInt` et effectuons différents types d'opérations d'addition. Nous testons également l'addition en place et le cas où une opération non prise en charge (l'addition d'un nombre à virgule flottante) est tentée.

3. Exécutez le script de test :

```bash
python3 /home/labex/project/test_math_ops.py
```

Vous devriez voir une sortie similaire à ceci :

```
a + b = MutInt(8)
a + 10 = MutInt(13)
7 + a = MutInt(10)
Before a += 5: a = MutInt(3)
After a += 5: a = MutInt(8)
Before a += 10: a = MutInt(8), f = MutInt(8)
After a += 10: a = MutInt(18), f = MutInt(18)
Error when adding float: unsupported operand type(s) for +: 'MutInt' and 'float'
```

Maintenant, notre classe `MutInt` prend en charge les opérations d'addition de base. Remarquez que lorsque nous avons utilisé `+=`, tant `a` que `f` ont été mis à jour. Cela montre que `a += 10` a modifié l'objet existant plutôt que de créer un nouveau.

Ce comportement avec les objets mutables est similaire aux types mutables intégrés de Python comme les listes. Par exemple :

```python
a = [1, 2, 3]
b = a
a += [4, 5]  # Both a and b are updated
```

En revanche, pour les types immuables comme les tuples, `+=` crée un nouvel objet :

```python
c = (1, 2, 3)
d = c
c += (4, 5)  # c is a new object, d still points to the old one
```
