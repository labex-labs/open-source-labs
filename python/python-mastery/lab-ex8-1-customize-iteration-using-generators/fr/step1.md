# Comprendre les générateurs Python

Les générateurs sont une fonctionnalité puissante en Python. Ils offrent un moyen simple et élégant de créer des itérateurs. En Python, lorsque vous manipulez des séquences de données, les itérateurs sont très utiles car ils vous permettent de parcourir une série de valeurs une par une. Les fonctions ordinaires retournent généralement une seule valeur puis cessent d'exécuter. Cependant, les générateurs sont différents. Ils peuvent produire une séquence de valeurs au fil du temps, ce qui signifie qu'ils peuvent générer plusieurs valeurs de manière progressive.

## Qu'est - ce qu'un générateur ?

Une fonction générateur ressemble à une fonction ordinaire. Mais la différence clé réside dans la façon dont elle retourne des valeurs. Au lieu d'utiliser l'instruction `return` pour fournir un seul résultat, une fonction générateur utilise l'instruction `yield`. L'instruction `yield` est spéciale. Chaque fois qu'elle est exécutée, l'état de la fonction est mis en pause, et la valeur qui suit le mot - clé `yield` est retournée à l'appelant. Lorsque la fonction générateur est appelée à nouveau, elle reprend son exécution là où elle s'était arrêtée.

Commençons par créer une simple fonction générateur. La fonction intégrée `range()` en Python ne prend pas en charge les pas fractionnaires. Nous allons donc créer une fonction générateur qui peut produire une plage de nombres avec un pas fractionnaire.

1. Tout d'abord, vous devez ouvrir un nouveau terminal Python dans le WebIDE. Pour ce faire, cliquez sur le menu "Terminal", puis sélectionnez "New Terminal".
2. Une fois le terminal ouvert, tapez le code suivant dans le terminal. Ce code définit une fonction générateur puis la teste.

```python
def frange(start, stop, step):
    current = start
    while current < stop:
        yield current
        current += step

# Test the generator with a for loop
for x in frange(0, 2, 0.25):
    print(x, end=' ')
```

Dans ce code, la fonction `frange` est une fonction générateur. Elle initialise une variable `current` avec la valeur `start`. Ensuite, tant que `current` est inférieur à la valeur `stop`, elle produit la valeur `current` puis incrémente `current` de la valeur `step`. La boucle `for` parcourt ensuite les valeurs produites par la fonction générateur `frange` et les affiche.

Vous devriez voir la sortie suivante :

```
0 0.25 0.5 0.75 1.0 1.25 1.5 1.75
```

## La nature à usage unique des générateurs

Une caractéristique importante des générateurs est qu'ils sont épuisables. Cela signifie qu'une fois que vous avez parcouru toutes les valeurs produites par un générateur, il ne peut plus être utilisé pour produire la même séquence de valeurs. Illustrons cela avec le code suivant :

```python
# Create a generator object
f = frange(0, 2, 0.25)

# First iteration works fine
print("First iteration:")
for x in f:
    print(x, end=' ')
print("\n")

# Second iteration produces nothing
print("Second iteration:")
for x in f:
    print(x, end=' ')
print("\n")
```

Dans ce code, nous créons tout d'abord un objet générateur `f` en utilisant la fonction `frange`. La première boucle `for` parcourt toutes les valeurs produites par le générateur et les affiche. Après la première itération, le générateur a été épuisé, ce qui signifie qu'il a déjà produit toutes les valeurs qu'il peut. Ainsi, lorsque nous essayons de le parcourir à nouveau dans la deuxième boucle `for`, il ne produit aucune nouvelle valeur.

Sortie :

```
First iteration:
0 0.25 0.5 0.75 1.0 1.25 1.5 1.75

Second iteration:

```

Notez que la deuxième itération n'a produit aucune sortie car le générateur était déjà épuisé.

## Création de générateurs réutilisables avec des classes

Si vous avez besoin de parcourir plusieurs fois la même séquence de valeurs, vous pouvez encapsuler le générateur dans une classe. En faisant cela, chaque fois que vous commencez une nouvelle itération, un nouveau générateur sera créé.

```python
class FRange:
    def __init__(self, start, stop, step):
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        n = self.start
        while n < self.stop:
            yield n
            n += self.step

# Create an instance
f = FRange(0, 2, 0.25)

# We can iterate multiple times
print("First iteration:")
for x in f:
    print(x, end=' ')
print("\n")

print("Second iteration:")
for x in f:
    print(x, end=' ')
print("\n")
```

Dans ce code, nous définissons une classe `FRange`. La méthode `__init__` initialise les valeurs `start`, `stop` et `step`. La méthode `__iter__` est une méthode spéciale dans les classes Python. Elle est utilisée pour créer un itérateur. À l'intérieur de la méthode `__iter__`, nous avons un générateur qui produit des valeurs de la même manière que la fonction `frange` que nous avons définie précédemment.

Lorsque nous créons une instance `f` de la classe `FRange` et que nous la parcourons plusieurs fois, chaque itération appelle la méthode `__iter__`, qui crée un nouveau générateur. Ainsi, nous pouvons obtenir la même séquence de valeurs plusieurs fois.

Sortie :

```
First iteration:
0 0.25 0.5 0.75 1.0 1.25 1.5 1.75

Second iteration:
0 0.25 0.5 0.75 1.0 1.25 1.5 1.75
```

Cette fois - ci, nous pouvons parcourir plusieurs fois car la méthode `__iter__()` crée un nouveau générateur chaque fois qu'elle est appelée.
