# Contexto

La función `hello` simula un trabajo que el servidor está realizando esperando unos segundos antes de enviar una respuesta al cliente. Mientras está trabajando, mantenga un ojo en el canal `Done()` del contexto para una señal de que debemos cancelar el trabajo y devolver lo antes posible.

- Versión de Golang 1.13 o superior.

```sh
# Ejecute el servidor en segundo plano.
$ go run context-in-http-servers.go &

# Simule una solicitud del cliente a `/hello`, presionando
# Ctrl+C poco después de comenzar para señalar
# la cancelación.
$ curl localhost:8090/hello
server: hello handler started
^C
server: context canceled
server: hello handler ended
```

A continuación está el código completo:

```go
// En el ejemplo anterior, vimos cómo configurar un simple
// [servidor HTTP](http-servers). Los servidores HTTP son útiles para
// demostrar el uso de `context.Context` para
// controlar la cancelación. Un `Context` lleva plazos de finalización,
// señales de cancelación y otros valores con ámbito de solicitud
// a través de los límites de API y gorutinas.
package main

import (
	"fmt"
	"net/http"
	"time"
)

func hello(w http.ResponseWriter, req *http.Request) {

	// Un `context.Context` se crea para cada solicitud por
	// la máquina `net/http`, y está disponible con
	// el método `Context()`.
	ctx := req.Context()
	fmt.Println("server: hello handler started")
	defer fmt.Println("server: hello handler ended")

	// Espere unos segundos antes de enviar una respuesta al
	// cliente. Esto podría simular un trabajo que el servidor está
	// realizando. Mientras está trabajando, mantenga un ojo en el
	// canal `Done()` del contexto para una señal de que debemos cancelar
	// el trabajo y devolver lo antes posible.
	select {
	case <-time.After(10 * time.Second):
		fmt.Fprintf(w, "hello\n")
	case <-ctx.Done():
		// El método `Err()` del contexto devuelve un error
		// que explica por qué el canal `Done()` fue
		// cerrado.
		err := ctx.Err()
		fmt.Println("server:", err)
		internalError := http.StatusInternalServerError
		http.Error(w, err.Error(), internalError)
	}
}

func main() {

	// Como antes, registramos nuestro controlador en la ruta "/hello"
	// y comenzamos a atender.
	http.HandleFunc("/hello", hello)
	http.ListenAndServe(":8090", nil)
}

```
