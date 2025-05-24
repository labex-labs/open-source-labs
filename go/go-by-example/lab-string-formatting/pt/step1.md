# Formatação de Strings

Você deve formatar diferentes tipos de dados usando vários verbos de formatação em Golang.

- Você deve usar o pacote `fmt` para formatar os dados.
- Você deve usar o verbo de formatação correto para cada tipo de dado.
- Você deve ser capaz de formatar inteiros, floats, strings e structs.
- Você deve ser capaz de controlar a largura e a precisão da saída.
- Você deve ser capaz de justificar à esquerda ou à direita a saída.

```sh
$ go run string-formatting.go
struct1: {1 2}
struct2: {x:1 y:2}
struct3: main.point{x:1, y:2}
type: main.point
bool: true
int: 123
bin: 1110
char: !
hex: 1c8
float1: 78.900000
float2: 1.234000e+08
float3: 1.234000E+08
str1: "string"
str2: "\"string\""
str3: 6865782074686973
pointer: 0xc0000ba000
width1: | 12 | 345 \
  | width2: | 1.20 | 3.45 \
  | width3: | 1.20 | 3.45 \
  | width4: | foo | b \
  | width5: | foo | b \
  | sprintf: a string
io: an error
```

Abaixo está o código completo:

```go
// Go oferece excelente suporte para formatação de strings na
// tradição `printf`. Aqui estão alguns exemplos de
// tarefas comuns de formatação de strings.

package main

import (
	"fmt"
	"os"
)

type point struct {
	x, y int
}

func main() {

	// Go oferece vários "verbos" de impressão projetados para
	// formatar valores gerais do Go. Por exemplo, isso imprime
	// uma instância de nossa struct `point`.
	p := point{1, 2}
	fmt.Printf("struct1: %v\n", p)

	// Se o valor for uma struct, a variante `%+v` irá
	// incluir os nomes dos campos da struct.
	fmt.Printf("struct2: %+v\n", p)

	// A variante `%#v` imprime uma representação de sintaxe Go
	// do valor, ou seja, o trecho de código-fonte que
	// produziria esse valor.
	fmt.Printf("struct3: %#v\n", p)

	// Para imprimir o tipo de um valor, use `%T`.
	fmt.Printf("type: %T\n", p)

	// A formatação de booleanos é direta.
	fmt.Printf("bool: %t\n", true)

	// Existem muitas opções para formatar inteiros.
	// Use `%d` para formatação padrão, base 10.
	fmt.Printf("int: %d\n", 123)

	// Isso imprime uma representação binária.
	fmt.Printf("bin: %b\n", 14)

	// Isso imprime o caractere correspondente ao
	// inteiro fornecido.
	fmt.Printf("char: %c\n", 33)

	// `%x` fornece codificação hexadecimal.
	fmt.Printf("hex: %x\n", 456)

	// Existem também várias opções de formatação para
	// floats. Para formatação decimal básica, use `%f`.
	fmt.Printf("float1: %f\n", 78.9)

	// `%e` e `%E` formatam o float em (versões ligeiramente
	// diferentes de) notação científica.
	fmt.Printf("float2: %e\n", 123400000.0)
	fmt.Printf("float3: %E\n", 123400000.0)

	// Para impressão básica de strings, use `%s`.
	fmt.Printf("str1: %s\n", "\"string\"")

	// Para colocar strings entre aspas duplas como no código-fonte Go, use `%q`.
	fmt.Printf("str2: %q\n", "\"string\"")

	// Assim como com os inteiros vistos anteriormente, `%x` renderiza
	// a string na base 16, com dois caracteres de saída
	// por byte de entrada.
	fmt.Printf("str3: %x\n", "hex this")

	// Para imprimir uma representação de um ponteiro, use `%p`.
	fmt.Printf("pointer: %p\n", &p)

	// Ao formatar números, você frequentemente desejará
	// controlar a largura e a precisão do
	// número resultante. Para especificar a largura de um inteiro, use um
	// número após o `%` no verbo. Por padrão, o
	// resultado será justificado à direita e preenchido com
	// espaços.
	fmt.Printf("width1: |%6d|%6d|\n", 12, 345)

	// Você também pode especificar a largura de floats impressos,
	// embora geralmente você também deseje restringir a
	// precisão decimal ao mesmo tempo com a
	// sintaxe width.precision.
	fmt.Printf("width2: |%6.2f|%6.2f|\n", 1.2, 3.45)

	// Para justificar à esquerda, use a flag `-`.
	fmt.Printf("width3: |%-6.2f|%-6.2f|\n", 1.2, 3.45)

	// Você também pode querer controlar a largura ao formatar
	// strings, especialmente para garantir que elas se alinhem em
	// saída semelhante a uma tabela. Para largura básica justificada à direita.
	fmt.Printf("width4: |%6s|%6s|\n", "foo", "b")

	// Para justificar à esquerda, use a flag `-` como com números.
	fmt.Printf("width5: |%-6s|%-6s|\n", "foo", "b")

	// Até agora, vimos `Printf`, que imprime a
	// string formatada para `os.Stdout`. `Sprintf` formata
	// e retorna uma string sem imprimi-la em nenhum lugar.
	s := fmt.Sprintf("sprintf: a %s", "string")
	fmt.Println(s)

	// Você pode formatar+imprimir para `io.Writers` diferentes de
	// `os.Stdout` usando `Fprintf`.
	fmt.Fprintf(os.Stderr, "io: an %s\n", "error")
}
```
