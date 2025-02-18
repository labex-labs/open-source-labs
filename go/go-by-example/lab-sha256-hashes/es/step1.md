# Hashes SHA256

Dada una cadena de texto, calcular su hash SHA256.

- El programa debe importar los paquetes `crypto/sha256` y `fmt`.
- El programa debe utilizar la función `sha256.New()` para crear un nuevo hash.
- El programa debe utilizar la función `Write` para escribir los bytes de la cadena de texto en el hash.
- El programa debe utilizar la función `Sum` para obtener el resultado final del hash como una porción de bytes.
- El programa debe imprimir la cadena de texto original y el resultado del hash en formato hexadecimal.

```sh
# Al ejecutar el programa se calcula el hash y se imprime en
# un formato hexadecimal legible para humanos.
$ go run sha256-hashes.go
sha256 this string
1af1dfa857bf1d8814fe1af8983c18080019922e557f15a8a...

# Puedes calcular otros hashes utilizando un patrón similar al
# mostrado anteriormente. Por ejemplo, para calcular
# hashes SHA512, importa `crypto/sha512` y utiliza
# `sha512.New()`.

# Ten en cuenta que si necesitas hashes criptográficamente seguros,
# debes investigar detenidamente
# [la fortaleza de los hashes](https://en.wikipedia.org/wiki/Cryptographic_hash_function)!
```

A continuación, se muestra el código completo:

```go
// [_Hashes SHA256_](https://en.wikipedia.org/wiki/SHA-2) se
// utilizan con frecuencia para calcular identificadores cortos para bloques binarios
// o de texto. Por ejemplo, los certificados TLS/SSL utilizan SHA256
// para calcular la firma de un certificado. Aquí se muestra cómo calcular
// hashes SHA256 en Go.

package main

// Go implementa varias funciones hash en varios
// paquetes `crypto/*`.
import (
	"crypto/sha256"
	"fmt"
)

func main() {
	s := "sha256 this string"

	// Aquí comenzamos con un nuevo hash.
	h := sha256.New()

	// `Write` espera bytes. Si tienes una cadena `s`,
	// utiliza `[]byte(s)` para convertirla en bytes.
	h.Write([]byte(s))

	// Esto obtiene el resultado final del hash como una porción
	// de bytes. El argumento de `Sum` se puede utilizar para agregar
	// a una porción de bytes existente: por lo general, no es necesario.
	bs := h.Sum(nil)

	fmt.Println(s)
	fmt.Printf("%x\n", bs)
}

```
