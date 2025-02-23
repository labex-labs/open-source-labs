# Methoden

Der bereitgestellte Code definiert einen Strukturtyp namens `rect` mit zwei Feldern, `width` und `height`. Zwei Methoden werden für diesen Strukturtyp definiert, `area` und `perim`. Die `area`-Methode berechnet die Fläche des Rechtecks, und die `perim`-Methode berechnet den Umfang des Rechtecks. Die Hauptfunktion ruft diese beiden Methoden auf und druckt ihre Ergebnisse.

- Die `area`-Methode sollte einen Empfänger vom Typ `*rect` haben.
- Die `perim`-Methode sollte einen Empfänger vom Typ `rect` haben.
- Die `area`-Methode sollte die Fläche des Rechtecks zurückgeben.
- Die `perim`-Methode sollte den Umfang des Rechtecks zurückgeben.
- Die `main`-Funktion sollte beide Methoden aufrufen und ihre Ergebnisse drucken.

```sh
$ go run methods.go
area: 50
perim: 30
area: 50
perim: 30

# Als nächstes betrachten wir Go's Mechanismus zur Gruppierung und
# Benennung verwandter Methodensätze: Schnittstellen.
```

Hier ist der vollständige Code:

```go
// Go unterstützt _Methoden_, die auf Strukturtypen definiert sind.

package main

import "fmt"

type rect struct {
	width, height int
}

// Diese `area`-Methode hat einen _Empfängertyp_ von `*rect`.
func (r *rect) area() int {
	return r.width * r.height
}

// Methoden können für Zeiger- oder Wertempfängertypen definiert werden.
// Hier ist ein Beispiel für einen Wertempfänger.
func (r rect) perim() int {
	return 2*r.width + 2*r.height
}

func main() {
	r := rect{width: 10, height: 5}

	// Hier rufen wir die 2 für unsere Struktur definierten Methoden auf.
	fmt.Println("area: ", r.area())
	fmt.Println("perim:", r.perim())

	// Go behandelt die Konvertierung zwischen Werten und
	// Zeigern für Methodenaufrufe automatisch. Sie können
	// einen Zeigerempfängertyp verwenden, um die Kopierung
	// bei Methodenaufrufen zu vermeiden oder um die Methode
	// zu ermöglichen, die empfangende Struktur zu mutieren.
	rp := &r
	fmt.Println("area: ", rp.area())
	fmt.Println("perim:", rp.perim())
}

```
