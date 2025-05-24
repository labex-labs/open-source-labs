# Exit (Saída)

O problema a ser resolvido neste laboratório é sair de um programa Go com um código de status específico usando a função `os.Exit`.

Para completar este laboratório, você precisará ter um conhecimento básico de programação Go e do pacote `os`.

```sh
# Se você executar `exit.go` usando `go run`, a saída
# será capturada por `go` e impressa.
$ go run exit.go
exit status 3

# Ao construir e executar um binário, você pode ver
# o status no terminal.
$ go build exit.go
$ ./exit
$ echo $?
3

# Observe que o `!` do nosso programa nunca foi impresso.
```

A seguir, o código completo:

```go
// Use `os.Exit` para sair imediatamente com um dado
// status.

package main

import (
	"fmt"
	"os"
)

func main() {

	// `defer`s _não_ serão executados ao usar `os.Exit`, então
	// este `fmt.Println` nunca será chamado.
	defer fmt.Println("!")

	// Saia com o status 3.
	os.Exit(3)
}

// Observe que, ao contrário de, por exemplo, C, Go não usa um valor inteiro
// de retorno de `main` para indicar o status de saída. Se
// você quiser sair com um status diferente de zero, você deve
// usar `os.Exit`.
```
