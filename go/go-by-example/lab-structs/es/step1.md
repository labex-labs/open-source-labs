# Structs

En este laboratorio, debes completar la función `newPerson` que construye un nuevo struct de persona con el nombre dado. El tipo de struct `person` tiene los campos `name` y `age`.

- El tipo de struct `person` debe tener los campos `name` y `age`.
- La función `newPerson` debe construir un nuevo struct de persona con el nombre dado.
- La función `newPerson` debe devolver un puntero al nuevo struct de persona creado.
- La función `main` debe imprimir lo siguiente:
  - Un nuevo struct con nombre "Bob" y edad 20.
  - Un nuevo struct con nombre "Alice" y edad 30.
  - Un nuevo struct con nombre "Fred" y edad 0.
  - Un puntero a un nuevo struct con nombre "Ann" y edad 40.
  - Un nuevo struct construido usando la función `newPerson` con nombre "Jon" y edad 42.
  - El campo `name` de un struct con nombre "Sean" y edad 50.
  - El campo `age` de un puntero a un struct con nombre "Sean" y edad 50.
  - El campo `age` de un puntero a un struct con nombre "Sean" y edad 50 después de que el campo `age` se haya actualizado a 51.

```sh
$ go run structs.go
{Bob 20}
{Alice 30}
{Fred 0}
&{Ann 40}
&{Jon 42}
Sean
50
51
```

A continuación está el código completo:

```go
// Los _structs_ de Go son colecciones tipadas de campos.
// Son útiles para agrupar datos juntos para formar
// registros.

package main

import "fmt"

// Este tipo de struct `person` tiene los campos `name` y `age`.
type person struct {
	name string
	age  int
}

// `newPerson` construye un nuevo struct de persona con el nombre dado.
func newPerson(name string) *person {
	// Puedes devolver con seguridad un puntero a una variable local
	// ya que una variable local sobrevivirá al alcance de la función.
	p := person{name: name}
	p.age = 42
	return &p
}

func main() {

	// Esta sintaxis crea un nuevo struct.
	fmt.Println(person{"Bob", 20})

	// Puedes nombrar los campos al inicializar un struct.
	fmt.Println(person{name: "Alice", age: 30})

	// Los campos omitidos tendrán valores por defecto.
	fmt.Println(person{name: "Fred"})

	// Un prefijo `&` produce un puntero al struct.
	fmt.Println(&person{name: "Ann", age: 40})

	// Es idiomático encapsular la creación de nuevos structs en funciones constructoras
	fmt.Println(newPerson("Jon"))

	// Accede a los campos de un struct con un punto.
	s := person{name: "Sean", age: 50}
	fmt.Println(s.name)

	// También puedes usar puntos con punteros a structs - los
	// punteros se desreferencian automáticamente.
	sp := &s
	fmt.Println(sp.age)

	// Los structs son mutables.
	sp.age = 51
	fmt.Println(sp.age)
}

```
