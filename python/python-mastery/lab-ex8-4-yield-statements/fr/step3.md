# Applications pratiques de la gestion des générateurs

Dans cette étape, nous allons explorer comment appliquer les concepts que nous avons appris sur la gestion des générateurs et la gestion des exceptions dans les générateurs à des scénarios du monde réel. Comprendre ces applications pratiques vous aidera à écrire un code Python plus robuste et plus efficace.

## Création d'un système de surveillance de fichiers robuste

Construisons une version plus fiable de notre système de surveillance de fichiers. Ce système sera capable de gérer différentes situations, telles que les délais d'attente (timeouts) et les demandes de l'utilisateur d'arrêter.

Tout d'abord, ouvrez l'éditeur WebIDE et créez un nouveau fichier nommé `robust_follow.py`. Voici le code que vous devez écrire dans ce fichier :

```python
import os
import time
import signal

class TimeoutError(Exception):
    pass

def timeout_handler(signum, frame):
    raise TimeoutError("Operation timed out")

def follow(filename, timeout=None):
    """
    A generator that yields new lines in a file.
    With timeout handling and proper cleanup.
    """
    try:
        # Set up timeout if specified
        if timeout:
            signal.signal(signal.SIGALRM, timeout_handler)
            signal.alarm(timeout)

        with open(filename, 'r') as f:
            f.seek(0, os.SEEK_END)
            while True:
                line = f.readline()
                if line == '':
                    # No new data, wait briefly
                    time.sleep(0.1)
                    continue
                yield line
    except TimeoutError:
        print(f"Following timed out after {timeout} seconds")
    except GeneratorExit:
        print("Following stopped by request")
    finally:
        # Clean up timeout alarm if it was set
        if timeout:
            signal.alarm(0)
        print("Follow generator cleanup complete")
```

Dans ce code, nous définissons d'abord une classe personnalisée `TimeoutError`. La fonction `timeout_handler` est utilisée pour lever cette erreur lorsqu'un délai d'attente expire. La fonction `follow` est un générateur qui lit un fichier et produit les nouvelles lignes. Si un délai d'attente est spécifié, il configure une alarme à l'aide du module `signal`. S'il n'y a pas de nouvelles données dans le fichier, il attend un court instant avant de réessayer. Le bloc `try - except - finally` est utilisé pour gérer différentes exceptions et garantir un nettoyage approprié.

Après avoir écrit le code, enregistrez le fichier.

## Expérimentation avec le système de surveillance de fichiers robuste

Maintenant, testons notre système de surveillance de fichiers amélioré. Ouvrez un terminal et lancez l'interpréteur Python avec les commandes suivantes :

```bash
cd ~/project
python3
```

### Expérience 1 : Utilisation de base

Dans l'interpréteur Python, nous allons tester la fonctionnalité de base de notre générateur `follow`. Voici le code à exécuter :

```python
>>> from robust_follow import follow
>>> f = follow('stocklog.csv')
>>> for i, line in enumerate(f):
...     print(f"Line {i+1}: {line.strip()}")
...     if i >= 2:  # Just read a few lines for the example
...         break
...
Line 1: "MO",70.29,"6/11/2007","09:30.09",-0.01,70.25,70.30,70.29,365314
Line 2: "VZ",42.91,"6/11/2007","09:34.28",-0.16,42.95,42.91,42.78,210151
Line 3: "HPQ",45.76,"6/11/2007","09:34.29",0.06,45.80,45.76,45.59,257169
```

Ici, nous importons la fonction `follow` de notre fichier `robust_follow.py`. Ensuite, nous créons un objet générateur `f` qui suit le fichier `stocklog.csv`. Nous utilisons une boucle `for` pour itérer sur les lignes produites par le générateur et afficher les trois premières lignes.

### Expérience 2 : Utilisation du délai d'attente

Voyons comment fonctionne la fonctionnalité de délai d'attente. Exécutez le code suivant dans l'interpréteur Python :

```python
>>> # Create a generator that will time out after 3 seconds
>>> f = follow('stocklog.csv', timeout=3)
>>> for line in f:
...     print(line.strip())
...     time.sleep(1)  # Process each line slowly
...
"MO",70.29,"6/11/2007","09:30.09",-0.01,70.25,70.30,70.29,365314
"VZ",42.91,"6/11/2007","09:34.28",-0.16,42.95,42.91,42.78,210151
"HPQ",45.76,"6/11/2007","09:34.29",0.06,45.80,45.76,45.59,257169
Following timed out after 3 seconds
Follow generator cleanup complete
```

Dans cette expérience, nous créons un générateur avec un délai d'attente de 3 secondes. Nous traitons chaque ligne lentement en attendant 1 seconde entre chaque ligne. Après environ 3 secondes, le générateur lève une exception de délai d'attente, et le code de nettoyage dans le bloc `finally` est exécuté.

