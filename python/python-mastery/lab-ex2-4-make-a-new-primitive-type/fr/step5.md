# Ajout de conversions de type

Notre classe `MutInt` prend actuellement en charge les opérations d'addition et de comparaison. Cependant, elle ne fonctionne pas avec les fonctions de conversion intégrées de Python telles que `int()` et `float()`. Ces fonctions de conversion sont très utiles en Python. Par exemple, lorsque vous souhaitez convertir une valeur en entier ou en nombre à virgule flottante pour différents calculs ou opérations, vous vous appuyez sur ces fonctions. Ajoutons donc à notre classe `MutInt` les capacités de fonctionner avec elles.

1. Ouvrez le fichier `mutint.py` dans le WebIDE et mettez - le à jour avec le code suivant :

```python
# mutint.py

from functools import total_ordering

@total_ordering
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
        """Return a developer - friendly string representation."""
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
        return self.__add__(other)

    def __iadd__(self, other):
        """Handle in - place addition: self += other."""
        if isinstance(other, MutInt):
            self.value += other.value
            return self
        elif isinstance(other, int):
            self.value += other
            return self
        else:
            return NotImplemented

    def __eq__(self, other):
        """Handle equality comparison: self == other."""
        if isinstance(other, MutInt):
            return self.value == other.value
        elif isinstance(other, int):
            return self.value == other
        else:
            return NotImplemented

    def __lt__(self, other):
        """Handle less - than comparison: self < other."""
        if isinstance(other, MutInt):
            return self.value < other.value
        elif isinstance(other, int):
            return self.value < other
        else:
            return NotImplemented

    def __int__(self):
        """Convert to int."""
        return self.value

    def __float__(self):
        """Convert to float."""
        return float(self.value)

    __index__ = __int__  # Support array indexing and other operations requiring an index
```

Nous avons ajouté trois nouvelles méthodes à la classe `MutInt` :

1. `__int__()` : Cette méthode est appelée lorsque vous utilisez la fonction `int()` sur un objet de notre classe `MutInt`. Par exemple, si vous avez un objet `MutInt` nommé `a` et que vous écrivez `int(a)`, Python appellera la méthode `__int__()` de l'objet `a`.
2. `__float__()` : De même, cette méthode est appelée lorsque vous utilisez la fonction `float()` sur notre objet `MutInt`.
3. `__index__()` : Cette méthode est utilisée pour les opérations qui nécessitent spécifiquement un index entier. Par exemple, lorsque vous souhaitez accéder à un élément dans une liste à l'aide d'un index, ou effectuer des opérations de longueur binaire, Python a besoin d'un index entier.

La méthode `__index__` est cruciale pour les opérations qui nécessitent un index entier, comme l'indexation de listes, le découpage (slicing) et les opérations de longueur binaire. Dans notre implémentation simple, nous l'avons définie comme étant la même que `__int__` car la valeur de notre objet `MutInt` peut être directement utilisée comme index entier.

2. Créez un nouveau fichier de test appelé `test_conversions.py` pour tester ces nouvelles méthodes :

```python
# test_conversions.py

from mutint import MutInt

# Create a MutInt object
a = MutInt(3)

# Test conversions
print(f"int(a): {int(a)}")
print(f"float(a): {float(a)}")

# Test using as an index
names = ['Dave', 'Guido', 'Paula', 'Thomas', 'Lewis']
print(f"names[a]: {names[a]}")

# Test using in bit operations (requires __index__)
print(f"1 << a: {1 << a}")  # Shift left by 3

# Test hex/oct/bin functions (requires __index__)
print(f"hex(a): {hex(a)}")
print(f"oct(a): {oct(a)}")
print(f"bin(a): {bin(a)}")

# Modify and test again
a.value = 5
print(f"\nAfter changing value to 5:")
print(f"int(a): {int(a)}")
print(f"names[a]: {names[a]}")
```

3. Exécutez le script de test :

```bash
python3 /home/labex/project/test_conversions.py
```

Vous devriez voir une sortie similaire à ceci :

```
int(a): 3
float(a): 3.0
names[a]: Paula
1 << a: 8
hex(a): 0x3
oct(a): 0o3
bin(a): 0b11

After changing value to 5:
int(a): 5
names[a]: Lewis
```

Maintenant, notre classe `MutInt` peut être convertie en types standard Python et utilisée dans des opérations qui nécessitent un index entier.

La méthode `__index__` est particulièrement importante. Elle a été introduite en Python pour permettre aux objets d'être utilisés dans des situations où un index entier est requis, comme l'indexation de listes, les opérations bit - à - bit et diverses fonctions telles que `hex()`, `oct()` et `bin()`.

Avec ces ajouts, notre classe `MutInt` est maintenant un type primitif assez complet. Elle peut être utilisée dans la plupart des contextes où un entier normal serait utilisé, avec l'avantage supplémentaire d'être mutable.

## Implémentation complète de MutInt

Voici notre implémentation complète de `MutInt` avec toutes les fonctionnalités que nous avons ajoutées :

```python
# mutint.py

from functools import total_ordering

@total_ordering
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
        """Return a developer - friendly string representation."""
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
        return self.__add__(other)

    def __iadd__(self, other):
        """Handle in - place addition: self += other."""
        if isinstance(other, MutInt):
            self.value += other.value
            return self
        elif isinstance(other, int):
            self.value += other
            return self
        else:
            return NotImplemented

    def __eq__(self, other):
        """Handle equality comparison: self == other."""
        if isinstance(other, MutInt):
            return self.value == other.value
        elif isinstance(other, int):
            return self.value == other
        else:
            return NotImplemented

    def __lt__(self, other):
        """Handle less - than comparison: self < other."""
        if isinstance(other, MutInt):
            return self.value < other.value
        elif isinstance(other, int):
            return self.value < other
        else:
            return NotImplemented

    def __int__(self):
        """Convert to int."""
        return self.value

    def __float__(self):
        """Convert to float."""
        return float(self.value)

    __index__ = __int__  # Support array indexing and other operations requiring an index
```

Cette implémentation couvre les aspects clés de la création d'un nouveau type primitif en Python. Pour la rendre encore plus complète, vous pourriez implémenter des méthodes supplémentaires pour d'autres opérations telles que la soustraction, la multiplication, la division, etc.
