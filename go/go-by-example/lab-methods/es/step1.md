# Métodos

El código proporcionado define un tipo de struct llamado `rect` con dos campos, `width` y `height`. Se definen dos métodos para este tipo de struct, `area` y `perim`. El método `area` calcula el área del rectángulo, y el método `perim` calcula el perímetro del rectángulo. La función principal llama a estos dos métodos y muestra sus resultados.

- El método `area` debe tener un tipo de receptor de `*rect`.
- El método `perim` debe tener un tipo de receptor de `rect`.
- El método `area` debe devolver el área del rectángulo.
- El método `perim` debe devolver el perímetro del rectángulo.
- La función `main` debe llamar a ambos métodos y mostrar sus resultados.

```sh
$ go run methods.go
area: 50
perim: 30
area: 50
perim: 30

# A continuación, veremos el mecanismo de Go para agrupar y
# nombrar conjuntos relacionados de métodos: interfaces.
```

A continuación está el código completo:

```go
// Go admite _métodos_ definidos en tipos de struct.

package main

import "fmt"

type rect struct {
	width, height int
}

// Este método `area` tiene un _tipo de receptor_ de `*rect`.
func (r *rect) area() int {
	return r.width * r.height
}

// Los métodos se pueden definir para tipos de receptor de puntero o valor.
// Aquí hay un ejemplo de un receptor de valor.
func (r rect) perim() int {
	return 2*r.width + 2*r.height
}

func main() {
	r := rect{width: 10, height: 5}

	// Aquí llamamos a los 2 métodos definidos para nuestro struct.
	fmt.Println("area: ", r.area())
	fmt.Println("perim:", r.perim())

	// Go maneja automáticamente la conversión entre valores
	// y punteros para las llamadas de método. Puede que desee usar
	// un tipo de receptor de puntero para evitar la copia en las llamadas
	// de método o para permitir que el método mutete el
	// struct receptor.
	rp := &r
	fmt.Println("area: ", rp.area())
	fmt.Println("perim:", rp.perim())
}

```
