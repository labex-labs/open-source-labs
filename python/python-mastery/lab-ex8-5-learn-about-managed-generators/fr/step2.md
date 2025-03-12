# Créer un planificateur de tâches (task scheduler) avec des générateurs

En programmation, un planificateur de tâches est un outil essentiel qui aide à gérer et exécuter efficacement plusieurs tâches. Dans cette section, nous allons utiliser des générateurs pour construire un simple planificateur de tâches capable d'exécuter plusieurs fonctions générateur de manière concurrente. Cela vous montrera comment les générateurs peuvent être gérés pour effectuer une multitâche coopérative, ce qui signifie que les tâches s'exécutent tour à tour et partagent le temps d'exécution.

Tout d'abord, vous devez créer un nouveau fichier. Accédez au répertoire `/home/labex/project` et créez un fichier nommé `multitask.py`. Ce fichier contiendra le code de notre planificateur de tâches.

```python
# multitask.py

from collections import deque

# Task queue
tasks = deque()

# Simple task scheduler
def run():
    while tasks:
        task = tasks.popleft()  # Get the next task
        try:
            task.send(None)     # Resume the task
            tasks.append(task)  # Put it back in the queue
        except StopIteration:
            print('Task done')  # Task is complete

# Example task 1: Countdown
def countdown(n):
    while n > 0:
        print('T-minus', n)
        yield              # Pause execution
        n -= 1

# Example task 2: Count up
def countup(n):
    x = 0
    while x < n:
        print('Up we go', x)
        yield              # Pause execution
        x += 1
```

Maintenant, décomposons le fonctionnement de ce planificateur de tâches :

1. Nous utilisons un `deque` (file doublement chaînée) pour stocker nos tâches générateur. Un `deque` est une structure de données qui permet d'ajouter et de supprimer des éléments efficacement des deux extrémités. C'est un excellent choix pour notre file de tâches car nous devons ajouter des tâches à la fin et les supprimer du début.
2. La fonction `run()` est le cœur de notre planificateur de tâches. Elle prend les tâches une par une dans la file :
   - Elle reprend chaque tâche en utilisant `send(None)`. Cela est similaire à l'utilisation de `next()` sur un générateur. Cela indique au générateur de reprendre l'exécution là où il s'était arrêté.
   - Après que la tâche ait cédé le contrôle (yield), elle est ajoutée à nouveau à la fin de la file. De cette façon, la tâche aura une autre chance de s'exécuter plus tard.
   - Lorsqu'une tâche est terminée (lève l'exception `StopIteration`), elle est supprimée de la file. Cela indique que la tâche a terminé son exécution.
3. Chaque instruction `yield` dans nos tâches générateur agit comme un point d'arrêt. Lorsqu'un générateur atteint une instruction `yield`, il met en pause son exécution et rend le contrôle au planificateur. Cela permet aux autres tâches de s'exécuter.

Cette approche met en œuvre une multitâche coopérative. Chaque tâche cède volontairement le contrôle au planificateur, permettant aux autres tâches de s'exécuter. De cette façon, plusieurs tâches peuvent partager le temps d'exécution et s'exécuter de manière concurrente.
