# Variables d'environnement

Dans ce défi, vous devrez définir, obtenir et lister les variables d'environnement.

## Exigences

- Utilisez `os.Setenv` pour définir une paire clé/valeur.
- Utilisez `os.Getenv` pour obtenir une valeur pour une clé.
- Utilisez `os.Environ` pour lister toutes les paires clé/valeur de l'environnement.
- Utilisez `strings.SplitN` pour séparer la clé et la valeur.

## Exemple

```sh
# En exécutant le programme, on voit que l'on récupère la valeur
# de `FOO` que l'on a définie dans le programme, mais que
# `BAR` est vide.
$ go run environment-variables.go
FOO: 1
BAR:

# La liste des clés de l'environnement dépendra de votre
# machine spécifique.
TERM_PROGRAM
PATH
SHELL
...
FOO

# Si on définit `BAR` dans l'environnement d'abord, le programme
# en cours de route récupère cette valeur.
$ BAR=2 go run environment-variables.go
FOO: 1
BAR: 2
...
```
