# Pruebas y Medición de Rendimiento

El problema que se debe resolver en este desafío es probar y medir el rendimiento de una implementación simple de una función de mínimo de enteros llamada `IntMin`.

## Requisitos

- El paquete `testing` debe ser importado.
- La función `IntMin` debe tomar dos parámetros enteros y devolver un entero.
- La función `TestIntMinBasic` debe probar la función `IntMin` para valores de entrada básicos.
- La función `TestIntMinTableDriven` debe probar la función `IntMin` utilizando un estilo basado en tablas.
- La función `BenchmarkIntMin` debe medir el rendimiento de la función `IntMin`.

## Ejemplo

```sh
# Ejecuta todas las pruebas en el proyecto actual en modo detallado.
$ go test -v
== RUN   TestIntMinBasic
--- PASS: TestIntMinBasic (0.00s)
=== RUN   TestIntMinTableDriven
=== RUN   TestIntMinTableDriven/0,1
=== RUN   TestIntMinTableDriven/1,0
=== RUN   TestIntMinTableDriven/2,-2
=== RUN   TestIntMinTableDriven/0,-1
=== RUN   TestIntMinTableDriven/-1,0
--- PASS: TestIntMinTableDriven (0.00s)
    --- PASS: TestIntMinTableDriven/0,1 (0.00s)
    --- PASS: TestIntMinTableDriven/1,0 (0.00s)
    --- PASS: TestIntMinTableDriven/2,-2 (0.00s)
    --- PASS: TestIntMinTableDriven/0,-1 (0.00s)
    --- PASS: TestIntMinTableDriven/-1,0 (0.00s)
PASS
ok  	examples/testing-and-benchmarking	0.023s

# Ejecuta todas las mediciones de rendimiento en el proyecto actual. Todas las pruebas
# se ejecutan antes de las mediciones de rendimiento. La bandera `bench` filtra
# los nombres de funciones de medición de rendimiento con una expresión regular.
$ go test -bench=.
goos: darwin
goarch: arm64
pkg: examples/testing
BenchmarkIntMin-8 1000000000 0.3136 ns/op
PASS
ok  	examples/testing-and-benchmarking	0.351s

```
