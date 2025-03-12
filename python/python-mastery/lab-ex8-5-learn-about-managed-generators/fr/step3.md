# Tester notre planificateur de tâches (task scheduler)

Maintenant, nous allons ajouter un test à notre fichier `multitask.py`. Le but de ce test est d'exécuter plusieurs tâches en même temps, ce qui est appelé une exécution concurrente. L'exécution concurrente permet à différentes tâches de progresser apparemment en même temps, même si, dans un environnement mono - thread, les tâches s'exécutent en réalité tour à tour.

Pour effectuer ce test, ajoutez le code suivant à la fin du fichier `multitask.py` :

```python
# Test our scheduler
if __name__ == '__main__':
    # Add tasks to the queue
    tasks.append(countdown(10))  # Count down from 10
    tasks.append(countdown(5))   # Count down from 5
    tasks.append(countup(20))    # Count up to 20

    # Run all tasks
    run()
```

Dans ce code, nous vérifions d'abord si le script est exécuté directement en utilisant `if __name__ == '__main__':`. Ensuite, nous ajoutons trois tâches différentes à la file `tasks`. Les tâches `countdown` compteront à rebours à partir des nombres donnés, et la tâche `countup` comptera jusqu'au nombre spécifié. Enfin, nous appelons la fonction `run()` pour commencer l'exécution de ces tâches.

Après avoir ajouté le code, exécutez - le avec la commande suivante dans le terminal :

```bash
python3 /home/labex/project/multitask.py
```

Lorsque vous exécutez le code, vous devriez voir une sortie similaire à celle - ci (l'ordre exact des lignes peut varier) :

```
T-minus 10
T-minus 5
Up we go 0
T-minus 9
T-minus 4
Up we go 1
T-minus 8
T-minus 3
Up we go 2
...
```

Remarquez comment les sorties des différentes tâches sont mélangées. Cela est une indication claire que notre planificateur exécute les trois tâches de manière concurrente. Chaque fois qu'une tâche atteint une instruction `yield`, le planificateur met en pause cette tâche et passe à une autre, permettant à toutes les tâches de progresser au fil du temps.

## Comment cela fonctionne

Regardons de plus près ce qui se passe lorsque notre planificateur s'exécute :

1. Tout d'abord, nous ajoutons trois tâches générateur à la file : `countdown(10)`, `countdown(5)` et `countup(20)`. Ces tâches générateur sont des fonctions spéciales qui peuvent mettre en pause et reprendre leur exécution aux instructions `yield`.
2. Ensuite, la fonction `run()` commence son travail :
   - Elle prend la première tâche, `countdown(10)`, dans la file.
   - Elle exécute cette tâche jusqu'à ce qu'elle atteigne une instruction `yield`. Lorsqu'elle atteint le `yield`, elle affiche "T-minus 10".
   - Après cela, elle ajoute la tâche `countdown(10)` de nouveau à la file afin qu'elle puisse être exécutée plus tard.
   - Ensuite, elle prend la tâche `countdown(5)` dans la file.
   - Elle exécute la tâche `countdown(5)` jusqu'à ce qu'elle atteigne une instruction `yield`, affichant "T-minus 5".
   - Et ce processus se poursuit...

Ce cycle se poursuit jusqu'à ce que toutes les tâches soient terminées. Chaque tâche a l'occasion de s'exécuter pendant un court instant, ce qui donne l'illusion d'une exécution concurrente sans avoir besoin d'utiliser des threads ou des callbacks. Les threads sont un moyen plus complexe d'obtenir de la concurrence, et les callbacks sont utilisés en programmation asynchrone. Notre simple planificateur utilise des générateurs pour obtenir un effet similaire de manière plus simple.
