# Atomare Zähler

Das Problem besteht darin, einen Zähler genau 1000 Mal zu erhöhen, indem 50 Goroutinen und das Paket `sync/atomic` verwendet werden.

## Anforderungen

- Verwenden Sie das Paket `sync/atomic`, um den Zähler zu erhöhen.
- Verwenden Sie eine WaitGroup, um auf alle Goroutinen zu warten, bis sie ihre Arbeit beendet haben.

## Beispiel

```sh
# Wir erwarten genau 50.000 Operationen. Hätten wir
# die nicht-atomare `ops++` verwendet, um den Zähler
# zu erhöhen, würden wir wahrscheinlich eine andere
# Zahl erhalten, die zwischen den Ausführungen
# variiert, da die Goroutinen sich gegenseitig
# stören würden. Darüber hinaus würden wir bei der
# Ausführung mit der `-race`-Flagge Datenkonfliktfehler
# erhalten.
$ go run atomic-counters.go
ops: 50000

# Als nächstes werden wir uns Mutexs ansehen, ein anderes
# Werkzeug zum Verwalten des Zustands.
```
