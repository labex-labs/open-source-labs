# Création d'un objet appelable de base

En Python, un objet appelable (callable object) est un objet qui peut être utilisé comme une fonction. Vous pouvez le considérer comme quelque chose que vous pouvez "appeler" en mettant des parenthèses après, de la même manière que vous appelez une fonction normale. Pour faire en sorte qu'une classe en Python se comporte comme un objet appelable, nous devons implémenter une méthode spéciale appelée `__call__`. Cette méthode est automatiquement invoquée lorsque vous utilisez l'objet avec des parenthèses, tout comme lorsque vous appelez une fonction.

Commençons par modifier le fichier `validate.py`. Nous allons ajouter une nouvelle classe appelée `ValidatedFunction` à ce fichier, et cette classe sera notre objet appelable. Pour ouvrir le fichier dans l'éditeur de code, exécutez la commande suivante dans le terminal :

```bash
code /home/labex/project/validate.py
```

Une fois le fichier ouvert, faites défiler jusqu'à la fin et ajoutez le code suivant :

```python
class ValidatedFunction:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print('Calling', self.func)
        result = self.func(*args, **kwargs)
        return result
```

Analysons ce que fait ce code. La classe `ValidatedFunction` a une méthode `__init__`, qui est le constructeur. Lorsque vous créez une instance de cette classe, vous lui passez une fonction. Cette fonction est ensuite stockée en tant qu'attribut de l'instance, nommé `self.func`.

La méthode `__call__` est la partie clé qui rend cette classe appelable. Lorsque vous appelez une instance de la classe `ValidatedFunction`, cette méthode `__call__` est exécutée. Voici ce qu'elle fait étape par étape :

1. Elle affiche un message qui indique quelle fonction est appelée. Cela est utile pour le débogage et pour comprendre ce qui se passe.
2. Elle appelle la fonction qui a été stockée dans `self.func` avec les arguments que vous avez passés lorsque vous avez appelé l'instance. Les `*args` et `**kwargs` vous permettent de passer n'importe quel nombre d'arguments positionnels et de mots-clés.
3. Elle retourne le résultat de l'appel de la fonction.

Maintenant, testons cette classe `ValidatedFunction`. Nous allons créer un nouveau fichier appelé `test_callable.py` pour écrire notre code de test. Pour ouvrir ce nouveau fichier dans l'éditeur de code, exécutez la commande suivante :

```bash
code /home/labex/project/test_callable.py
```

Ajoutez le code suivant au fichier `test_callable.py` :

```python
from validate import ValidatedFunction

def add(x, y):
    return x + y

# Wrap the add function with ValidatedFunction
validated_add = ValidatedFunction(add)

# Call the wrapped function
result = validated_add(2, 3)
print(f"Result: {result}")

# Try another call
result = validated_add(10, 20)
print(f"Result: {result}")
```

Dans ce code, nous importons d'abord la classe `ValidatedFunction` depuis le fichier `validate.py`. Ensuite, nous définissons une fonction simple appelée `add` qui prend deux nombres et retourne leur somme.

Nous créons une instance de la classe `ValidatedFunction`, en lui passant la fonction `add`. Cela "enveloppe" la fonction `add` à l'intérieur de l'instance de `ValidatedFunction`.

Nous appelons ensuite la fonction enveloppée deux fois, une fois avec les arguments `2` et `3`, puis avec `10` et `20`. Chaque fois que nous appelons la fonction enveloppée, la méthode `__call__` de la classe `ValidatedFunction` est invoquée, qui à son tour appelle la fonction `add` originale.

Pour exécuter le code de test, exécutez la commande suivante dans le terminal :

```bash
python3 /home/labex/project/test_callable.py
```

Vous devriez voir une sortie similaire à ceci :

```
Calling <function add at 0x7f2d1c3a9940>
Result: 5
Calling <function add at 0x7f2d1c3a9940>
Result: 30
```

Cette sortie montre que notre objet appelable fonctionne comme prévu. Lorsque nous appelons `validated_add(2, 3)`, cela appelle en fait la méthode `__call__` de la classe `ValidatedFunction`, qui appelle ensuite la fonction `add` originale.

Pour l'instant, notre classe `ValidatedFunction` ne fait que afficher un message et transférer l'appel à la fonction originale. Dans l'étape suivante, nous allons améliorer cette classe pour effectuer une validation de type en fonction des annotations de la fonction.
