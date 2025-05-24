# Ordenação por Funções

O problema a ser resolvido neste laboratório é implementar uma função de ordenação personalizada em Go que ordene uma fatia (slice) de strings por seu comprimento.

- O tipo `byLength` deve ser criado como um alias para o tipo `[]string`.
- A interface `sort.Interface` deve ser implementada no tipo `byLength`.
- As funções `Len` e `Swap` devem ser implementadas no tipo `byLength`.
- A função `Less` deve ser implementada no tipo `byLength` para conter a lógica de ordenação personalizada real.
- A função `main` deve converter a fatia `fruits` original para `byLength` e, em seguida, usar `sort.Sort` nessa fatia tipada.

```sh
# Executar nosso programa mostra uma lista ordenada por
# comprimento da string, como desejado.
$ go run sorting-by-functions.go
[kiwi peach banana]

# Seguindo este mesmo padrão de criação de um tipo
# personalizado, implementando os três métodos `Interface`
# nesse tipo e, em seguida, chamando sort.Sort em uma coleção
# desse tipo personalizado, podemos ordenar fatias (slices) Go
# por funções arbitrárias.
```

A seguir, o código completo:

```go
// Às vezes, queremos ordenar uma coleção por algo
// diferente de sua ordem natural. Por exemplo, suponha que
// quiséssemos ordenar strings por seu comprimento em vez de
// alfabeticamente. Aqui está um exemplo de ordenações personalizadas
// em Go.

package main

import (
	"fmt"
	"sort"
)

// Para ordenar por uma função personalizada em Go, precisamos de um
// tipo correspondente. Aqui, criamos um tipo `byLength`
// que é apenas um alias para o tipo embutido `[]string`.
type byLength []string

// Implementamos `sort.Interface` - `Len`, `Less` e
// `Swap` - em nosso tipo para que possamos usar a função
// genérica `Sort` do pacote `sort`. `Len` e `Swap`
// geralmente serão semelhantes em todos os tipos e `Less` conterá
// a lógica de ordenação personalizada real. Em nosso caso, nós
// queremos ordenar em ordem crescente de comprimento da string, então
// usamos `len(s[i])` e `len(s[j])` aqui.
func (s byLength) Len() int {
	return len(s)
}
func (s byLength) Swap(i, j int) {
	s[i], s[j] = s[j], s[i]
}
func (s byLength) Less(i, j int) bool {
	return len(s[i]) < len(s[j])
}

// Com tudo isso em vigor, agora podemos implementar nossa
// ordenação personalizada convertendo a fatia `fruits` original
// para `byLength` e, em seguida, usar `sort.Sort` nessa fatia tipada.
func main() {
	fruits := []string{"peach", "banana", "kiwi"}
	sort.Sort(byLength(fruits))
	fmt.Println(fruits)
}
```
