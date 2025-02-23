# Arguments de ligne de commande

Le programme imprime actuellement les arguments bruts de ligne de commande passés à celui-ci. Cependant, il doit être modifié pour imprimer des arguments spécifiques en fonction de leur index.

## Exigences

- Connaissance de base de Golang
- Familiarité avec les arguments de ligne de commande

## Exemple

```sh
# Pour expérimenter avec les arguments de ligne de commande, il est préférable de
# construire un binaire avec `go build` d'abord.
$ go build command-line-arguments.go
$./command-line-arguments a b c d
[./command-line-arguments a b c d]
[a b c d]
c

# Ensuite, nous examinerons le traitement plus avancé des commandes
# avec des drapeaux.
```
