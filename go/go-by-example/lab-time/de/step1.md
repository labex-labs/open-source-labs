# Zeit

Der folgende Code enthält Beispiele dafür, wie man in Go mit Zeit und Zeitspanne umgeht. Einige Teile des Codes fehlen jedoch. Ihre Aufgabe ist es, den Code zu vervollständigen, damit er wie erwartet funktioniert.

- Grundkenntnisse der Go-Programmiersprache.
- Vertrautheit mit der Zeit- und Zeitspanneunterstützung in Go.

```sh
$ go run time.go
2012-10-31 15:50:13.793654 +0000 UTC
2009-11-17 20:34:58.651387237 +0000 UTC
2009
November
17
20
34
58
651387237
UTC
Tuesday
true
false
false
25891h15m15.142266763s
25891.25420618521
1.5534752523711128e+06
9.320851514226677e+07
93208515142266763
2012-10-31 15:50:13.793654 +0000 UTC
2006-12-05 01:19:43.509120474 +0000 UTC

# Als nächstes betrachten wir die verwandte Idee der Zeit
# relativ zum Unix-Epoch.
```

Der vollständige Code ist unten:

```go
// Go bietet umfangreiche Unterstützung für Zeiten und Zeitspannen;
// hier sind einige Beispiele.

package main

import (
	"fmt"
	"time"
)

func main() {
	p := fmt.Println

	// Wir beginnen mit dem Abrufen der aktuellen Zeit.
	now := time.Now()
	p(now)

	// Man kann ein `time`-Struct erstellen, indem man das
	// Jahr, Monat, Tag usw. angibt. Zeiten sind immer mit
	// einem `Location` assoziiert, d.h. Zeitzone.
	then := time.Date(
		2009, 11, 17, 20, 34, 58, 651387237, time.UTC)
	p(then)

	// Man kann die verschiedenen Komponenten des Zeit-
	// werts wie erwartet extrahieren.
	p(then.Year())
	p(then.Month())
	p(then.Day())
	p(then.Hour())
	p(then.Minute())
	p(then.Second())
	p(then.Nanosecond())
	p(then.Location())

	// Der Montag-Sonntag `Weekday` ist ebenfalls verfügbar.
	p(then.Weekday())

	// Diese Methoden vergleichen zwei Zeiten und testen, ob
	// die erste vor, nach oder gleichzeitig mit der zweiten
	// auftritt, respective.
	p(then.Before(now))
	p(then.After(now))
	p(then.Equal(now))

	// Die `Sub`-Methode gibt eine `Duration` zurück, die
	// den Zeitintervall zwischen zwei Zeiten repräsentiert.
	diff := now.Sub(then)
	p(diff)

	// Wir können die Länge der Zeitspanne in verschiedenen
	// Einheiten berechnen.
	p(diff.Hours())
	p(diff.Minutes())
	p(diff.Seconds())
	p(diff.Nanoseconds())

	// Man kann `Add` verwenden, um eine Zeit um eine gegebene
	// Zeitspanne voranzuschieben, oder mit einem `-`, um
	// rückwärts um eine Zeitspanne zu gehen.
	p(then.Add(diff))
	p(then.Add(-diff))
}

```
