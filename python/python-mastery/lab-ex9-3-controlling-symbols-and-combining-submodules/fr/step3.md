# Exporter tout depuis le package

En Python, l'organisation des packages est essentielle pour gérer efficacement le code. Maintenant, nous allons pousser notre organisation de package plus loin. Nous allons définir quels symboles doivent être exportés au niveau du package. Exporter des symboles signifie rendre certaines fonctions, classes ou variables disponibles pour d'autres parties de votre code ou pour d'autres développeurs qui pourraient utiliser votre package.

## Ajouter `__all__` au package

Lorsque vous travaillez avec des packages Python, vous pouvez vouloir contrôler quels symboles sont accessibles lorsque quelqu'un utilise l'instruction `from structly import *`. C'est là que la liste `__all__` s'avère utile. En ajoutant une liste `__all__` au fichier `__init__.py` du package, vous pouvez précisément contrôler quels symboles sont disponibles lorsque quelqu'un utilise l'instruction `from structly import *`.

Tout d'abord, créons ou mettons à jour le fichier `__init__.py`. Nous allons utiliser la commande `touch` pour créer le fichier s'il n'existe pas.

```bash
touch ~/project/structly/__init__.py
```

Maintenant, ouvrez le fichier `__init__.py` et ajoutez une liste `__all__`. Cette liste doit inclure tous les symboles que nous voulons exporter. Les symboles sont regroupés en fonction de leur origine, par exemple les modules `structure`, `reader` et `tableformat`.

```python
# structly/__init__.py

from .structure import *
from .reader import *
from .tableformat import *

# Define what symbols are exported when using "from structly import *"
__all__ = ['Structure',  # from structure
           'read_csv_as_instances', 'read_csv_as_dicts', 'read_csv_as_columns',  # from reader
           'create_formatter', 'print_table']  # from tableformat
```

Après avoir ajouté le code, enregistrez le fichier et quittez l'éditeur.

## Comprendre `import *`

Le modèle `from module import *` n'est généralement pas recommandé dans la plupart des codes Python. Voici plusieurs raisons à cela :

1. Il peut polluer votre espace de noms avec des symboles inattendus. Cela signifie que vous pourriez avoir des variables ou des fonctions dans votre espace de noms actuel que vous n'attendiez pas, ce qui peut entraîner des conflits de noms.
2. Il rend difficile de savoir d'où viennent les symboles particuliers. Lorsque vous utilisez `import *`, il est difficile de savoir de quel module un symbole provient, ce qui peut rendre votre code plus difficile à comprendre et à maintenir.
3. Il peut entraîner des problèmes d'ombre (shadowing). L'ombre se produit lorsqu'une variable ou une fonction locale a le même nom qu'une variable ou une fonction d'un autre module, ce qui peut entraîner un comportement inattendu.

Cependant, il y a des cas spécifiques où l'utilisation de `import *` est appropriée :

- Pour les packages conçus pour être utilisés comme un tout cohérent. Si un package est destiné à être utilisé comme une unité unique, alors l'utilisation de `import *` peut faciliter l'accès à tous les symboles nécessaires.
- Lorsqu'un package définit une interface claire via `__all__`. En utilisant la liste `__all__`, vous pouvez contrôler quels symboles sont exportés, ce qui rend plus sûr l'utilisation de `import *`.
- Pour une utilisation interactive, comme dans un REPL Python (Read-Eval-Print Loop). Dans un environnement interactif, il peut être pratique d'importer tous les symboles d'un coup.

## Tester avec Import \*

Pour vérifier que nous pouvons importer tous les symboles d'un coup, créons un autre fichier de test. Nous allons utiliser la commande `touch` pour créer le fichier.

```bash
touch ~/project/test_import_all.py
```

Maintenant, ouvrez le fichier `test_import_all.py` et ajoutez le contenu suivant. Ce code importe tous les symboles du package `structly` puis teste si certains des symboles importants sont disponibles.

```python
# Test importing everything at once

from structly import *

# Try using the imported symbols
print(f"Structure symbol is available: {Structure is not None}")
print(f"read_csv_as_instances symbol is available: {read_csv_as_instances is not None}")
print(f"create_formatter symbol is available: {create_formatter is not None}")
print(f"print_table symbol is available: {print_table is not None}")

print("All symbols successfully imported!")
```

Enregistrez le fichier et quittez l'éditeur. Maintenant, exécutons le test. Tout d'abord, naviguez jusqu'au répertoire du projet en utilisant la commande `cd`, puis exécutez le script Python.

```bash
cd ~/project
python test_import_all.py
```

Si tout est configuré correctement, vous devriez voir une confirmation que tous les symboles ont été importés avec succès.
