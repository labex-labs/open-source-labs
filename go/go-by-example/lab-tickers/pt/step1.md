# _Timers_ e _Tickers_

Neste laboratório, você precisa criar um _ticker_ que "tique" a cada 500ms até que o paremos. Você usará um canal para aguardar os valores à medida que eles chegam.

- Use o pacote `time` para criar um _ticker_.
- Use um canal para aguardar os valores à medida que eles chegam.
- Use a instrução `select` para receber valores do canal.
- Pare o _ticker_ após 1600ms.

```sh
# Quando executamos este programa, o ticker deve "ticar" 3 vezes
# antes de pararmos.
$ go run tickers.go
Tick at 2012-09-23 11:29:56.487625 -0700 PDT
Tick at 2012-09-23 11:29:56.988063 -0700 PDT
Tick at 2012-09-23 11:29:57.488076 -0700 PDT
Ticker stopped
```

A seguir, o código completo:

```go
// [Timers](timers) são para quando você quer fazer
// algo uma vez no futuro - _tickers_ são para quando
// você quer fazer algo repetidamente em intervalos
// regulares. Aqui está um exemplo de um ticker que "tica"
// periodicamente até que o paremos.

package main

import (
	"fmt"
	"time"
)

func main() {

	// Tickers usam um mecanismo semelhante aos timers: um
	// canal que recebe valores. Aqui, usaremos o
	// builtin `select` no canal para aguardar os
	// valores à medida que eles chegam a cada 500ms.
	ticker := time.NewTicker(500 * time.Millisecond)
	done := make(chan bool)

	go func() {
		for {
			select {
			case <-done:
				return
			case t := <-ticker.C:
				fmt.Println("Tick at", t)
			}
		}
	}()

	// Tickers podem ser parados como timers. Uma vez que um ticker
	// é parado, ele não receberá mais nenhum valor em seu
	// canal. Vamos parar o nosso após 1600ms.
	time.Sleep(1600 * time.Millisecond)
	ticker.Stop()
	done <- true
	fmt.Println("Ticker stopped")
}
```
