# Comprendre les coroutines avec un suivi de fichier

Commençons par comprendre ce que sont les coroutines et comment elles fonctionnent en Python. Une coroutine est une version spécialisée d'une fonction génératrice. En Python, les fonctions commencent généralement au début chaque fois qu'elles sont appelées. Mais les coroutines sont différentes. Elles peuvent à la fois consommer et produire des données, et elles ont la capacité de suspendre et de reprendre leur exécution. Cela signifie qu'une coroutine peut suspendre son opération à un certain moment puis reprendre exactement là où elle s'était arrêtée plus tard.

## Création d'un suivi de fichier de base utilisant les coroutines

Dans cette étape, nous allons créer un suivi de fichier qui utilise les coroutines pour surveiller un fichier à la recherche de nouveau contenu et le traiter. Cela est similaire à la commande Unix `tail -f`, qui affiche en continu la fin d'un fichier et se met à jour à mesure que de nouvelles lignes sont ajoutées.

1. Ouvrez l'éditeur de code et créez un nouveau fichier nommé `cofollow.py` dans le répertoire `/home/labex/project`. C'est là que nous allons écrire notre code Python pour implémenter le suivi de fichier en utilisant les coroutines.

2. Copiez le code suivant dans le fichier :

```python
# cofollow.py
import os
import time

# Data source
def follow(filename, target):
    with open(filename, 'r') as f:
        f.seek(0, os.SEEK_END)  # Move to the end of the file
        while True:
            line = f.readline()
            if line != '':
                target.send(line)  # Send the line to the target coroutine
            else:
                time.sleep(0.1)  # Sleep briefly if no new content

# Decorator for coroutine functions
from functools import wraps

def consumer(func):
    @wraps(func)
    def start(*args, **kwargs):
        f = func(*args, **kwargs)
        f.send(None)  # Prime the coroutine (necessary first step)
        return f
    return start

# Sample coroutine
@consumer
def printer():
    while True:
        item = yield     # Receive an item sent to me
        print(item)

# Example use
if __name__ == '__main__':
    follow('stocklog.csv', printer())
```

3. Comprenons les éléments clés de ce code :
   - `follow(filename, target)` : Cette fonction est chargée d'ouvrir un fichier. Elle déplace d'abord le pointeur de fichier à la fin du fichier en utilisant `f.seek(0, os.SEEK_END)`. Ensuite, elle entre dans une boucle infinie où elle essaie continuellement de lire de nouvelles lignes dans le fichier. Si une nouvelle ligne est trouvée, elle envoie cette ligne à la coroutine cible en utilisant la méthode `send`. S'il n'y a pas de nouveau contenu, elle s'arrête brièvement (0,1 seconde) en utilisant `time.sleep(0.1)` avant de vérifier à nouveau.
   - Décorateur `@consumer` : En Python, les coroutines doivent être « amorcées » avant de pouvoir commencer à recevoir des données. Ce décorateur s'en charge. Il envoie automatiquement une valeur initiale `None` à la coroutine, ce qui est une étape nécessaire pour préparer la coroutine à recevoir des données réelles.
   - Coroutine `printer()` : Il s'agit d'une simple coroutine. Elle a une boucle infinie où elle utilise le mot-clé `yield` pour recevoir un élément qui lui est envoyé. Une fois qu'elle reçoit un élément, elle le affiche simplement.

4. Enregistrez le fichier et exécutez-le depuis le terminal :

```bash
cd /home/labex/project
python3 cofollow.py
```

5. Vous devriez voir le script afficher le contenu du fichier de journal des actions, et il continuera d'afficher les nouvelles lignes à mesure qu'elles sont ajoutées au fichier. Appuyez sur `Ctrl+C` pour arrêter le programme.

Le concept clé ici est que les données circulent de la fonction `follow` vers la coroutine `printer` via la méthode `send`. Cette « poussée » de données est l'opposé des générateurs, qui « tirent » les données par itération. Dans un générateur, vous utilisez généralement une boucle `for` pour itérer sur les valeurs qu'il produit. Mais dans cet exemple de coroutine, les données sont activement envoyées d'une partie du code à une autre.
