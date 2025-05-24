# Hashes SHA256

Dado uma string, calcule seu hash SHA256.

- O programa deve importar os pacotes `crypto/sha256` e `fmt`.
- O programa deve usar a função `sha256.New()` para criar um novo hash.
- O programa deve usar a função `Write` para escrever os bytes da string no hash.
- O programa deve usar a função `Sum` para obter o resultado final do hash como uma fatia de bytes (byte slice).
- O programa deve imprimir a string original e o resultado do hash em formato hexadecimal.

```sh
# Executar o programa calcula o hash e o imprime em
# um formato hexadecimal legível.
$ go run sha256-hashes.go
sha256 this string
1af1dfa857bf1d8814fe1af8983c18080019922e557f15a8a...

# Você pode calcular outros hashes usando um padrão semelhante ao
# mostrado acima. Por exemplo, para calcular
# hashes SHA512, importe `crypto/sha512` e use
# `sha512.New()`.

# Observe que, se você precisar de hashes criptograficamente seguros,
# você deve pesquisar cuidadosamente a
# [força do hash](https://en.wikipedia.org/wiki/Cryptographic_hash_function)!
```

Aqui está o código completo:

```go
// Os [_hashes SHA256_](https://en.wikipedia.org/wiki/SHA-2) são
// frequentemente usados para calcular identidades curtas para blocos
// binários ou de texto. Por exemplo, os certificados TLS/SSL usam SHA256
// para calcular a assinatura de um certificado. Veja como calcular
// hashes SHA256 em Go.

package main

// Go implementa várias funções de hash em vários
// pacotes `crypto/*`.
import (
	"crypto/sha256"
	"fmt"
)

func main() {
	s := "sha256 this string"

	// Aqui começamos com um novo hash.
	h := sha256.New()

	// `Write` espera bytes. Se você tiver uma string `s`,
	// use `[]byte(s)` para convertê-la em bytes.
	h.Write([]byte(s))

	// Isso obtém o resultado final do hash como uma fatia de
	// bytes. O argumento para `Sum` pode ser usado para anexar
	// a uma fatia de bytes existente: geralmente não é necessário.
	bs := h.Sum(nil)

	fmt.Println(s)
	fmt.Printf("%x\n", bs)
}

```
