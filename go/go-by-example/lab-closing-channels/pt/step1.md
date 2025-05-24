# Fechando Canais (Closing Channels)

Neste laboratório, você precisa modificar o código fornecido para fechar o canal `jobs` quando não houver mais tarefas para o trabalhador. Você também precisa usar o canal `done` para notificar quando todas as tarefas foram concluídas.

- Use um canal com buffer `jobs` para comunicar o trabalho a ser feito da gorrotina `main()` para uma gorrotina de trabalho.
- Use um canal `done` para notificar quando todas as tarefas foram concluídas.
- Use uma gorrotina de trabalho para receber repetidamente de `jobs` com `j, more := <-jobs`.
- Use a forma especial de recebimento de 2 valores para notificar em `done` quando todas as tarefas foram concluídas.
- Envie 3 tarefas para o trabalhador através do canal `jobs`, e então feche-o.
- Use a abordagem de [sincronização](channel-synchronization) para aguardar o trabalhador.

```sh
$ go run closing-channels.go
sent job 1
received job 1
sent job 2
received job 2
sent job 3
received job 3
sent all jobs
received all jobs

# A ideia de canais fechados leva naturalmente ao nosso próximo
# exemplo: `range` sobre canais.
```

Aqui está o código completo:

```go
// _Fechar_ um canal indica que nenhum valor adicional
// será enviado nele. Isso pode ser útil para comunicar
// a conclusão aos receptores do canal.

package main

import "fmt"

// Neste exemplo, usaremos um canal `jobs` para
// comunicar o trabalho a ser feito da gorrotina `main()`
// para uma gorrotina de trabalho. Quando não tivermos mais tarefas para
// o trabalhador, iremos `fechar` o canal `jobs`.
func main() {
	jobs := make(chan int, 5)
	done := make(chan bool)

	// Aqui está a gorrotina de trabalho. Ela recebe repetidamente
	// de `jobs` com `j, more := <-jobs`. Nesta
	// forma especial de recebimento de 2 valores, o valor `more`
	// será `false` se `jobs` foi `fechado` e todos
	// os valores no canal já foram recebidos.
	// Usamos isso para notificar em `done` quando terminamos
	// todas as nossas tarefas.
	go func() {
		for {
			j, more := <-jobs
			if more {
				fmt.Println("received job", j)
			} else {
				fmt.Println("received all jobs")
				done <- true
				return
			}
		}
	}()

	// Isso envia 3 tarefas para o trabalhador através do canal `jobs`,
	// e então o fecha.
	for j := 1; j <= 3; j++ {
		jobs <- j
		fmt.Println("sent job", j)
	}
	close(jobs)
	fmt.Println("sent all jobs")

	// Aguardamos o trabalhador usando a
	// abordagem de [sincronização](channel-synchronization)
	// que vimos anteriormente.
	<-done
}
```
