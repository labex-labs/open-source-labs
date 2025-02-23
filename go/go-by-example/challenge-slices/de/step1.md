# Slices

Das Problem, das in dieser Challenge zu lösen ist, besteht darin, Slice in Go zu erstellen und zu manipulieren. Du musst einen leeren Slice mit nicht null Länge erstellen, Werte im Slice setzen und abrufen, die `len`-Funktion verwenden, um die Länge des Slices zu erhalten, die `append`-Funktion verwenden, um neue Werte zum Slice hinzuzufügen, die `copy`-Funktion verwenden, um einen Slice zu kopieren und den Slice-Operator verwenden, um einen Teil des Elements aus einem bestehenden Slice zu erhalten.

## Anforderungen

Um diese Challenge zu absolvieren, musst du eine grundlegende Kenntnis der Go-Syntax und des Slice-Datentyps haben. Du musst auch mit den Funktionen `make`, `append` und `copy` sowie dem Slice-Operator vertraut sein.

## Beispiel

```sh
# Beachten Sie, dass Slice verschiedene Datentypen als Arrays sind,
# aber von `fmt.Println` ähnlich gerendert werden.
$ go run slices.go
emp: [ ]
set: [a b c]
get: c
len: 3
apd: [a b c d e f]
cpy: [a b c d e f]
sl1: [c d e]
sl2: [a b c d e]
sl3: [c d e f]
dcl: [g h i]
2d: [[0] [1 2] [2 3 4]]

# Lesen Sie diesen [tollen Blogbeitrag](https://go.dev/blog/slices-intro)
# vom Go-Team, um weitere Details über das Design und
# die Implementierung von Slice in Go zu erhalten.

# Jetzt, nachdem wir Arrays und Slice gesehen haben, werden wir uns
# die andere wichtige eingebautes Datenstruktur von Go ansehen: Maps.
```
