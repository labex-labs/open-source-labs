# Pruebas y Medición de Rendimiento

El problema que se debe resolver en este laboratorio es probar y medir el rendimiento de una implementación simple de una función de mínimo entero llamada `IntMin`.

- El paquete `testing` debe ser importado.
- La función `IntMin` debe tomar dos parámetros enteros y devolver un entero.
- La función `TestIntMinBasic` debe probar la función `IntMin` para valores de entrada básicos.
- La función `TestIntMinTableDriven` debe probar la función `IntMin` utilizando un estilo basado en tablas.
- La función `BenchmarkIntMin` debe medir el rendimiento de la función `IntMin`.

```sh
# Ejecute todas las pruebas en el proyecto actual en modo detallado.

# Ejecute todas las mediciones de rendimiento en el proyecto actual. Todas las pruebas
# se ejecutan antes de las mediciones de rendimiento. La bandera `bench` filtra
# los nombres de funciones de medición de rendimiento con una expresión regular.
```

A continuación está el código completo:

```go
// Las pruebas unitarias son una parte importante de la escritura
// de programas Go basados en principios. El paquete `testing`
// proporciona las herramientas que necesitamos para escribir pruebas unitarias
// y el comando `go test` ejecuta las pruebas.

// A título de demostración, este código está en el paquete
// `main`, pero podría ser cualquier paquete. El código de prueba
// generalmente reside en el mismo paquete que el código que prueba.
package main

import (
	"fmt"
	"testing"
)

// Vamos a probar esta simple implementación de un
// mínimo entero. Normalmente, el código que estamos probando
// estaría en un archivo fuente llamado algo como
// `intutils.go`, y el archivo de prueba para él entonces
// se llamaría `intutils_test.go`.
func IntMin(a, b int) int {
	if a < b {
		return a
	}
	return b
}

// Una prueba se crea escribiendo una función con un nombre
// que comienza con `Test`.
func TestIntMinBasic(t *testing.T) {
	ans := IntMin(2, -2)
	if ans!= -2 {
		// `t.Error*` informará sobre los fallos de la prueba pero continuará
		// ejecutando la prueba. `t.Fatal*` informará sobre los fallos de la prueba
		// y detendrá inmediatamente la prueba.
		t.Errorf("IntMin(2, -2) = %d; want -2", ans)
	}
}

// Escribir pruebas puede ser repetitivo, por lo que es idiomático
// utilizar un *estilo basado en tablas*, donde las entradas de prueba y
// las salidas esperadas se enumeran en una tabla y un solo bucle
// recorre sobre ellas y ejecuta la lógica de la prueba.
func TestIntMinTableDriven(t *testing.T) {
	var tests = []struct {
		a, b int
		want int
	}{
		{0, 1, 0},
		{1, 0, 0},
		{2, -2, -2},
		{0, -1, -1},
		{-1, 0, -1},
	}

	for _, tt := range tests {
		// t.Run permite ejecutar "subpruebas", una para cada
		// entrada de la tabla. Estas se muestran por separado
		// al ejecutar `go test -v`.
		testname := fmt.Sprintf("%d,%d", tt.a, tt.b)
		t.Run(testname, func(t *testing.T) {
			ans := IntMin(tt.a, tt.b)
			if ans!= tt.want {
				t.Errorf("got %d, want %d", ans, tt.want)
			}
		})
	}
}

// Las pruebas de rendimiento generalmente van en archivos `_test.go` y se nombran
// comenzando con `Benchmark`. El ejecutor de pruebas `testing` ejecuta cada función
// de prueba de rendimiento varias veces, aumentando `b.N` en cada ejecución hasta
// que recopila una medición precisa.
func BenchmarkIntMin(b *testing.B) {
	// Normalmente, la prueba de rendimiento ejecuta una función que estamos
	// midiendo en un bucle `b.N` veces.
	for i := 0; i < b.N; i++ {
		IntMin(1, 2)
	}
}

```
