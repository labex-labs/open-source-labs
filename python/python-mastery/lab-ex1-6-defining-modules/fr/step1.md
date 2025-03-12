# Comprendre les modules Python

En Python, un module est comme un conteneur qui contient des définitions et des instructions Python. Il s'agit essentiellement d'un fichier, et le nom de ce fichier est le nom du module avec l'extension `.py` ajoutée à la fin. Imaginez les modules comme des boîtes à outils. Ils vous aident à organiser votre code Python de manière logique, facilitant ainsi sa réutilisation et sa maintenance. Tout comme vous garderiez différents outils dans des boîtes séparées pour une meilleure organisation, vous pouvez regrouper le code Python lié dans différents modules.

Regardons les fichiers qui ont été préparés pour ce laboratoire (lab) :

1. Tout d'abord, nous allons ouvrir le fichier `stock.py` dans l'éditeur pour voir ce qu'il contient. Pour ce faire, nous allons utiliser les commandes suivantes. La commande `cd` change le répertoire pour le dossier `project` où se trouve notre fichier, et la commande `cat` affiche le contenu du fichier.

```bash
cd ~/project
cat stock.py
```

Ce fichier `stock.py` définit une classe `Stock`. Une classe est comme un modèle pour créer des objets. Dans ce cas, la classe `Stock` représente une action (stock). Elle a des attributs (qui sont comme des caractéristiques) pour le nom de l'action, le nombre de parts et le prix. Elle a également une méthode (qui est comme une fonction associée à la classe) pour calculer le coût de l'action.

2. Ensuite, examinons le fichier `pcost.py`. Nous allons à nouveau utiliser la commande `cat` pour afficher son contenu.

```bash
cat pcost.py
```

Ce fichier définit une fonction appelée `portfolio_cost()`. Une fonction est un bloc de code qui effectue une tâche spécifique. La fonction `portfolio_cost()` lit un fichier de portefeuille (portfolio) et calcule le coût total de toutes les actions dans ce portefeuille.

3. Maintenant, regardons les données d'échantillon de portefeuille. Nous allons utiliser la commande `cat` pour afficher le contenu du fichier `portfolio.dat`.

```bash
cat portfolio.dat
```

Ce fichier contient des données sur les actions dans un format simple. Chaque ligne a le symbole du ticker de l'action, le nombre de parts et le prix par part.

## Utilisation de l'instruction import

L'instruction `import` de Python est un outil puissant qui vous permet d'utiliser le code d'autres modules dans votre programme actuel. C'est comme emprunter des outils à d'autres boîtes à outils. Practiquons l'utilisation de différentes manières d'importer du code :

1. Tout d'abord, nous devons démarrer l'interpréteur Python. L'interpréteur Python est un programme qui exécute le code Python. Nous allons utiliser la commande suivante pour le démarrer.

```bash
python3
```

2. Maintenant, importons le module `pcost` et voyons ce qui se passe. Lorsque nous utilisons l'instruction `import`, Python cherche le fichier `pcost.py` et rend le code à l'intérieur disponible pour nous l'utiliser.

```python
import pcost
```

Vous devriez voir la sortie `44671.15`. C'est le coût calculé du portefeuille à partir du fichier `portfolio.dat`. Lorsque le module `pcost` est importé, le code en bas du fichier `pcost.py` s'exécute automatiquement.

3. Essayons d'appeler la fonction `portfolio_cost()` avec un autre fichier de portefeuille. Nous allons utiliser la syntaxe `pcost.portfolio_cost()` pour appeler la fonction du module `pcost`.

```python
pcost.portfolio_cost('portfolio2.dat')
```

La sortie devrait être `19908.75`, qui représente le coût total des actions dans le deuxième fichier de portefeuille.

4. Maintenant, importons une classe spécifique du module `stock`. Au lieu d'importer tout le module, nous pouvons simplement importer la classe `Stock` en utilisant l'instruction `from...import`.

```python
from stock import Stock
```

5. Après avoir importé la classe `Stock`, nous pouvons créer un objet `Stock`. Un objet est une instance d'une classe. Nous allons créer un objet `Stock` avec le nom `GOOG`, 100 parts et un prix de `490.10`. Ensuite, nous allons afficher le nom de l'action et calculer son coût en utilisant la méthode `cost()`.

```python
s = Stock('GOOG', 100, 490.10)
print(s.name)
print(s.cost())
```

La sortie devrait être :

```
GOOG
49010.0
```

6. Enfin, lorsque nous avons fini d'utiliser l'interpréteur Python, nous pouvons le quitter en utilisant la fonction `exit()`.

```python
exit()
```

Ce laboratoire (lab) a démontré deux manières différentes d'importer du code Python :

- `import module_name` - Cela importe tout le module, rendant toutes les fonctions, classes et variables de ce module disponibles pour utilisation.
- `from module_name import specific_item` - Cela importe seulement un élément spécifique (comme une classe ou une fonction) du module, ce qui peut être utile si vous n'avez besoin que d'une partie de la fonctionnalité du module.
