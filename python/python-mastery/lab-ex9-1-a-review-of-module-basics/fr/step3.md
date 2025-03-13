# Comprendre le comportement de chargement des modules

En Python, la manière dont les modules sont chargés présente certaines caractéristiques intéressantes. Dans cette étape, nous allons explorer ces comportements pour comprendre comment Python gère le chargement des modules.

1. Tout d'abord, voyons ce qui se passe lorsque nous essayons d'importer un module à nouveau au sein de la même session de l'interpréteur Python. Lorsque vous démarrez l'interpréteur Python, c'est comme ouvrir un espace de travail où vous pouvez exécuter du code Python. Une fois que vous avez importé un module, importer le même module à nouveau pourrait sembler recharger le module, mais ce n'est pas le cas.

```python
>>> import simplemod
```

Remarquez que cette fois, vous ne voyez pas le message "Loaded simplemod" s'afficher. C'est parce que **Python ne charge un module qu'une seule fois** par session de l'interpréteur. Les instructions `import` suivantes ne rechargent pas le module. Python se souvient qu'il a déjà chargé le module, donc il ne refait pas le processus de chargement.

2. Après avoir importé un module, vous pouvez modifier les variables à l'intérieur. Un module en Python est comme un conteneur qui contient des variables, des fonctions et des classes. Une fois que vous avez importé un module, vous pouvez accéder et modifier ses variables tout comme vous le feriez avec n'importe quel autre objet Python.

```python
>>> simplemod.x
42
>>> simplemod.x = 13
>>> simplemod.x
13
>>> simplemod.foo()
x is 13
```

Ici, nous vérifions d'abord la valeur de la variable `x` dans le module `simplemod`, qui est initialement `42`. Ensuite, nous changeons sa valeur en `13` et vérifions que le changement a été effectué. Lorsque nous appelons la fonction `foo` dans le module, elle reflète la nouvelle valeur de `x`.

3. Importer le module à nouveau ne réinitialise pas les modifications que nous avons apportées à ses variables. Même si nous essayons d'importer le module une fois de plus, Python ne le recharge pas, donc les modifications que nous avons apportées à ses variables persistent.

```python
>>> import simplemod
>>> simplemod.x
13
```

4. Si vous souhaitez forcer le rechargement d'un module, vous devez utiliser la fonction `importlib.reload()`. Parfois, vous avez peut - être apporté des modifications au code du module et vous souhaitez voir ces modifications prendre effet immédiatement. La fonction `importlib.reload()` vous permet de faire cela.

```python
>>> import importlib
>>> importlib.reload(simplemod)
Loaded simplemod
<module 'simplemod' from 'simplemod.py'>
>>> simplemod.x
42
>>> simplemod.foo()
x is 42
```

Le module a été rechargé, et la valeur de `x` a été réinitialisée à `42`. Cela montre que le module a été chargé à nouveau à partir de son code source, et toutes les variables ont été initialisées comme à l'origine.

5. Python garde une trace de tous les modules chargés dans le dictionnaire `sys.modules`. Ce dictionnaire agit comme un registre où Python stocke des informations sur tous les modules qui ont été chargés au cours de la session actuelle de l'interpréteur.

```python
>>> 'simplemod' in sys.modules
True
>>> sys.modules['simplemod']
<module 'simplemod' from 'simplemod.py'>
```

En vérifiant si le nom d'un module est dans le dictionnaire `sys.modules`, vous pouvez voir si le module a été chargé. Et en accédant au dictionnaire avec le nom du module comme clé, vous pouvez obtenir des informations sur le module.

6. Vous pouvez supprimer un module de ce dictionnaire pour forcer Python à le recharger lors de la prochaine importation. Si vous supprimez un module du dictionnaire `sys.modules`, Python oublie qu'il a déjà chargé le module. Donc, la prochaine fois que vous essayez de l'importer, Python le chargera à nouveau à partir de son code source.

```python
>>> del sys.modules['simplemod']
>>> import simplemod
Loaded simplemod
>>> simplemod.x
42
```

Le module a été rechargé car il a été supprimé de `sys.modules`. C'est une autre façon de vous assurer que vous travaillez avec la dernière version du code d'un module.
