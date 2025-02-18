# SHA256-Hashes

Gegeben sei eine Zeichenkette. Berechne ihren SHA256-Hash.

- Das Programm sollte die Pakete `crypto/sha256` und `fmt` importieren.
- Das Programm sollte die Funktion `sha256.New()` verwenden, um einen neuen Hash zu erstellen.
- Das Programm sollte die Funktion `Write` verwenden, um die Bytes der Zeichenkette in den Hash zu schreiben.
- Das Programm sollte die Funktion `Sum` verwenden, um das endgültige Hash-Ergebnis als Byte-Slice zu erhalten.
- Das Programm sollte die ursprüngliche Zeichenkette und das Hash-Ergebnis im hexadezimalen Format ausgeben.

```sh
# Wenn das Programm ausgeführt wird, wird der Hash berechnet und in
# einem menschenlesbaren hexadezimalen Format ausgegeben.
$ go run sha256-hashes.go
sha256 this string
1af1dfa857bf1d8814fe1af8983c18080019922e557f15a8a...

# Sie können andere Hashes berechnen, indem Sie ein ähnliches Muster wie
# das oben gezeigte verwenden. Beispielsweise können Sie um SHA512-Hashes
# zu berechnen, `crypto/sha512` importieren und `sha512.New()` verwenden.

# Beachten Sie, dass Sie, wenn Sie kryptografisch sichere Hashes benötigen,
# sorgfältig recherchieren sollten
# [Hashstärke](https://en.wikipedia.org/wiki/Cryptographic_hash_function)!
```

Hier ist der vollständige Code:

```go
// [_SHA256-Hashes_](https://en.wikipedia.org/wiki/SHA-2) werden
// häufig verwendet, um kurze Identitäten für Binär- oder Textdatenmengen
// zu berechnen. Beispielsweise verwenden TLS/SSL-Zertifikate SHA256,
// um die Signatur eines Zertifikats zu berechnen. Hier erfahren Sie, wie
// Sie SHA256-Hashes in Go berechnen.

package main

// Go implementiert mehrere Hash-Funktionen in verschiedenen
// `crypto/*`-Paketen.
import (
	"crypto/sha256"
	"fmt"
)

func main() {
	s := "sha256 this string"

	// Hier beginnen wir mit einem neuen Hash.
	h := sha256.New()

	// `Write` erwartet Bytes. Wenn Sie eine Zeichenkette `s` haben,
	// verwenden Sie `[]byte(s)`, um sie in Bytes umzuwandeln.
	h.Write([]byte(s))

	// Dies gibt das endgültige Hash-Ergebnis als Byte-Slice zurück.
	// Das Argument für `Sum` kann verwendet werden, um an eine
	// vorhandene Byte-Slice anzuhängen: normalerweise ist dies nicht erforderlich.
	bs := h.Sum(nil)

	fmt.Println(s)
	fmt.Printf("%x\n", bs)
}

```
