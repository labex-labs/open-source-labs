# Maps

In diesem Lab müssen Sie eine Map erstellen, die die Anzahl der Vorkommen jedes Wortes in einem gegebenen String speichert. Sie müssen den String in Wörter aufteilen und dann über jedes Wort iterieren, es der Map hinzuzufügen, wenn es noch nicht existiert, oder seinen Zähler zu erhöhen, wenn es bereits existiert.

- Sie müssen eine Map verwenden, um die Wortzahlen zu speichern.
- Sie müssen den Eingabestring in Wörter aufteilen.
- Sie müssen über jedes Wort im Eingabestring iterieren.
- Sie müssen jedes Wort der Map hinzufügen, wenn es noch nicht existiert, oder seinen Zähler erhöhen, wenn es bereits existiert.

```sh
# Beachten Sie, dass Maps im Format `map[k:v k:v]` erscheinen, wenn
# mit `fmt.Println` gedruckt.
$ go run maps.go
map: map[k1:7 k2:13]
v1: 7
v3: 0
len: 2
map: map[k1:7]
prs: false
map: map[bar:2 foo:1]
```

Hier ist der vollständige Code:

```go
// _Maps_ sind Go's eingebauter [assoziativer Datentyp](https://en.wikipedia.org/wiki/Associative_array)
// (manchmal auch _Hashes_ oder _Dicts_ in anderen Sprachen genannt).

package main

import "fmt"

func main() {

	// Um eine leere Map zu erstellen, verwenden Sie die eingebaut
	// `make`: `make(map[key-type]val-type)`.
	m := make(map[string]int)

	// Legen Sie Schlüssel/Wert-Paare mit der typischen `name[key] = val`
	// Syntax fest.
	m["k1"] = 7
	m["k2"] = 13

	// Ein Map mit z.B. `fmt.Println` ausgeben, zeigt alle
	// seine Schlüssel/Wert-Paare an.
	fmt.Println("map:", m)

	// Holen Sie sich einen Wert für einen Schlüssel mit `name[key]`.
	v1 := m["k1"]
	fmt.Println("v1:", v1)

	// Wenn der Schlüssel nicht existiert, wird der
	// [Nullwert](https://go.dev/ref/spec#The_zero_value) des
	// Wertetyps zurückgegeben.
	v3 := m["k3"]
	fmt.Println("v3:", v3)

	// Die eingebaut `len` gibt die Anzahl der Schlüssel/Wert
	// Paare zurück, wenn auf eine Map aufgerufen.
	fmt.Println("len:", len(m))

	// Die eingebaut `delete` entfernt Schlüssel/Wert-Paare aus
	// einer Map.
	delete(m, "k2")
	fmt.Println("map:", m)

	// Der optionale zweite Rückgabewert, wenn ein
	// Wert aus einer Map abgerufen wird, gibt an, ob der Schlüssel
	// in der Map vorhanden war. Dies kann verwendet werden, um
	// zwischen fehlenden Schlüsseln und Schlüsseln mit Nullwerten
	// wie `0` oder `""` zu unterscheiden. Hier mussten wir den Wert
	// selbst nicht, also ignorieren wir es mit dem _Leerbezeichner_
	// `_`.
	_, prs := m["k2"]
	fmt.Println("prs:", prs)

	// Sie können auch eine neue Map in derselben Zeile mit dieser Syntax
	// deklarieren und initialisieren.
	n := map[string]int{"foo": 1, "bar": 2}
	fmt.Println("map:", n)
}

```
