# Comprendre les classes de validateurs

Dans ce laboratoire, nous allons nous appuyer sur un ensemble de classes de validateurs pour créer un objet appelable (callable object). Avant de commencer à développer, il est important de comprendre les classes de validateurs fournies dans le fichier `validate.py`. Ces classes nous aideront à effectuer des vérifications de type, ce qui est une partie cruciale pour garantir que notre code fonctionne comme prévu.

Commençons par ouvrir le fichier `validate.py` dans l'IDE Web. Ce fichier contient le code des classes de validateurs que nous allons utiliser. Pour l'ouvrir, exécutez la commande suivante dans le terminal :

```bash
code /home/labex/project/validate.py
```

Une fois le fichier ouvert, vous verrez qu'il contient plusieurs classes. Voici un bref aperçu de ce que fait chaque classe :

1. `Validator` : C'est une classe de base. Elle a une méthode `check`, mais actuellement, cette méthode ne fait rien. Elle sert de point de départ pour les autres classes de validateurs.
2. `Typed` : C'est une sous-classe de `Validator`. Son principal rôle est de vérifier si une valeur est d'un type spécifique.
3. `Integer`, `Float` et `String` : Ce sont des validateurs de type spécifiques qui héritent de `Typed`. Ils sont conçus pour vérifier si une valeur est un entier, un nombre à virgule flottante ou une chaîne de caractères, respectivement.

Maintenant, voyons comment ces classes de validateurs fonctionnent en pratique. Nous allons créer un nouveau fichier appelé `test.py` pour les tester. Pour créer et ouvrir ce fichier, exécutez la commande suivante :

```bash
code /home/labex/project/test.py
```

Une fois le fichier `test.py` ouvert, ajoutez le code suivant. Ce code testera les validateurs `Integer` et `String` :

```python
from validate import Integer, String, Float

# Test Integer validator
print("Testing Integer validator:")
try:
    Integer.check(42)
    print("✓ Integer check passed for 42")
except TypeError as e:
    print(f"✗ Error: {e}")

try:
    Integer.check("Hello")
    print("✗ Integer check incorrectly passed for 'Hello'")
except TypeError as e:
    print(f"✓ Correctly raised error: {e}")

# Test String validator
print("\nTesting String validator:")
try:
    String.check("Hello")
    print("✓ String check passed for 'Hello'")
except TypeError as e:
    print(f"✗ Error: {e}")
```

Dans ce code, nous importons d'abord les validateurs `Integer`, `String` et `Float` depuis le fichier `validate.py`. Ensuite, nous testons le validateur `Integer` en essayant de vérifier une valeur entière (`42`) et une valeur de chaîne de caractères (`"Hello"`). Si la vérification réussit pour l'entier, nous affichons un message de succès. Si elle réussit incorrectement pour la chaîne de caractères, nous affichons un message d'erreur. Si la vérification lève correctement une `TypeError` pour la chaîne de caractères, nous affichons un message de succès. Nous effectuons un test similaire pour le validateur `String`.

Après avoir ajouté le code, exécutez le fichier de test en utilisant la commande suivante :

```bash
python3 /home/labex/project/test.py
```

Vous devriez voir une sortie similaire à ceci :

```
Testing Integer validator:
✓ Integer check passed for 42
✓ Correctly raised error: Expected <class 'int'>

Testing String validator:
✓ String check passed for 'Hello'
```

Comme vous pouvez le voir, ces classes de validateurs nous permettent d'effectuer facilement des vérifications de type. Par exemple, lorsque vous appelez `Integer.check(x)`, cela lèvera une `TypeError` si `x` n'est pas un entier.

Maintenant, pensons à un scénario pratique. Supposons que nous ayons une fonction qui exige que ses arguments soient de types spécifiques. Voici un exemple d'une telle fonction :

```python
def add(x, y):
    Integer.check(x)  # Make sure x is an integer
    Integer.check(y)  # Make sure y is an integer
    return x + y
```

Cette fonction fonctionne, mais il y a un problème. Nous devons ajouter manuellement les vérifications des validateurs chaque fois que nous voulons utiliser la vérification de type. Cela peut être chronophage et propice aux erreurs, en particulier pour les fonctions ou les projets plus importants.

Dans les prochaines étapes, nous allons résoudre ce problème en créant un objet appelable. Cet objet sera capable d'appliquer automatiquement ces vérifications de type en fonction des annotations de fonction. De cette façon, nous n'aurons pas à ajouter les vérifications manuellement à chaque fois.
