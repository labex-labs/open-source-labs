# Codificação Base64

Você deve escrever um programa Golang que codifica e decodifica uma determinada string usando a codificação base64 padrão e compatível com URL.

- O programa deve importar o pacote `encoding/base64` com o nome `b64` em vez do padrão `base64`.
- O programa deve codificar a string fornecida usando a codificação base64 padrão e compatível com URL.
- O programa deve decodificar a string codificada usando a decodificação base64 padrão e compatível com URL.
- O programa deve imprimir as strings codificadas e decodificadas no console.

```sh
# A string é codificada em valores ligeiramente diferentes com os
# codificadores base64 padrão e URL (trailing `+` vs `-`)
# mas ambos decodificam para a string original como desejado.
```

Aqui está o código completo:

```go
// Go fornece suporte embutido para [base64
// codificação/decodificação](https://en.wikipedia.org/wiki/Base64).

package main

// Esta sintaxe importa o pacote `encoding/base64` com
// o nome `b64` em vez do padrão `base64`. Isso irá
// nos poupar algum espaço abaixo.
import (
	b64 "encoding/base64"
	"fmt"
)

func main() {

	// Aqui está a `string` que vamos codificar/decodificar.
	data := "abc123!?$*&()'-=@~"

	// Go suporta base64 padrão e compatível com URL
	// base64. Veja como codificar usando o padrão
	// codificador. O codificador requer um `[]byte` então nós
	// convertemos nossa `string` para esse tipo.
	sEnc := b64.StdEncoding.EncodeToString([]byte(data))
	fmt.Println(sEnc)

	// A decodificação pode retornar um erro, que você pode verificar
	// se você já não sabe que a entrada é
	// bem formada.
	sDec, _ := b64.StdEncoding.DecodeString(sEnc)
	fmt.Println(string(sDec))
	fmt.Println()

	// Isso codifica/decodifica usando um base64 compatível com URL
	// formato.
	uEnc := b64.URLEncoding.EncodeToString([]byte(data))
	fmt.Println(uEnc)
	uDec, _ := b64.URLEncoding.DecodeString(uEnc)
	fmt.Println(string(uDec))
}
```
