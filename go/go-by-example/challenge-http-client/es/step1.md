# Cliente HTTP

Se te pide escribir un programa que envíe una solicitud HTTP GET a un servidor y muestre el estado de la respuesta HTTP y las primeras 5 líneas del cuerpo de la respuesta.

## Requisitos

- El programa debe utilizar el paquete `net/http` para emitir una solicitud HTTP GET.
- El programa debe mostrar el estado de la respuesta HTTP.
- El programa debe mostrar las primeras 5 líneas del cuerpo de la respuesta.
- El programa debe manejar los errores de manera adecuada.

## Ejemplo

```sh
$ go run http-clients.go
Estado de la respuesta: 200 OK
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Go by Example</title>

```
