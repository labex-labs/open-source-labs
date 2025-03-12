# Création d'un décorateur de vérification de type avec des arguments

Dans les étapes précédentes, nous avons appris à connaître le décorateur `@validated`. Ce décorateur est utilisé pour appliquer les annotations de type dans les fonctions Python. Les annotations de type sont un moyen de spécifier les types attendus pour les arguments et les valeurs de retour des fonctions. Maintenant, nous allons aller plus loin. Nous allons créer un décorateur plus flexible qui peut accepter des spécifications de type en tant qu'arguments. Cela signifie que nous pouvons définir les types que nous souhaitons pour chaque argument et la valeur de retour de manière plus explicite.

## Compréhension de l'objectif

Notre objectif est de créer un décorateur `@enforce()`. Ce décorateur nous permettra de spécifier des contraintes de type en utilisant des arguments nommés. Voici un exemple de son fonctionnement :

```python
@enforce(x=Integer, y=Integer, return_=Integer)
def add(x, y):
    return x + y
```

Dans cet exemple, nous utilisons le décorateur `@enforce` pour spécifier que les arguments `x` et `y` de la fonction `add` doivent être de type `Integer`, et que la valeur de retour doit également être de type `Integer`. Ce décorateur se comportera de manière similaire à notre décorateur `@validated` précédent, mais il nous donne plus de contrôle sur les spécifications de type.

## Création du décorateur enforce

1. Tout d'abord, ouvrez le fichier `validate.py` dans le WebIDE. Nous allons ajouter notre nouveau décorateur à ce fichier. Voici le code que nous allons ajouter :

```python
from functools import wraps

class Integer:
    @classmethod
    def __instancecheck__(cls, x):
        return isinstance(x, int)

def validated(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Get function annotations
        annotations = func.__annotations__
        # Check arguments against annotations
        for arg_name, arg_value in zip(func.__code__.co_varnames, args):
            if arg_name in annotations and not isinstance(arg_value, annotations[arg_name]):
                raise TypeError(f'Expected {arg_name} to be {annotations[arg_name].__name__}')

        # Run the function and get the result
        result = func(*args, **kwargs)

        # Check the return value
        if 'return' in annotations and not isinstance(result, annotations['return']):
            raise TypeError(f'Expected return value to be {annotations["return"].__name__}')

        return result
    return wrapper

def enforce(**type_specs):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Check argument types
            for arg_name, arg_value in zip(func.__code__.co_varnames, args):
                if arg_name in type_specs and not isinstance(arg_value, type_specs[arg_name]):
                    raise TypeError(f'Expected {arg_name} to be {type_specs[arg_name].__name__}')

            # Run the function and get the result
            result = func(*args, **kwargs)

            # Check the return value
            if 'return_' in type_specs and not isinstance(result, type_specs['return_']):
                raise TypeError(f'Expected return value to be {type_specs["return_"].__name__}')

            return result
        return wrapper
    return decorator
```

Analysons ce que fait ce code. La classe `Integer` est utilisée pour définir un type personnalisé. Le décorateur `validated` vérifie les types des arguments de la fonction et de la valeur de retour en fonction des annotations de type de la fonction. Le décorateur `enforce` est le nouveau que nous créons. Il prend des arguments nommés qui spécifient les types pour chaque argument et la valeur de retour. À l'intérieur de la fonction `wrapper` du décorateur `enforce`, nous vérifions si les types des arguments et de la valeur de retour correspondent aux types spécifiés. Sinon, nous levons une erreur `TypeError`.

2. Maintenant, testons notre nouveau décorateur `@enforce`. Nous allons exécuter quelques cas de test pour voir s'il fonctionne comme prévu. Voici le code pour exécuter les tests :

```bash
cd ~/project
python3 -c "from validate import enforce, Integer

@enforce(x=Integer, y=Integer, return_=Integer)
def add(x, y):
    return x + y

# This should work
print(add(2, 3))

# This should raise a TypeError
try:
    print(add('2', 3))
except TypeError as e:
    print(f'Error: {e}')

# This should raise a TypeError
try:
    @enforce(x=Integer, y=Integer, return_=Integer)
    def bad_add(x, y):
        return str(x + y)
    print(bad_add(2, 3))
except TypeError as e:
    print(f'Error: {e}')"
```

Dans ce code de test, nous définissons d'abord une fonction `add` avec le décorateur `@enforce`. Nous appelons ensuite la fonction `add` avec des arguments valides, ce qui devrait fonctionner sans erreur. Ensuite, nous appelons la fonction `add` avec un argument invalide, ce qui devrait lever une erreur `TypeError`. Enfin, nous définissons une fonction `bad_add` qui retourne une valeur du mauvais type, ce qui devrait également lever une erreur `TypeError`.

Lorsque vous exécutez ce code de test, vous devriez voir une sortie similaire à ceci :

```
5
Error: Expected x to be Integer
Error: Expected return value to be Integer
```

Cette sortie montre que notre décorateur `@enforce` fonctionne correctement. Il lève une erreur `TypeError` lorsque les types des arguments ou de la valeur de retour ne correspondent pas aux types spécifiés.

## Comparaison des deux approches

Les décorateurs `@validated` et `@enforce` atteignent le même objectif d'application de contraintes de type, mais ils le font de différentes manières.

1. Le décorateur `@validated` utilise les annotations de type intégrées à Python. Voici un exemple :

   ```python
   @validated
   def add(x: Integer, y: Integer) -> Integer:
       return x + y
   ```

   Avec cette approche, nous spécifions les types directement dans la définition de la fonction en utilisant des annotations de type. C'est une fonctionnalité intégrée à Python, et elle offre un meilleur support dans les environnements de développement intégré (IDE). Les IDE peuvent utiliser ces annotations de type pour fournir des complétions de code, des vérifications de type et d'autres fonctionnalités utiles.

2. Le décorateur `@enforce`, en revanche, utilise des arguments nommés pour spécifier les types. Voici un exemple :

   ```python
   @enforce(x=Integer, y=Integer, return_=Integer)
   def add(x, y):
       return x + y
   ```

   Cette approche est plus explicite car nous passons directement les spécifications de type en tant qu'arguments au décorateur. Elle peut être utile lorsque vous travaillez avec des bibliothèques qui reposent sur d'autres systèmes d'annotation.

Chaque approche a ses propres avantages. Les annotations de type sont une partie native de Python et offrent un meilleur support dans les IDE, tandis que l'approche `@enforce` nous donne plus de flexibilité et d'explicitation. Vous pouvez choisir l'approche qui convient le mieux à vos besoins en fonction du projet sur lequel vous travaillez.
