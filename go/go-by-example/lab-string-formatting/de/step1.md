# Zeichenkettenformatierung

Sie müssen verschiedene Datentypen mithilfe verschiedener Formatierungsverben in Golang formatieren.

- Sie müssen das `fmt`-Paket verwenden, um die Daten zu formatieren.
- Sie müssen für jeden Datentyp das richtige Formatierungsverb verwenden.
- Sie müssen in der Lage sein, Ganzzahlen, Fließkommazahlen, Zeichenketten und Structs (Strukturen) zu formatieren.
- Sie müssen in der Lage sein, die Breite und Genauigkeit der Ausgabe zu steuern.
- Sie müssen in der Lage sein, die Ausgabe links- oder rechtsbündig auszurichten.

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

Hier ist der vollständige Code:

```go
// Go bietet ausgezeichnete Unterstützung für die Formatierung von Zeichenketten
// im Stil von `printf`. Hier sind einige Beispiele für häufige Aufgaben
// zur Zeichenkettenformatierung.

package main

import (
	"fmt"
	"os"
)

type point struct {
	x, y int
}

func main() {

	// Go bietet mehrere Druck-"Verben", die für die Formatierung
	// allgemeiner Go-Werte konzipiert sind. Beispielsweise wird
	// hier eine Instanz unserer `point`-Struktur ausgegeben.
	p := point{1, 2}
	fmt.Printf("struct1: %v\n", p)

	// Wenn der Wert eine Struktur ist, wird die Variante `%+v`
	// auch die Feldnamen der Struktur enthalten.
	fmt.Printf("struct2: %+v\n", p)

	// Die Variante `%#v` gibt eine Go-Syntaxdarstellung des Werts aus,
	// d.h. das Quellcode-Snippet, das diesen Wert erzeugen würde.
	fmt.Printf("struct3: %#v\n", p)

	// Um den Typ eines Werts auszugeben, verwenden Sie `%T`.
	fmt.Printf("type: %T\n", p)

	// Die Formatierung von Booleschen Werten ist einfach.
	fmt.Printf("bool: %t\n", true)

	// Es gibt viele Optionen für die Formatierung von Ganzzahlen.
	// Verwenden Sie `%d` für die Standard-Dezimalformatierung.
	fmt.Printf("int: %d\n", 123)

	// Dies gibt eine Binärdarstellung aus.
	fmt.Printf("bin: %b\n", 14)

	// Dies gibt das Zeichen aus, das dem angegebenen Ganzzahlwert entspricht.
	fmt.Printf("char: %c\n", 33)

	// `%x` liefert eine Hexadezimalcodierung.
	fmt.Printf("hex: %x\n", 456)

	// Es gibt auch mehrere Formatierungsoptionen für Fließkommazahlen.
	// Für die einfache Dezimalformatierung verwenden Sie `%f`.
	fmt.Printf("float1: %f\n", 78.9)

	// `%e` und `%E` formatieren die Fließkommazahl in (leicht
	// unterschiedlichen Versionen der) wissenschaftlichen Notation.
	fmt.Printf("float2: %e\n", 123400000.0)
	fmt.Printf("float3: %E\n", 123400000.0)

	// Für die einfache Ausgabe von Zeichenketten verwenden Sie `%s`.
	fmt.Printf("str1: %s\n", "\"string\"")

	// Um Zeichenketten wie in Go-Quellcode in Anführungszeichen zu setzen,
	// verwenden Sie `%q`.
	fmt.Printf("str2: %q\n", "\"string\"")

	// Wie bei den zuvor gesehenen Ganzzahlen gibt `%x` die Zeichenkette
	// in Basis-16 aus, wobei pro Byte Eingabe zwei Ausgabebuchstaben verwendet werden.
	fmt.Printf("str3: %x\n", "hex this")

	// Um eine Darstellung eines Zeigers auszugeben, verwenden Sie `%p`.
	fmt.Printf("pointer: %p\n", &p)

	// Bei der Formatierung von Zahlen möchten Sie oft die Breite und Genauigkeit
	// des resultierenden Werts kontrollieren. Um die Breite einer Ganzzahl anzugeben,
	// verwenden Sie eine Zahl nach dem `%` im Verb. Standardmäßig wird das Ergebnis
	// rechtsbündig ausgerichtet und mit Leerzeichen aufgefüllt.
	fmt.Printf("width1: |%6d|%6d|\n", 12, 345)

	// Sie können auch die Breite von ausgegebenen Fließkommazahlen angeben,
	// obwohl Sie normalerweise gleichzeitig die Dezimalgenauigkeit mit der
	// Syntax Breite.Genauigkeit einschränken möchten.
	fmt.Printf("width2: |%6.2f|%6.2f|\n", 1.2, 3.45)

	// Um linksbündig auszurichten, verwenden Sie das `-`-Flag.
	fmt.Printf("width3: |%-6.2f|%-6.2f|\n", 1.2, 3.45)

	// Sie möchten möglicherweise auch die Breite bei der Formatierung von
	// Zeichenketten kontrollieren, insbesondere, um sicherzustellen, dass
	// sie in tabellenartigen Ausgaben ausgerichtet sind. Für die einfache
	// rechtsbündige Breite.
	fmt.Printf("width4: |%6s|%6s|\n", "foo", "b")

	// Um linksbündig auszurichten, verwenden Sie wie bei Zahlen das `-`-Flag.
	fmt.Printf("width5: |%-6s|%-6s|\n", "foo", "b")

	// Bisher haben wir `Printf` gesehen, das die formatierte Zeichenkette
	// an `os.Stdout` ausgibt. `Sprintf` formatiert und gibt eine Zeichenkette
	// zurück, ohne sie irgendwo auszugeben.
	s := fmt.Sprintf("sprintf: a %s", "string")
	fmt.Println(s)

	// Sie können die Formatierung und Ausgabe an `io.Writers` anderen als
	// `os.Stdout` mithilfe von `Fprintf` durchführen.
	fmt.Fprintf(os.Stderr, "io: an %s\n", "error")
}

```
