# Strings und Runes

Das Problem, das in diesem Lab gelöst werden soll, ist es, zu verstehen, wie man mit Strings und Runes in Go umgeht. Genauer gesagt wird in diesem Lab behandelt, wie man die Länge eines Strings erhält, wie man in einen String indexiert, wie man die Anzahl der Runes in einem String zählt und wie man über die Runes in einem String iteriert.

Um dieses Lab zu absolvieren, benötigen Sie:

- Ein grundlegendes Verständnis der Go-Syntax
- Kenntnisse über Go-Strings und -Runes
- Die Go-Standardbibliothek

```sh
$ go run strings-and-runes.go
Länge: 18
e0 b8 aa e0 b8 a7 e0 b8 b1 e0 b8 aa e0 b8 94 e0 b8 b5
Anzahl der Runes: 6
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

Hier ist der vollständige Code:

```go
// Ein Go-String ist ein schreibgeschützter Byte-Slice. Die Sprache
// und die Standardbibliothek behandeln Strings speziell - als
// Container für in [UTF-8](https://en.wikipedia.org/wiki/UTF-8) codierten Text.
// In anderen Sprachen bestehen Strings aus "Zeichen".
// In Go wird das Konzept eines Zeichens als `rune` bezeichnet - es ist
// ein Integer, der einen Unicode-Codepunkt repräsentiert.
// [Dieser Go-Blogbeitrag](https://go.dev/blog/strings) ist eine gute
// Einführung in das Thema.

package main

import (
	"fmt"
	"unicode/utf8"
)

func main() {

	// `s` ist ein `string`, dem ein Literalwert zugewiesen ist,
	// der das Wort "hello" auf Thai repräsentiert. Go-Stringliterale
	// sind UTF-8-kodierter Text.
	const s = "สวัสดี"

	// Da Strings der `[]byte`-Äquivalent sind, liefert dies
	// die Länge der gespeicherten Rohbytes.
	fmt.Println("Länge:", len(s))

	// Ein Indexzugriff auf einen String liefert die Rohbyte-Werte
	// an jeder Stelle. Diese Schleife generiert die Hex-Werte aller
	// Bytes, die die Codepunkte in `s` bilden.
	for i := 0; i < len(s); i++ {
		fmt.Printf("%x ", s[i])
	}
	fmt.Println()

	// Um zu zählen, wie viele _Runes_ in einem String sind, können wir
	// das `utf8`-Paket verwenden. Beachten Sie, dass die Laufzeit von
	// `RuneCountInString` von der Größe des Strings abhängt,
	// da es jedes UTF-8-Rune sequentiell dekodieren muss.
	// Einige thailändische Zeichen werden durch mehrere UTF-8-Codepunkte
	// repräsentiert, sodass das Ergebnis dieser Zählung überraschend sein kann.
	fmt.Println("Anzahl der Runes:", utf8.RuneCountInString(s))

	// Eine `range`-Schleife behandelt Strings speziell und dekodiert
	// jedes `rune` zusammen mit seinem Offset im String.
	for idx, runeValue := range s {
		fmt.Printf("%#U beginnt bei %d\n", runeValue, idx)
	}

	// Wir können die gleiche Iteration erreichen, indem wir die
	// `utf8.DecodeRuneInString`-Funktion explizit verwenden.
	fmt.Println("\nMit DecodeRuneInString")
	for i, w := 0, 0; i < len(s); i += w {
		runeValue, width := utf8.DecodeRuneInString(s[i:])
		fmt.Printf("%#U beginnt bei %d\n", runeValue, i)
		w = width

		// Dies demonstriert das Übergeben eines `rune`-Werts an eine Funktion.
		examineRune(runeValue)
	}
}

func examineRune(r rune) {

	// In einfachen Anführungszeichen eingeschlossene Werte sind _rune-Literale_.
	// Wir können einen `rune`-Wert direkt mit einem rune-Literal vergleichen.
	if r == 't' {
		fmt.Println("gefunden tee")
	} else if r == 'ส' {
		fmt.Println("gefunden so sua")
	}
}

```
