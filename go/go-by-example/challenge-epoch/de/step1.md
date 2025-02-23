# Epoche

Das Problem, das in dieser Herausforderung gelöst werden soll, ist es, ein Golang-Programm zu schreiben, das die Anzahl der Sekunden, Millisekunden oder Nanosekunden seit der Unix-Epoche berechnen kann.

## Anforderungen

Um diese Herausforderung zu absolvieren, musst du eine grundlegende Kenntnis von Golang haben und die folgenden Anforderungen erfüllen:

- Vertrautheit mit dem `time`-Paket in Golang.
- Kenntnisse darüber, wie die `Unix`, `UnixMilli` und `UnixNano`-Funktionen im `time`-Paket verwendet werden.

## Beispiel

```sh
$ go run epoch.go
2012-10-31 16:13:58.292387 +0000 UTC
1351700038
1351700038292
1351700038292387000
2012-10-31 16:13:58 +0000 UTC
2012-10-31 16:13:58.292387 +0000 UTC

# Als nächstes betrachten wir eine andere zeitbezogene Aufgabe: Zeit
# Parsing und Formatierung.
```
