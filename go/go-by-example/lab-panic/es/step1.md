# Panic

El laboratorio te pide que uses la función `panic` para fallar rápidamente en errores que no deben ocurrir durante la operación normal o que no estás preparado para manejar con gracia.

- Conocimientos básicos del lenguaje de programación Golang.
- Familiaridad con el manejo de errores en Golang.
- Comprensión de la función `panic` en Golang.

```sh
# Ejecutar este programa hará que se produzca un panic, imprima
# un mensaje de error y trazas de gorutinas, y salga con
# un estado distinto de cero.

# Cuando el primer panic en `main` se activa, el programa sale
# sin llegar al resto del código. Si quieres ver el programa
# intentar crear un archivo temporal, comenta el primer panic.
$ go run panic.go
panic: a problem

goroutine 1 [running]:
main.main() /.../panic.go:12 +0x47
...
exit status 2

# Tenga en cuenta que, a diferencia de algunos lenguajes que usan excepciones
# para manejar muchos errores, en Go es idiomático
# usar valores de retorno que indiquen errores siempre que sea posible.
```

A continuación está el código completo:

```go
// Un `panic` generalmente significa que algo salió inesperadamente
// mal. En general, lo usamos para fallar rápidamente en errores que
// no deben ocurrir durante la operación normal, o que no estamos
// preparados para manejar con gracia.

package main

import "os"

func main() {

	// Usaremos panic en todo este sitio para comprobar
	// errores inesperados. Este es el único programa del
	// sitio diseñado para causar un panic.
	panic("a problem")

	// Un uso común de panic es abortar si una función
	// devuelve un valor de error que no sabemos cómo
	// (o queremos) manejar. Aquí hay un ejemplo de
	// causar un `panic` si obtenemos un error inesperado al crear un nuevo archivo.
	_, err := os.Create("/tmp/file")
	if err!= nil {
		panic(err)
	}
}

```
