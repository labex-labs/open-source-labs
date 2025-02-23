# Serveur HTTP

Vous êtes requis d'écrire un serveur HTTP simple capable de gérer deux routes : `/hello` et `/headers`. La route `/hello` devrait renvoyer une réponse simple "hello", tandis que la route `/headers` devrait renvoyer tous les en-têtes de requête HTTP.

## Exigences

- Le serveur devrait utiliser le package `net/http`.
- La route `/hello` devrait renvoyer une réponse "hello".
- La route `/headers` devrait renvoyer tous les en-têtes de requête HTTP.
- Le serveur devrait écouter sur le port `8090`.

## Exemple

```sh
# Exécutez le serveur en arrière-plan.
$ go run http-servers.go &

# Accédez à la route `/hello`.
$ curl localhost:8090/hello
hello
```
