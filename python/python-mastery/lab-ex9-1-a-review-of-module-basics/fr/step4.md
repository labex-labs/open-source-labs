# Utilisation de la syntaxe from module import

En Python, il existe diverses manières d'importer des composants à partir de modules. L'une de ces manières est la syntaxe `from module import`, que nous allons explorer dans cette section.

Lorsque vous importez des composants à partir d'un module, il est souvent judicieux de commencer avec un environnement propre. Cela garantit qu'il n'y a pas de variables ou de paramètres laissés de côtés par des interactions précédentes qui pourraient interférer avec notre expérience actuelle.

1. Redémarrez l'interpréteur Python pour obtenir un environnement propre :

```python
>>> exit()
```

Cette commande quitte la session actuelle de l'interpréteur Python. Après avoir quitté, nous allons démarrer une nouvelle session pour garantir un environnement neuf.

```bash
python3
```

Cette commande bash démarre une nouvelle session de l'interpréteur Python 3. Maintenant que nous avons un environnement Python propre, nous pouvons commencer à importer des composants à partir d'un module.

2. Importez des composants spécifiques d'un module en utilisant la syntaxe `from module import` :

```python
>>> from simplemod import foo
Loaded simplemod
>>> foo()
x is 42
```

Ici, nous utilisons l'instruction `from simplemod import foo` pour importer uniquement la fonction `foo` du module `simplemod`. Remarquez que même si nous n'avons demandé que la fonction `foo`, le module `simplemod` entier a été chargé. Cela est indiqué par le message "Loaded simplemod". La raison en est que Python doit charger tout le module pour accéder à la fonction `foo`.

3. Lorsque vous utilisez `from module import`, vous ne pouvez pas accéder au module lui - même :

```python
>>> simplemod.foo()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'simplemod' is not defined
```

Lorsque nous utilisons la syntaxe `from module import`, nous n'introduisons que les composants spécifiés directement dans notre espace de noms. Le nom du module lui - même n'est pas importé. Donc, lorsque nous essayons d'accéder à `simplemod.foo()`, Python ne reconnaît pas `simplemod` car il n'a pas été importé de cette manière.

4. Vous pouvez importer plusieurs composants à la fois :

```python
>>> from simplemod import x, foo
>>> x
42
>>> foo()
x is 42
```

La syntaxe `from module import` nous permet d'importer plusieurs composants d'un module en une seule instruction. Ici, nous importons à la fois la variable `x` et la fonction `foo` du module `simplemod`. Après l'importation, nous pouvons accéder directement à ces composants dans notre code.

5. Lorsque vous importez une variable à partir d'un module, vous créez une nouvelle référence à l'objet, pas un lien vers la variable dans le module :

```python
>>> x = 13  # Change the local variable x
>>> x
13
>>> foo()
x is 42  # The function still uses the module's x, not your local x
```

Lorsque nous importons une variable à partir d'un module, nous créons essentiellement une nouvelle référence au même objet dans notre espace de noms local. Donc, lorsque nous changeons la variable locale `x` en `13`, cela n'affecte pas la variable `x` à l'intérieur du module `simplemod`. La fonction `foo()` fait toujours référence à la variable `x` du module, qui est `42`. Comprendre ce concept est crucial pour éviter les confusions dans votre code.
