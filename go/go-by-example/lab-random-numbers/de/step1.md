# Zufallszahlen

Sie müssen ein Programm schreiben, das Zufallszahlen im Integer- und Float-Format innerhalb eines bestimmten Bereichs generiert. Das Programm sollte auch in der Lage sein, verschiedene Zahlenfolgen durch Ändern des Seeds zu erzeugen.

- Das Programm sollte das Paket `math/rand` verwenden, um Zufallszahlen zu generieren.
- Das Programm sollte Zufallszahlen im Integer-Format innerhalb eines bestimmten Bereichs generieren.
- Das Programm sollte Zufallszahlen im Float-Format innerhalb eines bestimmten Bereichs generieren.
- Das Programm sollte in der Lage sein, verschiedene Zahlenfolgen durch Ändern des Seeds zu erzeugen.

```sh
# Je nach Ausführungsort dieses Beispiels können
# einige der generierten Zahlen unterschiedlich
# sein. Beachten Sie, dass auf dem Go Playground
# das Setzen des Seeds mit `time.Now()` aufgrund
# der Implementierung des Playgrounds immer noch
# deterministische Ergebnisse liefert.
$ go run random-numbers.go
81,87
0.6645600532184904
7.123187485356329,8.434115364335547
0,28
5,87
5,87

# Lesen Sie die Dokumentation des Pakets
# [`math/rand`](https://pkg.go.dev/math/rand), um
# Referenzen zu anderen Zufallszahlen zu erhalten,
# die Go liefern kann.
```

Hier ist der vollständige Code:

```go
// Das Paket `math/rand` von Go liefert die
// [Generierung von Pseudozufallszahlen](https://en.wikipedia.org/wiki/Pseudorandom_number_generator).

package main

import (
	"fmt"
	"math/rand"
	"time"
)

func main() {

	// Beispielsweise liefert `rand.Intn` eine zufällige
	// `int` n mit `0 <= n < 100`.
	fmt.Print(rand.Intn(100), ",")
	fmt.Print(rand.Intn(100))
	fmt.Println()

	// `rand.Float64` liefert eine `float64` `f` mit
	// `0.0 <= f < 1.0`.
	fmt.Println(rand.Float64())

	// Dies kann verwendet werden, um Zufallszahlen im
	// anderen Bereich zu generieren, z. B. `5.0 <= f' < 10.0`.
	fmt.Print((rand.Float64()*5)+5, ",")
	fmt.Print((rand.Float64() * 5) + 5)
	fmt.Println()

	// Der Standard-Zufallszahlengenerator ist
	// deterministisch, sodass er standardmäßig die
	// gleiche Zahlenfolge produziert. Um verschiedene
	// Zahlenfolgen zu erzeugen, geben Sie ihm einen
	// sich ändernden Seed. Beachten Sie, dass dies
	// nicht sicher ist, um Zufallszahlen zu verwenden,
	// die Sie als geheim behandeln möchten; verwenden
	// Sie `crypto/rand` für solche.
	s1 := rand.NewSource(time.Now().UnixNano())
	r1 := rand.New(s1)

	// Rufen Sie die resultierende `rand.Rand` genauso
	// wie die Funktionen auf dem `rand`-Paket auf.
	fmt.Print(r1.Intn(100), ",")
	fmt.Print(r1.Intn(100))
	fmt.Println()

	// Wenn Sie einen Source mit der gleichen Zahl
	// initialisieren, erzeugt er die gleiche
	// Zahlenfolge.
	s2 := rand.NewSource(42)
	r2 := rand.New(s2)
	fmt.Print(r2.Intn(100), ",")
	fmt.Print(r2.Intn(100))
	fmt.Println()
	s3 := rand.NewSource(42)
	r3 := rand.New(s3)
	fmt.Print(r3.Intn(100), ",")
	fmt.Print(r3.Intn(100))
}

```
