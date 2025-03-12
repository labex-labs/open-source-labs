# Comprendre les exceptions en Python

Dans cette étape, nous allons apprendre à propos des exceptions en Python. Les exceptions sont un concept important en programmation. Elles nous aident à gérer les situations inattendues qui peuvent se produire lors de l'exécution d'un programme. Nous allons également comprendre pourquoi le code actuel plante lorsqu'il tente de traiter des données invalides. Comprendre cela vous aidera à écrire des programmes Python plus robustes et fiables.

## Qu'est-ce qu'une exception ?

En Python, les exceptions sont des événements qui se produisent lors de l'exécution d'un programme et qui perturbent le flux normal des instructions. Imaginez - le comme un obstacle sur une autoroute. Lorsque tout se passe bien, votre programme suit un chemin prédéfini, tout comme une voiture sur une route dégagée. Mais lorsqu'une erreur se produit, Python crée un objet exception. Cet objet est comme un rapport qui contient des informations sur ce qui a mal tourné, comme le type d'erreur et où elle s'est produite dans le code.

Si ces exceptions ne sont pas correctement gérées, elles font planter le programme. Lorsqu'un plantage se produit, Python affiche un message de trace (traceback message). Ce message est comme une carte qui vous montre l'emplacement exact dans le code où l'erreur s'est produite. C'est très utile pour le débogage.

## Examiner le code actuel

Regardons d'abord la structure du fichier `reader.py`. Ce fichier contient des fonctions utilisées pour lire et convertir des données CSV. Pour ouvrir le fichier dans l'éditeur, nous devons nous rendre dans le bon répertoire. Nous allons utiliser la commande `cd` dans le terminal.

```bash
cd /home/labex/project
```

Maintenant que nous sommes dans le bon répertoire, regardons le contenu de `reader.py`. Ce fichier a plusieurs fonctions importantes :

1. `convert_csv()` : Cette fonction prend des lignes de données et utilise une fonction de conversion fournie pour les convertir. C'est comme une machine qui prend des matières premières (les lignes de données) et les transforme en une autre forme selon une recette spécifique (la fonction de conversion).
2. `csv_as_dicts()` : Cette fonction lit des données CSV et les transforme en une liste de dictionnaires. Elle effectue également une conversion de type, ce qui signifie qu'elle s'assure que chaque élément de données dans le dictionnaire est du bon type, comme une chaîne de caractères, un entier ou un nombre à virgule flottante.
3. `read_csv_as_dicts()` : C'est une fonction d'enrobage (wrapper function). C'est comme un gestionnaire qui appelle la fonction `csv_as_dicts()` pour faire le travail.

## Mettre en évidence le problème

Voyons ce qui se passe lorsque le code tente de traiter des données invalides. Nous allons ouvrir un interpréteur Python, qui est comme un terrain de jeu où nous pouvons tester notre code Python de manière interactive. Pour ouvrir l'interpréteur Python, nous allons utiliser la commande suivante dans le terminal :

```bash
python3
```

Une fois l'interpréteur Python ouvert, nous allons essayer de lire le fichier `missing.csv`. Ce fichier contient des données manquantes ou invalides. Nous allons utiliser la fonction `read_csv_as_dicts()` du fichier `reader.py` pour lire les données.

```python
from reader import read_csv_as_dicts
port = read_csv_as_dicts('missing.csv', types=[str, int, float])
```

Lorsque vous exécutez ce code, vous devriez voir un message d'erreur comme celui - ci :

```
Traceback (most recent call last):
  ...
ValueError: invalid literal for int() with base 10: ''
```

Cette erreur se produit parce que le code tente de convertir une chaîne de caractères vide en entier. Une chaîne de caractères vide ne représente pas un entier valide, donc Python ne peut pas effectuer la conversion. La fonction plante dès la première erreur qu'elle rencontre, et elle arrête le traitement du reste des données valides dans le fichier.

Pour quitter l'interpréteur Python, tapez la commande suivante :

```python
exit()
```

## Comprendre le flux des erreurs

L'erreur se produit dans la fonction `convert_csv()`, plus précisément à la ligne suivante :

```python
return list(map(lambda row: converter(headers, row), rows))
```

La fonction `map()` applique la fonction `converter` à chaque ligne de la liste `rows`. La fonction `converter` tente d'appliquer les types (str, int, float) à chaque ligne. Mais lorsqu'elle rencontre une ligne avec des données manquantes, elle échoue. La fonction `map()` n'a pas de moyen intégré pour gérer les exceptions. Donc, lorsqu'une exception se produit, tout le processus plante.

Dans l'étape suivante, vous allez modifier le code pour gérer ces exceptions de manière élégante. Cela signifie que au lieu de planter, le programme sera capable de gérer les erreurs et de continuer à traiter le reste des données.
