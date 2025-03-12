# Création de décorateurs avec des arguments

Jusqu'à présent, nous avons utilisé le décorateur `@logged`, qui affiche toujours un message fixe. Mais que faire si vous souhaitez personnaliser le format du message ? Dans cette section, nous allons apprendre à créer un nouveau décorateur qui peut accepter des arguments, vous offrant ainsi plus de flexibilité dans l'utilisation des décorateurs.

## Compréhension des décorateurs paramétrés

Un décorateur paramétré est un type spécial de fonction. Au lieu de modifier directement une autre fonction, il retourne un décorateur. La structure générale d'un décorateur paramétré ressemble à ceci :

```python
def decorator_with_args(arg1, arg2, ...):
    def actual_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Use arg1, arg2, ... here
            # Call the original function
            return func(*args, **kwargs)
        return wrapper
    return actual_decorator
```

Lorsque vous utilisez `@decorator_with_args(value1, value2)` dans votre code, Python appelle d'abord `decorator_with_args(value1, value2)`. Cet appel retourne le véritable décorateur, qui est ensuite appliqué à la fonction qui suit la syntaxe `@`. Ce processus en deux étapes est essentiel au fonctionnement des décorateurs paramétrés.

## Création du décorateur logformat

Créons un décorateur `@logformat(fmt)` qui prend une chaîne de formatage comme argument. Cela nous permettra de personnaliser le message de journalisation.

1. Ouvrez `logcall.py` dans le WebIDE et ajoutez le nouveau décorateur. Le code ci-dessous montre comment définir à la fois le décorateur `logged` existant et le nouveau décorateur `logformat` :

```python
from functools import wraps

def logged(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

def logformat(fmt):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(fmt.format(func=func))
            return func(*args, **kwargs)
        return wrapper
    return decorator
```

Dans le décorateur `logformat`, la fonction externe `logformat` prend une chaîne de formatage `fmt` comme argument. Elle retourne ensuite la fonction `decorator`, qui est le véritable décorateur qui modifie la fonction cible.

2. Maintenant, testons notre nouveau décorateur en modifiant `sample.py`. Le code suivant montre comment utiliser à la fois les décorateurs `logged` et `logformat` sur différentes fonctions :

```python
from logcall import logged, logformat

@logged
def add(x, y):
    "Adds two numbers"
    return x + y

@logged
def sub(x, y):
    "Subtracts y from x"
    return x - y

@logformat('{func.__code__.co_filename}:{func.__name__}')
def mul(x, y):
    "Multiplies two numbers"
    return x * y
```

Ici, les fonctions `add` et `sub` utilisent le décorateur `logged`, tandis que la fonction `mul` utilise le décorateur `logformat` avec une chaîne de formatage personnalisée.

3. Exécutez le fichier `sample.py` mis à jour pour voir les résultats. Ouvrez votre terminal et exécutez la commande suivante :

```bash
cd ~/project
python3 -c "import sample; print(sample.add(2, 3)); print(sample.mul(2, 3))"
```

Vous devriez voir une sortie similaire à :

```
Calling add
5
sample.py:mul
6
```

Cette sortie montre que le décorateur `logged` affiche le nom de la fonction comme prévu, et le décorateur `logformat` utilise la chaîne de formatage personnalisée pour afficher le nom du fichier et le nom de la fonction.

## Redéfinition du décorateur logged en utilisant logformat

Maintenant que nous avons un décorateur `logformat` plus flexible, nous pouvons redéfinir notre décorateur `logged` d'origine en l'utilisant. Cela nous aidera à réutiliser le code et à maintenir un format de journalisation cohérent.

1. Mettez à jour `logcall.py` avec le code suivant :

```python
from functools import wraps

def logformat(fmt):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(fmt.format(func=func))
            return func(*args, **kwargs)
        return wrapper
    return decorator

# Define logged using logformat
logged = lambda func: logformat("Calling {func.__name__}")(func)
```

Ici, nous utilisons une fonction lambda pour définir le décorateur `logged` en termes du décorateur `logformat`. La fonction lambda prend une fonction `func` et applique le décorateur `logformat` avec une chaîne de formatage spécifique.

2. Testez que le décorateur `logged` redéfini fonctionne toujours. Ouvrez votre terminal et exécutez la commande suivante :

```bash
cd ~/project
python3 -c "from logcall import logged; @logged
def greet(name):
    return f'Hello, {name}'
    
print(greet('World'))"
```

Vous devriez voir :

```
Calling greet
Hello, World
```

Cela montre que le décorateur `logged` redéfini fonctionne comme prévu, et nous avons réussi à réutiliser le décorateur `logformat` pour obtenir un format de journalisation cohérent.
