# XML

Se le pide que cree una estructura llamada `Plant` que se pueda mapear a XML. La estructura debe tener los siguientes campos:

- `Id` (int) - un atributo XML
- `Name` (string) - un elemento XML anidado
- `Origin` ([]string) - un elemento XML anidado

También debe crear una estructura llamada `Nesting` que contiene una slice de estructuras `Plant`. La estructura `Nesting` debe ser mapeada a un elemento XML llamado `nesting`, y las estructuras `Plant` deben estar anidadas bajo `<parent><child>...`.

Luego debe escribir código para serializar las estructuras `Plant` y `Nesting` a XML, y deserializar datos XML en la estructura `Plant`.

- La estructura `Plant` debe ser mapeada a un elemento XML llamado `plant`.
- El campo `Id` de la estructura `Plant` debe ser mapeado a un atributo XML llamado `id`.
- El campo `Name` de la estructura `Plant` debe ser mapeado a un elemento XML anidado llamado `name`.
- El campo `Origin` de la estructura `Plant` debe ser mapeado a un elemento XML anidado llamado `origin`.
- La estructura `Nesting` debe ser mapeada a un elemento XML llamado `nesting`.
- Las estructuras `Plant` en la slice `Nesting` deben estar anidadas bajo `<parent><child>...`.

```sh
$ go run xml.go
 <plant id="27">
   <name>Coffee</name>
   <origin>Ethiopia</origin>
   <origin>Brazil</origin>
 </plant>
<?xml version="1.0" encoding="UTF-8"?>
 <plant id="27">
   <name>Coffee</name>
   <origin>Ethiopia</origin>
   <origin>Brazil</origin>
 </plant>
Plant id=27, name=Coffee, origin=[Ethiopia Brazil]
 <nesting>
   <parent>
     <child>
       <plant id="27">
         <name>Coffee</name>
         <origin>Ethiopia</origin>
         <origin>Brazil</origin>
       </plant>
       <plant id="81">
         <name>Tomato</name>
         <origin>Mexico</origin>
         <origin>California</origin>
       </plant>
     </child>
   </parent>
 </nesting>

```

A continuación está el código completo:

```go
// Go ofrece soporte integrado para XML y formatos similares
// con el paquete `encoding.xml`.

package main

import (
	"encoding/xml"
	"fmt"
)

// Plant se mapeará a XML. Similar a los ejemplos de JSON,
// las etiquetas de campo contienen directivas para el
// codificador y el decodificador. Aquí usamos algunas
// características especiales del paquete XML: el nombre de
// campo `XMLName` dicta el nombre del elemento XML que
// representa esta estructura; `id,attr` significa que el
// campo `Id` es un _atributo_ XML en lugar de un
// elemento anidado.
type Plant struct {
	XMLName xml.Name `xml:"plant"`
	Id      int      `xml:"id,attr"`
	Name    string   `xml:"name"`
	Origin  []string `xml:"origin"`
}

func (p Plant) String() string {
	return fmt.Sprintf("Plant id=%v, name=%v, origin=%v",
		p.Id, p.Name, p.Origin)
}

func main() {
	coffee := &Plant{Id: 27, Name: "Coffee"}
	coffee.Origin = []string{"Ethiopia", "Brazil"}

	// Emitir XML que representa nuestra planta; usando
	// `MarshalIndent` para producir una salida más
	// legible para humanos.
	out, _ := xml.MarshalIndent(coffee, " ", "  ")
	fmt.Println(string(out))

	// Para agregar un encabezado XML genérico a la salida,
	// agregarlo explícitamente.
	fmt.Println(xml.Header + string(out))

	// Usar `Unmarshal` para analizar un flujo de bytes con
	// XML en una estructura de datos. Si el XML está
	// malformado o no se puede mapear en Plant, se
	// devolverá un error descriptivo.
	var p Plant
	if err := xml.Unmarshal(out, &p); err!= nil {
		panic(err)
	}
	fmt.Println(p)

	tomato := &Plant{Id: 81, Name: "Tomato"}
	tomato.Origin = []string{"Mexico", "California"}

	// La etiqueta de campo `parent>child>plant` le dice al
	// codificador que anide todas las `plant` bajo
	// `<parent><child>...`
	type Nesting struct {
		XMLName xml.Name `xml:"nesting"`
		Plants  []*Plant `xml:"parent>child>plant"`
	}

	nesting := &Nesting{}
	nesting.Plants = []*Plant{coffee, tomato}

	out, _ = xml.MarshalIndent(nesting, " ", "  ")
	fmt.Println(string(out))
}

```
