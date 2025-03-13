# Division de modules pour une meilleure organisation du code

Au fur et à mesure que vos projets Python grandissent, vous pourriez constater qu'un seul fichier de module devient assez volumineux et contient plusieurs composants liés mais distincts. Lorsque cela se produit, il est recommandé de diviser le module en un package avec des sous-modules. Cette approche rend votre code plus organisé, plus facile à maintenir et plus évolutif.

## Comprendre la structure actuelle

Le module `tableformat.py` est un bon exemple d'un module volumineux. Il contient plusieurs classes de formateurs, chacune étant responsable du formatage des données d'une manière différente :

- `TableFormatter` (classe de base) : C'est la classe de base pour toutes les autres classes de formateurs. Elle définit la structure de base et les méthodes que les autres classes hériteront et implémenteront.
- `TextTableFormatter` : Cette classe formate les données en texte brut.
- `CSVTableFormatter` : Cette classe formate les données au format CSV (Comma-Separated Values, valeurs séparées par des virgules).
- `HTMLTableFormatter` : Cette classe formate les données au format HTML (Hypertext Markup Language, langage de balisage hypertexte).

Nous allons réorganiser ce module en une structure de package avec des fichiers séparés pour chaque type de formateur. Cela rendra le code plus modulaire et plus facile à gérer.

## Étape 1 : Nettoyer les fichiers de cache

Avant de commencer à réorganiser le code, il est préférable de nettoyer tous les fichiers de cache Python. Ces fichiers sont créés par Python pour accélérer l'exécution de votre code, mais ils peuvent parfois causer des problèmes lorsque vous apportez des modifications à votre code.

```bash
cd ~/project/structly
rm -rf __pycache__
```

Dans les commandes ci-dessus, `cd ~/project/structly` change le répertoire actuel pour le répertoire `structly` de votre projet. `rm -rf __pycache__` supprime le répertoire `__pycache__` et tout son contenu. L'option `-r` signifie récursif, ce qui signifie qu'elle supprimera tous les fichiers et sous-répertoires à l'intérieur du répertoire `__pycache__`. L'option `-f` signifie forcé, ce qui signifie qu'elle supprimera les fichiers sans demander de confirmation.

## Étape 2 : Créer la nouvelle structure de package

Maintenant, créons une nouvelle structure de répertoire pour notre package. Nous allons créer un répertoire nommé `tableformat` et un sous-répertoire nommé `formats` à l'intérieur.

```bash
mkdir -p tableformat/formats
```

La commande `mkdir` est utilisée pour créer des répertoires. L'option `-p` signifie parents, ce qui signifie qu'elle créera tous les répertoires parents nécessaires s'ils n'existent pas. Donc, si le répertoire `tableformat` n'existe pas, il sera créé en premier, puis le répertoire `formats` sera créé à l'intérieur.

## Étape 3 : Déplacer et renommer le fichier original

Ensuite, nous allons déplacer le fichier original `tableformat.py` dans la nouvelle structure et le renommer en `formatter.py`.

```bash
mv tableformat.py tableformat/formatter.py
```

La commande `mv` est utilisée pour déplacer ou renommer des fichiers. Dans ce cas, nous déplaçons le fichier `tableformat.py` dans le répertoire `tableformat` et le renommons en `formatter.py`.

## Étape 4 : Diviser le code en fichiers séparés

Maintenant, nous devons créer des fichiers pour chaque formateur et déplacer le code pertinent dans ceux-ci.

### 1. Créer le fichier du formateur de base

```bash
touch tableformat/formatter.py
```

La commande `touch` est utilisée pour créer un fichier vide. Dans ce cas, nous créons un fichier nommé `formatter.py` dans le répertoire `tableformat`.

Nous allons conserver la classe de base `TableFormatter` et toutes les fonctions utilitaires générales telles que `print_table` et `create_formatter` dans ce fichier. Le fichier devrait ressembler à ceci :

```python
# Base TableFormatter class and utility functions

__all__ = ['TableFormatter', 'print_table', 'create_formatter']

class TableFormatter:
    def headings(self, headers):
        '''
        Emit table headings.
        '''
        raise NotImplementedError()

    def row(self, rowdata):
        '''
        Emit a single row of table data.
        '''
        raise NotImplementedError()

def print_table(objects, columns, formatter):
    '''
    Make a nicely formatted table from a list of objects and attribute names.
    '''
    formatter.headings(columns)
    for obj in objects:
        rowdata = [getattr(obj, name) for name in columns]
        formatter.row(rowdata)

def create_formatter(fmt):
    '''
    Create an appropriate formatter given an output format name.
    '''
    if fmt == 'text':
        from .formats.text import TextTableFormatter
        return TextTableFormatter()
    elif fmt == 'csv':
        from .formats.csv import CSVTableFormatter
        return CSVTableFormatter()
    elif fmt == 'html':
        from .formats.html import HTMLTableFormatter
        return HTMLTableFormatter()
    else:
        raise ValueError(f'Unknown format {fmt}')
```

La variable `__all__` est utilisée pour spécifier quels symboles doivent être importés lorsque vous utilisez `from module import *`. Dans ce cas, nous spécifions que seuls les symboles `TableFormatter`, `print_table` et `create_formatter` doivent être importés.

La classe `TableFormatter` est la classe de base pour toutes les autres classes de formateurs. Elle définit deux méthodes, `headings` et `row`, qui sont destinées à être implémentées par les sous-classes.

La fonction `print_table` est une fonction utilitaire qui prend une liste d'objets, une liste de noms de colonnes et un objet formateur, et affiche les données dans un tableau formaté.

