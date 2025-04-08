# Tests und Benchmarking

Das Problem, das in diesem Labor gelöst werden soll, ist es, eine einfache Implementierung einer ganzzahligen Minimum-Funktion namens `IntMin` zu testen und zu benchmarken.

- Das `testing`-Paket muss importiert werden.
- Die `IntMin`-Funktion muss zwei ganzzahlige Parameter entgegennehmen und eine Ganzzahl zurückgeben.
- Die `TestIntMinBasic`-Funktion muss die `IntMin`-Funktion für grundlegende Eingabewerte testen.
- Die `TestIntMinTableDriven`-Funktion muss die `IntMin`-Funktion im tabellenbasierten Stil testen.
- Die `BenchmarkIntMin`-Funktion muss die `IntMin`-Funktion benchmarken.

```sh
# Führen Sie alle Tests im aktuellen Projekt im detaillierten Modus aus.

# Führen Sie alle Benchmarks im aktuellen Projekt aus. Alle Tests
# werden vor den Benchmarks ausgeführt. Die `bench`-Flag filtriert
# Benchmark-Funktionsnamen mit einer regulären Ausdruck.
```

Hier ist der vollständige Code:

```go
// Unit-Tests sind ein wichtiger Teil beim Schreiben
// sauberer Go-Programme. Das `testing`-Paket
// liefert die Tools, die wir zum Schreiben von Unit-Tests
// benötigen, und der Befehl `go test` führt die Tests aus.

// Zum Zwecke der Demonstration ist dieser Code im Paket
// `main`, aber es könnte jedes beliebige Paket sein. Testcode
// befindet sich normalerweise im gleichen Paket wie der Code,
// den er testet.
package main

import (
	"fmt"
	"testing"
)

// Wir werden diese einfache Implementierung einer
// ganzzahligen Minimum testen. Normalerweise wäre der Code,
// den wir testen, in einer Quelldatei namens etwa
// `intutils.go`, und die zugehörige Testdatei würde dann
// `intutils_test.go` heißen.
func IntMin(a, b int) int {
	if a < b {
		return a
	}
	return b
}

// Ein Test wird erstellt, indem man eine Funktion mit einem Namen
// beginnt, der mit `Test` beginnt.
func TestIntMinBasic(t *testing.T) {
	ans := IntMin(2, -2)
	if ans!= -2 {
		// `t.Error*` meldet Testfehler, setzt aber die
		// Ausführung des Tests fort. `t.Fatal*` meldet Testfehler
		// und stoppt den Test sofort.
		t.Errorf("IntMin(2, -2) = %d; want -2", ans)
	}
}

// Das Schreiben von Tests kann repetitiv sein, daher ist es üblich,
// einen *tabellenbasierten Stil* zu verwenden, bei dem Testeingaben
// und erwartete Ausgaben in einer Tabelle aufgelistet sind und eine
// einzelne Schleife über sie iteriert und die Testlogik ausführt.
func TestIntMinTableDriven(t *testing.T) {
	var tests = []struct {
		a, b int
		want int
	}{
		{0, 1, 0},
		{1, 0, 0},
		{2, -2, -2},
		{0, -1, -1},
		{-1, 0, -1},
	}

	for _, tt := range tests {
		// t.Run ermöglicht das Ausführen von "Untertests",
		// einer für jede Tabellenzeile. Diese werden separat
		// angezeigt, wenn man `go test -v` ausführt.
		testname := fmt.Sprintf("%d,%d", tt.a, tt.b)
		t.Run(testname, func(t *testing.T) {
			ans := IntMin(tt.a, tt.b)
			if ans!= tt.want {
				t.Errorf("got %d, want %d", ans, tt.want)
			}
		})
	}
}

// Benchmark-Tests befinden sich normalerweise in `_test.go`-Dateien
// und beginnen mit `Benchmark`. Der `testing`-Runner führt jede
// Benchmark-Funktion mehrmals aus, erhöht `b.N` bei jeder Ausführung,
// bis er eine genaue Messung erhält.
func BenchmarkIntMin(b *testing.B) {
	// Normalerweise führt der Benchmark eine Funktion,
	// die wir benchmarken, in einer Schleife `b.N` Mal aus.
	for i := 0; i < b.N; i++ {
		IntMin(1, 2)
	}
}

```
