# Exploration de l'inspection des cadres de pile (stack frames)

L'approche `_init(locals())` que nous avons utilisée est fonctionnelle, mais elle présente un inconvénient. Chaque fois que nous définissons une méthode `__init__`, nous devons explicitement appeler `locals()`. Cela peut devenir un peu fastidieux, surtout lorsqu'on travaille avec plusieurs classes. Heureusement, nous pouvons rendre notre code plus propre et plus efficace en utilisant l'inspection des cadres de pile. Cette technique nous permet d'accéder automatiquement aux variables locales de l'appelant sans avoir à appeler `locals()` explicitement.

Commençons à explorer cette technique dans l'interpréteur Python. Tout d'abord, ouvrez votre terminal et accédez au répertoire du projet. Ensuite, lancez l'interpréteur Python. Vous pouvez le faire en exécutant les commandes suivantes :

```bash
cd ~/project
python3
```

Maintenant que nous sommes dans l'interpréteur Python, nous devons importer le module `sys`. Le module `sys` permet d'accéder à certaines variables utilisées ou maintenues par l'interpréteur Python. Nous l'utiliserons pour accéder aux informations sur le cadre de pile.

```python
import sys
```

Ensuite, nous allons définir une version améliorée de notre fonction `_init()`. Cette nouvelle version accédera directement au cadre de l'appelant, éliminant ainsi le besoin de passer `locals()` explicitement.

```python
def _init():
    # Get the caller's frame (1 level up in the call stack)
    frame = sys._getframe(1)

    # Get the local variables from that frame
    locs = frame.f_locals

    # Extract self and set other variables as attributes
    self = locs.pop('self')
    for name, val in locs.items():
        setattr(self, name, val)
```

Dans ce code, `sys._getframe(1)` récupère l'objet cadre de la fonction appelante. L'argument `1` signifie que nous regardons un niveau plus haut dans la pile d'appels. Une fois que nous avons l'objet cadre, nous pouvons accéder à ses variables locales en utilisant `frame.f_locals`. Cela nous donne un dictionnaire de toutes les variables locales dans la portée de l'appelant. Nous extrayons ensuite la variable `self` et définissons les variables restantes comme des attributs de l'objet `self`.

Maintenant, testons cette nouvelle fonction `_init()` avec une nouvelle version de notre classe `Stock`.

```python
class Stock:
    def __init__(self, name, shares, price):
        _init()  # No need to pass locals() anymore!

# Test it
s = Stock('GOOG', 100, 490.1)
print(s.name, s.shares, s.price)

# Also works with keyword arguments
s = Stock(name='AAPL', shares=50, price=125.3)
print(s.name, s.shares, s.price)
```

Comme vous pouvez le voir, la méthode `__init__` n'a plus besoin de passer `locals()` explicitement. Cela rend notre code plus propre et plus facile à lire du point de vue de l'appelant.

### Fonctionnement de l'inspection des cadres de pile

Lorsque vous appelez `sys._getframe(1)`, Python renvoie l'objet cadre représentant le cadre d'exécution de l'appelant. L'argument `1` signifie "un niveau au - dessus du cadre actuel" (la fonction appelante).

Un objet cadre contient des informations importantes sur le contexte d'exécution. Cela inclut la fonction actuellement exécutée, les variables locales dans cette fonction et le numéro de ligne actuellement exécutée.

En accédant à `frame.f_locals`, nous obtenons un dictionnaire de toutes les variables locales dans la portée de l'appelant. C'est similaire à ce que `locals()` renverrait si appelé directement depuis cette portée.

Cette technique est assez puissante, mais elle doit être utilisée avec prudence. Elle est généralement considérée comme une fonctionnalité avancée de Python et peut sembler un peu "magique" car elle dépasse les limites normales de portée de Python.

Une fois que vous avez terminé vos expériences avec l'inspection des cadres de pile, vous pouvez quitter l'interpréteur Python en exécutant la commande suivante :

```python
exit()
```
