# Création d'un gestionnaire de contexte

Un gestionnaire de contexte est un type spécial d'objet en Python. En Python, les objets peuvent avoir différentes méthodes qui définissent leur comportement. Un gestionnaire de contexte définit spécifiquement deux méthodes importantes : `__enter__` et `__exit__`. Ces méthodes fonctionnent en conjonction avec l'instruction `with`. L'instruction `with` est utilisée pour configurer un contexte spécifique pour un bloc de code. Imaginez cela comme la création d'un petit environnement où certaines choses se produisent, et lorsque le bloc de code est terminé, le gestionnaire de contexte s'occupe du nettoyage.

Dans cette étape, nous allons créer un gestionnaire de contexte qui a une fonction très utile. Il redirigera temporairement la sortie standard (`sys.stdout`). La sortie standard est là où la sortie normale de votre programme Python va, généralement la console. En la redirigeant, nous pouvons envoyer la sortie dans un fichier à la place. Cela est pratique lorsque vous voulez enregistrer la sortie qui serait autrement simplement affichée sur la console.

Tout d'abord, nous devons créer un nouveau fichier pour écrire le code de notre gestionnaire de contexte. Nous nommerons ce fichier `redirect.py`. Vous pouvez le créer en utilisant la commande suivante dans le terminal :

```bash
touch /home/labex/project/redirect.py
```

Maintenant que le fichier est créé, ouvrez-le dans un éditeur. Une fois qu'il est ouvert, ajoutez le code Python suivant au fichier :

```python
import sys

class redirect_stdout:
    def __init__(self, out_file):
        self.out_file = out_file

    def __enter__(self):
        self.stdout = sys.stdout
        sys.stdout = self.out_file
        return self.out_file

    def __exit__(self, ty, val, tb):
        sys.stdout = self.stdout
```

Analysons ce que fait ce gestionnaire de contexte :

1. `__init__` : C'est la méthode d'initialisation. Lorsque nous créons une instance de la classe `redirect_stdout`, nous passons un objet fichier. Cette méthode stocke cet objet fichier dans la variable d'instance `self.out_file`. Ainsi, elle se souvient où nous voulons rediriger la sortie.
2. `__enter__` :
   - Tout d'abord, elle sauvegarde le `sys.stdout` actuel. Cela est important car nous devons le restaurer plus tard.
   - Ensuite, elle remplace le `sys.stdout` actuel par notre objet fichier. À partir de ce moment, toute sortie qui irait normalement à la console ira dans le fichier à la place.
   - Enfin, elle retourne l'objet fichier. Cela est utile car nous pourrions vouloir utiliser l'objet fichier à l'intérieur du bloc `with`.
3. `__exit__` :
   - Cette méthode restaure le `sys.stdout` original. Ainsi, après que le bloc `with` est terminé, la sortie reviendra normalement à la console.
   - Elle prend trois paramètres : le type d'exception (`ty`), la valeur de l'exception (`val`) et la trace d'exécution (`tb`). Ces paramètres sont requis par le protocole du gestionnaire de contexte. Ils sont utilisés pour gérer les exceptions qui pourraient se produire à l'intérieur du bloc `with`.

Maintenant, testons notre gestionnaire de contexte. Nous l'utiliserons pour rediriger la sortie d'un tableau dans un fichier. Tout d'abord, lancez l'interpréteur Python :

```bash
python3
```

Ensuite, exécutez le code Python suivant dans l'interpréteur :

```python
>>> import stock, reader, tableformat
>>> from redirect import redirect_stdout
>>> portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
>>> formatter = tableformat.create_formatter('text')
>>> with redirect_stdout(open('out.txt', 'w')) as file:
...     tableformat.print_table(portfolio, ['name','shares','price'], formatter)
...     file.close()
...
>>> # Let's check the content of the output file
>>> print(open('out.txt').read())
      name     shares      price
---------- ---------- ----------
        AA        100       32.2
       IBM         50       91.1
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50       65.1
       IBM        100      70.44
```

Parfait ! Notre gestionnaire de contexte a fonctionné comme prévu. Il a redirigé avec succès la sortie du tableau dans le fichier `out.txt`.

Les gestionnaires de contexte sont une fonctionnalité très puissante en Python. Ils vous aident à gérer correctement les ressources. Voici quelques cas d'utilisation courants pour les gestionnaires de contexte :

- Opérations sur les fichiers : Lorsque vous ouvrez un fichier, un gestionnaire de contexte peut s'assurer que le fichier est correctement fermé, même si une erreur se produit.
- Connexions à la base de données : Il peut garantir que la connexion à la base de données est fermée une fois que vous avez fini de l'utiliser.
- Verrous dans les programmes multithreadés : Les gestionnaires de contexte peuvent gérer le verrouillage et le déverrouillage des ressources de manière sûre.
- Changement temporaire des paramètres de l'environnement : Vous pouvez changer certains paramètres pour un bloc de code puis les restaurer automatiquement.

Ce modèle est très important car il garantit que les ressources sont correctement nettoyées, même si une exception se produit à l'intérieur du bloc `with`.

Une fois que vous avez terminé les tests, vous pouvez quitter l'interpréteur Python :

```python
>>> exit()
```
