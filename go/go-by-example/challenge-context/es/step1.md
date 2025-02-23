# Contexto

La función `hello` simula un trabajo que el servidor está realizando esperando unos segundos antes de enviar una respuesta al cliente. Mientras está trabajando, mantenga un ojo en el canal `Done()` del contexto para una señal de que debemos cancelar el trabajo y devolver lo antes posible.

## Requisitos

- Versión de Golang 1.13 o superior.

## Ejemplo

```sh
# Ejecute el servidor en segundo plano.
$ go run context-in-http-servers.go &

# Simule una solicitud de cliente a `/hello`, presionando
# Ctrl+C poco después de comenzar para señalar
# la cancelación.
$ curl localhost:8090/hello
server: hello handler started
^C
server: context canceled
server: hello handler ended
```
