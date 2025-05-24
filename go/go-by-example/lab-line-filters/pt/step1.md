# Filtros de Linha (Line Filters)

O problema a ser resolvido neste laboratório é escrever um programa Go que lê texto de entrada de stdin, capitaliza todas as letras no texto e, em seguida, imprime o texto modificado em stdout.

- O programa deve ler o texto de entrada de stdin.
- O programa deve capitalizar todas as letras no texto de entrada.
- O programa deve imprimir o texto modificado em stdout.

```sh
# Para testar nosso filtro de linha, primeiro crie um arquivo com algumas
# linhas em minúsculas.
$ echo 'hello' > /tmp/lines
$ echo 'filter' >> /tmp/lines

# Em seguida, use o filtro de linha para obter linhas em maiúsculas.
$ cat /tmp/lines | go run line-filters.go
HELLO
FILTER
```

A seguir, o código completo:

```go
// Um _filtro de linha_ é um tipo comum de programa que lê
// a entrada em stdin, processa-a e, em seguida, imprime algum
// resultado derivado em stdout. `grep` e `sed` são filtros de linha
// comuns.

// Aqui está um exemplo de filtro de linha em Go que escreve uma
// versão capitalizada de todo o texto de entrada. Você pode usar este
// padrão para escrever seus próprios filtros de linha em Go.
package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {

	// Envolver o `os.Stdin` sem buffer com um buffer
	// scanner nos dá um método `Scan` conveniente que
	// avança o scanner para o próximo token; que é
	// a próxima linha no scanner padrão.
	scanner := bufio.NewScanner(os.Stdin)

	for scanner.Scan() {
		// `Text` retorna o token atual, aqui a próxima linha,
		// da entrada.
		ucl := strings.ToUpper(scanner.Text())

		// Escreva a linha em maiúsculas.
		fmt.Println(ucl)
	}

	// Verifique se há erros durante o `Scan`. Fim do arquivo é
	// esperado e não relatado por `Scan` como um erro.
	if err := scanner.Err(); err != nil {
		fmt.Fprintln(os.Stderr, "error:", err)
		os.Exit(1)
	}
}
```
