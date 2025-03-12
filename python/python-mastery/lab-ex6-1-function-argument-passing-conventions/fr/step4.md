# Restriction des noms d'attributs

Actuellement, notre classe `Structure` permet de définir n'importe quel attribut sur ses instances. Pour les débutants, cela peut sembler pratique au départ, mais cela peut en réalité entraîner de nombreux problèmes. Lorsque vous travaillez avec une classe, vous vous attendez à ce que certains attributs soient présents et utilisés d'une manière spécifique. Si les utilisateurs font une faute de frappe dans les noms d'attributs ou essaient de définir des attributs qui ne font pas partie de la conception originale, cela peut entraîner des erreurs difficiles à trouver.

## La nécessité de restreindre les attributs

Examinons un scénario simple pour comprendre pourquoi nous devons restreindre les noms d'attributs. Considérez le code suivant :

```python
s = Stock('GOOG', 100, 490.1)
s.shares = 50      # Correct attribute name
s.share = 60       # Typo in attribute name - creates a new attribute instead of updating
```

Dans la deuxième ligne, il y a une faute de frappe. Au lieu de `shares`, nous avons écrit `share`. En Python, au lieu de lever une erreur, il créera simplement un nouvel attribut appelé `share`. Cela peut entraîner des bugs subtils car vous pourriez penser que vous mettez à jour l'attribut `shares`, mais vous créez en réalité un nouvel attribut. Cela peut faire que votre code se comporte de manière inattendue et soit très difficile à déboguer.

## Implémentation de la restriction des attributs

Pour résoudre ce problème, nous pouvons redéfinir la méthode `__setattr__`. Cette méthode est appelée chaque fois que vous essayez de définir un attribut sur un objet. En la redéfinissant, nous pouvons contrôler quels attributs peuvent être définis et lesquels ne peuvent pas.

Mettez à jour votre classe `Structure` dans le fichier `structure.py` avec le code suivant :

```python
def __setattr__(self, name, value):
    """
    Restrict attribute setting to only those defined in _fields
    or attributes starting with underscore (private attributes).
    """
    if name.startswith('_'):
        # Allow setting private attributes (starting with '_')
        super().__setattr__(name, value)
    elif name in self._fields:
        # Allow setting attributes defined in _fields
        super().__setattr__(name, value)
    else:
        # Raise an error for other attributes
        raise AttributeError(f'No attribute {name}')
```

Voici comment cette méthode fonctionne :

1. Si le nom de l'attribut commence par un tiret bas (`_`), il est considéré comme un attribut privé. Les attributs privés sont souvent utilisés à des fins internes dans une classe. Nous autorisons la définition de ces attributs car ils font partie de l'implémentation interne de la classe.
2. Si le nom de l'attribut est dans la liste `_fields`, cela signifie qu'il s'agit d'un des attributs définis dans la conception de la classe. Nous autorisons la définition de ces attributs car ils font partie du comportement attendu de la classe.
3. Si le nom de l'attribut ne répond à aucune de ces conditions, nous levons une erreur `AttributeError`. Cela indique à l'utilisateur qu'il essaie de définir un attribut qui n'existe pas dans la classe.

## Test de la restriction des attributs

Maintenant que nous avons implémenté la restriction des attributs, testons-la pour nous assurer qu'elle fonctionne comme prévu. Créez un fichier nommé `test_attributes.py` avec le code suivant :

```python
# test_attributes.py
from structure import Stock

s = Stock('GOOG', 100, 490.1)

# This should work - valid attribute
print("Setting shares to 50")
s.shares = 50
print(f"Shares is now: {s.shares}")

# This should work - private attribute
print("\nSetting _internal_data")
s._internal_data = "Some data"
print(f"_internal_data is: {s._internal_data}")

# This should fail - invalid attribute
print("\nTrying to set an invalid attribute:")
try:
    s.share = 60  # Typo in attribute name
    print("This should not print")
except AttributeError as e:
    print(f"Error correctly caught: {e}")
```

Pour exécuter le test, ouvrez votre terminal et entrez la commande suivante :

```bash
python3 test_attributes.py
```

Vous devriez voir la sortie suivante :

```
Setting shares to 50
Shares is now: 50

Setting _internal_data
_internal_data is: Some data

Trying to set an invalid attribute:
Error correctly caught: No attribute share
```

Cette sortie montre que notre classe empêche désormais les erreurs accidentelles d'attributs. Elle nous permet de définir des attributs valides et des attributs privés, mais elle lève une erreur lorsque nous essayons de définir un attribut invalide.

## L'importance de la restriction des attributs

Restreindre les noms d'attributs est très important pour écrire un code robuste et maintenable. Voici pourquoi :

1. Cela permet de détecter les fautes de frappe dans les noms d'attributs. Si vous faites une erreur lors de la saisie d'un nom d'attribut, le code lèvera une erreur au lieu de créer un nouvel attribut. Cela facilite la détection et la correction des erreurs dès le début du processus de développement.
2. Cela empêche les tentatives de définir des attributs qui n'existent pas dans la conception de la classe. Cela garantit que la classe est utilisée comme prévu et que le code se comporte de manière prévisible.
3. Cela évite la création accidentelle de nouveaux attributs. La création de nouveaux attributs peut entraîner un comportement inattendu et rendre le code plus difficile à comprendre et à maintenir.

En restreignant les noms d'attributs, nous rendons notre code plus fiable et plus facile à utiliser.
