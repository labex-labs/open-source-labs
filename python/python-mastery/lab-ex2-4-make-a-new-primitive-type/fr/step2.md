# Amélioration de la représentation sous forme de chaîne de caractères

Lorsque vous affichez un objet `MutInt` en Python, vous verrez une sortie du type `<__main__.MutInt object at 0x...>`. Cette sortie n'est pas très utile car elle ne vous indique pas la valeur réelle de l'objet `MutInt`. Pour faciliter la compréhension de ce que représente l'objet, nous allons implémenter des méthodes spéciales pour la représentation sous forme de chaîne de caractères.

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
```

Nous avons ajouté trois méthodes importantes à la classe `MutInt` :

- `__str__()` : Cette méthode est appelée lorsque vous utilisez la fonction `str()` sur l'objet ou lorsque vous affichez directement l'objet. Elle doit retourner une chaîne de caractères lisible par un humain.
- `__repr__()` : Cette méthode fournit la représentation sous forme de chaîne de caractères "officielle" de l'objet. Elle est principalement utilisée pour le débogage et devrait idéalement retourner une chaîne de caractères qui, si elle est passée à la fonction `eval()`, recréerait l'objet.
- `__format__()` : Cette méthode vous permet d'utiliser le système de formatage de chaînes de caractères de Python avec vos objets `MutInt`. Vous pouvez utiliser des spécifications de formatage telles que le remplissage et le formatage de nombres.

2. Créez un nouveau fichier de test appelé `test_string_repr.py` pour tester ces nouvelles méthodes :

```python
# test_string_repr.py

from mutint import MutInt

# Create a MutInt object
a = MutInt(3)

# Test string representation
print(f"str(a): {str(a)}")
print(f"repr(a): {repr(a)}")

# Test direct printing
print(f"Print a: {a}")

# Test string formatting
print(f"Formatted with padding: '{a:*^10}'")
print(f"Formatted as decimal: '{a:d}'")

# Test mutability
a.value = 42
print(f"After changing value, repr(a): {repr(a)}")
```

Dans ce fichier de test, nous importons d'abord la classe `MutInt`. Ensuite, nous créons un objet `MutInt` avec la valeur `3`. Nous testons les méthodes `__str__()` et `__repr__()` en utilisant les fonctions `str()` et `repr()`. Nous testons également l'affichage direct, le formatage de chaînes de caractères et la mutabilité de l'objet `MutInt`.

3. Exécutez le script de test :

```bash
python3 /home/labex/project/test_string_repr.py
```

Lorsque vous exécutez cette commande, Python exécutera le script `test_string_repr.py`. Vous devriez voir une sortie similaire à ceci :

```
str(a): 3
repr(a): MutInt(3)
Print a: 3
Formatted with padding: '****3*****'
Formatted as decimal: '3'
After changing value, repr(a): MutInt(42)
```

Maintenant, nos objets `MutInt` s'affichent correctement. La représentation sous forme de chaîne de caractères montre la valeur sous - jacente, et nous pouvons utiliser le formatage de chaînes de caractères tout comme avec les entiers normaux.

La différence entre `__str__()` et `__repr__()` est que `__str__()` est destinée à produire une sortie conviviale pour l'humain, tandis que `__repr__()` devrait idéalement produire une chaîne de caractères qui, lorsqu'elle est passée à `eval()`, recréerait l'objet. C'est pourquoi nous avons inclus le nom de la classe dans la méthode `__repr__()`.

La méthode `__format__()` permet à notre objet de fonctionner avec le système de formatage de Python, nous pouvons donc utiliser des spécifications de formatage telles que le remplissage et le formatage de nombres.
