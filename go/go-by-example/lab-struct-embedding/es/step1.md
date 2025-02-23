# Incrustación de structs

Crea un struct llamado `container` que incruste un struct llamado `base`. El struct `base` debe tener un campo llamado `num` de tipo `int` y un método llamado `describe()` que devuelva una cadena. El struct `container` debe tener un campo llamado `str` de tipo `string`. El struct `container` debe ser capaz de acceder al campo `num` y al método `describe()` del struct `base`.

- El struct `base` debe tener un campo llamado `num` de tipo `int`.
- El struct `base` debe tener un método llamado `describe()` que devuelva una cadena.
- El struct `container` debe tener un campo llamado `str` de tipo `string`.
- El struct `container` debe incrustar el struct `base`.
- El struct `container` debe ser capaz de acceder al campo `num` y al método `describe()` del struct `base`.

```sh
$ go run struct-embedding.go
co={num: 1, str: some name}
also num: 1
describe: base with num=1
describer: base with num=1
```

A continuación está el código completo:

```go
// Go admite la _incrustación_ de structs e interfaces
// para expresar una composición de tipos más fluida.
// Esto no debe confundirse con [`//go:embed`](embed-directive) que es
// una directiva de Go introducida en la versión 1.16+ de Go para incrustar
// archivos y carpetas en el binario de la aplicación.

package main

import "fmt"

type base struct {
	num int
}

func (b base) describe() string {
	return fmt.Sprintf("base with num=%v", b.num)
}

// Un `container` _incrusta_ un `base`. Una incrustación se ve
// como un campo sin nombre.
type container struct {
	base
	str string
}

func main() {

	// Al crear structs con literales, tenemos que
	// inicializar la incrustación explícitamente; aquí
	// el tipo incrustado sirve como nombre de campo.
	co := container{
		base: base{
			num: 1,
		},
		str: "some name",
	}

	// Podemos acceder a los campos del base directamente en `co`,
	// por ejemplo `co.num`.
	fmt.Printf("co={num: %v, str: %v}\n", co.num, co.str)

	// Alternativamente, podemos escribir la ruta completa usando
	// el nombre del tipo incrustado.
	fmt.Println("also num:", co.base.num)

	// Dado que `container` incrusta `base`, los métodos de
	// `base` también se convierten en métodos de un `container`. Aquí
	// invocamos un método que se incrustó de `base` directamente en `co`.
	fmt.Println("describe:", co.describe())

	type describer interface {
		describe() string
	}

	// Incrustar structs con métodos puede usarse para otorgar
	// implementaciones de interfaz a otros structs. Aquí
	// vemos que un `container` ahora implementa la
	// interfaz `describer` porque incrusta `base`.
	var d describer = co
	fmt.Println("describer:", d.describe())
}

```
