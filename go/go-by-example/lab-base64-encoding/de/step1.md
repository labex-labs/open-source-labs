# Base64-Kodierung

Sie müssen ein Golang-Programm schreiben, das einen gegebenen String mit der standardmäßigen und der URL-kompatiblen Base64-Kodierung codiert und decodiert.

- Das Programm sollte das `encoding/base64`-Paket mit dem Namen `b64` importieren, statt des Standardnamens `base64`.
- Das Programm sollte den gegebenen String mit der standardmäßigen und der URL-kompatiblen Base64-Kodierung codieren.
- Das Programm sollte die codierten Strings mit der standardmäßigen und der URL-kompatiblen Base64-Dekodierung decodieren.
- Das Programm sollte die codierten und decodierten Strings in der Konsole ausgeben.

```sh
# Der String codiert sich mit den standardmäßigen und
# URL-basierten Base64-Codierern zu leicht unterschiedlichen
# Werten (Endung `+` vs `-`), aber beide decodieren
# wie gewünscht zum ursprünglichen String.
$ go run base64-encoding.go
YWJjMTIzIT8kKiYoKSctPUB+
abc123!?$*&()'-=@~

YWJjMTIzIT8kKiYoKSctPUB-
abc123!?$*&()'-=@~

```

Hier ist der vollständige Code:

```go
// Go bietet eine integrierte Unterstützung für die [Base64-
// Kodierung/Dekodierung](https://en.wikipedia.org/wiki/Base64).

package main

// Diese Syntax importiert das `encoding/base64`-Paket mit
// dem Namen `b64` statt des Standardnamens `base64`. Dies
// spart uns etwas Platz unten.
import (
	b64 "encoding/base64"
	"fmt"
)

func main() {

	// Hier ist der `string`, den wir codieren/decodieren werden.
	data := "abc123!?$*&()'-=@~"

	// Go unterstützt sowohl die standardmäßige als auch die
	// URL-kompatible Base64. So codieren wir mit dem
	// standardmäßigen Codierer. Der Codierer erfordert ein
	// `[]byte`, also konvertieren wir unseren `string` in
	// diesen Typ.
	sEnc := b64.StdEncoding.EncodeToString([]byte(data))
	fmt.Println(sEnc)

	// Die Dekodierung kann einen Fehler zurückgeben, den Sie
	// überprüfen können, wenn Sie nicht bereits wissen, dass
	// die Eingabe gut geformt ist.
	sDec, _ := b64.StdEncoding.DecodeString(sEnc)
	fmt.Println(string(sDec))
	fmt.Println()

	// Dies codiert/decodiert mit einem URL-kompatiblen
	// Base64-Format.
	uEnc := b64.URLEncoding.EncodeToString([]byte(data))
	fmt.Println(uEnc)
	uDec, _ := b64.URLEncoding.DecodeString(uEnc)
	fmt.Println(string(uDec))
}

```
