# Funções de String

Complete o código abaixo para imprimir a saída de várias funções de string fornecidas pelo pacote `strings`.

- Use o pacote `strings` para completar o laboratório.
- Use a função `fmt.Println` para imprimir a saída.
- Não modifique o nome da função ou os parâmetros.

```sh
$ go run string-functions.go
Contains: true
Count: 2
HasPrefix: true
HasSuffix: true
Index: 1
Join: a-b
Repeat: aaaaa
Replace: f00
Replace: f0o
Split: [a b c d e]
ToLower: test
ToUpper: TEST
```

Aqui está o código completo:

```go
// O pacote `strings` da biblioteca padrão fornece muitas
// funções úteis relacionadas a strings. Aqui estão alguns exemplos
// para dar uma ideia do pacote.

package main

import (
	"fmt"
	s "strings"
)

// Nós apelidamos `fmt.Println` para um nome mais curto, pois vamos usá-lo
// muito abaixo.
var p = fmt.Println

func main() {

	// Aqui está uma amostra das funções disponíveis em
	// `strings`. Como estas são funções do
	// pacote, não métodos no próprio objeto string,
	// precisamos passar a string em questão como o primeiro
	// argumento para a função. Você pode encontrar mais
	// funções nos documentos do pacote [`strings`](https://pkg.go.dev/strings).
	p("Contains:  ", s.Contains("test", "es"))
	p("Count:     ", s.Count("test", "t"))
	p("HasPrefix: ", s.HasPrefix("test", "te"))
	p("HasSuffix: ", s.HasSuffix("test", "st"))
	p("Index:     ", s.Index("test", "e"))
	p("Join:      ", s.Join([]string{"a", "b"}, "-"))
	p("Repeat:    ", s.Repeat("a", 5))
	p("Replace:   ", s.Replace("foo", "o", "0", -1))
	p("Replace:   ", s.Replace("foo", "o", "0", 1))
	p("Split:     ", s.Split("a-b-c-d-e", "-"))
	p("ToLower:   ", s.ToLower("TEST"))
	p("ToUpper:   ", s.ToUpper("test"))
}
```
