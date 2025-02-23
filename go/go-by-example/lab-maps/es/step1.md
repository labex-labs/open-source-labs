# Maps

En esta práctica, tendrás que crear un mapa que almacene el número de veces que cada palabra aparece en una cadena dada. Tendrás que dividir la cadena en palabras y luego iterar sobre cada palabra, agregándola al mapa si no existe o incrementando su contador si ya existe.

- Debes usar un mapa para almacenar los conteos de palabras.
- Debes dividir la cadena de entrada en palabras.
- Debes iterar sobre cada palabra en la cadena de entrada.
- Debes agregar cada palabra al mapa si no existe o incrementar su contador si ya existe.

```sh
# Tenga en cuenta que los mapas aparecen en la forma `map[k:v k:v]` cuando
# se imprime con `fmt.Println`.
$ go run maps.go
map: map[k1:7 k2:13]
v1: 7
v3: 0
len: 2
map: map[k1:7]
prs: false
map: map[bar:2 foo:1]
```

A continuación está el código completo:

```go
// Los _Maps_ son el tipo de datos asociativo integrado de Go
// (a veces llamado _hash_ o _diccionario_ en otros lenguajes).

package main

import "fmt"

func main() {

	// Para crear un mapa vacío, use la función interna `make`:
	// `make(map[key-type]val-type)`.
	m := make(map[string]int)

	// Establezca pares clave/valor usando la sintaxis típica `name[key] = val`.
	m["k1"] = 7
	m["k2"] = 13

	// Imprimir un mapa con, por ejemplo, `fmt.Println` mostrará todos sus
	// pares clave/valor.
	fmt.Println("map:", m)

	// Obtenga un valor para una clave con `name[key]`.
	v1 := m["k1"]
	fmt.Println("v1:", v1)

	// Si la clave no existe, se devuelve el
	// [valor cero](https://go.dev/ref/spec#The_zero_value) del
	// tipo de valor.
	v3 := m["k3"]
	fmt.Println("v3:", v3)

	// La función interna `len` devuelve el número de pares clave/valor
	// cuando se llama en un mapa.
	fmt.Println("len:", len(m))

	// La función interna `delete` elimina pares clave/valor de
	// un mapa.
	delete(m, "k2")
	fmt.Println("map:", m)

	// El segundo valor de retorno opcional al obtener un
	// valor de un mapa indica si la clave estaba presente
	// en el mapa. Esto se puede usar para distinguir
	// entre claves faltantes y claves con valores cero
	// como `0` o `""`. Aquí no necesitábamos el valor
	// en sí mismo, así que lo ignoramos con el _identificador en blanco_
	// `_`.
	_, prs := m["k2"]
	fmt.Println("prs:", prs)

	// También puede declarar e inicializar un nuevo mapa en
	// la misma línea con esta sintaxis.
	n := map[string]int{"foo": 1, "bar": 2}
	fmt.Println("map:", n)
}

```
