# Servidor HTTP

Se te pide escribir un servidor HTTP simple que pueda manejar dos rutas: `/hello` y `/headers`. La ruta `/hello` debe devolver una respuesta simple de "hola", mientras que la ruta `/headers` debe devolver todos los encabezados de solicitud HTTP.

## Requisitos

- El servidor debe utilizar el paquete `net/http`.
- La ruta `/hello` debe devolver una respuesta de "hola".
- La ruta `/headers` debe devolver todos los encabezados de solicitud HTTP.
- El servidor debe escuchar en el puerto `8090`.

## Ejemplo

```sh
# Ejecuta el servidor en segundo plano.
$ go run http-servers.go &

# Accede a la ruta `/hello`.
$ curl localhost:8090/hello
hello
```
