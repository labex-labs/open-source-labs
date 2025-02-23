# Démarrage de processus

Le défi consiste à implémenter un programme Go qui démarre des processus externes et collecte leur sortie.

## Exigences

- Le programme doit être capable de démarrer des processus externes.
- Le programme doit être capable de collecter la sortie des processus externes.
- Le programme doit gérer les erreurs qui peuvent survenir pendant l'exécution des processus externes.

## Exemple

```sh
# Les programmes démarrés renvoient une sortie identique
# à celle que nous obtiendrions si nous les exécutions directement à partir de la ligne de commande.
$ go run spawning-processes.go
> date
Thu 05 May 2022 10:10:12 PM PDT

# date n'a pas de drapeau `-x` donc il se terminera avec
# un message d'erreur et un code de retour non nul.
commande terminée avec rc = 1
hello > grep
hello grep

-a > ls -l -h
drwxr-xr-x 4 mark 136B Oct 3 16:29.
drwxr-xr-x 91 mark 3.0K Oct 3 12:50..
-rw-r--r-- 1 mark 1.3K Oct 3 16:28 spawning-processes.go
```
