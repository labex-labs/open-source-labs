# Zustandsbehaftete Goroutinen

Beim parallelen Programmieren ist es unerlässlich, den Zugang zu einem gemeinsamen Zustand zu synchronisieren, um Wettlaufbedingungen und Datenschädigungen zu vermeiden. In dieser Aufgabe wird ein Szenario vorgestellt, in dem eine einzelne Goroutine den Zustand besitzt und andere Goroutinen Nachrichten senden, um den Zustand zu lesen oder zu schreiben.

## Anforderungen

- Verwenden Sie Kanäle, um Les- und Schreibanforderungen an die den Zustand besitzende Goroutine zu senden.
- Verwenden Sie die `readOp`- und `writeOp`-Strukturen, um Anforderungen und Antworten zu kapseln.
- Verwenden Sie eine Map, um den Zustand zu speichern.
- Verwenden Sie `resp`-Kanäle, um Erfolg und Rückgabewerte anzuzeigen.
- Verwenden Sie das `atomic`-Paket, um die Anzahl der Les- und Schreiboperationen zu zählen.
- Verwenden Sie das `time`-Paket, um eine Verzögerung zwischen den Operationen hinzuzufügen.

## Beispiel

```sh
# Wenn wir unser Programm ausführen, zeigt sich, dass das
# Beispiel zur Zustandsverwaltung auf der Grundlage von
# Goroutinen insgesamt etwa 80.000 Operationen
# durchführt.
$ go run stateful-goroutines.go
readOps: 71708
writeOps: 7177

# Für diesen speziellen Fall war der auf Goroutinen
# basierende Ansatz etwas aufwendiger als der auf
# Mutex basierende. Er kann in bestimmten Fällen jedoch
# nützlich sein, beispielsweise wenn Sie andere Kanäle
# verwenden oder wenn das Verwalten mehrerer solcher
# Mutexe fehleranfällig wäre. Sie sollten den Ansatz
# verwenden, der Ihnen am natürlichsten erscheint,
# insbesondere was die Korrektheit Ihres Programms
# betrifft.
```
