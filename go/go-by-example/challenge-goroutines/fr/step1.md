# Goroutines

Le problème à résoudre dans ce défi est de créer et d'exécuter des goroutines pour exécuter des fonctions de manière concurrente.

## Exigences

- La fonction `f` doit afficher sa chaîne d'entrée et une variable compteur trois fois.
- La fonction `main` doit appeler la fonction `f` de manière synchrone et afficher "direct" et une variable compteur trois fois.
- La fonction `main` doit appeler la fonction `f` de manière asynchrone en utilisant une goroutine et afficher "goroutine" et une variable compteur trois fois.
- La fonction `main` doit démarrer une goroutine pour exécuter une fonction anonyme qui affiche un message.
- La fonction `main` doit attendre que les goroutines aient fini d'être exécutées avant d'afficher "terminé".

## Exemple

```sh
# Lorsque nous exécutons ce programme, nous voyons d'abord la sortie de l'appel bloquant, puis la sortie des deux goroutines. La sortie des goroutines peut être intercalée, car les goroutines sont exécutées de manière concurrente par le runtime Go.
$ go run goroutines.go
direct : 0
direct : 1
direct : 2
goroutine : 0
going
goroutine : 1
goroutine : 2
terminé

# Ensuite, nous examinerons un complément aux goroutines dans les programmes Go concurrentiels : les canaux.
```
