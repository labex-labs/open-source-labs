# Timers (Temporizadores)

O laboratório requer a implementação de um timer que espera por uma duração especificada e então dispara. Adicionalmente, o timer deve ser cancelável antes de disparar.

- O pacote `time` deve ser importado.
- Dois timers devem ser criados, um que espera por 2 segundos e outro que espera por 1 segundo.
- O primeiro timer deve imprimir "Timer 1 fired" quando disparar.
- O segundo timer deve imprimir "Timer 2 fired" quando disparar.
- O segundo timer deve ser cancelado antes de disparar.
- O programa deve esperar por 2 segundos para mostrar que o segundo timer não disparou.

```sh
// O primeiro timer disparará ~2s depois que iniciarmos o
// programa, mas o segundo deve ser parado antes que tenha
// a chance de disparar.
$ go run timers.go
Timer 1 fired
Timer 2 stopped
```

Aqui está o código completo:

```go
// Frequentemente queremos executar código Go em algum momento no
// futuro, ou repetidamente em algum intervalo. Os recursos
// _timer_ e _ticker_ embutidos do Go tornam ambas as tarefas
// fáceis. Vamos olhar primeiro para timers e depois
// para [tickers](tickers).

package main

import (
	"fmt"
	"time"
)

func main() {

	// Timers representam um único evento no futuro. Você
	// diz ao timer quanto tempo você quer esperar, e ele
	// fornece um canal que será notificado naquele
	// tempo. Este timer esperará 2 segundos.
	timer1 := time.NewTimer(2 * time.Second)

	// O `<-timer1.C` bloqueia no canal `C` do timer
	// até que ele envie um valor indicando que o timer
	// disparou.
	<-timer1.C
	fmt.Println("Timer 1 fired")

	// Se você apenas quisesse esperar, poderia ter usado
	// `time.Sleep`. Uma razão pela qual um timer pode ser útil é
	// que você pode cancelar o timer antes que ele dispare.
	// Aqui está um exemplo disso.
	timer2 := time.NewTimer(time.Second)
	go func() {
		<-timer2.C
		fmt.Println("Timer 2 fired")
	}()
	stop2 := timer2.Stop()
	if stop2 {
		fmt.Println("Timer 2 stopped")
	}

	// Dê ao `timer2` tempo suficiente para disparar, se ele
	// fosse, para mostrar que ele foi de fato parado.
	time.Sleep(2 * time.Second)
}
```
