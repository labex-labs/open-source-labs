# Mise en œuvre de la validation de type avec les annotations de fonction

En Python, vous avez la possibilité d'ajouter des annotations de type aux paramètres de fonction. Ces annotations servent à indiquer les types de données attendus pour les paramètres et la valeur de retour d'une fonction. Elles n'imposent pas les types au moment de l'exécution par défaut, mais elles peuvent être utilisées à des fins de validation.

Jetons un coup d'œil à un exemple :

```python
def add(x: int, y: int) -> int:
    return x + y
```

Dans ce code, `x: int` et `y: int` nous indiquent que les paramètres `x` et `y` devraient être des entiers. Le `-> int` à la fin indique que la fonction `add` retourne un entier. Ces annotations de type sont stockées dans l'attribut `__annotations__` de la fonction, qui est un dictionnaire qui associe les noms des paramètres à leurs types annotés.

Maintenant, nous allons améliorer notre classe `ValidatedFunction` pour utiliser ces annotations de type pour la validation. Pour ce faire, nous devrons utiliser le module `inspect` de Python. Ce module fournit des fonctions utiles pour obtenir des informations sur des objets en temps réel tels que des modules, des classes, des méthodes, des fonctions, etc. Dans notre cas, nous l'utiliserons pour associer les arguments de la fonction à leurs noms de paramètres correspondants.

Tout d'abord, nous devons modifier la classe `ValidatedFunction` dans le fichier `validate.py`. Vous pouvez ouvrir ce fichier en utilisant la commande suivante :

```bash
code /home/labex/project/validate.py
```

Remplacez la classe `ValidatedFunction` existante par la version améliorée suivante :

```python
import inspect

class ValidatedFunction:
    def __init__(self, func):
        self.func = func
        self.signature = inspect.signature(func)

    def __call__(self, *args, **kwargs):
        # Bind the arguments to the function parameters
        bound = self.signature.bind(*args, **kwargs)

        # Validate each argument against its annotation
        for name, val in bound.arguments.items():
            if name in self.func.__annotations__:
                # Get the validator class from the annotation
                validator = self.func.__annotations__[name]
                # Apply the validation
                validator.check(val)

        # Call the function with the validated arguments
        return self.func(*args, **kwargs)
```

Voici ce que fait cette version améliorée :

1. Elle utilise `inspect.signature()` pour obtenir des informations sur les paramètres de la fonction, telles que leurs noms, leurs valeurs par défaut et leurs types annotés.
2. La méthode `bind()` de la signature est utilisée pour associer les arguments fournis aux noms de paramètres correspondants. Cela nous aide à associer chaque argument à son paramètre correct dans la fonction.
3. Elle vérifie chaque argument par rapport à son annotation de type (si elle existe). Si une annotation est trouvée, elle récupère la classe de validateur à partir de l'annotation et applique la validation en utilisant la méthode `check()`.
4. Enfin, elle appelle la fonction originale avec les arguments validés.

Maintenant, testons cette classe `ValidatedFunction` améliorée avec quelques fonctions qui utilisent nos classes de validateurs dans leurs annotations de type. Ouvrez le fichier `test_validation.py` en utilisant la commande suivante :

```bash
code /home/labex/project/test_validation.py
```

Ajoutez le code suivant au fichier :

```python
from validate import ValidatedFunction, Integer, String

def greet(name: String, times: Integer):
    return name * times

# Wrap the greet function with ValidatedFunction
validated_greet = ValidatedFunction(greet)

# Valid call
try:
    result = validated_greet("Hello ", 3)
    print(f"Valid call result: {result}")
except TypeError as e:
    print(f"Unexpected error: {e}")

# Invalid call - wrong type for 'name'
try:
    result = validated_greet(123, 3)
    print(f"Invalid call unexpectedly succeeded: {result}")
except TypeError as e:
    print(f"Expected error for name: {e}")

# Invalid call - wrong type for 'times'
try:
    result = validated_greet("Hello ", "3")
    print(f"Invalid call unexpectedly succeeded: {result}")
except TypeError as e:
    print(f"Expected error for times: {e}")
```

Dans ce code, nous définissons une fonction `greet` avec les annotations de type `name: String` et `times: Integer`. Cela signifie que le paramètre `name` devrait être validé à l'aide de la classe `String`, et le paramètre `times` devrait être validé à l'aide de la classe `Integer`. Nous enveloppons ensuite la fonction `greet` avec notre classe `ValidatedFunction` pour activer la validation de type.

Nous effectuons trois cas de test : un appel valide, un appel invalide avec le mauvais type pour `name`, et un appel invalide avec le mauvais type pour `times`. Chaque appel est enveloppé dans un bloc `try-except` pour capturer toute exception `TypeError` qui pourrait être levée lors de la validation.

Pour exécuter le fichier de test, utilisez la commande suivante :

```bash
python3 /home/labex/project/test_validation.py
```

Vous devriez voir une sortie similaire à la suivante :

```
Valid call result: Hello Hello Hello
Expected error for name: Expected <class 'str'>
Expected error for times: Expected <class 'int'>
```

Cette sortie démontre que notre objet appelable `ValidatedFunction` impose maintenant la validation de type en fonction des annotations de fonction. Lorsque nous passons des arguments du mauvais type, les classes de validateurs détectent l'erreur et lèvent une `TypeError`. De cette façon, nous pouvons nous assurer que les fonctions sont appelées avec les bons types de données, ce qui aide à prévenir les bugs et rend notre code plus robuste.
