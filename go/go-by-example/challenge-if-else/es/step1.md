# if-else

Se te pide que completes la función `checkNumber` que toma un entero como entrada y devuelve una cadena. Si el número es par, devuelve "even" (par), en caso contrario devuelve "odd" (impar).

## Requisitos

- La función debe llamarse `checkNumber`.
- La función debe tomar un entero como entrada.
- La función debe devolver una cadena.
- Si el número es par, devuelve "even".
- Si el número es impar, devuelve "odd".

## Ejemplo

```sh
$ go run if-else.go
7 es impar
8 es divisible por 4
9 tiene 1 dígito

# No hay [ternario if](https://en.wikipedia.org/wiki/%3F:)
# en Go, por lo que necesitarás usar una declaración `if` completa incluso
# para condiciones básicas.
```
