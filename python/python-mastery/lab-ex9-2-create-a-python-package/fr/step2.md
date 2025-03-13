# Création de la structure du package

Maintenant, nous allons créer notre package Python. Mais d'abord, comprenons ce qu'est un package Python. Un package Python est un moyen d'organiser des modules Python liés dans une seule hiérarchie de répertoires. Cela aide à gérer et à réutiliser le code plus efficacement. Pour créer un package Python, nous devons suivre ces étapes :

1. Créer un répertoire portant le nom du package. Ce répertoire servira de conteneur pour tous les modules appartenant au package.
2. Créer un fichier `__init__.py` à l'intérieur de ce répertoire. Ce fichier est crucial car il permet à Python de reconnaître le répertoire comme un package. Lorsque vous importez le package, le code dans `__init__.py` est exécuté, ce qui peut être utilisé pour initialiser le package.
3. Déplacer nos fichiers de modules Python dans ce répertoire. Cette étape garantit que tout le code lié est regroupé au sein du package.

Créons la structure du package étape par étape :

1. Tout d'abord, créez un répertoire appelé `structly`. Ce sera le répertoire racine de notre package.

```bash
mkdir structly
```

2. Ensuite, créez un fichier `__init__.py` vide à l'intérieur du répertoire `structly`.

```bash
touch structly/__init__.py
```

Le fichier `__init__.py` peut être vide, mais il est nécessaire pour que Python traite le répertoire comme un package. Lorsque vous importez le package, le code dans `__init__.py` est exécuté, ce qui peut être utilisé pour initialiser le package.

3. Maintenant, déplaçons nos fichiers de modules Python dans le répertoire `structly`. Ces fichiers de modules contiennent les fonctions et les classes que nous souhaitons inclure dans notre package.

```bash
mv structure.py validate.py reader.py tableformat.py structly/
```

4. Vérifions que tous les fichiers ont été déplacés correctement. Nous pouvons utiliser la commande `ls -l` pour lister le contenu du répertoire `structly`.

```bash
ls -l structly/
```

Vous devriez voir les fichiers suivants listés :

```
__init__.py
reader.py
structure.py
tableformat.py
validate.py
```

Maintenant, nous avons créé une structure de package de base. La hiérarchie des répertoires devrait ressembler à ceci :

```
project/
├── portfolio.csv
├── stock.py
└── structly/
    ├── __init__.py
    ├── reader.py
    ├── structure.py
    ├── tableformat.py
    └── validate.py
```

À l'étape suivante, nous allons corriger les instructions d'importation pour que le package fonctionne correctement.
