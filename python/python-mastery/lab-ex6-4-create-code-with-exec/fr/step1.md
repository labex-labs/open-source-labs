# Comprendre les bases de exec()

En Python, la fonction `exec()` est un outil puissant qui vous permet d'exécuter du code créé dynamiquement à l'exécution. Cela signifie que vous pouvez générer du code à la volée en fonction de certaines entrées ou configurations, ce qui est extrêmement utile dans de nombreux scénarios de programmation.

Commençons par explorer l'utilisation de base de la fonction `exec()`. Pour ce faire, nous allons ouvrir un shell Python. Ouvrez votre terminal et tapez `python3`. Cette commande lancera l'interpréteur Python interactif, où vous pouvez exécuter directement du code Python.

```bash
python3
```

Maintenant, nous allons définir un morceau de code Python sous forme de chaîne de caractères, puis utiliser la fonction `exec()` pour l'exécuter. Voici comment cela fonctionne :

```python
>>> code = '''
for i in range(n):
    print(i, end=' ')
'''
>>> n = 10
>>> exec(code)
0 1 2 3 4 5 6 7 8 9
```

Dans cet exemple :

1. Tout d'abord, nous avons défini une chaîne de caractères nommée `code`. Cette chaîne contient une boucle `for` Python. La boucle est conçue pour itérer `n` fois et afficher chaque numéro d'itération.
2. Ensuite, nous avons défini une variable `n` et lui avons assigné la valeur 10. Cette variable est utilisée comme borne supérieure pour la fonction `range()` dans notre boucle.
3. Après cela, nous avons appelé la fonction `exec()` avec la chaîne `code` comme argument. La fonction `exec()` prend la chaîne et l'exécute comme code Python.
4. Enfin, la boucle s'est exécutée et a affiché les nombres de 0 à 9.

Le véritable potentiel de la fonction `exec()` devient plus évident lorsque nous l'utilisons pour créer des structures de code plus complexes, telles que des fonctions ou des méthodes. Essayons un exemple plus avancé où nous allons créer dynamiquement une méthode `__init__()` pour une classe.

```python
>>> class Stock:
...     _fields = ('name', 'shares', 'price')
...
>>> argstr = ','.join(Stock._fields)
>>> code = f'def __init__(self, {argstr}):\n'
>>> for name in Stock._fields:
...     code += f'    self.{name} = {name}\n'
...
>>> print(code)
def __init__(self, name,shares,price):
    self.name = name
    self.shares = shares
    self.price = price

>>> locs = { }
>>> exec(code, locs)
>>> Stock.__init__ = locs['__init__']

>>> # Now try the class
>>> s = Stock('GOOG', 100, 490.1)
>>> s.name
'GOOG'
>>> s.shares
100
>>> s.price
490.1
```

Dans cet exemple plus complexe :

1. Nous avons d'abord défini une classe `Stock` avec un attribut `_fields`. Cet attribut est un tuple qui contient les noms des attributs de la classe.
2. Ensuite, nous avons créé une chaîne qui représente le code Python pour une méthode `__init__`. Cette méthode est utilisée pour initialiser les attributs de l'objet.
3. Ensuite, nous avons utilisé la fonction `exec()` pour exécuter la chaîne de code. Nous avons également passé un dictionnaire vide `locs` à `exec()`. La fonction résultante de l'exécution est stockée dans ce dictionnaire.
4. Après cela, nous avons assigné la fonction stockée dans le dictionnaire comme méthode `__init__` de notre classe `Stock`.
5. Enfin, nous avons créé une instance de la classe `Stock` et vérifié que la méthode `__init__` fonctionne correctement en accédant aux attributs de l'objet.

Cet exemple montre comment la fonction `exec()` peut être utilisée pour créer dynamiquement des méthodes en fonction de données disponibles à l'exécution.
