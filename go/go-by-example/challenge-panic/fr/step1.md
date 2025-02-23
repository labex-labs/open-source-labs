# Panic

Le défi vous oblige à utiliser la fonction `panic` pour échouer rapidement en cas d'erreurs qui ne devraient pas se produire pendant le fonctionnement normal ou que vous n'êtes pas préparé à gérer de manière gracieuse.

## Exigences

- Connaissance de base du langage de programmation Golang.
- Familiarité avec la gestion des erreurs en Golang.
- Compréhension de la fonction `panic` en Golang.

## Exemple

```sh
# Exécuter ce programme entraînera une panique, imprimera
# un message d'erreur et des traces de goroutine, et sortira
# avec un statut non nul.

# Lorsque la première panique dans `main` se déclenche, le programme sort
# sans atteindre le reste du code. Si vous voulez voir le programme
# essayer de créer un fichier temporaire, commentez la première panique.
$ go run panic.go
panic: un problème

goroutine 1 [en cours d'exécution] :
main.main() /.../panic.go:12 +0x47
...
statut de sortie 2

# Notez que contrairement à certains langages qui utilisent des exceptions
# pour la gestion de nombreuses erreurs, en Go il est courant
# d'utiliser des valeurs de retour indiquant une erreur dès que possible.
```
