# Context

La fonction `hello` simule un certain travail effectué par le serveur en attendant quelques secondes avant d'envoyer une réponse au client. Pendant le travail, surveillez la chaîne `Done()` du contexte pour un signal indiquant qu'il faut annuler le travail et retourner le plus rapidement possible.

## Exigences

- Version de Golang 1.13 ou ultérieure.

## Exemple

```sh
# Lancez le serveur en arrière-plan.
$ go run context-in-http-servers.go &

# Simulez une requête client à `/hello`, en appuyant
# sur Ctrl+C peu de temps après le lancement pour
# signaler l'annulation.
$ curl localhost:8090/hello
server: hello handler started
^C
server: context canceled
server: hello handler ended
```
