# Closures (Fechamentos)

Você precisa criar uma função que retorna outra função. A função retornada deve incrementar uma variável em um a cada vez que é chamada. A variável deve ser única para cada função retornada.

- A função `intSeq` deve retornar outra função.
- A função retornada deve incrementar uma variável em um a cada vez que é chamada.
- A variável deve ser única para cada função retornada.

```sh
$ go run closures.go
1
2
3
1

# The last feature of functions we'll look at for now is
# recursion.
```

Aqui está o código completo:

```go
// Go suporta [_funções anônimas_](https://en.wikipedia.org/wiki/Anonymous_function),
// que podem formar <a href="https://en.wikipedia.org/wiki/Closure_(computer_science)"><em>closures</em></a>.
// Funções anônimas são úteis quando você deseja definir
// uma função inline sem ter que nomeá-la.

package main

import "fmt"

// Esta função `intSeq` retorna outra função, que
// definimos anonimamente no corpo de `intSeq`. A
// função retornada _fecha sobre_ a variável `i` para
// formar um closure.
func intSeq() func() int {
	i := 0
	return func() int {
		i++
		return i
	}
}

func main() {

	// Chamamos `intSeq`, atribuindo o resultado (uma função)
	// a `nextInt`. Este valor de função captura seu
	// próprio valor `i`, que será atualizado cada vez
	// que chamarmos `nextInt`.
	nextInt := intSeq()

	// Veja o efeito do closure chamando `nextInt`
	// algumas vezes.
	fmt.Println(nextInt())
	fmt.Println(nextInt())
	fmt.Println(nextInt())

	// Para confirmar que o estado é único para essa
	// função em particular, crie e teste uma nova.
	newInts := intSeq()
	fmt.Println(newInts())
}
```
