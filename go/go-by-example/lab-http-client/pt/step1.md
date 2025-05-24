# Cliente HTTP

Você deve escrever um programa que envia uma requisição HTTP GET para um servidor e imprime o status da resposta HTTP e as primeiras 5 linhas do corpo da resposta.

- O programa deve usar o pacote `net/http` para emitir uma requisição HTTP GET.
- O programa deve imprimir o status da resposta HTTP.
- O programa deve imprimir as primeiras 5 linhas do corpo da resposta.
- O programa deve tratar erros de forma adequada.

```sh
$ go run http-clients.go
Response status: 200 OK
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Go by Example</title>

```

Abaixo está o código completo:

```go
// A biblioteca padrão do Go vem com excelente suporte
// para clientes e servidores HTTP no pacote `net/http`.
// Neste exemplo, vamos usá-lo para emitir requisições HTTP simples.
package main

import (
	"bufio"
	"fmt"
	"net/http"
)

func main() {

	// Emite uma requisição HTTP GET para um servidor. `http.Get` é um
	// atalho conveniente para criar um objeto `http.Client`
	// e chamar seu método `Get`; ele usa o
	// objeto `http.DefaultClient`, que possui configurações padrão úteis.
	resp, err := http.Get("https://gobyexample.com")
	if err != nil {
		panic(err)
	}
	defer resp.Body.Close()

	// Imprime o status da resposta HTTP.
	fmt.Println("Response status:", resp.Status)

	// Imprime as primeiras 5 linhas do corpo da resposta.
	scanner := bufio.NewScanner(resp.Body)
	for i := 0; scanner.Scan() && i < 5; i++ {
		fmt.Println(scanner.Text())
	}

	if err := scanner.Err(); err != nil {
		panic(err)
	}
}
```
