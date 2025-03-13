# Comprendre les packages Python

Avant de commencer à créer un package Python, comprenons ce qu'est un package Python. Un package Python est essentiellement un répertoire. À l'intérieur de ce répertoire, il y a plusieurs fichiers de modules Python, qui ne sont que des fichiers `.py` contenant du code Python. De plus, il y a un fichier spécial nommé `__init__.py`. Ce fichier peut être vide, mais sa présence indique que le répertoire est un package Python. Le but de cette structure est de vous aider à organiser le code lié dans une seule hiérarchie de répertoires.

Les packages offrent plusieurs avantages. Premièrement, ils vous permettent de structurer votre code de manière logique. Au lieu d'avoir tous vos fichiers Python éparpillés, vous pouvez regrouper les fonctionnalités liées dans un package. Deuxièmement, ils aident à éviter les conflits de noms entre les modules. Étant donné que les packages créent un espace de noms, vous pouvez avoir des modules avec le même nom dans différents packages sans aucun problème. Troisièmement, ils rendent l'importation et l'utilisation de votre code plus pratique. Vous pouvez importer un package entier ou des modules spécifiques de celui-ci facilement.

Maintenant, regardons les fichiers que nous avons actuellement dans notre répertoire de projet. Pour lister les fichiers, nous utiliserons la commande suivante dans le terminal :

```bash
ls -l
```

Lorsque vous exécutez cette commande, vous devriez voir les fichiers suivants :

```
portfolio.csv
reader.py
stock.py
structure.py
tableformat.py
validate.py
```

Ces fichiers Python sont tous liés et fonctionnent ensemble, mais actuellement, ils ne sont que des modules séparés. Dans ce laboratoire, notre objectif est de les organiser en un package cohérent appelé `structly`.

Comprenons brièvement ce que chaque fichier fait :

- `structure.py` : Ce fichier définit une classe de base `Structure` et divers descripteurs. Ces descripteurs sont utilisés pour la validation de type, ce qui signifie qu'ils aident à s'assurer que les données utilisées dans votre programme ont le bon type.
- `validate.py` : Il contient la fonctionnalité de validation utilisée par le module `structure`. Cela aide à valider les données selon certaines règles.
- `reader.py` : Ce fichier fournit des fonctions utilisées pour lire des données CSV. CSV (Comma-Separated Values, valeurs séparées par des virgules) est un format de fichier courant pour stocker des données tabulaires.
- `tableformat.py` : Il contient des classes et des fonctions utilisées pour formater les données en tableaux. Cela est utile lorsque vous souhaitez afficher les données de manière plus organisée.
- `stock.py` : Ce fichier utilise les autres modules pour définir une classe `Stock` et traiter les données d'actions. Il combine la fonctionnalité des autres modules pour effectuer des tâches spécifiques liées aux données d'actions.

À l'étape suivante, nous allons créer notre structure de package.
