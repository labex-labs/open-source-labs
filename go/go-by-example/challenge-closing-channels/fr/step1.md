# Fermeture des canaux

Dans ce défi, vous devez modifier le code donné pour fermer le canal `jobs` lorsqu'il n'y a plus de tâches pour le travailleur. Vous devrez également utiliser le canal `done` pour être averti lorsque toutes les tâches ont été terminées.

## Exigences

- Utiliser un canal tamponné `jobs` pour communiquer le travail à effectuer de la goroutine `main()` à une goroutine de travail.
- Utiliser un canal `done` pour être averti lorsque toutes les tâches ont été terminées.
- Utiliser une goroutine de travail pour recevoir répétitivement de `jobs` avec `j, more := <-jobs`.
- Utiliser la forme à 2 valeurs spéciale de la réception pour être averti sur `done` lorsque toutes les tâches ont été terminées.
- Envoyer 3 tâches au travailleur via le canal `jobs`, puis le fermer.
- Utiliser l'approche de [synchronisation](channel-synchronization) pour attendre le travailleur.

## Exemple

```sh
$ go run closing-channels.go
envoyé travail 1
reçu travail 1
envoyé travail 2
reçu travail 2
envoyé travail 3
reçu travail 3
tous les travaux ont été envoyés
tous les travaux ont été reçus

# L'idée des canaux fermés conduit naturellement à notre prochain
# exemple : `range` sur des canaux.
```
