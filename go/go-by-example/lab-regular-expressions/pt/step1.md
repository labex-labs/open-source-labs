# Expressões Regulares (Regular Expressions)

O laboratório exige que você complete o código para realizar várias tarefas relacionadas a expressões regulares em Golang.

- Use o pacote `regexp` para realizar tarefas relacionadas a expressões regulares.
- Use `MatchString` para testar se um padrão corresponde a uma string.
- Use `Compile` para otimizar uma struct `Regexp`.
- Use `MatchString` para testar uma correspondência como `Compile`.
- Use `FindString` para encontrar a correspondência para a expressão regular.
- Use `FindStringIndex` para encontrar a primeira correspondência e retornar os índices de início e fim da correspondência em vez do texto correspondente.
- Use `FindStringSubmatch` para retornar informações para `p([a-z]+)ch` e `([a-z]+)`.
- Use `FindStringSubmatchIndex` para retornar informações sobre os índices das correspondências e subcorrespondências.
- Use `FindAllString` para encontrar todas as correspondências para uma expressão regular.
- Use `FindAllStringSubmatchIndex` para aplicar a todas as correspondências na entrada, não apenas a primeira.
- Use `Match` para testar uma correspondência com argumentos `[]byte` e remover `String` do nome da função.
- Use `MustCompile` para criar variáveis globais com expressões regulares.
- Use `ReplaceAllString` para substituir subconjuntos de strings por outros valores.
- Use `ReplaceAllFunc` para transformar o texto correspondente com uma função fornecida.

```sh
# Para uma referência completa sobre expressões regulares em Go, verifique
# a documentação do pacote [`regexp`](https://pkg.go.dev/regexp).
```

Aqui está o código completo:

```go
// Go oferece suporte integrado para [expressões regulares](https://en.wikipedia.org/wiki/Regular_expression).
// Aqui estão alguns exemplos de tarefas comuns relacionadas a regexp
// em Go.

package main

import (
	"bytes"
	"fmt"
	"regexp"
)

func main() {

	// Isso testa se um padrão corresponde a uma string.
	match, _ := regexp.MatchString("p([a-z]+)ch", "peach")
	fmt.Println(match)

	// Acima, usamos um padrão de string diretamente, mas para
	// outras tarefas de regexp, você precisará `Compile` uma
	// struct `Regexp` otimizada.
	r, _ := regexp.Compile("p([a-z]+)ch")

	// Muitos métodos estão disponíveis nessas structs. Aqui está
	// um teste de correspondência como vimos anteriormente.
	fmt.Println(r.MatchString("peach"))

	// Isso encontra a correspondência para a expressão regular.
	fmt.Println(r.FindString("peach punch"))

	// Isso também encontra a primeira correspondência, mas retorna o
	// índices de início e fim para a correspondência em vez do
	// texto correspondente.
	fmt.Println("idx:", r.FindStringIndex("peach punch"))

	// As variantes `Submatch` incluem informações sobre
	// tanto as correspondências de padrão completo quanto as subcorrespondências
	// dentro dessas correspondências. Por exemplo, isso retornará
	// informações para `p([a-z]+)ch` e `([a-z]+)`.
	fmt.Println(r.FindStringSubmatch("peach punch"))

	// Da mesma forma, isso retornará informações sobre o
	// índices de correspondências e subcorrespondências.
	fmt.Println(r.FindStringSubmatchIndex("peach punch"))

	// As variantes `All` dessas funções se aplicam a todas as
	// correspondências na entrada, não apenas a primeira. Para
	// por exemplo, encontrar todas as correspondências para uma expressão regular.
	fmt.Println(r.FindAllString("peach punch pinch", -1))

	// Essas variantes `All` estão disponíveis para as outras
	// funções que vimos acima também.
	fmt.Println("all:", r.FindAllStringSubmatchIndex(
		"peach punch pinch", -1))

	// Fornecer um inteiro não negativo como o segundo
	// argumento para essas funções limitará o número
	// de correspondências.
	fmt.Println(r.FindAllString("peach punch pinch", 2))

	// Nossos exemplos acima tinham argumentos de string e usavam
	// nomes como `MatchString`. Também podemos fornecer
	// argumentos `[]byte` e remover `String` do
	// nome da função.
	fmt.Println(r.Match([]byte("peach")))

	// Ao criar variáveis globais com expressões
	// regulares, você pode usar a variação `MustCompile`
	// de `Compile`. `MustCompile` entra em pânico em vez de
	// retornar um erro, o que o torna mais seguro para usar para
	// variáveis globais.
	r = regexp.MustCompile("p([a-z]+)ch")
	fmt.Println("regexp:", r)

	// O pacote `regexp` também pode ser usado para substituir
	// subconjuntos de strings por outros valores.
	fmt.Println(r.ReplaceAllString("a peach", "<fruit>"))

	// A variante `Func` permite que você transforme o texto correspondente
	// com uma função fornecida.
	in := []byte("a peach")
	out := r.ReplaceAllFunc(in, bytes.ToUpper)
	fmt.Println(string(out))
}
```
