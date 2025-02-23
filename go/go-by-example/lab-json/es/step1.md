# JSON

Se te pide que completes el código proporcionado para codificar y decodificar datos JSON en Golang. El código contiene ejemplos de codificación y decodificación de tipos de datos básicos, así como de tipos de datos personalizados.

- Conocimientos básicos del lenguaje de programación Golang.
- Conocimiento de la codificación y decodificación de datos JSON en Golang.
- Capacidad para leer y entender el código de Golang existente.

```sh
$ go run json.go
true
1
2.34
"gopher"
["apple","peach","pear"]
{"apple":5,"lettuce":7}
{"Page":1,"Fruits":["apple","peach","pear"]}
{"page":1,"fruits":["apple","peach","pear"]}
map[num:6.13 strs:[a b]]
6.13
a
{1 [apple peach]}
apple
{"apple":5,"lettuce":7}


# Aquí hemos cubierto los conceptos básicos de JSON en Go, pero consulta
# la publicación del blog [JSON and Go](https://go.dev/blog/json)
# y la documentación del paquete [JSON package docs](https://pkg.go.dev/encoding/json)
# para obtener más información.

```

A continuación se muestra el código completo:

```go
// Go ofrece soporte integrado para la codificación y
// decodificación de JSON, incluyendo la conversión entre
// tipos de datos integrados y personalizados.

package main

import (
	"encoding/json"
	"fmt"
	"os"
)

// Utilizaremos estas dos estructuras para demostrar la codificación y
// decodificación de tipos personalizados más adelante.
type response1 struct {
	Page   int
	Fruits []string
}

// Solo los campos exportados se codificarán/decodificarán en JSON.
// Los campos deben comenzar con una letra mayúscula para ser exportados.
type response2 struct {
	Page   int      `json:"page"`
	Fruits []string `json:"fruits"`
}

func main() {

	// Primero veremos cómo codificar tipos de datos básicos a
	// cadenas JSON. Aquí hay algunos ejemplos para valores atómicos.
	bolB, _ := json.Marshal(true)
	fmt.Println(string(bolB))

	intB, _ := json.Marshal(1)
	fmt.Println(string(intB))

	fltB, _ := json.Marshal(2.34)
	fmt.Println(string(fltB))

	strB, _ := json.Marshal("gopher")
	fmt.Println(string(strB))

	// Y aquí hay algunos para slices y maps, que se codifican
	// a arrays y objetos JSON como se esperaría.
	slcD := []string{"apple", "peach", "pear"}
	slcB, _ := json.Marshal(slcD)
	fmt.Println(string(slcB))

	mapD := map[string]int{"apple": 5, "lettuce": 7}
	mapB, _ := json.Marshal(mapD)
	fmt.Println(string(mapB))

	// El paquete JSON puede codificar automáticamente tus
	// tipos de datos personalizados. Solo incluirá los campos
	// exportados en la salida codificada y, por defecto,
	// usará esos nombres como claves JSON.
	res1D := &response1{
		Page:   1,
		Fruits: []string{"apple", "peach", "pear"}}
	res1B, _ := json.Marshal(res1D)
	fmt.Println(string(res1B))

	// Puedes usar etiquetas en las declaraciones de campos de struct
	// para personalizar los nombres de claves JSON codificadas. Revisa la
	// definición de `response2` arriba para ver un ejemplo de tales etiquetas.
	res2D := &response2{
		Page:   1,
		Fruits: []string{"apple", "peach", "pear"}}
	res2B, _ := json.Marshal(res2D)
	fmt.Println(string(res2B))

	// Ahora veamos cómo decodificar datos JSON en valores de Go.
	// Aquí hay un ejemplo para una estructura de datos genérica.
	byt := []byte(`{"num":6.13,"strs":["a","b"]}`)

	// Necesitamos proporcionar una variable donde el paquete JSON
	// pueda poner los datos decodificados. Esta
	// `map[string]interface{}` contendrá un mapa de cadenas
	// a tipos de datos arbitrarios.
	var dat map[string]interface{}

	// Aquí está la decodificación real, y una comprobación de
	// errores asociados.
	if err := json.Unmarshal(byt, &dat); err!= nil {
		panic(err)
	}
	fmt.Println(dat)

	// Para poder usar los valores en el mapa decodificado,
	// necesitaremos convertirlos al tipo adecuado.
	// Por ejemplo, aquí convertimos el valor en `num` al
	// tipo `float64` esperado.
	num := dat["num"].(float64)
	fmt.Println(num)

	// Acceder a datos anidados requiere una serie de
	// conversiones.
	strs := dat["strs"].([]interface{})
	str1 := strs[0].(string)
	fmt.Println(str1)

	// También podemos decodificar JSON en tipos de datos personalizados.
	// Esto tiene la ventaja de agregar una seguridad adicional
	// de tipos a nuestros programas y eliminar la necesidad de
	// aserciones de tipo al acceder a los datos decodificados.
	str := `{"page": 1, "fruits": ["apple", "peach"]}`
	res := response2{}
	json.Unmarshal([]byte(str), &res)
	fmt.Println(res)
	fmt.Println(res.Fruits[0])

	// En los ejemplos anteriores siempre usamos bytes y
	// cadenas como intermediarios entre los datos y la
	// representación JSON en la salida estándar. También podemos
	// transmitir codificaciones JSON directamente a `os.Writer`s como
	// `os.Stdout` o incluso a cuerpos de respuesta HTTP.
	enc := json.NewEncoder(os.Stdout)
	d := map[string]int{"apple": 5, "lettuce": 7}
	enc.Encode(d)
}

```
