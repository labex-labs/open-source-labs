# Sortieren nach Funktionen

Das Problem, das in dieser Herausforderung gelöst werden soll, besteht darin, eine benutzerdefinierte Sortierfunktion in Go zu implementieren, die eine Zeichenfolgen-Slice nach ihrer Länge sortiert.

## Anforderungen

- Der `byLength`-Typ sollte als Alias für den `[]string`-Typ erstellt werden.
- Die `sort.Interface` sollte auf dem `byLength`-Typ implementiert werden.
- Die `Len`- und `Swap`-Funktionen sollten auf dem `byLength`-Typ implementiert werden.
- Die `Less`-Funktion sollte auf dem `byLength`-Typ implementiert werden, um die tatsächliche benutzerdefinierte Sortierlogik zu enthalten.
- Die `main`-Funktion sollte die ursprüngliche `fruits`-Slice in `byLength` umwandeln und dann `sort.Sort` auf dieser typisierten Slice verwenden.

## Beispiel

```sh
# Wenn wir unser Programm ausführen, wird eine Liste
# angezeigt, die wie gewünscht nach der Zeichenfolgenlänge
# sortiert ist.
$ go run sorting-by-functions.go
[kiwi peach banana]

# Indem wir dieses gleiche Muster von der Erstellung eines
# benutzerdefinierten Typs, der Implementierung der drei
# `Interface`-Methoden auf diesem Typ und dem Aufruf von
# sort.Sort auf einer Sammlung dieses benutzerdefinierten
# Typs befolgen, können wir Go-Slices nach beliebigen
# Funktionen sortieren.
```
