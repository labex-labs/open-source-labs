# Importation et utilisation de modules

Maintenant que nous avons créé un module, il est temps de comprendre comment l'importer et utiliser ses composants. En Python, un module est un fichier contenant des définitions et des instructions Python. Lorsque vous importez un module, vous avez accès à toutes les fonctions, classes et variables définies à l'intérieur. Cela vous permet de réutiliser le code et d'organiser vos programmes plus efficacement.

1. Tout d'abord, nous devons ouvrir un nouveau terminal dans le WebIDE. Ce terminal servira de workspace où nous pouvons exécuter des commandes Python. Pour ouvrir un nouveau terminal, cliquez sur "Terminal" > "New Terminal".

2. Une fois le terminal ouvert, nous devons démarrer l'interpréteur Python. L'interpréteur Python est un programme qui lit et exécute le code Python. Pour le démarrer, tapez la commande suivante dans le terminal et appuyez sur Entrée :

```bash
python3
```

3. Maintenant que l'interpréteur Python est en cours d'exécution, nous pouvons importer notre module. En Python, nous utilisons l'instruction `import` pour inclure un module dans notre programme actuel. Tapez la commande suivante dans l'interpréteur Python :

```python
>>> import simplemod
Loaded simplemod
```

Vous remarquerez que "Loaded simplemod" apparaît dans la sortie. C'est parce que l'instruction `print` dans notre module `simplemod` s'exécute lorsque le module est chargé. Lorsque Python importe un module, il exécute tout le code de niveau supérieur dans ce module, y compris les instructions `print`.

4. Après avoir importé le module, nous pouvons accéder à ses composants en utilisant la notation pointée. La notation pointée est un moyen d'accéder aux attributs (variables et fonctions) d'un objet en Python. Dans ce cas, le module est un objet, et ses fonctions, variables et classes sont ses attributs. Voici quelques exemples de comment accéder à différents composants du module `simplemod` :

```python
>>> simplemod.x
42
>>> simplemod.foo()
x is 42
>>> spam_instance = simplemod.Spam()
>>> spam_instance.yow()
Yow!
```

Dans la première ligne, nous accédons à la variable `x` définie dans le module `simplemod`. Dans la deuxième ligne, nous appelons la fonction `foo` du module `simplemod`. Dans la troisième et la quatrième lignes, nous créons une instance de la classe `Spam` définie dans le module `simplemod` et appelons sa méthode `yow`.

5. Parfois, vous pourriez rencontrer une erreur `ImportError` lorsque vous essayez d'importer un module. Cette erreur se produit lorsque Python ne peut pas trouver le module que vous essayez d'importer. Pour savoir où Python cherche les modules, vous pouvez examiner la variable `sys.path`. La variable `sys.path` est une liste de répertoires que Python recherche lorsqu'il cherche des modules. Tapez les commandes suivantes dans l'interpréteur Python :

```python
>>> import sys
>>> sys.path
['', '/usr/lib/python310.zip', '/usr/lib/python3.10', '/usr/lib/python3.10/lib-dynload', '/usr/local/lib/python3.10/dist-packages', '/usr/lib/python3/dist-packages']
```

Le premier élément de la liste (la chaîne vide) représente le répertoire de travail actuel. C'est là que Python cherche le fichier `simplemod.py`. Si votre module n'est pas dans l'un des répertoires répertoriés dans `sys.path`, Python ne pourra pas le trouver, et vous obtiendrez une erreur `ImportError`. Assurez - vous que votre fichier `simplemod.py` se trouve dans le répertoire de travail actuel ou dans l'un des autres répertoires de `sys.path`.
