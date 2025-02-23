# Plantillas de texto

En este desafío, se te pide demostrar el uso del paquete `text/template` para generar contenido dinámico.

## Requisitos

- Utilizar el paquete `text/template` para generar contenido dinámico.
- Utilizar la función `template.Must` para generar un error en caso de que `Parse` devuelva un error.
- Utilizar la acción `{{.FieldName}}` para acceder a los campos de un struct.
- Utilizar la acción `{{if..}} si {{else..}} no {{end}}\n` para proporcionar una ejecución condicional para las plantillas.
- Utilizar la acción `{{range.}}{{.}} {{end}}\n` para recorrer slices, arrays, maps o canales.

## Ejemplo

```sh
$ go run templates.go
Valor: algún texto
Valor: 5
Valor: [Go Rust C++ C#]
Nombre: Jane Doe
Nombre: Mickey Mouse
si
no
Rango: Go Rust C++ C#
```
