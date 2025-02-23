# Zeichenkettenformatierung

Sie müssen verschiedene Datentypen in Golang mit verschiedenen Formatierungsverben formatieren.

## Anforderungen

- Sie müssen das `fmt`-Paket verwenden, um die Daten zu formatieren.
- Sie müssen das richtige Formatierungsverb für jeden Datentyp verwenden.
- Sie müssen in der Lage sein, Ganzzahlen, Gleitkommazahlen, Zeichenketten und Strukturen zu formatieren.
- Sie müssen die Breite und Genauigkeit der Ausgabe steuern können.
- Sie müssen die Ausgabe linksbündig oder rechtsbündig ausrichten können.

## Beispiel

```sh
$ go run string-formatting.go
struct1: {1 2}
struct2: {x:1 y:2}
struct3: main.point{x:1, y:2}
type: main.point
bool: true
int: 123
bin: 1110
char:!
hex: 1c8
float1: 78.900000
float2: 1.234000e+08
float3: 1.234000E+08
str1: "string"
str2: "\"string\""
str3: 6865782074686973
pointer: 0xc0000ba000
width1: | 12 | 345 \
  | width2: | 1.20 | 3.45 \
  | width3: | 1.20 | 3.45 \
  | width4: | foo | b \
  | width5: | foo | b \
  | sprintf: a string
io: an error
```
