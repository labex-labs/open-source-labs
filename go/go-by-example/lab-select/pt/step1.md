# Select (Seleção)

Neste laboratório, você recebe dois canais, `c1` e `c2`, que receberão um valor após algum tempo. Sua tarefa é usar `select` para aguardar ambos os valores simultaneamente, imprimindo cada um conforme chega.

- Você deve usar a instrução `select` para aguardar em ambos os canais.
- Você deve imprimir o valor recebido de cada canal conforme ele chega.

```sh
# Recebemos os valores `"one"` e então `"two"` como
# esperado.
$ time go run select.go
received one
received two

# Observe que o tempo total de execução é de apenas ~2 segundos
# já que os `Sleeps` de 1 e 2 segundos executam
# concorrentemente.
real 0m2.245s
```

Aqui está o código completo:

```go
// O _select_ do Go permite que você aguarde em múltiplas operações de canal.
// Combinar goroutines e canais com select é um recurso poderoso do Go.

package main

import (
	"fmt"
	"time"
)

func main() {

	// Para nosso exemplo, vamos selecionar em dois canais.
	c1 := make(chan string)
	c2 := make(chan string)

	// Cada canal receberá um valor após algum tempo, para simular, por exemplo,
	// operações RPC bloqueantes executando em goroutines concorrentes.
	go func() {
		time.Sleep(1 * time.Second)
		c1 <- "one"
	}()
	go func() {
		time.Sleep(2 * time.Second)
		c2 <- "two"
	}()

	// Usaremos `select` para aguardar ambos esses valores
	// simultaneamente, imprimindo cada um conforme chega.
	for i := 0; i < 2; i++ {
		select {
		case msg1 := <-c1:
			fmt.Println("received", msg1)
		case msg2 := <-c2:
			fmt.Println("received", msg2)
		}
	}
}
```
