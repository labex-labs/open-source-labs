# Contrôler les symboles exportés avec `__all__`

En Python, lorsque vous utilisez l'instruction `from module import *`, vous pouvez vouloir contrôler quels symboles (fonctions, classes, variables) sont importés depuis un module. C'est là que la variable `__all__` s'avère utile. L'instruction `from module import *` est un moyen d'importer tous les symboles d'un module dans l'espace de noms actuel. Cependant, parfois, vous ne voulez pas importer chaque symbole, surtout s'il y en a beaucoup ou si certains sont destinés à être internes au module. La variable `__all__` vous permet de spécifier exactement quels symboles doivent être importés lorsque vous utilisez cette instruction.

## Qu'est-ce que `__all__`?

La variable `__all__` est une liste de chaînes de caractères. Chaque chaîne de caractères dans cette liste représente un symbole (fonction, classe ou variable) que le module exporte lorsque quelqu'un utilise l'instruction `from module import *`. Si la variable `__all__` n'est pas définie dans un module, l'instruction `import *` importera tous les symboles qui ne commencent pas par un tiret bas. Les symboles commençant par un tiret bas sont généralement considérés comme privés ou internes au module et ne sont pas destinés à être importés directement.

## Modifier chaque sous-module

Maintenant, ajoutons la variable `__all__` à chaque sous-module du package `structly`. Cela nous aidera à contrôler quels symboles sont exportés depuis chaque sous-module lorsque quelqu'un utilise l'instruction `from module import *`.

1. Tout d'abord, modifions `structure.py` :

```bash
touch ~/project/structly/structure.py
```

Cette commande crée un nouveau fichier nommé `structure.py` dans le répertoire `structly` de votre projet. Après avoir créé le fichier, nous devons ajouter la variable `__all__`. Ajoutez cette ligne tout en haut du fichier, juste après les instructions d'importation :

```python
__all__ = ['Structure']
```

Cette ligne indique à Python que lorsque quelqu'un utilise `from structure import *`, seul le symbole `Structure` sera importé. Enregistrez le fichier et quittez l'éditeur.

2. Ensuite, modifions `reader.py` :

```bash
touch ~/project/structly/reader.py
```

Cette commande crée un nouveau fichier nommé `reader.py` dans le répertoire `structly`. Maintenant, parcourez le fichier pour trouver toutes les fonctions qui commencent par `read_csv_as_`. Ce sont ces fonctions que nous voulons exporter. Ensuite, ajoutez une liste `__all__` avec tous les noms de ces fonctions. Elle devrait ressembler à ceci :

```python
__all__ = ['read_csv_as_instances', 'read_csv_as_dicts', 'read_csv_as_columns']
```

Notez que les noms réels des fonctions peuvent varier en fonction de ce que vous trouvez dans le fichier. Assurez-vous d'inclure toutes les fonctions `read_csv_as_*` que vous trouvez. Enregistrez le fichier et quittez l'éditeur.

3. Maintenant, modifions `tableformat.py` :

```bash
touch ~/project/structly/tableformat.py
```

Cette commande crée un nouveau fichier nommé `tableformat.py` dans le répertoire `structly`. Ajoutez cette ligne tout en haut du fichier :

```python
__all__ = ['create_formatter', 'print_table']
```

Cette ligne spécifie que lorsque quelqu'un utilise `from tableformat import *`, seuls les symboles `create_formatter` et `print_table` seront importés. Enregistrez le fichier et quittez l'éditeur.

## Importations unifiées dans `__init__.py`

Maintenant que chaque module définit ce qu'il exporte, nous pouvons mettre à jour le fichier `__init__.py` pour importer tous ces symboles. Le fichier `__init__.py` est un fichier spécial dans les packages Python. Il est exécuté lorsque le package est importé, et il peut être utilisé pour initialiser le package et importer des symboles depuis les sous-modules.

```bash
touch ~/project/structly/__init__.py
```

Cette commande crée un nouveau fichier `__init__.py` dans le répertoire `structly`. Modifiez le contenu du fichier comme suit :

```python
# structly/__init__.py

from .structure import *
from .reader import *
from .tableformat import *
```

Ces lignes importent tous les symboles exportés depuis les sous-modules `structure`, `reader` et `tableformat`. Le point (`.`) avant les noms des modules indique que ce sont des importations relatives, c'est-à-dire des importations depuis le même package. Enregistrez le fichier et quittez l'éditeur.

## Tester nos modifications

Créons un fichier de test simple pour vérifier que nos modifications fonctionnent. Ce fichier de test tentera d'importer les symboles que nous avons spécifiés dans les variables `__all__` et affichera un message de réussite si les importations sont réussies.

```bash
touch ~/project/test_structly.py
```

Cette commande crée un nouveau fichier nommé `test_structly.py` dans le répertoire du projet. Ajoutez ce contenu au fichier :

```python
# A simple test to verify our imports work correctly

from structly import Structure
from structly import read_csv_as_instances
from structly import create_formatter, print_table

print("Successfully imported all required symbols!")
```

Ces lignes tentent d'importer la classe `Structure`, la fonction `read_csv_as_instances` et les fonctions `create_formatter` et `print_table` depuis le package `structly`. Si les importations sont réussies, le programme affichera le message "Successfully imported all required symbols!". Enregistrez le fichier et quittez l'éditeur. Maintenant, exécutons ce test :

```bash
cd ~/project
python test_structly.py
```

La commande `cd ~/project` change le répertoire de travail actuel pour le répertoire du projet. La commande `python test_structly.py` exécute le script `test_structly.py`. Si tout fonctionne correctement, vous devriez voir le message "Successfully imported all required symbols!" affiché à l'écran.
