# Interfaces

El problema es implementar una interfaz en Go, solo necesitamos implementar todos los métodos de la interfaz. Aquí implementamos `geometry` en `rect`s y `circle`s.

## Requisitos

- Implementar una interfaz en Go.
- Implementar todos los métodos de la interfaz.
- Utilizar una función genérica `measure` para trabajar con cualquier `geometry`.
- Utilizar instancias de los structs `circle` y `rect` como argumentos para `measure`.

## Ejemplo

```sh
$ go run interfaces.go
{3 4}
12
14
{5}
78.53981633974483
31.41592653589793

# Para aprender más sobre las interfaces de Go, consulta esta
# [excelente publicación en el blog](https://jordanorelli.tumblr.com/post/32665860244/how-to-use-interfaces-in-go).
```
