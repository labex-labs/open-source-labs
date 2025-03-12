# Travailler avec les objets `Future` pour la programmation concurrente

En Python, lorsque vous avez besoin d'exécuter des fonctions en même temps, c'est-à-dire de manière concurrente, le langage propose des outils utiles tels que les threads et les processus. Mais vous allez vous heurter à un problème courant : comment obtenir la valeur retournée par une fonction qui s'exécute dans un autre thread ? C'est là que le concept de `Future` devient très important.

Un objet `Future` est comme un placeholder pour un résultat qui sera disponible ultérieurement. C'est un moyen de représenter une valeur que produira une fonction à l'avenir, même avant que la fonction n'ait terminé son exécution. Comprenons mieux ce concept grâce à un exemple simple.

### Étape 1 : Créer un nouveau fichier

Tout d'abord, vous devez créer un nouveau fichier Python. Nous l'appellerons `futures_demo.py`. Vous pouvez utiliser la commande suivante dans votre terminal pour créer ce fichier :

```
touch ~/project/futures_demo.py
```

### Étape 2 : Ajouter le code de base de la fonction

Maintenant, ouvrez le fichier `futures_demo.py` et ajoutez le code Python suivant. Ce code définit une fonction simple et montre comment fonctionne un appel de fonction normal.

```python
import time
import threading
from concurrent.futures import Future, ThreadPoolExecutor

def worker(x, y):
    """A function that takes time to complete"""
    print('Starting work...')
    time.sleep(5)  # Simulate a time-consuming task
    print('Work completed')
    return x + y

# Part 1: Normal function call
print("--- Part 1: Normal function call ---")
result = worker(2, 3)
print(f"Result: {result}")
```

Dans ce code, la fonction `worker` prend deux nombres, les additionne, mais simule d'abord une tâche longue en suspendant son exécution pendant 5 secondes. Lorsque vous appelez cette fonction de manière normale, le programme attend que la fonction se termine avant d'obtenir la valeur de retour.

### Étape 3 : Exécuter le code de base

Enregistrez le fichier et exécutez - le en utilisant la commande suivante dans votre terminal :

```
python ~/project/futures_demo.py
```

Vous devriez voir une sortie similaire à ceci :

```
--- Part 1: Normal function call ---
Starting work...
Work completed
Result: 5
```

Cela montre qu'un appel de fonction normal attend que la fonction se termine avant de retourner le résultat.

### Étape 4 : Exécuter la fonction dans un thread séparé

Ensuite, voyons ce qui se passe lorsque nous exécutons la fonction `worker` dans un thread séparé. Ajoutez le code suivant au fichier `futures_demo.py` :

```python
# Part 2: Running in a separate thread (problem: no way to get result)
print("\n--- Part 2: Running in a separate thread ---")
t = threading.Thread(target=worker, args=(2, 3))
t.start()
print("Main thread continues while worker runs...")
t.join()  # Wait for the thread to complete
print("Worker thread finished, but we don't have its return value!")
```

Ici, nous utilisons la classe `threading.Thread` pour démarrer la fonction `worker` dans un nouveau thread. Le thread principal ne attend pas que la fonction `worker` se termine et continue son exécution. Cependant, lorsque le thread `worker` se termine, nous n'avons pas de moyen simple d'obtenir la valeur de retour.

### Étape 5 : Exécuter le code avec thread

Enregistrez à nouveau le fichier et exécutez - le en utilisant la même commande :

```
python ~/project/futures_demo.py
```

Vous remarquerez que le thread principal continue, le thread `worker` s'exécute, mais nous ne pouvons pas accéder à la valeur de retour de la fonction `worker`.

### Étape 6 : Utiliser manuellement un objet `Future`

Pour résoudre le problème d'obtention de la valeur de retour d'un thread, nous pouvons utiliser un objet `Future`. Ajoutez le code suivant au fichier `futures_demo.py` :

