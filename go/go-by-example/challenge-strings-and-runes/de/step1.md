# Strings und Runen

Das Problem, das in dieser Herausforderung gelöst werden soll, ist es, zu verstehen, wie man mit Strings und Runen in Go umgeht. Insbesondere wird die Herausforderung behandeln, wie man die Länge eines Strings erhält, wie man in einen String indexiert, wie man die Anzahl der Runen in einem String zählt und wie man über die Runen in einem String iteriert.

## Anforderungen

Um diese Herausforderung zu absolvieren, benötigen Sie:

- Ein grundlegendes Verständnis der Go-Syntax
- Kenntnisse über Go-Strings und -Runen
- Die Go-Standardbibliothek

## Beispiel

```sh
$ go run strings-and-runes.go
Länge: 18
e0 b8 aa e0 b8 a7 e0 b8 b1 e0 b8 aa e0 b8 94 e0 b8 b5
Rune-Zahl: 6
U+0E2A 'ส' beginnt bei 0
U+0E27 'ว' beginnt bei 3
U+0E31 'ั' beginnt bei 6
U+0E2A 'ส' beginnt bei 9
U+0E14 'ด' beginnt bei 12
U+0E35 'ี' beginnt bei 15

Mit DecodeRuneInString
U+0E2A 'ส' beginnt bei 0
gefunden so sua
U+0E27 'ว' beginnt bei 3
U+0E31 'ั' beginnt bei 6
U+0E2A 'ส' beginnt bei 9
gefunden so sua
U+0E14 'ด' beginnt bei 12
U+0E35 'ี' beginnt bei 15
```
