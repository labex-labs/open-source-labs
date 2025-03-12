# Conservation des métadonnées de fonction dans les décorateurs

En Python, les décorateurs (decorators) sont un outil puissant qui vous permet de modifier le comportement des fonctions. Cependant, lorsque vous utilisez un décorateur pour envelopper une fonction, il y a un petit problème. Par défaut, les métadonnées de la fonction d'origine, telles que son nom, sa chaîne de documentation (docstring) et ses annotations, sont perdues. Les métadonnées sont importantes car elles facilitent l'introspection (l'examen de la structure du code) et la génération de documentation. Vérifions d'abord ce problème.

Ouvrez votre terminal dans le WebIDE. Nous allons exécuter quelques commandes Python pour voir ce qui se passe lorsque nous utilisons un décorateur. Les commandes suivantes créeront une simple fonction `add` enveloppée dans un décorateur, puis afficheront la fonction et sa docstring.

```bash
cd ~/project
python3 -c "from logcall import logged; @logged
def add(x,y):
    'Adds two things'
    return x+y
    
print(add)
print(add.__doc__)"
```

Lorsque vous exécutez ces commandes, vous verrez une sortie similaire à ceci :

```
<function wrapper at 0x...>
None
```

Notez que au lieu d'afficher le nom de la fonction comme `add`, il affiche `wrapper`. Et la docstring, qui devrait être `'Adds two things'`, est `None`. Cela peut être un gros problème lorsque vous utilisez des outils qui dépendent de ces métadonnées, comme les outils d'introspection ou les générateurs de documentation.

## Résolution du problème avec functools.wraps

Le module `functools` de Python vient à la rescousse. Il fournit un décorateur `wraps` qui peut nous aider à conserver les métadonnées de la fonction. Voyons comment nous pouvons modifier notre décorateur `logged` pour utiliser `wraps`.

1. Tout d'abord, ouvrez le fichier `logcall.py` dans le WebIDE. Vous pouvez accéder au répertoire du projet en utilisant la commande suivante dans le terminal :

```bash
cd ~/project
```

2. Maintenant, mettez à jour le décorateur `logged` dans `logcall.py` avec le code suivant. Le décorateur `@wraps(func)` est la clé ici. Il copie toutes les métadonnées de la fonction d'origine `func` vers la fonction enveloppante.

```python
from functools import wraps

def logged(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper
```

3. Le décorateur `@wraps(func)` a un rôle important. Il prend toutes les métadonnées (comme le nom, la docstring et les annotations) de la fonction d'origine `func` et les attache à la fonction `wrapper`. De cette façon, lorsque nous utilisons la fonction décorée, elle aura les bonnes métadonnées.

4. Testons notre décorateur amélioré. Exécutez les commandes suivantes dans le terminal :

```bash
python3 -c "from logcall import logged; @logged
def add(x,y):
    'Adds two things'
    return x+y
    
print(add)
print(add.__doc__)"
```

Maintenant, vous devriez voir :

```
<function add at 0x...>
Adds two things
```

Génial ! Le nom de la fonction et la docstring sont conservés. Cela signifie que notre décorateur fonctionne maintenant comme prévu et que les métadonnées de la fonction d'origine sont intactes.

## Correction du décorateur validate.py

Maintenant, appliquons la même correction au décorateur `validated` dans `validate.py`. Ce décorateur est utilisé pour valider les types des arguments de fonction et la valeur de retour en fonction des annotations de la fonction.

1. Ouvrez `validate.py` dans le WebIDE.

2. Mettez à jour le décorateur `validated` avec le décorateur `@wraps`. Le code suivant montre comment le faire. Le décorateur `@wraps(func)` est ajouté à la fonction `wrapper` à l'intérieur du décorateur `validated` pour conserver les métadonnées.

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
```

3. Testons que notre décorateur `validated` conserve maintenant les métadonnées. Exécutez les commandes suivantes dans le terminal :

```bash
python3 -c "from validate import validated, Integer; @validated
def multiply(x: Integer, y: Integer) -> Integer:
    'Multiplies two integers'
    return x * y
    
print(multiply)
print(multiply.__doc__)"
```

Vous devriez voir :

```
<function multiply at 0......>
Multiplies two integers
```

Maintenant, les deux décorateurs, `logged` et `validated`, conservent correctement les métadonnées des fonctions qu'ils décorent. Cela garantit que lorsque vous utilisez ces décorateurs, les fonctions auront toujours leurs noms, docstrings et annotations d'origine, ce qui est très utile pour la lisibilité et la maintenance du code.
