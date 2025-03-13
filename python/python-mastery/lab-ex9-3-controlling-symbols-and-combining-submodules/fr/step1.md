# Comprendre la complexité des importations de packages

Lorsque vous commencez à travailler avec des packages Python, vous réaliserez rapidement que l'importation de modules peut devenir assez compliquée et verbeuse. Cette complexité peut rendre votre code plus difficile à lire et à écrire. Dans ce laboratoire (lab), nous allons examiner de près ce problème et apprendre à simplifier le processus d'importation.

## Structure d'importation actuelle

Tout d'abord, ouvrons le terminal. Le terminal est un outil puissant qui vous permet d'interagir avec le système d'exploitation de votre ordinateur. Une fois le terminal ouvert, nous devons nous déplacer vers le répertoire du projet. Le répertoire du projet est l'endroit où tous les fichiers liés à notre projet Python sont stockés. Pour ce faire, nous allons utiliser la commande `cd`, qui signifie "change directory" (changer de répertoire).

```bash
cd ~/project
```

Maintenant que nous sommes dans le répertoire du projet, examinons la structure actuelle du package `structly`. Un package en Python est un moyen d'organiser des modules liés. Nous pouvons utiliser la commande `ls -la` pour lister tous les fichiers et répertoires à l'intérieur du package `structly`, y compris les fichiers cachés.

```bash
ls -la structly
```

Vous remarquerez qu'il y a plusieurs modules Python à l'intérieur du package `structly`. Ces modules contiennent des fonctions et des classes que nous pouvons utiliser dans notre code. Cependant, si nous voulons utiliser la fonctionnalité de ces modules, nous devons actuellement utiliser de longues instructions d'importation. Par exemple :

```python
from structly.structure import Structure
from structly.reader import read_csv_as_instances
from structly.tableformat import create_formatter, print_table
```

Ces longs chemins d'importation peuvent être fastidieux à écrire, surtout si vous devez les utiliser plusieurs fois dans votre code. Ils rendent également votre code moins lisible, ce qui peut être un problème lorsque vous essayez de comprendre ou de déboguer votre code. Dans ce laboratoire (lab), nous allons apprendre à organiser le package de manière à simplifier ces importations.

Commençons par regarder le contenu du fichier `__init__.py` du package. Le fichier `__init__.py` est un fichier spécial dans les packages Python. Il est exécuté lorsque le package est importé, et il peut être utilisé pour initialiser le package et configurer les importations nécessaires.

```bash
cat structly/__init__.py
```

Il est probable que vous constatiez que le fichier `__init__.py` est soit vide, soit contient très peu de code. Dans les prochaines étapes, nous allons modifier ce fichier pour simplifier nos instructions d'importation.

## L'objectif

À la fin de ce laboratoire (lab), notre objectif est d'être en mesure d'utiliser des instructions d'importation beaucoup plus simples. Au lieu des longs chemins d'importation que nous avons vus précédemment, nous serons en mesure d'utiliser des instructions telles que :

```python
from structly import Structure, read_csv_as_instances, create_formatter, print_table
```

Ou même :

```python
from structly import *
```

L'utilisation de ces instructions d'importation plus simples rendra notre code plus propre et plus facile à manipuler. Cela nous fera également gagner du temps et des efforts lors de l'écriture et de la maintenance de notre code.
