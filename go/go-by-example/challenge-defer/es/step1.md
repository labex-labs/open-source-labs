# Defer

En este desafío, debes utilizar `defer` para crear un archivo, escribir en él y luego cerrarlo cuando hayas terminado.

## Requisitos

- La función `createFile` debe crear un archivo con la ruta dada y devolver un puntero al archivo.
- La función `writeFile` debe escribir la cadena "data" en el archivo.
- La función `closeFile` debe cerrar el archivo y comprobar si hay errores.

## Ejemplo

```sh
# Ejecutar el programa confirma que el archivo se cierra
# después de ser escrito.
$ go run defer.go
creando
escribiendo
cerrando
```
