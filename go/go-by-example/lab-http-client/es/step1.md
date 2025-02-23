# Cliente HTTP

Se te pide escribir un programa que envíe una solicitud HTTP GET a un servidor y muestre el estado de la respuesta HTTP y las primeras 5 líneas del cuerpo de la respuesta.

- El programa debe utilizar el paquete `net/http` para emitir una solicitud HTTP GET.
- El programa debe mostrar el estado de la respuesta HTTP.
- El programa debe mostrar las primeras 5 líneas del cuerpo de la respuesta.
- El programa debe manejar los errores de manera adecuada.

```sh
$ go run http-clients.go
Estado de la respuesta: 200 OK
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Go by Example</title>

```

A continuación está el código completo:

```go
// La biblioteca estándar de Go cuenta con un excelente soporte
// para clientes y servidores HTTP en el paquete `net/http`.
// En este ejemplo lo utilizaremos para emitir solicitudes HTTP
// simples.
package main

import (
	"bufio"
	"fmt"
	"net/http"
)

func main() {

	// Emitir una solicitud HTTP GET a un servidor. `http.Get` es
	// un atajo práctico para crear un objeto `http.Client`
	// y llamar a su método `Get`; utiliza el objeto
	// `http.DefaultClient` que tiene configuraciones por defecto
	// útiles.
	resp, err := http.Get("https://gobyexample.com")
	if err!= nil {
		panic(err)
	}
	defer resp.Body.Close()

	// Mostrar el estado de la respuesta HTTP.
	fmt.Println("Estado de la respuesta:", resp.Status)

	// Mostrar las primeras 5 líneas del cuerpo de la respuesta.
	scanner := bufio.NewScanner(resp.Body)
	for i := 0; scanner.Scan() && i < 5; i++ {
		fmt.Println(scanner.Text())
	}

	if err := scanner.Err(); err!= nil {
		panic(err)
	}
}

```
