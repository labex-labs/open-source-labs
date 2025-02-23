# Text Templates

In diesem Lab müssen Sie die Verwendung des Pakets `text/template` demonstrieren, um dynamischen Inhalt zu generieren.

- Verwenden Sie das Paket `text/template`, um dynamischen Inhalt zu generieren.
- Verwenden Sie die Funktion `template.Must`, um einen Fehler auszulösen, wenn `Parse` einen Fehler zurückgibt.
- Verwenden Sie die Aktion `{{.FieldName}}`, um auf die Felder von Structs zuzugreifen.
- Verwenden Sie die Aktion `{{if.. -}} ja {{else -}} nein {{end}}\n`, um bedingte Ausführung für Vorlagen zu ermöglichen.
- Verwenden Sie die Aktion `{{range.}}{{.}} {{end}}\n`, um durch Slices, Arrays, Maps oder Kanäle zu iterieren.

```sh
$ go run templates.go
Wert: einiger Text
Wert: 5
Wert: [Go Rust C++ C#]
Name: Jane Doe
Name: Mickey Mouse
ja
nein
Range: Go Rust C++ C#
```

Hier ist der vollständige Code:

```go
// Go bietet eine integrierte Unterstützung für die Erstellung von dynamischem Inhalt oder das Anzeigen von benutzerdefinierter Ausgabe an den Benutzer mit dem Paket `text/template`. Ein verwandtes Paket
// namens `html/template` bietet die gleiche API, hat jedoch zusätzliche Sicherheitsmerkmale und sollte zur Generierung von HTML verwendet werden.

package main

import (
	"os"
	"text/template"
)

func main() {

	// Wir können eine neue Vorlage erstellen und ihren Körper aus
	// einem String analysieren.
	// Vorlagen sind eine Mischung aus statischem Text und "Aktionen", die in
	// `{{...}}` eingeschlossen sind und zur dynamischen Einfügung von Inhalt verwendet werden.
	t1 := template.New("t1")
	t1, err := t1.Parse("Wert ist {{.}}\n")
	if err!= nil {
		panic(err)
	}

	// Alternativ können wir die Funktion `template.Must` verwenden, um
	// einen Fehler auszulösen, wenn `Parse` einen Fehler zurückgibt. Dies ist besonders
	// nützlich für Vorlagen, die im globalen Bereich initialisiert werden.
	t1 = template.Must(t1.Parse("Wert: {{.}}\n"))

	// Indem wir die Vorlage "ausführen", generieren wir ihren Text mit
	// spezifischen Werten für ihre Aktionen. Die Aktion `{{.}}` wird
	// durch den Wert ersetzt, der als Parameter an `Execute` übergeben wird.
	t1.Execute(os.Stdout, "einiger Text")
	t1.Execute(os.Stdout, 5)
	t1.Execute(os.Stdout, []string{
		"Go",
		"Rust",
		"C++",
		"C#",
	})

	// Hilfsfunktion, die wir unten verwenden werden.
	Create := func(name, t string) *template.Template {
		return template.Must(template.New(name).Parse(t))
	}

	// Wenn die Daten ein Struct sind, können wir die Aktion `{{.FieldName}}` verwenden, um auf
	// seine Felder zuzugreifen. Die Felder müssen exportiert sein, um beim Ausführen einer Vorlage zugänglich zu sein.
	t2 := Create("t2", "Name: {{.Name}}\n")

	t2.Execute(os.Stdout, struct {
		Name string
	}{"Jane Doe"})

	// Das gleiche gilt für Maps; bei Maps gibt es keine Einschränkung für den
	// Fall der Schlüsselnamen.
	t2.Execute(os.Stdout, map[string]string{
		"Name": "Mickey Mouse",
	})

	// if/else ermöglichen die bedingte Ausführung von Vorlagen. Ein Wert wird als
	// falsch betrachtet, wenn es der Standardwert eines Typs ist, wie z. B. 0, eine leere Zeichenkette,
	// ein nil-Zeiger usw.
	// Dieses Beispiel zeigt auch eine andere
	// Eigenschaft von Vorlagen: das Verwenden von `-` in Aktionen, um Leerzeichen zu entfernen.
	t3 := Create("t3",
		"{{if.. -}} ja {{else -}} nein {{end}}\n")
	t3.Execute(os.Stdout, "nicht leer")
	t3.Execute(os.Stdout, "")

	// range-Blöcke ermöglichen es uns, durch Slices, Arrays, Maps oder Kanäle zu iterieren. Innerhalb
	// des range-Blocks ist `{{.}}` auf den aktuellen Iterationsgegenstand gesetzt.
	t4 := Create("t4",
		"Range: {{range.}}{{.}} {{end}}\n")
	t4.Execute(os.Stdout,
		[]string{
			"Go",
			"Rust",
			"C++",
			"C#",
		})
}

```
