# Context

Die `hello`-Funktion simuliert einige Arbeit, die der Server ausführt, indem er einige Sekunden wartet, bevor er eine Antwort an den Client sendet. Während der Arbeit überwacht man den `Done()`-Kanal des Kontexts auf ein Signal, dass wir die Arbeit abbrechen und so bald wie möglich zurückkehren sollten.

## Anforderungen

- Golang-Version 1.13 oder höher.

## Beispiel

```sh
# Führen Sie den Server im Hintergrund aus.
$ go run context-in-http-servers.go &

# Simulieren Sie einen Clientanfrage an `/hello`, drücken
# Sie kurz nach dem Start `Strg+C`, um
# eine Stornierung zu signalisieren.
$ curl localhost:8090/hello
server: hello handler started
^C
server: context canceled
server: hello handler ended
```
