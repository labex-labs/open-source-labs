# Créer votre premier décorateur

## Qu'est-ce qu'un décorateur ?

En Python, les décorateurs (decorators) sont une syntaxe spéciale qui peut être très utile pour les débutants. Ils vous permettent de modifier le comportement des fonctions ou des méthodes. Imaginez un décorateur comme une fonction qui prend une autre fonction en entrée. Elle retourne ensuite une nouvelle fonction. Cette nouvelle fonction étend souvent ou modifie le comportement de la fonction originale.

Les décorateurs sont appliqués en utilisant le symbole `@`. Vous placez ce symbole suivi du nom du décorateur directement au-dessus de la définition d'une fonction. C'est un moyen simple de dire à Python que vous voulez utiliser le décorateur sur cette fonction particulière.

## Créer un simple décorateur de journalisation

Créons un simple décorateur qui enregistre des informations lorsqu'une fonction est appelée. La journalisation (logging) est une tâche courante dans les applications du monde réel, et utiliser un décorateur pour cela est un excellent moyen de comprendre le fonctionnement des décorateurs.

1. Tout d'abord, ouvrez l'éditeur VSCode. Dans le répertoire `/home/labex/project`, créez un nouveau fichier nommé `logcall.py`. Ce fichier contiendra notre fonction de décorateur.

2. Ajoutez le code suivant à `logcall.py` :

```python
# logcall.py

def logged(func):
    print('Adding logging to', func.__name__)
    def wrapper(*args, **kwargs):
        print('Calling', func.__name__)
        return func(*args, **kwargs)
    return wrapper
```

Analysons ce que fait ce code :

- La fonction `logged` est notre décorateur. Elle prend une autre fonction, que nous appelons `func`, en argument. Cette fonction `func` est celle à laquelle nous voulons ajouter la journalisation.
- Lorsque le décorateur est appliqué à une fonction, il affiche un message. Ce message nous indique que la journalisation est ajoutée à la fonction du nom donné.
- À l'intérieur de la fonction `logged`, nous définissons une fonction interne appelée `wrapper`. Cette fonction `wrapper` remplacera la fonction originale.
  - Lorsque la fonction décorée est appelée, la fonction `wrapper` affiche un message indiquant que la fonction est en cours d'appel.
  - Elle appelle ensuite la fonction originale (`func`) avec tous les arguments qui lui ont été passés. Les `*args` et `**kwargs` sont utilisés pour accepter n'importe quel nombre d'arguments positionnels et de mots-clés.
  - Enfin, elle retourne le résultat de la fonction originale.
- La fonction `logged` retourne la fonction `wrapper`. Cette fonction `wrapper` sera maintenant utilisée à la place de la fonction originale, ajoutant ainsi la fonctionnalité de journalisation.

## Utilisation du décorateur

3. Maintenant, dans le même répertoire (`/home/labex/project`), créez un autre fichier nommé `sample.py` avec le code suivant :

```python
# sample.py

from logcall import logged

@logged
def add(x, y):
    return x + y

@logged
def sub(x, y):
    return x - y
```

La syntaxe `@logged` est très importante ici. Elle indique à Python d'appliquer le décorateur `logged` aux fonctions `add` et `sub`. Ainsi, chaque fois que ces fonctions sont appelées, la fonctionnalité de journalisation ajoutée par le décorateur sera exécutée.

## Test du décorateur

4. Pour tester votre décorateur, ouvrez un terminal dans VSCode. Tout d'abord, changez de répertoire pour le répertoire du projet en utilisant la commande suivante :

```bash
cd /home/labex/project
```

Ensuite, lancez l'interpréteur Python :

```bash
python3
```

5. Dans l'interpréteur Python, importez le module `sample` et testez les fonctions décorées :

```python
>>> import sample
Adding logging to add
Adding logging to sub
>>> sample.add(3, 4)
Calling add
7
>>> sample.sub(2, 3)
Calling sub
-1
>>> exit()
```

Notez que lorsque vous importez le module `sample`, les messages "Adding logging to..." sont affichés. Cela est dû au fait que le décorateur est appliqué lorsque le module est importé. Chaque fois que vous appelez l'une des fonctions décorées, le message "Calling..." est affiché. Cela montre que le décorateur fonctionne comme prévu.

Ce simple décorateur démontre le concept de base des décorateurs. Il enveloppe la fonction originale avec une fonctionnalité supplémentaire (la journalisation dans ce cas) sans modifier le code de la fonction originale. C'est une fonctionnalité puissante en Python que vous pouvez utiliser dans de nombreux scénarios différents.
