# Pools de travailleurs

Implémentez un pool de travailleurs qui reçoit des travaux sur le canal `jobs` et envoie les résultats correspondants sur le canal `results`. Le pool de travailleurs devrait avoir plusieurs instances concurrentes, et chaque travailleur devrait dormir une seconde par travail pour simuler une tâche coûteuse.

## Exigences

- Utilisez des goroutines et des canaux pour implémenter le pool de travailleurs.
- Le pool de travailleurs devrait avoir plusieurs instances concurrentes.
- Chaque travailleur devrait dormir une seconde par travail pour simuler une tâche coûteuse.
- Le pool de travailleurs devrait recevoir des travaux sur le canal `jobs` et envoyer les résultats correspondants sur le canal `results`.

## Exemple

```sh
# Notre programme en cours d'exécution montre les 5 travaux exécutés par
# divers travailleurs. Le programme ne prend que environ 2 secondes
# malgré un travail total d'environ 5 secondes car
# il y a 3 travailleurs qui opèrent en parallèle.
$ time go run worker-pools.go
worker 1 started job 1
worker 2 started job 2
worker 3 started job 3
worker 1 finished job 1
worker 1 started job 4
worker 2 finished job 2
worker 2 started job 5
worker 3 finished job 3
worker 1 finished job 4
worker 2 finished job 5

Temps réel 0m2,358s
```
