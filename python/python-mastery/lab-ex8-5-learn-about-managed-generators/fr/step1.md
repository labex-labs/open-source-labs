# Les générateurs en tant que tâches

Dans un fichier `multitask.py`, définissez le code suivant :

```python
# multitask.py

from collections import deque

tasks = deque()
def run():
    while tasks:
        task = tasks.popleft()
        try:
            task.send(None)
            tasks.append(task)
        except StopIteration:
            print('Tâche terminée')
```

Ce code implémente un petit planificateur de tâches qui exécute des fonctions génératrices. Essayez-le en l'exécutant avec les fonctions suivantes.

```python
# multitask.py
...

def countdown(n):
    while n > 0:
        print('T-minus', n)
        yield
        n -= 1

def countup(n):
    x = 0
    while x < n:
        print('Up we go', x)
        yield
        x += 1

if __name__ == '__main__':
    tasks.append(countdown(10))
    tasks.append(countdown(5))
    tasks.append(countup(20))
    run()
```

Lorsque vous exécutez ceci, vous devriez voir la sortie de tous les générateurs intercalée. Par exemple :

```python
T-minus 10
T-minus 5
Up we go 0
T-minus 9
T-minus 4
Up we go 1
T-minus 8
T-minus 3
Up we go 2
T-minus 7
T-minus 2
Up we go 3
T-minus 6
T-minus 1
Up we go 4
T-minus 5
Tâche terminée
Up we go 5
T-minus 4
Up we go 6
T-minus 3
Up we go 7
T-minus 2
Up we go 8
T-minus 1
Up we go 9
Tâche terminée
Up we go 10
Up we go 11
Up we go 12
Up we go 13
Up we go 14
Up we go 15
Up we go 16
Up we go 17
Up we go 18
Up we go 19
Tâche terminée
```

Cela est intéressant, mais pas particulièrement convaincant. Passons au prochain exemple.
