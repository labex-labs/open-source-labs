# Plantillas de texto

En este laboratorio, se te pide demostrar el uso del paquete `text/template` para generar contenido dinámico.

- Utiliza el paquete `text/template` para generar contenido dinámico.
- Utiliza la función `template.Must` para generar un error en caso de que `Parse` devuelva un error.
- Utiliza la acción `{{.FieldName}}` para acceder a los campos de un struct.
- Utiliza la acción `{{if. -}} si {{else -}} no {{end}}\n` para proporcionar una ejecución condicional para las plantillas.
- Utiliza la acción `{{range.}}{{.}} {{end}}\n` para recorrer slices, arrays, maps o canales.

```sh
$ go run templates.go
Valor: algún texto
Valor: 5
Valor: [Go Rust C++ C#]
Nombre: Jane Doe
Nombre: Mickey Mouse
si
no
Rango: Go Rust C++ C#
```

A continuación se muestra el código completo:

```go
// Go ofrece soporte integrado para crear contenido dinámico o mostrar una
// salida personalizada al usuario con el paquete `text/template`. Un paquete
// hermano llamado `html/template` proporciona la misma API pero tiene
// características de seguridad adicionales y se debe utilizar para generar HTML.

package main

import (
	"os"
	"text/template"
)

func main() {

	// Podemos crear una nueva plantilla y analizar su cuerpo a partir de
	// una cadena.
	// Las plantillas son una mezcla de texto estático y "acciones" encerradas
	// en `{{...}}` que se utilizan para insertar dinámicamente contenido.
	t1 := template.New("t1")
	t1, err := t1.Parse("Valor es {{.}}\n")
	if err!= nil {
		panic(err)
	}

	// Alternativamente, podemos utilizar la función `template.Must` para
	// generar un error en caso de que `Parse` devuelva un error. Esto es
	// especialmente útil para las plantillas inicializadas en el ámbito global.
	t1 = template.Must(t1.Parse("Valor: {{.}}\n"))

	// Al "ejecutar" la plantilla, generamos su texto con
	// valores específicos para sus acciones. La acción `{{.}}` es
	// reemplazada por el valor pasado como parámetro a `Execute`.
	t1.Execute(os.Stdout, "algún texto")
	t1.Execute(os.Stdout, 5)
	t1.Execute(os.Stdout, []string{
		"Go",
		"Rust",
		"C++",
		"C#",
	})

	// Función auxiliar que utilizaremos más adelante.
	Create := func(name, t string) *template.Template {
		return template.Must(template.New(name).Parse(t))
	}

	// Si los datos son un struct, podemos utilizar la acción `{{.FieldName}}` para acceder
	// a sus campos. Los campos deben ser exportados para ser accesibles cuando
	// se está ejecutando una plantilla.
	t2 := Create("t2", "Nombre: {{.Nombre}}\n")

	t2.Execute(os.Stdout, struct {
		Nombre string
	}{"Jane Doe"})

	// Lo mismo se aplica a los maps; con los maps no hay restricción sobre el
	// caso de los nombres de las claves.
	t2.Execute(os.Stdout, map[string]string{
		"Nombre": "Mickey Mouse",
	})

	// if/else proporcionan una ejecución condicional para las plantillas. Un valor se considera
	// falso si es el valor predeterminado de un tipo, como 0, una cadena vacía,
	// un puntero nulo, etc.
	// Este ejemplo demuestra otra
	// característica de las plantillas: utilizar `-` en las acciones para eliminar el espacio en blanco.
	t3 := Create("t3",
		"{{if. -}} si {{else -}} no {{end}}\n")
	t3.Execute(os.Stdout, "no está vacío")
	t3.Execute(os.Stdout, "")

	// Los bloques range nos permiten recorrer slices, arrays, maps o canales. Dentro
	// del bloque range, `{{.}}` se establece en el elemento actual de la iteración.
	t4 := Create("t4",
		"Rango: {{range.}}{{.}} {{end}}\n")
	t4.Execute(os.Stdout,
		[]string{
			"Go",
			"Rust",
			"C++",
			"C#",
		})
}

```
