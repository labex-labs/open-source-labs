# Goroutines

O problema a ser resolvido neste laboratório é criar e executar goroutines para executar funções concorrentemente.

- A função `f` deve imprimir sua _string_ de entrada e uma variável contador três vezes.
- A função `main` deve chamar a função `f` de forma síncrona e imprimir "direct" e uma variável contador três vezes.
- A função `main` deve chamar a função `f` de forma assíncrona usando uma goroutine e imprimir "goroutine" e uma variável contador três vezes.
- A função `main` deve iniciar uma goroutine para executar uma função anônima que imprime uma mensagem.
- A função `main` deve esperar que as goroutines terminem a execução antes de imprimir "done".

```sh
# Quando executamos este programa, vemos a saída da
# chamada bloqueante primeiro, depois a saída das duas
# goroutines. A saída das goroutines pode ser intercalada,
# porque as goroutines estão sendo executadas concorrentemente pelo
# Go runtime.

# Em seguida, veremos um complemento para goroutines em
# programas Go concorrentes: canais.
```

Aqui está o código completo:

```go
// Uma _goroutine_ é uma thread de execução leve.

package main

import (
	"fmt"
	"time"
)

func f(from string) {
	for i := 0; i < 3; i++ {
		fmt.Println(from, ":", i)
	}
}

func main() {

	// Suponha que temos uma chamada de função `f(s)`. Aqui está como
	// chamaríamos isso da maneira usual, executando-o
	// de forma síncrona.
	f("direct")

	// Para invocar esta função em uma goroutine, use
	// `go f(s)`. Esta nova goroutine será executada
	// concorrentemente com a chamada.
	go f("goroutine")

	// Você também pode iniciar uma goroutine para uma função anônima
	// chamada.
	go func(msg string) {
		fmt.Println(msg)
	}("going")

	// Nossas duas chamadas de função estão sendo executadas de forma assíncrona em
	// goroutines separadas agora. Espere que elas terminem
	// (para uma abordagem mais robusta, use um [WaitGroup](waitgroups)).
	time.Sleep(time.Second)
	fmt.Println("done")
}
```