```python
# Part 3: Using a Future to get the result
print("\n--- Part 3: Using a Future manually ---")

def do_work_with_future(x, y, future):
    """Wrapper that sets the result in the Future"""
    result = worker(x, y)
    future.set_result(result)

# Create a Future object
fut = Future()

# Start a thread that will set the result in the Future
t = threading.Thread(target=do_work_with_future, args=(2, 3, fut))
t.start()

print("Main thread continues...")
print("Waiting for the result...")
# Block until the result is available
result = fut.result()  # This will wait until set_result is called
print(f"Got the result: {result}")
```

Dans ce code, nous créons un objet `Future` et le passons à une nouvelle fonction `do_work_with_future`. Cette fonction appelle la fonction `worker` puis définit le résultat dans l'objet `Future`. Le thread principal peut ensuite utiliser la méthode `result()` de l'objet `Future` pour obtenir le résultat lorsque celui - ci est disponible.

### Étape 7 : Exécuter le code avec `Future`

Enregistrez le fichier et exécutez - le à nouveau :

```
python ~/project/futures_demo.py
```

Maintenant, vous verrez que nous pouvons obtenir avec succès la valeur de retour de la fonction s'exécutant dans le thread.

### Étape 8 : Utiliser `ThreadPoolExecutor`

La classe `ThreadPoolExecutor` en Python facilite encore plus le travail avec des tâches concurrentes. Ajoutez le code suivant au fichier `futures_demo.py` :

```python
# Part 4: Using ThreadPoolExecutor (easier way)
print("\n--- Part 4: Using ThreadPoolExecutor ---")
with ThreadPoolExecutor() as executor:
    # Submit the work to the executor
    future = executor.submit(worker, 2, 3)

    print("Main thread continues after submitting work...")
    print("Checking if the future is done:", future.done())

    # Get the result (will wait if not ready)
    result = future.result()
    print("Now the future is done:", future.done())
    print(f"Final result: {result}")
```

La classe `ThreadPoolExecutor` s'occupe de créer et de gérer les objets `Future` pour vous. Vous n'avez qu'à soumettre la fonction et ses arguments, et elle retournera un objet `Future` que vous pouvez utiliser pour obtenir le résultat.

### Étape 9 : Exécuter le code complet

Enregistrez le fichier une dernière fois et exécutez - le :

```
python ~/project/futures_demo.py
```

### Explication

1. **Appel de fonction normal** : Lorsque vous appelez une fonction de manière normale, le programme attend que la fonction se termine et obtient directement la valeur de retour.
2. **Problème avec les threads** : Exécuter une fonction dans un thread séparé a un inconvénient. Il n'y a pas de moyen intégré d'obtenir la valeur de retour de la fonction s'exécutant dans ce thread.
3. **Utilisation manuelle d'un objet `Future`** : En créant un objet `Future` et en le passant au thread, nous pouvons définir le résultat dans l'objet `Future` puis obtenir le résultat depuis le thread principal.
4. **Utilisation de `ThreadPoolExecutor`** : Cette classe simplifie la programmation concurrente. Elle gère la création et la gestion des objets `Future` pour vous, ce qui facilite l'exécution concurrente de fonctions et l'obtention de leurs valeurs de retour.

Les objets `Future` ont plusieurs méthodes utiles :

- `result()` : Cette méthode est utilisée pour obtenir le résultat de la fonction. Si le résultat n'est pas encore prêt, elle attendra jusqu'à ce qu'il le soit.
- `done()` : Vous pouvez utiliser cette méthode pour vérifier si le calcul de la fonction est terminé.
- `add_done_callback()` : Cette méthode vous permet d'enregistrer une fonction qui sera appelée lorsque le résultat sera prêt.

Ce modèle est très important en programmation concurrente, notamment lorsque vous avez besoin d'obtenir des résultats de fonctions s'exécutant en parallèle.
