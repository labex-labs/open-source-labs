# Sortie

Le problème à résoudre dans ce défi est de quitter un programme Go avec un code de statut spécifique en utilisant la fonction `os.Exit`.

## Exigences

Pour terminer ce défi, vous devrez avoir une compréhension de base de la programmation Go et du package `os`.

## Exemple

```sh
# Si vous exécutez `exit.go` avec `go run`, la sortie
# sera capturée par `go` et affichée.
$ go run exit.go
statut de sortie 3

# En construisant et exécutant un binaire, vous pouvez voir
# le statut dans le terminal.
$ go build exit.go
$./exit
$ echo $?
3

# Notez que le `!` de notre programme n'a jamais été imprimé.
```
