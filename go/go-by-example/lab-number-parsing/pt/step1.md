# Análise de Números

A análise de números a partir de strings é uma tarefa comum em muitos programas. Este laboratório exige que você use o pacote `strconv` embutido para analisar diferentes tipos de números a partir de strings.

- Use o pacote `strconv` para analisar números de strings.
- Analise um float com `ParseFloat`.
- Analise um int com `ParseInt`.
- Analise um número formatado em hexadecimal com `ParseInt`.
- Analise um int sem sinal com `ParseUint`.
- Analise um int na base 10 com `Atoi`.
- Lide com os erros retornados pelas funções de análise.

```sh
$ go run number-parsing.go
1.234
123
456
789
135
strconv.ParseInt: parsing "wat": invalid syntax

# Em seguida, veremos outra tarefa comum de análise: URLs.
```

A seguir, o código completo:

```go
// Analisar números de strings é uma tarefa básica, mas comum
// em muitos programas; aqui está como fazê-lo em Go.

package main

// O pacote embutido `strconv` fornece a análise de números.
import (
	"fmt"
	"strconv"
)

func main() {

	// Com `ParseFloat`, este `64` informa quantos bits de
	// precisão analisar.
	f, _ := strconv.ParseFloat("1.234", 64)
	fmt.Println(f)

	// Para `ParseInt`, o `0` significa inferir a base da
	// string. `64` exige que o resultado caiba em 64
	// bits.
	i, _ := strconv.ParseInt("123", 0, 64)
	fmt.Println(i)

	// `ParseInt` reconhecerá números formatados em hexadecimal.
	d, _ := strconv.ParseInt("0x1c8", 0, 64)
	fmt.Println(d)

	// Um `ParseUint` também está disponível.
	u, _ := strconv.ParseUint("789", 0, 64)
	fmt.Println(u)

	// `Atoi` é uma função de conveniência para análise básica de
	// `int` na base 10.
	k, _ := strconv.Atoi("135")
	fmt.Println(k)

	// As funções de análise retornam um erro em caso de entrada inválida.
	_, e := strconv.Atoi("wat")
	fmt.Println(e)
}
```
