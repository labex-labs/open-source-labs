# Select

In dieser Aufgabe erhältst du zwei Kanäle, `c1` und `c2`, die nach einer gewissen Zeit einen Wert empfangen werden. Deine Aufgabe besteht darin, `select` zu verwenden, um gleichzeitig auf beide dieser Werte zu warten und jeden Wert, sobald er eintrifft, auszugeben.

## Anforderungen

- Du sollst die `select`-Anweisung verwenden, um auf beide Kanäle zu warten.
- Du sollst den empfangenen Wert von jedem Kanal ausgeben, sobald er eintrifft.

## Beispiel

```sh
# Wir empfangen die Werte `"one"` und dann `"two"` wie
# erwartet.
$ time go run select.go
empfangen one
empfangen two

# Beachte, dass die gesamte Ausführungszeit nur etwa 2 Sekunden beträgt,
# da sowohl die 1- als auch die 2-Sekunden-`Sleeps` gleichzeitig ausgeführt werden.
real 0m2.245s
```
