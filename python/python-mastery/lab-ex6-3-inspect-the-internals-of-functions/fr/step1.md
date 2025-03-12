# Exploration des attributs de fonction

En Python, les fonctions sont considérées comme des objets de première classe. Que signifie cela ? Eh bien, c'est similaire à la façon dont vous avez différents types d'objets dans le monde réel, comme un livre ou un stylo. En Python, les fonctions sont également des objets, et tout comme les autres objets, elles ont leur propre ensemble d'attributs. Ces attributs peuvent nous fournir beaucoup d'informations utiles sur la fonction, comme son nom, où elle est définie et comment elle est implémentée.

Commençons notre exploration en ouvrant un shell interactif Python. Ce shell est comme une aire de jeu où nous pouvons écrire et exécuter du code Python immédiatement. Pour ce faire, nous allons d'abord naviguer jusqu'au répertoire du projet, puis démarrer l'interpréteur Python. Voici les commandes à exécuter dans votre terminal :

```bash
cd ~/project
python3
```

Maintenant que nous sommes dans le shell interactif Python, définissons une fonction simple. Cette fonction prendra deux nombres et les additionnera. Voici comment nous pouvons la définir :

```python
def add(x, y):
    'Adds two things'
    return x + y
```

Dans ce code, nous avons créé une fonction nommée `add`. Elle prend deux paramètres, `x` et `y`, et retourne leur somme. La chaîne de caractères `'Adds two things'` est appelée une docstring, qui est utilisée pour documenter ce que fait la fonction.

## Utilisation de dir() pour inspecter les attributs de fonction

En Python, la fonction `dir()` est un outil pratique. Elle peut être utilisée pour obtenir une liste de tous les attributs et méthodes qu'un objet possède. Utilisons-la pour voir quels attributs notre fonction `add` a. Exécutez le code suivant dans le shell interactif Python :

```python
dir(add)
```

Lorsque vous exécutez ce code, vous verrez une longue liste d'attributs. Voici un exemple de ce à quoi l'affichage pourrait ressembler :

```
['__annotations__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
```

Cette liste montre tous les attributs et méthodes associés à la fonction `add`.

## Accès aux informations de base sur la fonction

Maintenant, examinons de plus près certains des attributs de base des fonctions. Ces attributs peuvent nous indiquer des informations importantes sur la fonction. Exécutez le code suivant dans le shell interactif Python :

```python
print(add.__name__)
print(add.__module__)
print(add.__doc__)
```

Lorsque vous exécutez ce code, vous verrez le résultat suivant :

```
add
__main__
Adds two things
```

Comprenons ce que chaque attribut signifie :

- `__name__` : Cet attribut nous donne le nom de la fonction. Dans notre cas, la fonction s'appelle `add`.
- `__module__` : Il nous indique le module dans lequel la fonction est définie. Lorsque nous exécutons du code dans le shell interactif, le module est généralement `__main__`.
- `__doc__` : C'est la chaîne de documentation de la fonction, ou docstring. Elle fournit une brève description de ce que fait la fonction.

## Examen du code de la fonction

L'attribut `__code__` d'une fonction est très intéressant. Il contient des informations sur la façon dont la fonction est implémentée, y compris son bytecode et d'autres détails. Voyons ce que nous pouvons en apprendre. Exécutez le code suivant dans le shell interactif Python :

```python
print(add.__code__.co_varnames)
print(add.__code__.co_argcount)
```

Le résultat sera :

```
('x', 'y')
2
```

Voici ce que ces attributs nous indiquent :

- `co_varnames` : C'est un tuple qui contient les noms de toutes les variables locales utilisées par la fonction. Dans notre fonction `add`, les variables locales sont `x` et `y`.
- `co_argcount` : Cet attribut nous indique le nombre d'arguments que la fonction attend. Notre fonction `add` attend deux arguments, donc la valeur est 2.

Si vous êtes curieux de découvrir plus d'attributs de l'objet `__code__`, vous pouvez à nouveau utiliser la fonction `dir()`. Exécutez le code suivant :

```python
dir(add.__code__)
```

Cela affichera tous les attributs de l'objet code, qui contiennent des détails de bas niveau sur la façon dont la fonction est implémentée.
