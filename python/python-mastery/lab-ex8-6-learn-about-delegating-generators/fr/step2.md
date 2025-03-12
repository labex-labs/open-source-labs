# Utilisation de `yield from` dans les coroutines

Dans cette étape, nous allons explorer comment utiliser l'instruction `yield from` avec les coroutines pour des applications plus pratiques. Les coroutines sont un concept puissant en Python, et comprendre comment utiliser `yield from` avec elles peut grandement simplifier votre code.

## Coroutines et passage de messages

Les coroutines sont des fonctions spéciales qui peuvent recevoir des valeurs via l'instruction `yield`. Elles sont incroyablement utiles pour des tâches telles que le traitement de données et la gestion d'événements. Dans le fichier `cofollow.py`, il y a un décorateur `consumer`. Ce décorateur aide à configurer les coroutines en les faisant avancer automatiquement jusqu'au premier point `yield`. Cela signifie que vous n'avez pas à démarrer manuellement la coroutine ; le décorateur s'en charge pour vous.

Créons une coroutine qui reçoit des valeurs et valide leur type. Voici comment vous pouvez le faire :

1. Tout d'abord, ouvrez le fichier `cofollow.py` dans l'éditeur. Vous pouvez utiliser la commande suivante dans le terminal pour naviguer jusqu'au bon répertoire :

```bash
cd /home/labex/project
```

2. Ensuite, ajoutez la fonction `receive` suivante à la fin du fichier `cofollow.py`. Cette fonction est une coroutine qui recevra un message et en validera le type.

```python
def receive(expected_type):
    """
    A coroutine that receives a message and validates its type.
    Returns the received message if it matches the expected type.
    """
    msg = yield
    assert isinstance(msg, expected_type), f'Expected type {expected_type}'
    return msg
```

Voici ce que fait cette fonction :

- Elle utilise `yield` sans expression pour recevoir une valeur. Lorsqu'une valeur est envoyée à la coroutine, cette instruction `yield` la capturera.
- Elle vérifie si la valeur reçue est du type attendu en utilisant la fonction `isinstance`. Si le type ne correspond pas, elle lève une `AssertionError`.
- Si la vérification de type réussit, elle retourne la valeur.

3. Maintenant, créons une coroutine qui utilise `yield from` avec notre fonction `receive`. Cette nouvelle coroutine recevra et affichera uniquement des entiers.

```python
@consumer
def print_ints():
    """
    A coroutine that receives and prints integers only.
    Uses yield from to delegate to the receive coroutine.
    """
    while True:
        val = yield from receive(int)
        print('Got:', val)
```

4. Pour tester cette coroutine, ouvrez un interpréteur Python et exécutez le code suivant :

```python
from cofollow import print_ints

p = print_ints()
p.send(42)
p.send(13)
try:
    p.send('13')  # This should raise an AssertionError
except AssertionError as e:
    print(f"Error: {e}")
```

Vous devriez voir la sortie suivante :

```
Got: 42
Got: 13
Error: Expected type <class 'int'>
```

## Comprendre le fonctionnement de `yield from` avec les coroutines

Lorsque nous utilisons `yield from receive(int)` dans la coroutine `print_ints`, les étapes suivantes se produisent :

1. Le contrôle est délégué à la coroutine `receive`. Cela signifie que la coroutine `print_ints` se met en pause et que la coroutine `receive` commence à s'exécuter.
2. La coroutine `receive` utilise `yield` pour recevoir une valeur. Elle attend qu'une valeur lui soit envoyée.
3. Lorsqu'une valeur est envoyée à `print_ints`, elle est en fait reçue par `receive`. L'instruction `yield from` s'occupe de passer la valeur de `print_ints` à `receive`.
4. La coroutine `receive` valide le type de la valeur reçue. Si le type est correct, elle retourne la valeur.
5. La valeur retournée devient le résultat de l'expression `yield from` dans la coroutine `print_ints`. Cela signifie que la variable `val` dans `print_ints` reçoit la valeur retournée par `receive`.

L'utilisation de `yield from` rend le code plus lisible que si nous devions gérer directement le rendu et la réception. Elle abstrait la complexité du passage de valeurs entre les coroutines.

## Création de coroutines de vérification de type plus avancées

Étendons nos fonctions utilitaires pour gérer une validation de type plus complexe. Voici comment vous pouvez le faire :

1. Ajoutez les fonctions suivantes au fichier `cofollow.py` :

```python
def receive_dict():
    """Receive and validate a dictionary"""
    result = yield from receive(dict)
    return result

def receive_str():
    """Receive and validate a string"""
    result = yield from receive(str)
    return result

@consumer
def process_data():
    """Process different types of data using the receive utilities"""
    while True:
        print("Waiting for a string...")
        name = yield from receive_str()
        print(f"Got string: {name}")

        print("Waiting for a dictionary...")
        data = yield from receive_dict()
        print(f"Got dictionary with {len(data)} items: {data}")

        print("Processing complete for this round.")
```

2. Pour tester la nouvelle coroutine, ouvrez un interpréteur Python et exécutez le code suivant :

```python
from cofollow import process_data

proc = process_data()
proc.send("John Doe")
proc.send({"age": 30, "city": "New York"})
proc.send("Jane Smith")
try:
    proc.send(123)  # This should raise an AssertionError
except AssertionError as e:
    print(f"Error: {e}")
```

Vous devriez voir une sortie comme celle-ci :

```
Waiting for a string...
Got string: John Doe
Waiting for a dictionary...
Got dictionary with 2 items: {'age': 30, 'city': 'New York'}
Processing complete for this round.
Waiting for a string...
Got string: Jane Smith
Waiting for a dictionary...
Error: Expected type <class 'dict'>
```

L'instruction `yield from` rend le code plus propre et plus lisible. Elle nous permet de nous concentrer sur la logique de haut niveau de notre programme plutôt que de nous perdre dans les détails du passage de messages entre les coroutines.
