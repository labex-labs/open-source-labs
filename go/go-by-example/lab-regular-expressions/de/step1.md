# Reguläre Ausdrücke

In diesem Lab müssen Sie den Code vervollständigen, um verschiedene reguläre-Ausdruck-verwandte Aufgaben in Golang durchzuführen.

- Verwenden Sie das `regexp`-Paket, um reguläre-Ausdruck-verwandte Aufgaben durchzuführen.
- Verwenden Sie `MatchString`, um zu testen, ob ein Muster einer Zeichenfolge entspricht.
- Verwenden Sie `Compile`, um eine `Regexp`-Struktur zu optimieren.
- Verwenden Sie `MatchString`, um eine Übereinstimmung wie `Compile` zu testen.
- Verwenden Sie `FindString`, um die Übereinstimmung für den regulären Ausdruck zu finden.
- Verwenden Sie `FindStringIndex`, um die erste Übereinstimmung zu finden und die Start- und Endindizes für die Übereinstimmung statt des übereinstimmenden Texts zurückzugeben.
- Verwenden Sie `FindStringSubmatch`, um Informationen für sowohl `p([a-z]+)ch` als auch `([a-z]+)` zurückzugeben.
- Verwenden Sie `FindStringSubmatchIndex`, um Informationen über die Indizes von Übereinstimmungen und Teilübereinstimmungen zurückzugeben.
- Verwenden Sie `FindAllString`, um alle Übereinstimmungen für einen regulären Ausdruck zu finden.
- Verwenden Sie `FindAllStringSubmatchIndex`, um auf alle Übereinstimmungen in der Eingabe anzuwenden, nicht nur auf die erste.
- Verwenden Sie `Match`, um eine Übereinstimmung mit `[]byte`-Argumenten zu testen und `String` aus dem Funktionsnamen zu entfernen.
- Verwenden Sie `MustCompile`, um globale Variablen mit regulären Ausdrücken zu erstellen.
- Verwenden Sie `ReplaceAllString`, um Teilmengen von Zeichenfolgen mit anderen Werten zu ersetzen.
- Verwenden Sie `ReplaceAllFunc`, um das übereinstimmende Text mit einer angegebenen Funktion zu transformieren.

```sh
$ go run regular-expressions.go
true
true
peach
idx: [0 5]
[peach ea]
[0 5 1 3]
[peach punch pinch]
all: [[0 5 1 3] [6 11 7 9] [12 17 13 15]]
[peach punch]
true
regexp: p([a-z]+)ch
a <fruit>
a PEACH

# Für eine vollständige Referenz zu Go regulären Ausdrücken überprüfen Sie
# die Dokumentation des [`regexp`](https://pkg.go.dev/regexp)-Pakets.

```

Hier ist der vollständige Code:

```go
// Go bietet integrierte Unterstützung für [reguläre Ausdrücke](https://en.wikipedia.org/wiki/Regular_expression).
// Hier sind einige Beispiele für häufige reguläre-Ausdruck-verwandte Aufgaben
// in Go.

package main

import (
	"bytes"
	"fmt"
	"regexp"
)

func main() {

	// Dies testet, ob ein Muster einer Zeichenfolge entspricht.
	match, _ := regexp.MatchString("p([a-z]+)ch", "peach")
	fmt.Println(match)

	// Obigen haben wir einen Zeichenfolgenmuster direkt verwendet, aber für
	// andere reguläre-Ausdruck-Aufgaben müssen Sie eine optimierte
	// `Regexp`-Struktur `Compile`.
	r, _ := regexp.Compile("p([a-z]+)ch")

	// Viele Methoden sind auf diesen Strukturen verfügbar. Hier ist
	// ein Übereinstimmungstest wie wir ihn zuvor gesehen haben.
	fmt.Println(r.MatchString("peach"))

	// Dies findet die Übereinstimmung für den regulären Ausdruck.
	fmt.Println(r.FindString("peach punch"))

	// Dies findet ebenfalls die erste Übereinstimmung, aber gibt die
	// Start- und Endindizes für die Übereinstimmung statt des
	// übereinstimmenden Texts zurück.
	fmt.Println("idx:", r.FindStringIndex("peach punch"))

	// Die `Submatch`-Varianten enthalten Informationen über
	// sowohl die gesamten Musterübereinstimmungen als auch die Teilübereinstimmungen
	// innerhalb dieser Übereinstimmungen. Beispielsweise wird dies
	// Informationen für sowohl `p([a-z]+)ch` als auch `([a-z]+)` zurückgeben.
	fmt.Println(r.FindStringSubmatch("peach punch"))

	// Ähnlich wird dies Informationen über die
	// Indizes von Übereinstimmungen und Teilübereinstimmungen zurückgeben.
	fmt.Println(r.FindStringSubmatchIndex("peach punch"))

	// Die `All`-Varianten dieser Funktionen gelten für alle
	// Übereinstimmungen in der Eingabe, nicht nur die erste. Zum
	// Beispiel um alle Übereinstimmungen für einen regulären Ausdruck zu finden.
	fmt.Println(r.FindAllString("peach punch pinch", -1))

	// Diese `All`-Varianten sind auch für die anderen
	// Funktionen verfügbar, die wir oben gesehen haben.
	fmt.Println("all:", r.FindAllStringSubmatchIndex(
		"peach punch pinch", -1))

	// Die Angabe eines nicht-negativen Integers als zweites
	// Argument für diese Funktionen wird die Anzahl der
	// Übereinstimmungen begrenzen.
	fmt.Println(r.FindAllString("peach punch pinch", 2))

	// Unsere obigen Beispiele hatten Zeichenfolgenargumente und verwendeten
	// Namen wie `MatchString`. Wir können auch `[]byte`-Argumente
	// angeben und `String` aus dem Funktionsnamen entfernen.
	fmt.Println(r.Match([]byte("peach")))

	// Wenn Sie globale Variablen mit regulären
	// Ausdrücken erstellen, können Sie die `MustCompile`-Variante
	// von `Compile` verwenden. `MustCompile` stürzt anstatt
	// einen Fehler zurückzugeben, was es sicherer macht, für
	// globale Variablen zu verwenden.
	r = regexp.MustCompile("p([a-z]+)ch")
	fmt.Println("regexp:", r)

	// Das `regexp`-Paket kann auch verwendet werden, um
	// Teilmengen von Zeichenfolgen mit anderen Werten zu ersetzen.
	fmt.Println(r.ReplaceAllString("a peach", "<fruit>"))

	// Die `Func`-Variante ermöglicht es Ihnen, das übereinstimmende
	// Text mit einer angegebenen Funktion zu transformieren.
	in := []byte("a peach")
	out := r.ReplaceAllFunc(in, bytes.ToUpper)
	fmt.Println(string(out))
}

```
