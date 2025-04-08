# JSON

Sie müssen den bereitgestellten Code vervollständigen, um JSON-Daten in Golang zu kodieren und zu dekodieren. Der Code enthält Beispiele für die Kodierung und Dekodierung von grundlegenden Datentypen sowie benutzerdefinierten Datentypen.

- Grundkenntnisse der Golang-Programmiersprache.
- Vertrautheit mit der Kodierung und Dekodierung von JSON-Daten in Golang.
- Fähigkeit, vorhandenen Golang-Code zu lesen und zu verstehen.

```sh


# Wir haben hier die Grundlagen von JSON in Go behandelt, aber schauen Sie sich den [JSON and Go](https://go.dev/blog/json)
# Blogbeitrag und die [JSON-Paketdokumentation](https://pkg.go.dev/encoding/json)
# für mehr an.
```

Hier ist der vollständige Code:

```go
// Go bietet integrierte Unterstützung für die JSON-Kodierung und
// -Dekodierung, einschließlich von und zu eingebauten und benutzerdefinierten
// Datentypen.

package main

import (
	"encoding/json"
	"fmt"
	"os"
)

// Wir werden diese beiden Structs verwenden, um die Kodierung und
// Dekodierung benutzerdefinierter Typen im Folgenden zu demonstrieren.
type response1 struct {
	Page   int
	Fruits []string
}

// Nur exportierte Felder werden in JSON kodiert/dekodiert.
// Felder müssen mit einem Großbuchstaben beginnen, um exportiert zu werden.
type response2 struct {
	Page   int      `json:"page"`
	Fruits []string `json:"fruits"`
}

func main() {

	// Zunächst betrachten wir die Kodierung von grundlegenden Datentypen in
	// JSON-Strings. Hier sind einige Beispiele für atomare
	// Werte.
	bolB, _ := json.Marshal(true)
	fmt.Println(string(bolB))

	intB, _ := json.Marshal(1)
	fmt.Println(string(intB))

	fltB, _ := json.Marshal(2.34)
	fmt.Println(string(fltB))

	strB, _ := json.Marshal("gopher")
	fmt.Println(string(strB))

	// Und hier sind einige für Slices und Maps, die wie erwartet in JSON-Arrays und -Objekte kodiert werden.
	slcD := []string{"apple", "peach", "pear"}
	slcB, _ := json.Marshal(slcD)
	fmt.Println(string(slcB))

	mapD := map[string]int{"apple": 5, "lettuce": 7}
	mapB, _ := json.Marshal(mapD)
	fmt.Println(string(mapB))

	// Das JSON-Paket kann Ihre benutzerdefinierten Datentypen automatisch kodieren.
	// Es wird nur exportierte Felder in der codierten Ausgabe enthalten und wird standardmäßig
	// diese Namen als JSON-Schlüssel verwenden.
	res1D := &response1{
		Page:   1,
		Fruits: []string{"apple", "peach", "pear"}}
	res1B, _ := json.Marshal(res1D)
	fmt.Println(string(res1B))

	// Sie können Tags bei der Deklaration von Struct-Feldern verwenden,
	// um die codierten JSON-Schlüsselnamen anzupassen. Schauen Sie sich die Definition von `response2` oben an,
	// um ein Beispiel für solche Tags zu sehen.
	res2D := &response2{
		Page:   1,
		Fruits: []string{"apple", "peach", "pear"}}
	res2B, _ := json.Marshal(res2D)
	fmt.Println(string(res2B))

	// Jetzt betrachten wir die Dekodierung von JSON-Daten in Go
	// Werte. Hier ist ein Beispiel für eine generische Datenstruktur.
	byt := []byte(`{"num":6.13,"strs":["a","b"]}`)

	// Wir müssen eine Variable angeben, in die das JSON-Paket
	// die dekodierten Daten ablegen kann. Diese `map[string]interface{}` wird eine Map von Strings
	// zu beliebigen Datentypen halten.
	var dat map[string]interface{}

	// Hier ist die tatsächliche Dekodierung und eine Prüfung auf
	// zugehörige Fehler.
	if err := json.Unmarshal(byt, &dat); err!= nil {
		panic(err)
	}
	fmt.Println(dat)

	// Um die Werte in der dekodierten Map zu verwenden,
	// müssen wir sie in ihren entsprechenden Typ umwandeln.
	// Beispielsweise wandeln wir hier den Wert in `num` in den erwarteten `float64`-Typ um.
	num := dat["num"].(float64)
	fmt.Println(num)

	// Das Zugreifen auf geschachtelte Daten erfordert eine Reihe von
	// Umwandlungen.
	strs := dat["strs"].([]interface{})
	str1 := strs[0].(string)
	fmt.Println(str1)

	// Wir können auch JSON in benutzerdefinierte Datentypen dekodieren.
	// Dies hat den Vorteil, zusätzliche Typsicherheit in unseren Programmen hinzuzufügen und die
	// Notwendigkeit von Typbehauptungen beim Zugriff auf die dekodierten
	// Daten zu eliminieren.
	str := `{"page": 1, "fruits": ["apple", "peach"]}`
	res := response2{}
	json.Unmarshal([]byte(str), &res)
	fmt.Println(res)
	fmt.Println(res.Fruits[0])

	// In den obigen Beispielen haben wir immer Bytes und
	// Strings als Zwischenschritte zwischen den Daten und
	// der JSON-Darstellung auf der Standardausgabe verwendet. Wir können auch
	// JSON-Kodierungen direkt an `os.Writer`s wie
	// `os.Stdout` oder sogar HTTP-Antwortkörpern streamen.
	enc := json.NewEncoder(os.Stdout)
	d := map[string]int{"apple": 5, "lettuce": 7}
	enc.Encode(d)
}

```
