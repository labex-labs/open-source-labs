# Recover

La fonction `mayPanic` dans le code fourni provoquera un `panic` lorsqu'elle est appelée. Votre tâche consiste à modifier la fonction `main` pour récupérer du `panic` et afficher le message d'erreur.

## Exigences

- Utilisez la fonction `recover` pour gérer le `panic` dans la fonction `mayPanic`.
- Affichez le message d'erreur lorsqu'un `panic` se produit.

## Exemple

```sh
$ go run recover.go
Recovered. Error:
a problem
```
