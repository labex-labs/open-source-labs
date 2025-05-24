# Argumentos de Linha de Comando

O programa atualmente imprime os argumentos de linha de comando brutos que lhe são passados. No entanto, ele precisa ser modificado para imprimir argumentos específicos com base em seu índice.

- Conhecimento básico de Golang
- Familiaridade com argumentos de linha de comando

```sh
# Para experimentar com argumentos de linha de comando, é melhor
# construir um binário com `go build` primeiro.
$ go build command-line-arguments.go
$ ./command-line-arguments a b c d
[./command-line-arguments a b c d]
[a b c d]
c

# Em seguida, veremos um processamento de linha de comando mais avançado
# com flags.
```

A seguir, o código completo:

```go
// Os [_argumentos de linha de comando_](https://en.wikipedia.org/wiki/Command-line_interface#Arguments)
// são uma forma comum de parametrizar a execução de programas.
// Por exemplo, `go run hello.go` usa os argumentos `run` e
// `hello.go` para o programa `go`.

package main

import (
	"fmt"
	"os"
)

func main() {

	// `os.Args` fornece acesso aos argumentos de linha de comando brutos.
	// Observe que o primeiro valor nesta fatia
	// é o caminho para o programa, e `os.Args[1:]`
	// contém os argumentos para o programa.
	argsWithProg := os.Args
	argsWithoutProg := os.Args[1:]

	// Você pode obter argumentos individuais com indexação normal.
	arg := os.Args[3]

	fmt.Println(argsWithProg)
	fmt.Println(argsWithoutProg)
	fmt.Println(arg)
}
```
