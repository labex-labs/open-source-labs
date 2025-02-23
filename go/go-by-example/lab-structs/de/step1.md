# Structs

In diesem Labor müssen Sie die Funktion `newPerson` vervollständigen, die eine neue Person-Struktur mit dem angegebenen Namen konstruiert. Der `person`-Strukturtyp hat die Felder `name` und `age`.

- Der `person`-Strukturtyp muss die Felder `name` und `age` haben.
- Die Funktion `newPerson` muss eine neue Person-Struktur mit dem angegebenen Namen konstruieren.
- Die Funktion `newPerson` muss einen Zeiger auf die neu erstellte Person-Struktur zurückgeben.
- Die `main`-Funktion muss folgende ausgeben:
  - Eine neue Struktur mit Namen "Bob" und Alter 20.
  - Eine neue Struktur mit Namen "Alice" und Alter 30.
  - Eine neue Struktur mit Namen "Fred" und Alter 0.
  - Einen Zeiger auf eine neue Struktur mit Namen "Ann" und Alter 40.
  - Eine neue Struktur, die mit der `newPerson`-Funktion konstruiert wurde, mit Namen "Jon" und Alter 42.
  - Das `name`-Feld einer Struktur mit Namen "Sean" und Alter 50.
  - Das `age`-Feld eines Zeigers auf eine Struktur mit Namen "Sean" und Alter 50.
  - Das `age`-Feld eines Zeigers auf eine Struktur mit Namen "Sean" und Alter 50, nachdem das `age`-Feld auf 51 aktualisiert wurde.

```sh
$ go run structs.go
{Bob 20}
{Alice 30}
{Fred 0}
&{Ann 40}
&{Jon 42}
Sean
50
51
```

Hier ist der vollständige Code:

```go
// Go's _structs_ sind gruppierte Felder.
// Sie eignen sich gut, um Daten zusammenzufassen und damit
// Aufzeichnungen zu bilden.

package main

import "fmt"

// Dieser `person`-Strukturtyp hat die Felder `name` und `age`.
type person struct {
	name string
	age  int
}

// `newPerson` konstruiert eine neue Person-Struktur mit dem angegebenen Namen.
func newPerson(name string) *person {
	// Sie können sicher einen Zeiger auf eine lokale Variable zurückgeben,
	// da eine lokale Variable über den Gültigkeitsbereich der Funktion hinausleben wird.
	p := person{name: name}
	p.age = 42
	return &p
}

func main() {

	// Diese Syntax erstellt eine neue Struktur.
	fmt.Println(person{"Bob", 20})

	// Sie können die Felder beim Initialisieren einer Struktur benennen.
	fmt.Println(person{name: "Alice", age: 30})

	// Ausgelassene Felder werden mit dem Nullwert initialisiert.
	fmt.Println(person{name: "Fred"})

	// Ein `&`-Prefix liefert einen Zeiger auf die Struktur.
	fmt.Println(&person{name: "Ann", age: 40})

	// Es ist üblich, die Erstellung neuer Strukturen in Konstruktorfunktionen zu kapseln
	fmt.Println(newPerson("Jon"))

	// Zugriff auf Strukturfelder mit einem Punkt.
	s := person{name: "Sean", age: 50}
	fmt.Println(s.name)

	// Sie können auch Punkte mit Strukturzeigern verwenden - die
	// Zeiger werden automatisch aufgelöst.
	sp := &s
	fmt.Println(sp.age)

	// Strukturen sind veränderbar.
	sp.age = 51
	fmt.Println(sp.age)
}

```
