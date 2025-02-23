# Números aleatorios

Se te pide escribir un programa que genere enteros y flotantes aleatorios dentro de un rango especificado. El programa también debería ser capaz de producir secuencias variables de números cambiando la semilla.

## Requisitos

- El programa debe utilizar el paquete `math/rand` para generar números aleatorios.
- El programa debe generar enteros aleatorios dentro de un rango especificado.
- El programa debe generar flotantes aleatorios dentro de un rango especificado.
- El programa debe ser capaz de producir secuencias variables de números cambiando la semilla.

## Ejemplo

```sh
# Dependiendo de donde ejecutes este ejemplo, algunos de los
# números generados pueden ser diferentes. Tenga en cuenta que en
# la plataforma de Go playground sembrando con `time.Now()` todavía
# produce resultados deterministas debido a la forma en que está
# implementada la plataforma.
$ go run random-numbers.go
81,87
0.6645600532184904
7.123187485356329,8.434115364335547
0,28
5,87
5,87

# Consulte la documentación del paquete [`math/rand`](https://pkg.go.dev/math/rand)
# para obtener referencias sobre otras cantidades aleatorias que
# Go puede proporcionar.
```
