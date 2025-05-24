# Ordenação

O problema a ser resolvido neste laboratório é ordenar fatias (slices) de strings e inteiros usando o pacote `sort`.

- O pacote `sort` deve ser importado.
- A função `sort.Strings()` deve ser usada para ordenar uma fatia de strings.
- A função `sort.Ints()` deve ser usada para ordenar uma fatia de inteiros.
- A função `sort.IntsAreSorted()` deve ser usada para verificar se uma fatia de inteiros já está ordenada.

```sh
# Executar nosso programa imprime as strings e inteiros ordenados
# e `true` como resultado do nosso teste `AreSorted`.
$ go run sorting.go
Strings: [a b c]
Ints: [2 4 7]
Sorted: true
```

A seguir, o código completo:

```go
// O pacote `sort` do Go implementa a ordenação para tipos nativos (builtins)
// e tipos definidos pelo usuário. Vamos olhar primeiro para a ordenação de
// tipos nativos.

package main

import (
	"fmt"
	"sort"
)

func main() {

	// Os métodos de ordenação são específicos para o tipo nativo;
	// aqui está um exemplo para strings. Observe que a ordenação é
	// in-place, então ela altera a fatia fornecida e não
	// retorna uma nova.
	strs := []string{"c", "a", "b"}
	sort.Strings(strs)
	fmt.Println("Strings:", strs)

	// Um exemplo de ordenação de `int`s.
	ints := []int{7, 2, 4}
	sort.Ints(ints)
	fmt.Println("Ints:   ", ints)

	// Também podemos usar `sort` para verificar se uma fatia já
	// está em ordem ordenada.
	s := sort.IntsAreSorted(ints)
	fmt.Println("Sorted: ", s)
}
```
