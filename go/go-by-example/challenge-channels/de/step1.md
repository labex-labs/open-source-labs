# Channels

In dieser Aufgabe müssen Sie einen neuen Channel erstellen und einen Wert von einer neuen Goroutine in diesen senden. Anschließend empfangen Sie den Wert aus dem Channel und geben ihn aus.

## Anforderungen

- Sie müssen die Syntax `make(chan val-type)` verwenden, um einen neuen Channel zu erstellen.
- Der Channel muss mit den Werten typisiert sein, die er transportiert.
- Sie müssen die Syntax `channel <-` verwenden, um einen Wert in den Channel zu senden.
- Sie müssen die Syntax `<-channel` verwenden, um einen Wert aus dem Channel zu empfangen.
- Sie müssen eine neue Goroutine verwenden, um den Wert in den Channel zu senden.

## Beispiel

```sh
# Wenn wir das Programm ausführen, wird die Nachricht
# "ping" erfolgreich von einer Goroutine zur anderen
# über unseren Channel weitergeleitet.
$ go run channels.go
ping

# Standardmäßig blockieren Senden und Empfangen, bis
# sowohl der Sender als auch der Empfänger bereit sind.
# Diese Eigenschaft hat es uns ermöglicht, am Ende
# unseres Programms auf die Nachricht "ping" zu warten,
# ohne dass wir eine andere Synchronisation verwenden
# mussten.
```
