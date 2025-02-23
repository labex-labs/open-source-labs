# Sortieren

Das Problem, das in dieser Herausforderung gelöst werden muss, ist es, Slices von Strings und ganzen Zahlen mit dem Paket `sort` zu sortieren.

## Anforderungen

- Das Paket `sort` muss importiert werden.
- Die Funktion `sort.Strings()` muss verwendet werden, um einen Slice von Strings zu sortieren.
- Die Funktion `sort.Ints()` muss verwendet werden, um einen Slice von ganzen Zahlen zu sortieren.
- Die Funktion `sort.IntsAreSorted()` muss verwendet werden, um zu überprüfen, ob ein Slice von ganzen Zahlen bereits sortiert ist.

## Beispiel

```sh
# Wenn wir unser Programm ausführen, werden die sortierten String- und Int-Slices
# und `true` als Ergebnis unserer `AreSorted`-Prüfung ausgegeben.
$ go run sorting.go
Strings: [a b c]
Ints: [2 4 7]
Sortiert: true
```
