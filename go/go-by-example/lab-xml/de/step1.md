# XML

Sie müssen eine Struktur namens `Plant` erstellen, die in XML abgebildet werden kann. Die Struktur sollte die folgenden Felder haben:

- `Id` (int) - ein XML-Attribut
- `Name` (string) - ein geschachtelter XML-Element
- `Origin` ([]string) - ein geschachtelter XML-Element

Sie sollten auch eine Struktur namens `Nesting` erstellen, die eine Liste von `Plant`-Strukturen enthält. Die `Nesting`-Struktur sollte einem XML-Element namens `nesting` zugeordnet werden, und die `Plant`-Strukturen sollten unter `<parent><child>...` geschachtelt werden.

Sie sollten dann Code schreiben, um die `Plant`- und `Nesting`-Strukturen in XML zu marshalisieren und XML-Daten in die `Plant`-Struktur zu unmarshalieren.

- Die `Plant`-Struktur sollte einem XML-Element namens `plant` zugeordnet werden.
- Das `Id`-Feld der `Plant`-Struktur sollte einem XML-Attribut namens `id` zugeordnet werden.
- Das `Name`-Feld der `Plant`-Struktur sollte einem geschachtelten XML-Element namens `name` zugeordnet werden.
- Das `Origin`-Feld der `Plant`-Struktur sollte einem geschachtelten XML-Element namens `origin` zugeordnet werden.
- Die `Nesting`-Struktur sollte einem XML-Element namens `nesting` zugeordnet werden.
- Die `Plant`-Strukturen in der `Nesting`-Liste sollten unter `<parent><child>...` geschachtelt werden.

```sh
$ go run xml.go
 <plant id="27">
   <name>Coffee</name>
   <origin>Ethiopia</origin>
   <origin>Brazil</origin>
 </plant>
<?xml version="1.0" encoding="UTF-8"?>
 <plant id="27">
   <name>Coffee</name>
   <origin>Ethiopia</origin>
   <origin>Brazil</origin>
 </plant>
Plant id=27, name=Coffee, origin=[Ethiopia Brazil]
 <nesting>
   <parent>
     <child>
       <plant id="27">
         <name>Coffee</name>
         <origin>Ethiopia</origin>
         <origin>Brazil</origin>
       </plant>
       <plant id="81">
         <name>Tomato</name>
         <origin>Mexico</origin>
         <origin>California</origin>
       </plant>
     </child>
   </parent>
 </nesting>

```

Hier ist der vollständige Code:

```go
// Go bietet in-built Unterstützung für XML und XML-ähnliche
// Formate mit dem `encoding.xml`-Paket.

package main

import (
	"encoding/xml"
	"fmt"
)

// Plant wird in XML abgebildet. Ähnlich wie in den
// JSON-Beispielen enthalten die Feldtags Direktiven für den
// Encoder und Decoder. Hier verwenden wir einige spezielle
// Funktionen des XML-Pakets: Das `XMLName`-Feldname bestimmt
// den Namen des XML-Elements, das diese Struktur repräsentiert;
// `id,attr` bedeutet, dass das `Id`-Feld ein XML-
// _Attribut_ ist, statt eines geschachtelten Elements.
type Plant struct {
	XMLName xml.Name `xml:"plant"`
	Id      int      `xml:"id,attr"`
	Name    string   `xml:"name"`
	Origin  []string `xml:"origin"`
}

func (p Plant) String() string {
	return fmt.Sprintf("Plant id=%v, name=%v, origin=%v",
		p.Id, p.Name, p.Origin)
}

func main() {
	coffee := &Plant{Id: 27, Name: "Coffee"}
	coffee.Origin = []string{"Ethiopia", "Brazil"}

	// Emit XML representing our plant; using
	// `MarshalIndent` to produce a more
	// human-readable output.
	out, _ := xml.MarshalIndent(coffee, " ", "  ")
	fmt.Println(string(out))

	// To add a generic XML header to the output, append
	// it explicitly.
	fmt.Println(xml.Header + string(out))

	// Use `Unmarshal` to parse a stream of bytes with XML
	// into a data structure. If the XML is malformed or
	// cannot be mapped onto Plant, a descriptive error
	// will be returned.
	var p Plant
	if err := xml.Unmarshal(out, &p); err!= nil {
		panic(err)
	}
	fmt.Println(p)

	tomato := &Plant{Id: 81, Name: "Tomato"}
	tomato.Origin = []string{"Mexico", "California"}

	// The `parent>child>plant` field tag tells the encoder
	// to nest all `plant`s under `<parent><child>...`
	type Nesting struct {
		XMLName xml.Name `xml:"nesting"`
		Plants  []*Plant `xml:"parent>child>plant"`
	}

	nesting := &Nesting{}
	nesting.Plants = []*Plant{coffee, tomato}

	out, _ = xml.MarshalIndent(nesting, " ", "  ")
	fmt.Println(string(out))
}

```
