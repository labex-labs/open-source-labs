# Client HTTP

Vous êtes requis d'écrire un programme qui envoie une requête HTTP GET à un serveur et imprime le statut de la réponse HTTP et les 5 premières lignes du corps de la réponse.

## Exigences

- Le programme doit utiliser le package `net/http` pour émettre une requête HTTP GET.
- Le programme doit imprimer le statut de la réponse HTTP.
- Le programme doit imprimer les 5 premières lignes du corps de la réponse.
- Le programme doit gérer les erreurs de manière appropriée.

## Exemple

```sh
$ go run http-clients.go
Statut de la réponse : 200 OK
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Go by Example</title>

```
