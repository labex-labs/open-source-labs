# Variáveis de Ambiente

Neste laboratório, você precisará definir, obter e listar variáveis de ambiente.

- Use `os.Setenv` para definir um par chave/valor.
- Use `os.Getenv` para obter um valor para uma chave.
- Use `os.Environ` para listar todos os pares chave/valor no ambiente.
- Use `strings.SplitN` para dividir a chave e o valor.

```sh
# Executar o programa mostra que pegamos o valor
# para `FOO` que definimos no programa, mas que
# `BAR` está vazio.
$ go run environment-variables.go
FOO: 1
BAR:

# A lista de chaves no ambiente dependerá da sua
# máquina específica.
TERM_PROGRAM
PATH
SHELL
...
FOO

# Se definirmos `BAR` no ambiente primeiro, o programa em execução
# pega esse valor.
$ BAR=2 go run environment-variables.go
FOO: 1
BAR: 2
...
```

A seguir, o código completo:

```go
// [Variáveis de ambiente](https://en.wikipedia.org/wiki/Environment_variable)
// são um mecanismo universal para [transmitir informações de configuração
// para programas Unix](https://www.12factor.net/config).
// Vamos ver como definir, obter e listar variáveis de ambiente.

package main

import (
	"fmt"
	"os"
	"strings"
)

func main() {

	// Para definir um par chave/valor, use `os.Setenv`. Para obter um
	// valor para uma chave, use `os.Getenv`. Isso retornará
	// uma string vazia se a chave não estiver presente no
	// ambiente.
	os.Setenv("FOO", "1")
	fmt.Println("FOO:", os.Getenv("FOO"))
	fmt.Println("BAR:", os.Getenv("BAR"))

	// Use `os.Environ` para listar todos os pares chave/valor no
	// ambiente. Isso retorna uma fatia de strings na
	// forma `KEY=value`. Você pode usar `strings.SplitN` para
	// obter a chave e o valor. Aqui imprimimos todas as chaves.
	fmt.Println()
	for _, e := range os.Environ() {
		pair := strings.SplitN(e, "=", 2)
		fmt.Println(pair[0])
	}
}
```
