# Ajout de conversions de type

Notre classe `MutInt` prend actuellement en charge les opérations d'addition et de comparaison. Cependant, elle ne fonctionne pas avec les fonctions de conversion intégrées de Python telles que `int()` et `float()`. Ces fonctions de conversion sont très utiles en Python. Par exemple, lorsque vous souhaitez convertir une valeur en un entier ou un nombre à virgule flottante pour différents calculs ou opérations, vous vous fiez à ces fonctions. Ajoutons donc les capacités à notre classe `MutInt` pour qu'elle fonctionne avec elles.

1. Ouvrez `mutint.py` dans le WebIDE et mettez-le à jour avec le code suivant :

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

    def __lshift__(self, other):
        """Handle left shift: self << other."""
        if isinstance(other, MutInt):
            return MutInt(self.value << other.value)
        elif isinstance(other, int):
            return MutInt(self.value << other)
        else:
            return NotImplemented

    def __rlshift__(self, other):
        """Handle reversed left shift: other << self."""
        if isinstance(other, int):
            return MutInt(other << self.value)
        else:
            return NotImplemented
```

Nous avons ajouté trois nouvelles méthodes à la classe `MutInt` :

1. `__int__()` : cette méthode est appelée lorsque vous utilisez la fonction `int()` sur un objet de notre classe `MutInt`. Par exemple, si vous avez un objet `MutInt` `a`, et que vous écrivez `int(a)`, Python appellera la méthode `__int__()` de l'objet `a`.
2. `__float__()` : de même, cette méthode est appelée lorsque vous utilisez la fonction `float()` sur notre objet `MutInt`.
3. `__index__()` : cette méthode est utilisée pour les opérations qui nécessitent spécifiquement un index entier. Par exemple, lorsque vous souhaitez accéder à un élément dans une liste en utilisant un index, ou effectuer des opérations de longueur de bits (bit-length operations), Python a besoin d'un index entier.
4. `__lshift__()`: Cette méthode gère les opérations de décalage à gauche (left shift operations) lorsque l'objet `MutInt` se trouve à gauche de l'opérateur `<<`.
5. `__rlshift__()`: Cette méthode gère les opérations de décalage à gauche (left shift operations) lorsque l'objet `MutInt` se trouve à droite de l'opérateur `<<`.

La méthode `__index__` est cruciale pour les opérations qui exigent un index entier, comme l'indexation de liste, le découpage (slicing) et les opérations de longueur de bits. Dans notre implémentation simple, nous la définissons comme étant la même que `__int__` car la valeur de notre objet `MutInt` peut être directement utilisée comme index entier.

Les méthodes `__lshift__` et `__rlshift__` sont essentielles pour prendre en charge les opérations de décalage de bits vers la gauche (bitwise left shift operations). Elles permettent à nos objets `MutInt` de participer à des opérations au niveau du bit, ce qui est une exigence courante pour les types similaires aux entiers.

2. Créez un nouveau fichier de test appelé `test_conversions.py` pour tester ces nouvelles méthodes :

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
a.value = 4
print(f"\nAfter changing value to 4:")
print(f"int(a): {int(a)}")
print(f"names[a]: {names[a]}")
```

3. Exécutez le script de test :

```bash
python3 /home/labex/project/test_conversions.py
```

Vous devriez voir une sortie similaire à celle-ci :

```
int(a): 3
float(a): 3.0
names[a]: Thomas
1 << a: 8
hex(a): 0x3
oct(a): 0o3
bin(a): 0b11

After changing value to 4:
int(a): 4
names[a]: Lewis
```

Maintenant, notre classe `MutInt` peut être convertie en types Python standard et utilisée dans des opérations qui nécessitent un index entier.

La méthode `__index__` est particulièrement importante. Elle a été introduite dans Python pour permettre aux objets d'être utilisés dans des situations où un index entier est requis, telles que l'indexation de liste, les opérations au niveau du bit et diverses fonctions comme `hex()`, `oct()` et `bin()`.

Avec ces ajouts, notre classe `MutInt` est maintenant un type primitif assez complet. Elle peut être utilisée dans la plupart des contextes où un entier régulier serait utilisé, avec l'avantage supplémentaire d'être mutable.

## Implémentation complète de MutInt

Voici notre implémentation complète de `MutInt` avec toutes les fonctionnalités que nous avons ajoutées :

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

    def __lshift__(self, other):
        """Handle left shift: self << other."""
        if isinstance(other, MutInt):
            return MutInt(self.value << other.value)
        elif isinstance(other, int):
            return MutInt(self.value << other)
        else:
            return NotImplemented

    def __rlshift__(self, other):
        """Handle reversed left shift: other << self."""
        if isinstance(other, int):
            return MutInt(other << self.value)
        else:
            return NotImplemented
```

Cette implémentation couvre les aspects clés de la création d'un nouveau type primitif en Python. Pour la rendre encore plus complète, vous pourriez implémenter des méthodes supplémentaires pour d'autres opérations comme la soustraction, la multiplication, la division, etc.
