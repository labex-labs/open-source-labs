# Gestion des exceptions dans les générateurs

Dans cette étape, nous allons apprendre à gérer les exceptions dans les générateurs et les coroutines. Mais d'abord, comprenons ce qu'est une exception. Une exception est un événement qui se produit lors de l'exécution d'un programme et perturbe le flux normal des instructions du programme. En Python, nous pouvons utiliser la méthode `throw()` pour gérer les exceptions dans les générateurs et les coroutines.

## Comprendre les coroutines

Une coroutine est un type spécial de générateur. Contrairement aux générateurs ordinaires qui produisent principalement des valeurs, les coroutines peuvent à la fois consommer des valeurs (en utilisant la méthode `send()`) et produire des valeurs. Le fichier `cofollow.py` contient une implémentation simple d'une coroutine.

Ouvrons le fichier `cofollow.py` dans l'éditeur WebIDE. Voici le code à l'intérieur :

```python
def consumer(func):
    def start(*args,**kwargs):
        c = func(*args,**kwargs)
        next(c)
        return c
    return start

@consumer
def printer():
    while True:
        item = yield
        print(item)
```

Maintenant, décomposons ce code. Le `consumer` est un décorateur. Un décorateur est une fonction qui prend une autre fonction en argument, lui ajoute une certaine fonctionnalité, puis retourne la fonction modifiée. Dans ce cas, le décorateur `consumer` déplace automatiquement le générateur jusqu'à sa première instruction `yield`. Cela est important car il prépare le générateur à recevoir des valeurs.

La coroutine `printer()` est définie avec le décorateur `@consumer`. À l'intérieur de la fonction `printer()`, nous avons une boucle `while` infinie. L'instruction `item = yield` est là que se passe la magie. Elle met en pause l'exécution de la coroutine et attend de recevoir une valeur. Lorsqu'une valeur est envoyée à la coroutine, elle reprend son exécution et affiche la valeur reçue.

## Ajout de la gestion des exceptions à la coroutine

Maintenant, nous allons modifier la coroutine `printer()` pour gérer les exceptions. Nous allons mettre à jour la fonction `printer()` dans `cofollow.py` comme ceci :

```python
@consumer
def printer():
    while True:
        try:
            item = yield
            print(item)
        except Exception as e:
            print('ERROR: %r' % e)
```

Le bloc `try` contient le code qui peut lever une exception. Dans notre cas, il s'agit du code qui reçoit et affiche la valeur. Si une exception se produit dans le bloc `try`, l'exécution saute au bloc `except`. Le bloc `except` intercepte l'exception et affiche un message d'erreur. Après avoir apporté ces modifications, enregistrez le fichier.

## Expérimentation de la gestion des exceptions dans les coroutines

Commençons à expérimenter en lançant des exceptions dans la coroutine. Ouvrez un terminal et lancez l'interpréteur Python en utilisant les commandes suivantes :

```bash
cd ~/project
python3
```

### Expérience 1 : Utilisation de base d'une coroutine

```python
>>> from cofollow import printer
>>> p = printer()
>>> p.send('hello')  # Send a value to the coroutine
hello
>>> p.send(42)  # Send another value
42
```

Ici, nous importons d'abord la coroutine `printer` du module `cofollow`. Ensuite, nous créons une instance de la coroutine `printer` nommée `p`. Nous utilisons la méthode `send()` pour envoyer des valeurs à la coroutine. Comme vous pouvez le voir, la coroutine traite les valeurs que nous lui envoyons sans aucun problème.

### Expérience 2 : Lancement d'une exception dans la coroutine

```python
>>> p.throw(ValueError('It failed'))  # Throw an exception into the coroutine
ERROR: ValueError('It failed')
```

Dans cette expérience, nous utilisons la méthode `throw()` pour injecter une exception `ValueError` dans la coroutine. Le bloc `try-except` dans la coroutine `printer()` intercepte l'exception et affiche un message d'erreur. Cela montre que notre gestion des exceptions fonctionne comme prévu.

### Expérience 3 : Lancement d'une vraie exception dans la coroutine

```python
>>> try:
...     int('n/a')  # This will raise a ValueError
... except ValueError as e:
...     p.throw(e)  # Throw the caught exception into the coroutine
...
ERROR: ValueError("invalid literal for int() with base 10: 'n/a'")
```

Ici, nous essayons d'abord de convertir la chaîne `'n/a'` en entier, ce qui lève une exception `ValueError`. Nous interceptionnons cette exception et utilisons ensuite la méthode `throw()` pour la transmettre à la coroutine. La coroutine intercepte l'exception et affiche le message d'erreur.

### Expérience 4 : Vérification que la coroutine continue de fonctionner

```python
>>> p.send('still working')  # The coroutine continues to run after handling exceptions
still working
```

Après avoir géré les exceptions, nous envoyons une autre valeur à la coroutine en utilisant la méthode `send()`. La coroutine est toujours active et peut traiter la nouvelle valeur. Cela montre que notre coroutine peut continuer à fonctionner même après avoir rencontré des erreurs.

## Points clés

1. Les générateurs et les coroutines peuvent gérer les exceptions au niveau de l'instruction `yield`. Cela signifie que nous pouvons intercepter et gérer les erreurs qui se produisent lorsque la coroutine attend ou traite une valeur.
2. La méthode `throw()` vous permet d'injecter des exceptions dans un générateur ou une coroutine. Cela est utile pour les tests et pour gérer les erreurs qui se produisent en dehors de la coroutine.
3. Gérer correctement les exceptions dans les générateurs vous permet de créer des générateurs robustes et tolérants aux erreurs qui peuvent continuer à fonctionner même en cas d'erreur. Cela rend votre code plus fiable et plus facile à maintenir.

Pour quitter l'interpréteur Python, vous pouvez taper `exit()` ou appuyer sur `Ctrl+D`.
