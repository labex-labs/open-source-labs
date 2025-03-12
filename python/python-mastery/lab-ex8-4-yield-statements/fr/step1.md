# Comprendre la durée de vie et la fermeture des générateurs

Dans cette étape, nous allons explorer la durée de vie des générateurs Python et apprendre à les fermer correctement. Les générateurs en Python sont un type spécial d'itérateur qui vous permet de générer une séquence de valeurs à la volée, plutôt que de les calculer toutes d'un coup et de les stocker en mémoire. Cela peut être très utile lorsqu'il s'agit de traiter de grands ensembles de données ou des séquences infinies.

## Qu'est-ce que le générateur `follow()` ?

Commençons par regarder le fichier `follow.py` dans le répertoire du projet. Ce fichier contient une fonction générateur appelée `follow()`. Une fonction générateur est définie comme une fonction normale, mais au lieu d'utiliser le mot-clé `return`, elle utilise `yield`. Lorsqu'une fonction générateur est appelée, elle retourne un objet générateur, sur lequel vous pouvez itérer pour obtenir les valeurs qu'elle produit.

La fonction générateur `follow()` lit en continu les lignes d'un fichier et produit chaque ligne au fur et à mesure qu'elle est lue. Cela est similaire à la commande Unix `tail -f`, qui surveille en continu un fichier pour les nouvelles lignes.

Ouvrez le fichier `follow.py` dans l'éditeur WebIDE :

```python
import os
import time

def follow(filename):
    with open(filename,'r') as f:
        f.seek(0,os.SEEK_END)
        while True:
            line = f.readline()
            if line == '':
                time.sleep(0.1)    # Sleep briefly to avoid busy wait
                continue
            yield line
```

Dans ce code, l'instruction `with open(filename, 'r') as f` ouvre le fichier en mode lecture et s'assure qu'il est correctement fermé lorsque le bloc est quitté. La ligne `f.seek(0, os.SEEK_END)` déplace le pointeur de fichier à la fin du fichier, de sorte que le générateur commence à lire à partir de la fin. La boucle `while True` lit en continu les lignes du fichier. Si la ligne est vide, cela signifie qu'il n'y a pas encore de nouvelles lignes, donc le programme dort pendant 0,1 seconde pour éviter une attente active puis passe à l'itération suivante. Si la ligne n'est pas vide, elle est produite.

Ce générateur s'exécute dans une boucle infinie, ce qui soulève une question importante : que se passe-t-il lorsque nous arrêtons d'utiliser le générateur ou que nous voulons le terminer avant la fin ?

## Modifier le générateur pour gérer la fermeture

Nous devons modifier la fonction `follow()` dans `follow.py` pour gérer le cas où le générateur est correctement fermé. Pour ce faire, nous allons ajouter un bloc `try-except` qui intercepte l'exception `GeneratorExit`. L'exception `GeneratorExit` est levée lorsqu'un générateur est fermé, soit par la collecte de mémoire inutilisée (garbage collection) soit en appelant la méthode `close()`.

```python
import os
import time

def follow(filename):
    try:
        with open(filename,'r') as f:
            f.seek(0,os.SEEK_END)
            while True:
                line = f.readline()
                if line == '':
                    time.sleep(0.1)    # Sleep briefly to avoid busy wait
                    continue
                yield line
    except GeneratorExit:
        print('Following Done')
```

Dans ce code modifié, le bloc `try` contient la logique principale du générateur. Si une exception `GeneratorExit` est levée, le bloc `except` l'intercepte et affiche le message 'Following Done'. C'est une façon simple d'effectuer des actions de nettoyage lorsque le générateur est fermé.

Enregistrez le fichier après avoir apporté ces modifications.

## Expérimenter la fermeture des générateurs

Maintenant, effectuons quelques expériences pour voir comment les générateurs se comportent lorsqu'ils sont collectés par le ramasse-miettes ou fermés explicitement.

Ouvrez un terminal et lancez l'interpréteur Python :

```bash
cd ~/project
python3
```

### Expérience 1 : Collecte de mémoire inutilisée d'un générateur en cours d'exécution

```python
>>> from follow import follow
>>> # Experiment: Garbage collection of a running generator
>>> f = follow('stocklog.csv')
>>> next(f)
'"MO",70.29,"6/11/2007","09:30.09",-0.01,70.25,70.30,70.29,365314\n'
>>> del f  # Delete the generator object
Following Done  # This message appears because of our GeneratorExit handler
```

