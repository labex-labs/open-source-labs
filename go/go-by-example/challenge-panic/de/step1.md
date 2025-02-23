# Panik

Die Herausforderung erfordert, dass Sie die `panic`-Funktion verwenden, um bei Fehlern, die während des normalen Betriebs nicht auftreten sollten oder die Sie nicht elegant behandeln möchten, schnell zu scheitern.

## Anforderungen

- Grundkenntnisse der Golang-Programmiersprache.
- Vertrautheit mit der Fehlerbehandlung in Golang.
- Verständnis der `panic`-Funktion in Golang.

## Beispiel

```sh
# Wenn Sie dieses Programm ausführen, wird es in Panik geraten,
# eine Fehlermeldung und Goroutine-Spuren ausgeben und mit
# einem nicht nullen Status beenden.

# Wenn der erste Panik in `main` ausgelöst wird, beendet
# das Programm, ohne den Rest des Codes auszuführen. Wenn Sie
# möchten, dass das Programm versucht, eine temporäre Datei
# zu erstellen, kommentieren Sie die erste Panik aus.
$ go run panic.go
panic: ein Problem

goroutine 1 [laufend]:
main.main() /.../panic.go:12 +0x47
...
Beendigungsstatus 2

# Beachten Sie, dass im Gegensatz zu einigen Sprachen, die
# Ausnahmen für die Behandlung vieler Fehler verwenden, in Go
# es idiomatisch ist, wo immer möglich Fehler-indizierende
# Rückgabewerte zu verwenden.
```