### Expérience 3 : Fermeture explicite

Testons comment le générateur gère une fermeture explicite. Exécutez le code suivant :

```python
>>> f = follow('stocklog.csv')
>>> for i, line in enumerate(f):
...     print(f"Line {i+1}: {line.strip()}")
...     if i >= 1:
...         print("Explicitly closing the generator...")
...         f.close()
...
Line 1: "MO",70.29,"6/11/2007","09:30.09",-0.01,70.25,70.30,70.29,365314
Line 2: "VZ",42.91,"6/11/2007","09:34.28",-0.16,42.95,42.91,42.78,210151
Explicitly closing the generator...
Following stopped by request
Follow generator cleanup complete
```

Ici, nous créons un générateur et commençons à itérer sur ses lignes. Après avoir traité deux lignes, nous fermons explicitement le générateur en utilisant la méthode `close`. Le générateur gère ensuite l'exception `GeneratorExit` et effectue le nettoyage nécessaire.

## Création d'un pipeline de traitement de données avec gestion des erreurs

Ensuite, nous allons créer un simple pipeline de traitement de données en utilisant des coroutines. Ce pipeline sera capable de gérer les erreurs à différents stades.

Ouvrez l'éditeur WebIDE et créez un nouveau fichier nommé `pipeline.py`. Voici le code à écrire dans ce fichier :

```python
def consumer(func):
    def start(*args,**kwargs):
        c = func(*args,**kwargs)
        next(c)
        return c
    return start

@consumer
def grep(pattern, target):
    """Filter lines containing pattern and send to target"""
    try:
        while True:
            line = yield
            if pattern in line:
                target.send(line)
    except Exception as e:
        target.throw(e)

@consumer
def printer():
    """Print received items"""
    try:
        while True:
            item = yield
            print(f"PRINTER: {item}")
    except Exception as e:
        print(f"PRINTER ERROR: {repr(e)}")

def follow_and_process(filename, pattern):
    """Follow a file and process its contents"""
    import time
    import os

    output = printer()
    filter_pipe = grep(pattern, output)

    try:
        with open(filename, 'r') as f:
            f.seek(0, os.SEEK_END)
            while True:
                line = f.readline()
                if not line:
                    time.sleep(0.1)
                    continue
                filter_pipe.send(line)
    except KeyboardInterrupt:
        print("Processing stopped by user")
    finally:
        filter_pipe.close()
        output.close()
```

Dans ce code, le décorateur `consumer` est utilisé pour initialiser les coroutines. La coroutine `grep` filtre les lignes qui contiennent un motif spécifique et les envoie à une autre coroutine. La coroutine `printer` affiche les éléments reçus. La fonction `follow_and_process` lit un fichier, filtre ses lignes à l'aide de la coroutine `grep` et affiche les lignes correspondantes à l'aide de la coroutine `printer`. Elle gère également l'exception `KeyboardInterrupt` et garantit un nettoyage approprié.

Après avoir écrit le code, enregistrez le fichier.

## Test du pipeline de traitement de données

Testons notre pipeline de traitement de données. Dans un terminal, exécutez la commande suivante :

```bash
cd ~/project
python3 -c "from pipeline import follow_and_process; follow_and_process('stocklog.csv', 'IBM')"
```

Vous devriez voir une sortie similaire à ceci :

```
PRINTER: "IBM",102.86,"6/11/2007","09:34.44",-0.21,102.87,102.86,102.77,147550

PRINTER: "IBM",102.91,"6/11/2007","09:37.31",-0.16,102.87,102.91,102.77,190859

PRINTER: "IBM",102.95,"6/11/2007","09:39.44",-0.12,102.87,102.95,102.77,225350
```

Cette sortie montre que le pipeline fonctionne correctement, filtrant et affichant les lignes qui contiennent le motif "IBM".

Pour arrêter le processus, appuyez sur `Ctrl+C`. Vous devriez voir le message suivant :

```
Processing stopped by user
```

## Points clés

1. Une gestion appropriée des exceptions dans les générateurs vous permet de créer des systèmes robustes capables de gérer les erreurs de manière gracieuse. Cela signifie que vos programmes ne planteront pas de manière inattendue en cas de problème.
2. Vous pouvez utiliser des techniques telles que les délais d'attente pour empêcher les générateurs de s'exécuter indéfiniment. Cela aide à gérer les ressources système et garantit que votre programme ne reste pas bloqué dans une boucle infinie.
3. Les générateurs et les coroutines peuvent former des pipelines de traitement de données puissants où les erreurs peuvent être propagées et gérées au niveau approprié. Cela facilite la construction de systèmes de traitement de données complexes.
4. Le bloc `finally` dans les générateurs garantit que les opérations de nettoyage sont effectuées, quelle que soit la façon dont le générateur se termine. Cela aide à maintenir l'intégrité de votre programme et à éviter les fuites de ressources.
