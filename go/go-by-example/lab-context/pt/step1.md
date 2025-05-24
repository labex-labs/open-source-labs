# Context (Contexto)

A função `hello` simula algum trabalho que o servidor está fazendo, esperando alguns segundos antes de enviar uma resposta ao cliente. Enquanto trabalha, fique de olho no canal `Done()` do contexto para um sinal de que devemos cancelar o trabalho e retornar o mais rápido possível.

- Versão Golang 1.13 ou superior.

```sh
# Execute o servidor em segundo plano.
$ go run context-in-http-servers.go &

# Simule uma requisição do cliente para `/hello`, pressionando
# Ctrl+C logo após iniciar para sinalizar
# o cancelamento.
$ curl localhost:8090/hello
server: hello handler started
^C
server: context canceled
server: hello handler ended
```

A seguir, o código completo:

```go
// No exemplo anterior, analisamos a configuração de um simples
// [servidor HTTP](http-servers). Servidores HTTP são úteis para
// demonstrar o uso de `context.Context` para
// controlar o cancelamento. Um `Context` carrega prazos,
// sinais de cancelamento e outros valores com escopo de requisição
// através de limites de API e goroutines.
package main

import (
	"fmt"
	"net/http"
	"time"
)

func hello(w http.ResponseWriter, req *http.Request) {

	// Um `context.Context` é criado para cada requisição pelo
	// mecanismo `net/http` e está disponível com
	// o método `Context()`.
	ctx := req.Context()
	fmt.Println("server: hello handler started")
	defer fmt.Println("server: hello handler ended")

	// Espere alguns segundos antes de enviar uma resposta ao
	// cliente. Isso poderia simular algum trabalho que o servidor está
	// fazendo. Enquanto trabalha, fique de olho no canal
	// `Done()` do contexto para um sinal de que devemos cancelar
	// o trabalho e retornar o mais rápido possível.
	select {
	case <-time.After(10 * time.Second):
		fmt.Fprintf(w, "hello\n")
	case <-ctx.Done():
		// O método `Err()` do contexto retorna um erro
		// que explica por que o canal `Done()` foi
		// fechado.
		err := ctx.Err()
		fmt.Println("server:", err)
		internalError := http.StatusInternalServerError
		http.Error(w, err.Error(), internalError)
	}
}

func main() {

	// Como antes, registramos nosso handler na rota "/hello"
	// e começamos a servir.
	http.HandleFunc("/hello", hello)
	http.ListenAndServe(":8090", nil)
}
```
