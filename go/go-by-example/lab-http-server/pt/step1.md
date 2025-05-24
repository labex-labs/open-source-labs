# Servidor HTTP

Você deve escrever um servidor HTTP simples que possa lidar com duas rotas: `/hello` e `/headers`. A rota `/hello` deve retornar uma resposta simples "hello", enquanto a rota `/headers` deve retornar todos os cabeçalhos da requisição HTTP.

- O servidor deve usar o pacote `net/http`.
- A rota `/hello` deve retornar uma resposta "hello".
- A rota `/headers` deve retornar todos os cabeçalhos da requisição HTTP.
- O servidor deve escutar na porta `8090`.

```sh
# Execute o servidor em segundo plano.
$ go run http-servers.go &

# Acesse a rota `/hello`.
$ curl localhost:8090/hello
hello
```

A seguir, o código completo:

```go
// Escrever um servidor HTTP básico é fácil usando o
// pacote `net/http`.
package main

import (
	"fmt"
	"net/http"
)

// Um conceito fundamental em servidores `net/http` são
// *handlers* (manipuladores). Um manipulador é um objeto que implementa a
// interface `http.Handler`. Uma maneira comum de escrever
// um manipulador é usando o adaptador `http.HandlerFunc`
// em funções com a assinatura apropriada.
func hello(w http.ResponseWriter, req *http.Request) {

	// Funções que servem como manipuladores recebem um
	// `http.ResponseWriter` e um `http.Request` como
	// argumentos. O response writer é usado para preencher a
	// resposta HTTP. Aqui, nossa resposta simples é apenas
	// "hello\n".
	fmt.Fprintf(w, "hello\n")
}

func headers(w http.ResponseWriter, req *http.Request) {

	// Este manipulador faz algo um pouco mais
	// sofisticado, lendo todos os cabeçalhos da requisição HTTP
	// e ecoando-os no corpo da resposta.
	for name, headers := range req.Header {
		for _, h := range headers {
			fmt.Fprintf(w, "%v: %v\n", name, h)
		}
	}
}

func main() {

	// Registramos nossos manipuladores nas rotas do servidor usando a
	// função de conveniência `http.HandleFunc`. Ela configura
	// o *roteador padrão* no pacote `net/http` e
	// recebe uma função como argumento.
	http.HandleFunc("/hello", hello)
	http.HandleFunc("/headers", headers)

	// Finalmente, chamamos `ListenAndServe` com a porta
	// e um manipulador. `nil` diz para usar o padrão
	// roteador que acabamos de configurar.
	http.ListenAndServe(":8090", nil)
}
```
