# Konstanten

Das Problem, das gelöst werden soll, ist es, die Verwendung von Konstanten in Golang für Zeichen-, Zeichenfolge-, boolesche und numerische Werte zu demonstrieren.

Das Labor hat die folgenden Anforderungen:

- Verwenden Sie das Schlüsselwort `const`, um einen Konstantenwert zu deklarieren.
- Konstanten sollten Zeichen-, Zeichenfolge-, boolesche und numerische Werte sein.
- Ein `const`-Statement kann überall dort auftauchen, wo ein `var`-Statement auftauchen kann.
- Zeigen Sie, dass konstante Ausdrücke mit beliebiger Genauigkeit arithmetische Operationen durchführen.
- Ein numerischer Konstante hat keinen Typ, bis ihm ein Typ zugewiesen wird, beispielsweise durch eine explizite Konvertierung.
- Eine Zahl kann durch Verwendung in einem Kontext, der einen Typ erfordert, wie einer Variablenezuweisung oder einer Funktionsaufruf, einen Typ zugewiesen werden.

```sh
$ go run constant.go
constant
6e+11
600000000000
-0.28470407323754404
```

Hier ist der vollständige Code:

```go
// Go unterstützt _Konstanten_ von Zeichen, Zeichenfolgen, booleschen
// und numerischen Werten.

package main

import (
	"fmt"
	"math"
)

// `const` deklariert einen Konstantenwert.
const s string = "constant"

func main() {
	fmt.Println(s)

	// Ein `const`-Statement kann überall dort auftauchen, wo ein `var`
	// Statement auftauchen kann.
	const n = 500000000

	// Konstante Ausdrücke führen arithmetische Operationen mit
	// beliebiger Genauigkeit durch.
	const d = 3e20 / n
	fmt.Println(d)

	// Ein numerischer Konstante hat keinen Typ, bis ihm ein Typ zugewiesen
	// wird, beispielsweise durch eine explizite Konvertierung.
	fmt.Println(int64(d))

	// Eine Zahl kann durch Verwendung in einem Kontext, der einen Typ
	// erfordert, wie einer Variablenezuweisung oder einer Funktionsaufruf,
	// einen Typ zugewiesen werden. Beispielsweise erwartet hier `math.Sin`
	// einen `float64`.
	fmt.Println(math.Sin(n))
}

```