Dans cette expérience, nous importons d'abord la fonction `follow` du fichier `follow.py`. Ensuite, nous créons un objet générateur `f` en appelant `follow('stocklog.csv')`. Nous utilisons la fonction `next()` pour obtenir la prochaine ligne du générateur. Enfin, nous supprimons l'objet générateur à l'aide de l'instruction `del`. Lorsque l'objet générateur est supprimé, il est automatiquement fermé, ce qui déclenche notre gestionnaire d'exception `GeneratorExit`, et le message 'Following Done' est affiché.

### Expérience 2 : Fermeture explicite d'un générateur

```python
>>> f = follow('stocklog.csv')
>>> for line in f:
...     print(line, end='')
...     if 'IBM' in line:
...         f.close()  # Explicitly close the generator
...
"MO",70.29,"6/11/2007","09:30.09",-0.01,70.25,70.30,70.29,365314
"VZ",42.91,"6/11/2007","09:34.28",-0.16,42.95,42.91,42.78,210151
"HPQ",45.76,"6/11/2007","09:34.29",0.06,45.80,45.76,45.59,257169
"GM",31.45,"6/11/2007","09:34.31",0.45,31.00,31.50,31.45,582429
"IBM",102.86,"6/11/2007","09:34.44",-0.21,102.87,102.86,102.77,147550
Following Done
>>> for line in f:
...     print(line, end='')  # No output: generator is closed
...
```

Dans cette expérience, nous créons un nouvel objet générateur `f` et nous itérons sur lui à l'aide d'une boucle `for`. À l'intérieur de la boucle, nous affichons chaque ligne et vérifions si la ligne contient la chaîne 'IBM'. Si c'est le cas, nous appelons la méthode `close()` sur le générateur pour le fermer explicitement. Lorsque le générateur est fermé, l'exception `GeneratorExit` est levée, et notre gestionnaire d'exception affiche le message 'Following Done'. Après que le générateur est fermé, si nous essayons d'itérer à nouveau sur lui, il n'y aura pas de sortie car le générateur n'est plus actif.

### Expérience 3 : Sortie et reprise d'un générateur

```python
>>> f = follow('stocklog.csv')
>>> for line in f:
...     print(line, end='')
...     if 'IBM' in line:
...         break  # Break out of the loop, but don't close the generator
...
"MO",70.29,"6/11/2007","09:30.09",-0.01,70.25,70.30,70.29,365314
"VZ",42.91,"6/11/2007","09:34.28",-0.16,42.95,42.91,42.78,210151
"HPQ",45.76,"6/11/2007","09:34.29",0.06,45.80,45.76,45.59,257169
"GM",31.45,"6/11/2007","09:34.31",0.45,31.00,31.50,31.45,582429
"IBM",102.86,"6/11/2007","09:34.44",-0.21,102.87,102.86,102.77,147550
>>> # Resume iteration - the generator is still active
>>> for line in f:
...     print(line, end='')
...     if 'IBM' in line:
...         break
...
"CAT",78.36,"6/11/2007","09:37.19",-0.16,78.32,78.36,77.99,237714
"VZ",42.99,"6/11/2007","09:37.20",-0.08,42.95,42.99,42.78,268459
"IBM",102.91,"6/11/2007","09:37.31",-0.16,102.87,102.91,102.77,190859
>>> del f  # Clean up
Following Done
```

Dans cette expérience, nous créons un objet générateur `f` et nous itérons sur lui à l'aide d'une boucle `for`. À l'intérieur de la boucle, nous affichons chaque ligne et vérifions si la ligne contient la chaîne 'IBM'. Si c'est le cas, nous utilisons l'instruction `break` pour sortir de la boucle. Sortir de la boucle ne ferme pas le générateur, donc le générateur est toujours actif. Nous pouvons ensuite reprendre l'itération en démarrant une nouvelle boucle `for` sur le même objet générateur. Enfin, nous supprimons l'objet générateur pour nettoyer, ce qui déclenche le gestionnaire d'exception `GeneratorExit`.

## Points clés

1. Lorsqu'un générateur est fermé (soit par la collecte de mémoire inutilisée soit en appelant `close()`), une exception `GeneratorExit` est levée à l'intérieur du générateur.
2. Vous pouvez intercepter cette exception pour effectuer des actions de nettoyage lorsque le générateur est fermé.
3. Sortir de l'itération d'un générateur (avec `break`) ne ferme pas le générateur, ce qui permet de le reprendre plus tard.

Quittez l'interpréteur Python en tapant `exit()` ou en appuyant sur `Ctrl+D`.
