# Strukturembettung

Erstellen Sie eine Struktur namens `container`, die eine Struktur namens `base` einbetten. Die `base`-Struktur sollte ein Feld namens `num` vom Typ `int` und eine Methode namens `describe()` haben, die einen String zurückgibt. Die `container`-Struktur sollte ein Feld namens `str` vom Typ `string` haben. Die `container`-Struktur sollte auf das `num`-Feld und die `describe()`-Methode der `base`-Struktur zugreifen können.

- Die `base`-Struktur sollte ein Feld namens `num` vom Typ `int` haben.
- Die `base`-Struktur sollte eine Methode namens `describe()` haben, die einen String zurückgibt.
- Die `container`-Struktur sollte ein Feld namens `str` vom Typ `string` haben.
- Die `container`-Struktur sollte die `base`-Struktur einbetten.
- Die `container`-Struktur sollte auf das `num`-Feld und die `describe()`-Methode der `base`-Struktur zugreifen können.

```sh
$ go run struct-embedding.go
co={num: 1, str: some name}
also num: 1
describe: base with num=1
describer: base with num=1
```

Hier ist der vollständige Code:

```go
// Go unterstützt das _Einbetten_ von Strukturen und Schnittstellen,
// um eine nahtlosere _Komposition_ von Typen auszudrücken.
// Dies ist nicht zu verwechseln mit [`//go:embed`](embed-directive),
// die eine Go-Direktive ist, die in Go-Version 1.16+ eingeführt wurde,
// um Dateien und Ordner in die Anwendungsbinärdatei zu einbetten.

package main

import "fmt"

type base struct {
	num int
}

func (b base) describe() string {
	return fmt.Sprintf("base with num=%v", b.num)
}

// Ein `container` _bettet_ eine `base` ein. Ein Einbettung sieht
// wie ein Feld ohne Namen aus.
type container struct {
	base
	str string
}

func main() {

	// Wenn wir Strukturen mit Literalen erstellen, müssen wir
	// die Einbettung explizit initialisieren; hier dient der
	// eingebettete Typ als Feldname.
	co := container{
		base: base{
			num: 1,
		},
		str: "some name",
	}

	// Wir können die Felder der Basis direkt auf `co` zugreifen,
	// z.B. `co.num`.
	fmt.Printf("co={num: %v, str: %v}\n", co.num, co.str)

	// Alternativ können wir den vollen Pfad angeben, indem wir
	// den Namen des eingebetteten Typs verwenden.
	fmt.Println("also num:", co.base.num)

	// Da `container` `base` einbettet, werden auch die Methoden
	// von `base` zu Methoden von `container`. Hier rufen wir
	// eine Methode auf, die von `base` eingebettet wurde, direkt
	// auf `co` auf.
	fmt.Println("describe:", co.describe())

	type describer interface {
		describe() string
	}

	// Einbettung von Strukturen mit Methoden kann verwendet werden,
	// um Schnittstellenimplementierungen auf andere Strukturen zu übertragen.
	// Hier sehen wir, dass ein `container` jetzt die `describer`-Schnittstelle
	// implementiert, weil es `base` einbettet.
	var d describer = co
	fmt.Println("describer:", d.describe())
}

```
