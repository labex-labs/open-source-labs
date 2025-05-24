# Strings e Runes

O problema a ser resolvido neste laboratório é entender como trabalhar com strings e runes em Go. Especificamente, o laboratório abordará como obter o comprimento de uma string, como indexar em uma string, como contar o número de runes em uma string e como iterar sobre as runes em uma string.

Para completar este laboratório, você precisará:

- Uma compreensão básica da sintaxe Go
- Conhecimento de strings e runes em Go
- A biblioteca padrão Go

```sh
$ go run strings-and-runes.go
Len: 18
e0 b8 aa e0 b8 a7 e0 b8 b1 e0 b8 aa e0 b8 94 e0 b8 b5
Rune count: 6
U+0E2A 'ส' starts at 0
U+0E27 'ว' starts at 3
U+0E31 'ั' starts at 6
U+0E2A 'ส' starts at 9
U+0E14 'ด' starts at 12
U+0E35 'ี' starts at 15

Using DecodeRuneInString
U+0E2A 'ส' starts at 0
found so sua
U+0E27 'ว' starts at 3
U+0E31 'ั' starts at 6
U+0E2A 'ส' starts at 9
found so sua
U+0E14 'ด' starts at 12
U+0E35 'ี' starts at 15
```

A seguir, o código completo:

```go
// Uma string Go é uma fatia de bytes somente leitura. A linguagem
// e a biblioteca padrão tratam strings de forma especial - como
// contêineres de texto codificados em [UTF-8](https://en.wikipedia.org/wiki/UTF-8).
// Em outras linguagens, strings são feitas de "caracteres".
// Em Go, o conceito de um caractere é chamado de `rune` - é
// um inteiro que representa um ponto de código Unicode.
// [Esta postagem do blog Go](https://go.dev/blog/strings) é uma boa
// introdução ao tópico.

package main

import (
	"fmt"
	"unicode/utf8"
)

func main() {

	// `s` é uma `string` atribuída a um valor literal
	// representando a palavra "olá" em tailandês
	// idioma. Literais de string Go são UTF-8
	// texto codificado.
	const s = "สวัสดี"

	// Como strings são equivalentes a `[]byte`, isso
	// produzirá o comprimento dos bytes brutos armazenados dentro.
	fmt.Println("Len:", len(s))

	// Indexar em uma string produz os valores de byte brutos em
	// cada índice. Este loop gera os valores hexadecimais de todos
	// os bytes que constituem os pontos de código em `s`.
	for i := 0; i < len(s); i++ {
		fmt.Printf("%x ", s[i])
	}
	fmt.Println()

	// Para contar quantas _runes_ estão em uma string, podemos usar
	// o pacote `utf8`. Observe que o tempo de execução de
	// `RuneCountInString` depende do tamanho da string,
	// porque ele precisa decodificar cada rune UTF-8 sequencialmente.
	// Alguns caracteres tailandeses são representados por vários UTF-8
	// pontos de código, então o resultado desta contagem pode ser surpreendente.
	fmt.Println("Rune count:", utf8.RuneCountInString(s))

	// Um loop `range` lida com strings especialmente e decodifica
	// cada `rune` junto com seu deslocamento na string.
	for idx, runeValue := range s {
		fmt.Printf("%#U starts at %d\n", runeValue, idx)
	}

	// Podemos alcançar a mesma iteração usando o
	// função `utf8.DecodeRuneInString` explicitamente.
	fmt.Println("\nUsing DecodeRuneInString")
	for i, w := 0, 0; i < len(s); i += w {
		runeValue, width := utf8.DecodeRuneInString(s[i:])
		fmt.Printf("%#U starts at %d\n", runeValue, i)
		w = width

		// Isso demonstra a passagem de um valor `rune` para uma função.
		examineRune(runeValue)
	}
}

func examineRune(r rune) {

	// Valores entre aspas simples são _literais de rune_. Nós
	// pode comparar um valor `rune` a um literal de rune diretamente.
	if r == 't' {
		fmt.Println("found tee")
	} else if r == 'ส' {
		fmt.Println("found so sua")
	}
}
```
