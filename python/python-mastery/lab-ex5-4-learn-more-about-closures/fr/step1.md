# Les fermetures (Closures) en tant que structure de données

En Python, les fermetures offrent un moyen puissant d'encapsuler des données. L'encapsulation consiste à garder les données privées et à contrôler l'accès à celles-ci. Avec les fermetures, vous pouvez créer des fonctions qui gèrent et modifient des données privées sans avoir à utiliser des classes ou des variables globales. Les variables globales peuvent être accédées et modifiées depuis n'importe quel endroit de votre code, ce qui peut entraîner un comportement inattendu. Les classes, en revanche, nécessitent une structure plus complexe. Les fermetures offrent une alternative plus simple pour l'encapsulation de données.

Créons un fichier appelé `counter.py` pour illustrer ce concept :

1. Ouvrez l'WebIDE et créez un nouveau fichier nommé `counter.py` dans le répertoire `/home/labex/project`. C'est là que nous allons écrire le code qui définit notre compteur basé sur une fermeture.

2. Ajoutez le code suivant au fichier :

```python
def counter(value):
    """
    Create a counter with increment and decrement functions.

    Args:
        value: Initial value of the counter

    Returns:
        Two functions: one to increment the counter, one to decrement it
    """
    def incr():
        nonlocal value
        value += 1
        return value

    def decr():
        nonlocal value
        value -= 1
        return value

    return incr, decr
```

Dans ce code, nous définissons une fonction appelée `counter()`. Cette fonction prend une valeur initiale `value` en argument. À l'intérieur de la fonction `counter()`, nous définissons deux fonctions internes : `incr()` et `decr()`. Ces fonctions internes ont accès au même variable `value`. Le mot-clé `nonlocal` est utilisé pour indiquer à Python que nous voulons modifier la variable `value` de la portée englobante (la fonction `counter()`). Sans le mot-clé `nonlocal`, Python créerait une nouvelle variable locale à l'intérieur des fonctions internes au lieu de modifier la variable `value` de la portée externe.

3. Maintenant, créons un fichier de test pour voir cela en action. Créez un nouveau fichier nommé `test_counter.py` avec le contenu suivant :

```python
from counter import counter

# Create a counter starting at 0
up, down = counter(0)

# Increment the counter several times
print("Incrementing the counter:")
print(up())  # Should print 1
print(up())  # Should print 2
print(up())  # Should print 3

# Decrement the counter
print("\nDecrementing the counter:")
print(down())  # Should print 2
print(down())  # Should print 1
```

Dans ce fichier de test, nous importons d'abord la fonction `counter()` depuis le fichier `counter.py`. Ensuite, nous créons un compteur démarrant à 0 en appelant `counter(0)` et en déballant les fonctions retournées dans `up` et `down`. Nous appelons ensuite la fonction `up()` plusieurs fois pour incrémenter le compteur et afficher les résultats. Après cela, nous appelons la fonction `down()` pour décrémenter le compteur et afficher les résultats.

4. Exécutez le fichier de test en exécutant la commande suivante dans le terminal :

```bash
python3 test_counter.py
```

Vous devriez voir la sortie suivante :

```
Incrementing the counter:
1
2
3

Decrementing the counter:
2
1
```

Remarquez qu'il n'y a pas de définition de classe ici. Les fonctions `up()` et `down()` manipulent une valeur partagée qui n'est ni une variable globale ni un attribut d'instance. Cette valeur est stockée dans la fermeture, ce qui la rend accessible uniquement aux fonctions retournées par `counter()`.

Voici un exemple de comment les fermetures peuvent être utilisées comme une structure de données. La variable enfermée `value` est maintenue entre les appels de fonction, et elle est privée pour les fonctions qui y accèdent. Cela signifie qu'aucune autre partie de votre code ne peut directement accéder ou modifier cette variable `value`, offrant ainsi un niveau de protection des données.
