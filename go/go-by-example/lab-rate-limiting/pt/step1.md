# Limitação de Taxa (Rate Limiting)

O problema é limitar o tratamento de requisições recebidas para manter a qualidade do serviço e controlar a utilização de recursos.

- Linguagem de programação Go
- Compreensão básica de goroutines, canais (channels) e tickers

```sh
# Executando nosso programa, vemos o primeiro lote de requisições
# sendo tratado uma vez a cada ~200 milissegundos, como desejado.
$ go run rate-limiting.go
request 1 2012-10-19 00:38:18.687438 +0000 UTC
request 2 2012-10-19 00:38:18.887471 +0000 UTC
request 3 2012-10-19 00:38:19.087238 +0000 UTC
request 4 2012-10-19 00:38:19.287338 +0000 UTC
request 5 2012-10-19 00:38:19.487331 +0000 UTC

# Para o segundo lote de requisições, servimos as primeiras
# 3 imediatamente por causa da limitação de taxa "burstable",
# então servimos as 2 restantes com atrasos de ~200ms cada.
request 1 2012-10-19 00:38:20.487578 +0000 UTC
request 2 2012-10-19 00:38:20.487645 +0000 UTC
request 3 2012-10-19 00:38:20.487676 +0000 UTC
request 4 2012-10-19 00:38:20.687483 +0000 UTC
request 5 2012-10-19 00:38:20.887542 +0000 UTC
```

A seguir, o código completo:

```go
// A [_limitação de taxa_](https://en.wikipedia.org/wiki/Rate_limiting)
// é um mecanismo importante para controlar a utilização de recursos
// e manter a qualidade do serviço. Go
// suporta elegantemente a limitação de taxa com goroutines,
// canais (channels) e [tickers](tickers).

package main

import (
	"fmt"
	"time"
)

func main() {

	// Primeiro, vamos analisar a limitação de taxa básica. Suponha
	// que queremos limitar o tratamento de requisições recebidas.
	// Serviremos essas requisições de um canal com o
	// mesmo nome.
	requests := make(chan int, 5)
	for i := 1; i <= 5; i++ {
		requests <- i
	}
	close(requests)

	// Este canal `limiter` receberá um valor
	// a cada 200 milissegundos. Este é o regulador em
	// nosso esquema de limitação de taxa.
	limiter := time.Tick(200 * time.Millisecond)

	// Ao bloquear em uma recepção do canal `limiter`
	// antes de servir cada requisição, nos limitamos a
	// 1 requisição a cada 200 milissegundos.
	for req := range requests {
		<-limiter
		fmt.Println("request", req, time.Now())
	}

	// Podemos querer permitir rajadas curtas de requisições em
	// nosso esquema de limitação de taxa, preservando o
	// limite geral de taxa. Podemos conseguir isso por
	// bufferizando nosso canal limiter. Este canal `burstyLimiter`
	// permitirá rajadas de até 3 eventos.
	burstyLimiter := make(chan time.Time, 3)

	// Preencha o canal para representar a explosão permitida.
	for i := 0; i < 3; i++ {
		burstyLimiter <- time.Now()
	}

	// A cada 200 milissegundos, tentaremos adicionar um novo
	// valor a `burstyLimiter`, até seu limite de 3.
	go func() {
		for t := range time.Tick(200 * time.Millisecond) {
			burstyLimiter <- t
		}
	}()

	// Agora simule mais 5 requisições recebidas. As primeiras
	// 3 delas se beneficiarão da capacidade de rajada
	// de `burstyLimiter`.
	burstyRequests := make(chan int, 5)
	for i := 1; i <= 5; i++ {
		burstyRequests <- i
	}
	close(burstyRequests)
	for req := range burstyRequests {
		<-burstyLimiter
		fmt.Println("request", req, time.Now())
	}
}
```
