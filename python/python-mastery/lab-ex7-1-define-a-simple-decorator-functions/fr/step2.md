# Créer un décorateur de validation

Dans cette étape, nous allons créer un décorateur (decorator) plus pratique. En Python, un décorateur est un type spécial de fonction qui peut modifier le comportement d'une autre fonction. Le décorateur que nous allons créer va valider les arguments d'une fonction en fonction des annotations de type (type annotations). Les annotations de type sont un moyen de spécifier les types de données attendus pour les arguments d'une fonction et sa valeur de retour. C'est un cas d'utilisation courant dans les applications du monde réel car cela permet de s'assurer que les fonctions reçoivent les bons types d'entrée, ce qui peut prévenir de nombreux bugs.

## Comprendre les classes de validation

Nous avons déjà créé un fichier appelé `validate.py` pour vous, et il contient quelques classes de validation. Les classes de validation sont utilisées pour vérifier si une valeur répond à certains critères. Pour voir ce qu'il y a dans ce fichier, vous devez l'ouvrir dans l'éditeur VSCode. Vous pouvez le faire en exécutant les commandes suivantes dans le terminal :

```bash
cd /home/labex/project
code validate.py
```

Le fichier contient trois classes :

1. `Validator` - C'est une classe de base. Une classe de base fournit un cadre général ou une structure que d'autres classes peuvent hériter. Dans ce cas, elle fournit la structure de base pour la validation.
2. `Integer` - Cette classe de validateur est utilisée pour s'assurer qu'une valeur est un entier. Si vous passez une valeur non entière à une fonction qui utilise ce validateur, elle lèvera une erreur.
3. `PositiveInteger` - Cette classe de validateur s'assure qu'une valeur est un entier positif. Donc, si vous passez un entier négatif ou zéro, elle lèvera également une erreur.

## Ajouter le décorateur de validation

Maintenant, nous allons ajouter une fonction décorateur nommée `validated` au fichier `validate.py`. Ce décorateur effectuera plusieurs tâches importantes :

1. Il inspectera les annotations de type d'une fonction. Les annotations de type sont comme de petites notes qui nous indiquent quel type de données la fonction attend.
2. Il validera les arguments passés à la fonction par rapport à ces annotations de type. Cela signifie qu'il vérifiera si les valeurs passées à la fonction sont du bon type.
3. Il validera également la valeur de retour de la fonction par rapport à son annotation. Ainsi, il s'assurera que la fonction retourne le type de données qu'elle est censée retourner.
4. Si la validation échoue, il lèvera des messages d'erreur informatifs. Ces messages vous diront exactement ce qui a mal fonctionné, comme quel argument avait le mauvais type.

Ajoutez le code suivant à la fin du fichier `validate.py` :

```python
# Add to validate.py

import inspect
import functools

def validated(func):
    sig = inspect.signature(func)

    print(f'Validating {func.__name__} {sig}')

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Bind arguments to the signature
        bound = sig.bind(*args, **kwargs)
        errors = []

        # Validate each argument
        for name, value in bound.arguments.items():
            if name in sig.parameters:
                param = sig.parameters[name]
                if param.annotation != inspect.Parameter.empty:
                    try:
                        # Create an instance of the validator and validate the value
                        if isinstance(param.annotation, type) and issubclass(param.annotation, Validator):
                            validator = param.annotation()
                            bound.arguments[name] = validator.validate(value)
                    except Exception as e:
                        errors.append(f'    {name}: {e}')

        # If validation errors, raise an exception
        if errors:
            raise TypeError('Bad Arguments\n' + '\n'.join(errors))

        # Call the function
        result = func(*bound.args, **bound.kwargs)

        # Validate the return value
        if sig.return_annotation != inspect.Signature.empty:
            try:
                if isinstance(sig.return_annotation, type) and issubclass(sig.return_annotation, Validator):
                    validator = sig.return_annotation()
                    result = validator.validate(result)
            except Exception as e:
                raise TypeError(f'Bad return: {e}') from None

        return result

    return wrapper
```

Ce code utilise le module `inspect` de Python. Le module `inspect` nous permet d'obtenir des informations sur des objets en temps réel, comme des fonctions. Ici, nous l'utilisons pour examiner la signature de la fonction et valider les arguments en fonction des annotations de type. Nous utilisons également `functools.wraps`. C'est une fonction auxiliaire qui conserve les métadonnées de la fonction originale, telles que son nom et sa docstring. Les métadonnées sont comme des informations supplémentaires sur la fonction qui nous aident à comprendre ce qu'elle fait.

## Tester le décorateur de validation

Créons un fichier pour tester notre décorateur de validation. Nous allons créer un nouveau fichier appelé `test_validate.py` et y ajouter le code suivant :

```python
# test_validate.py

from validate import Integer, PositiveInteger, validated

@validated
def add(x: Integer, y: Integer) -> Integer:
    return x + y

@validated
def pow(x: Integer, y: Integer) -> Integer:
    return x ** y

# Test with a class
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def cost(self):
        return self.shares * self.price

    @validated
    def sell(self, nshares: PositiveInteger):
        self.shares -= nshares
```

Maintenant, nous allons tester notre décorateur dans l'interpréteur Python. Tout d'abord, accédez au répertoire du projet et lancez l'interpréteur Python en exécutant ces commandes dans le terminal :

```bash
cd /home/labex/project
python3
```

Ensuite, dans l'interpréteur Python, nous pouvons exécuter le code suivant pour tester notre décorateur :

```python
>>> from test_validate import add, pow, Stock
Validating add (x: validate.Integer, y: validate.Integer) -> validate.Integer
Validating pow (x: validate.Integer, y: validate.Integer) -> validate.Integer
Validating sell (self, nshares: validate.PositiveInteger) -> <class 'inspect._empty'>
>>>
>>> # Test with valid inputs
>>> add(2, 3)
5
>>>
>>> # Test with invalid inputs
>>> add('2', '3')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/labex/project/validate.py", line 75, in wrapper
    raise TypeError('Bad Arguments\n' + '\n'.join(errors))
TypeError: Bad Arguments
    x: Expected <class 'int'>
    y: Expected <class 'int'>
>>>
>>> # Test valid power
>>> pow(2, 3)
8
>>>
>>> # Test with negative exponent (produces non - integer result)
>>> pow(2, -1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/labex/project/validate.py", line 83, in wrapper
    raise TypeError(f'Bad return: {e}') from None
TypeError: Bad return: Expected <class 'int'>
>>>
>>> # Test with a class
>>> s = Stock("GOOG", 100, 490.1)
>>> s.sell(50)
>>> s.shares
50
>>>
>>> # Test with invalid shares
>>> s.sell(-10)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/labex/project/validate.py", line 75, in wrapper
    raise TypeError('Bad Arguments\n' + '\n'.join(errors))
TypeError: Bad Arguments
    nshares: Expected value > 0
>>> exit()
```

Comme vous pouvez le voir, notre décorateur `validated` a réussi à appliquer la vérification de type sur les arguments et les valeurs de retour des fonctions. Cela est très utile car cela rend notre code plus robuste. Au lieu de laisser les erreurs de type se propager plus profondément dans le code et causer des bugs difficiles à trouver, nous les capturons aux limites des fonctions.
