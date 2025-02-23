# Errores

El desafío proporciona dos funciones que devuelven un error si el argumento de entrada es 42. La primera función devuelve un valor de error básico, mientras que la segunda función utiliza un tipo personalizado para representar el error.

## Requisitos

- El paquete `errors` debe ser importado.
- La función `f1` debe devolver un error si el argumento de entrada es 42.
- La función `f2` debe devolver un error del tipo `argError` si el argumento de entrada es 42.
- El tipo `argError` debe tener dos campos: `arg` y `prob`.
- El tipo `argError` debe implementar el método `Error()`.
- La función `main` debe llamar a `f1` y `f2` con argumentos de entrada de 7 y 42.
- La función `main` debe imprimir el resultado de cada llamada a función, junto con cualquier error que haya sido devuelto.
- La función `main` debe demostrar cómo utilizar programáticamente los datos en un error personalizado.

## Ejemplo

```sh
$ go run errors.go
f1 funcionó: 10
f1 falló: no se puede trabajar con 42
f2 funcionó: 10
f2 falló: 42 - no se puede trabajar con él
42
no se puede trabajar con él

# Consulte esta [gran publicación](https://go.dev/blog/error-handling-and-go)
# en el blog de Go para obtener más información sobre el manejo de errores.
```