La fonction `create_formatter` est une fonction usine qui prend un nom de format en argument et renvoie un objet formateur approprié.

Enregistrez le fichier et quittez l'éditeur après avoir apporté ces modifications.

### 2. Créer le formateur de texte

```bash
touch tableformat/formats/text.py
```

Nous allons ajouter seulement la classe `TextTableFormatter` à ce fichier.

```python
# Text formatter implementation

__all__ = ['TextTableFormatter']

from ..formatter import TableFormatter

class TextTableFormatter(TableFormatter):
    '''
    Emit a table in plain-text format
    '''
    def headings(self, headers):
        print(' '.join('%10s' % h for h in headers))
        print(('-'*10 + ' ')*len(headers))

    def row(self, rowdata):
        print(' '.join('%10s' % d for d in rowdata))
```

La variable `__all__` spécifie que seul le symbole `TextTableFormatter` doit être importé lorsque vous utilisez `from module import *`.

L'instruction `from ..formatter import TableFormatter` importe la classe `TableFormatter` depuis le fichier `formatter.py` dans le répertoire parent.

La classe `TextTableFormatter` hérite de la classe `TableFormatter` et implémente les méthodes `headings` et `row` pour formater les données en texte brut.

Enregistrez le fichier et quittez l'éditeur après avoir apporté ces modifications.

### 3. Créer le formateur CSV

```bash
touch tableformat/formats/csv.py
```

Nous allons ajouter seulement la classe `CSVTableFormatter` à ce fichier.

```python
# CSV formatter implementation

__all__ = ['CSVTableFormatter']

from ..formatter import TableFormatter

class CSVTableFormatter(TableFormatter):
    '''
    Output data in CSV format.
    '''
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(str(d) for d in rowdata))
```

De même que dans les étapes précédentes, nous spécifions la variable `__all__`, importons la classe `TableFormatter` et implémentons les méthodes `headings` et `row` pour formater les données au format CSV.

Enregistrez le fichier et quittez l'éditeur après avoir apporté ces modifications.

### 4. Créer le formateur HTML

```bash
touch tableformat/formats/html.py
```

Nous allons ajouter seulement la classe `HTMLTableFormatter` à ce fichier.

```python
# HTML formatter implementation

__all__ = ['HTMLTableFormatter']

from ..formatter import TableFormatter

class HTMLTableFormatter(TableFormatter):
    '''
    Output data in HTML format.
    '''
    def headings(self, headers):
        print('<tr>', end='')
        for h in headers:
            print(f'<th>{h}</th>', end='')
        print('</tr>')

    def row(self, rowdata):
        print('<tr>', end='')
        for d in rowdata:
            print(f'<td>{d}</td>', end='')
        print('</tr>')
```

Encore une fois, nous spécifions la variable `__all__`, importons la classe `TableFormatter` et implémentons les méthodes `headings` et `row` pour formater les données au format HTML.

Enregistrez le fichier et quittez l'éditeur après avoir apporté ces modifications.

## Étape 5 : Créer les fichiers d'initialisation de package

En Python, les fichiers `__init__.py` sont utilisés pour marquer les répertoires comme des packages Python. Nous devons créer des fichiers `__init__.py` dans les répertoires `tableformat` et `formats`.

### 1. Créer un fichier pour le package `tableformat`

```bash
touch tableformat/__init__.py
```

Ajoutez ce contenu au fichier :

```python
# Re-export the original symbols from tableformat.py
from .formatter import *
```

Cette instruction importe tous les symboles depuis le fichier `formatter.py` et les rend disponibles lorsque vous importez le package `tableformat`.

Enregistrez le fichier et quittez l'éditeur après avoir apporté ces modifications.

### 2. Créer un fichier pour le package `formats`

```bash
touch tableformat/formats/__init__.py
```

Vous pouvez laisser ce fichier vide ou ajouter une simple chaîne de documentation (docstring) :

```python
'''
Format implementations for different output formats.
'''
```

La chaîne de documentation fournit une brève description de ce que fait le package `formats`.

Enregistrez le fichier et quittez l'éditeur après avoir apporté ces modifications.

## Étape 6 : Tester la nouvelle structure

Créons un test simple pour vérifier que nos modifications fonctionnent correctement.

```bash
cd ~/project
touch test_tableformat.py
```

Ajoutez ce contenu au fichier `test_tableformat.py` :

```python
# Test the tableformat package restructuring

from structly import *

# Create formatters of each type
text_fmt = create_formatter('text')
csv_fmt = create_formatter('csv')
html_fmt = create_formatter('html')

# Define some test data
class TestData:
    def __init__(self, name, value):
        self.name = name
        self.value = value

# Create a list of test objects
data = [
    TestData('apple', 10),
    TestData('banana', 20),
    TestData('cherry', 30)
]

# Test text formatter
print("\nText Format:")
print_table(data, ['name', 'value'], text_fmt)

# Test CSV formatter
print("\nCSV Format:")
print_table(data, ['name', 'value'], csv_fmt)

# Test HTML formatter
print("\nHTML Format:")
print_table(data, ['name', 'value'], html_fmt)
```

Ce code de test importe les fonctions et classes nécessaires depuis le package `structly`, crée des formateurs de chaque type, définit des données de test et teste chaque formateur en affichant les données dans le format correspondant.

Enregistrez le fichier et quittez l'éditeur après avoir apporté ces modifications. Maintenant, exécutez le test :

```bash
python test_tableformat.py
```

Vous devriez voir les mêmes données formatées de trois manières différentes (texte, CSV et HTML). Si vous voyez la sortie attendue, cela signifie que votre réorganisation de code a réussi.
