# Servidor HTTP

Se te pide escribir un servidor HTTP simple que pueda manejar dos rutas: `/hello` y `/headers`. La ruta `/hello` debe devolver una respuesta simple "hello", mientras que la ruta `/headers` debe devolver todos los encabezados de solicitud HTTP.

- El servidor debe utilizar el paquete `net/http`.
- La ruta `/hello` debe devolver una respuesta "hello".
- La ruta `/headers` debe devolver todos los encabezados de solicitud HTTP.
- El servidor debe escuchar en el puerto `8090`.

```sh
# Ejecuta el servidor en segundo plano.
$ go run http-servers.go &

# Accede a la ruta `/hello`.
$ curl localhost:8090/hello
hello
```

A continuación está el código completo:

```go
// Escribir un servidor HTTP básico es fácil utilizando el
// paquete `net/http`.
package main

import (
	"fmt"
	"net/http"
)

// Un concepto fundamental en los servidores `net/http` es
// *manejadores*. Un manejador es un objeto que implementa la
// interfaz `http.Handler`. Una forma común de escribir
// un manejador es utilizando el adaptador `http.HandlerFunc`
// en funciones con la firma adecuada.
func hello(w http.ResponseWriter, req *http.Request) {

	// Las funciones que sirven como manejadores toman un
	// `http.ResponseWriter` y un `http.Request` como
	// argumentos. El escritor de respuesta se utiliza para llenar
	// la respuesta HTTP. Aquí nuestra respuesta simple es solo
	// "hello\n".
	fmt.Fprintf(w, "hello\n")
}

func headers(w http.ResponseWriter, req *http.Request) {

	// Este manejador hace algo un poco más sofisticado
	// leyendo todos los encabezados de solicitud HTTP y
	// echándolos en el cuerpo de la respuesta.
	for name, headers := range req.Header {
		for _, h := range headers {
			fmt.Fprintf(w, "%v: %v\n", name, h)
		}
	}
}

func main() {

	// Registramos nuestros manejadores en las rutas del servidor
	// utilizando la función de conveniencia `http.HandleFunc`.
	// Establece el *enrutador predeterminado* en el paquete
	// `net/http` y toma una función como argumento.
	http.HandleFunc("/hello", hello)
	http.HandleFunc("/headers", headers)

	// Finalmente, llamamos a `ListenAndServe` con el puerto
	// y un manejador. `nil` le dice que use el enrutador
	// predeterminado que acabamos de configurar.
	http.ListenAndServe(":8090", nil)
}

```
