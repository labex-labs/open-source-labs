# Kanäle schließen

In dieser Aufgabe musst du den gegebenen Code so ändern, dass der `jobs`-Kanal geschlossen wird, wenn es keine weiteren Aufgaben für die Arbeitsroutine gibt. Du musst auch den `done`-Kanal verwenden, um zu signalisieren, wenn alle Aufgaben abgeschlossen sind.

## Anforderungen

- Verwende einen gepufferten Kanal `jobs`, um Arbeit von der `main()`-Goroutine an eine Arbeits-Goroutine zu übermitteln.
- Verwende einen Kanal `done`, um zu signalisieren, wenn alle Aufgaben abgeschlossen sind.
- Verwende eine Arbeits-Goroutine, um wiederholt von `jobs` mit `j, more := <-jobs` zu empfangen.
- Verwende die spezielle Zwei-Wert-Form des Empfangs, um auf `done` zu signalisieren, wenn alle Aufgaben abgeschlossen sind.
- Sende 3 Aufgaben an die Arbeitsroutine über den `jobs`-Kanal und schließe ihn anschließend.
- Verwende die [Synchronisierung](channel-synchronization)-Methode, um auf die Arbeitsroutine zu warten.

## Beispiel

```sh
$ go run closing-channels.go
sent job 1
received job 1
sent job 2
received job 2
sent job 3
received job 3
sent all jobs
received all jobs

# Die Idee geschlossener Kanäle führt natürlich zu unserem nächsten
# Beispiel: `range` über Kanäle.
```
