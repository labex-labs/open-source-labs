# Signaux

Dans certains cas, nous souhaitons que nos programmes Go gèrent intelligemment les signaux Unix. Par exemple, nous pouvons vouloir qu'un serveur s'arrête proprement lorsqu'il reçoit un `SIGTERM`, ou qu'un outil de ligne de commande arrête de traiter l'entrée s'il reçoit un `SIGINT`.

## Exigences

- Créer un canal tamponné pour recevoir des notifications de `os.Signal`.
- Enregistrer le canal pour recevoir des notifications de signaux spécifiés à l'aide de `signal.Notify`.
- Créer une goroutine pour exécuter une réception bloquante de signaux.
- Afficher le signal reçu et avertir le programme qu'il peut se terminer.
- Attendre le signal attendu puis sortir.

## Exemple

```sh
# Lorsque nous exécutons ce programme, il bloquera en attendant un
# signal. En appuyant sur `ctrl-C` (que le
# terminal affiche comme `^C`), nous pouvons envoyer un signal `SIGINT`,
# faisant en sorte que le programme affiche `interrupt` puis sorte.
$ go run signals.go
en attente de signal
^C
interrupt
sortie
```
