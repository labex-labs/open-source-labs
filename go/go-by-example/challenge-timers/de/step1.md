# Zeitgeber

Die Herausforderung erfordert die Implementierung eines Zeitgebers, der für eine bestimmte Zeitspanne wartet und dann feuert. Darüber hinaus sollte der Zeitgeber vor dem Auslösen abgebrochen werden können.

## Anforderungen

- Das `time`-Paket sollte importiert werden.
- Zwei Zeitgeber sollten erstellt werden, ein Zeitgeber, der 2 Sekunden wartet, und ein anderer, der 1 Sekunde wartet.
- Der erste Zeitgeber sollte "Timer 1 fired" ausgeben, wenn er feuert.
- Der zweite Zeitgeber sollte "Timer 2 fired" ausgeben, wenn er feuert.
- Der zweite Zeitgeber sollte vor dem Auslösen abgebrochen werden.
- Das Programm sollte 2 Sekunden warten, um zu zeigen, dass der zweite Zeitgeber nicht ausgelöst wurde.

## Beispiel

```sh
// Der erste Zeitgeber wird ~2s nach dem Start des
// Programms feuern, aber der zweite sollte vor dem Auslösen
// gestoppt werden.
$ go run timers.go
Timer 1 fired
Timer 2 stopped
```
