# XML

Você precisará criar uma struct chamada `Plant` que possa ser mapeada para XML. A struct deve ter os seguintes campos:

- `Id` (int) - um atributo XML
- `Name` (string) - um elemento XML aninhado
- `Origin` ([]string) - um elemento XML aninhado

Você também deve criar uma struct chamada `Nesting` que contenha uma slice de structs `Plant`. A struct `Nesting` deve ser mapeada para um elemento XML chamado `nesting`, e as structs `Plant` devem ser aninhadas sob `<parent><child>...`.

Em seguida, você deve escrever código para serializar (marshal) as structs `Plant` e `Nesting` para XML, e deserializar (unmarshal) dados XML na struct `Plant`.

- A struct `Plant` deve ser mapeada para um elemento XML chamado `plant`.
- O campo `Id` da struct `Plant` deve ser mapeado para um atributo XML chamado `id`.
- O campo `Name` da struct `Plant` deve ser mapeado para um elemento XML aninhado chamado `name`.
- O campo `Origin` da struct `Plant` deve ser mapeado para um elemento XML aninhado chamado `origin`.
- A struct `Nesting` deve ser mapeada para um elemento XML chamado `nesting`.
- As structs `Plant` na slice `Nesting` devem ser aninhadas sob `<parent><child>...`.

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

Segue o código completo:

```go
// Go oferece suporte embutido para XML e formatos semelhantes a XML
// com o pacote `encoding.xml`.

package main

import (
	"encoding/xml"
	"fmt"
)

// Plant será mapeado para XML. Semelhante aos
// exemplos JSON, as tags de campo contêm diretivas para o
// codificador e decodificador. Aqui usamos alguns recursos especiais
// do pacote XML: o nome do campo `XMLName` dita
// o nome do elemento XML que representa esta struct;
// `id,attr` significa que o campo `Id` é um XML
// _atributo_ em vez de um elemento aninhado.
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

	// Emite XML representando nossa planta; usando
	// `MarshalIndent` para produzir uma saída mais
	// legível por humanos.
	out, _ := xml.MarshalIndent(coffee, " ", "  ")
	fmt.Println(string(out))

	// Para adicionar um cabeçalho XML genérico à saída, anexe
	// explicitamente.
	fmt.Println(xml.Header + string(out))

	// Use `Unmarshal` para analisar um fluxo de bytes com XML
	// em uma estrutura de dados. Se o XML estiver malformado ou
	// não puder ser mapeado para Plant, um erro descritivo
	// será retornado.
	var p Plant
	if err := xml.Unmarshal(out, &p); err != nil {
		panic(err)
	}
	fmt.Println(p)

	tomato := &Plant{Id: 81, Name: "Tomato"}
	tomato.Origin = []string{"Mexico", "California"}

	// A tag de campo `parent>child>plant` diz ao codificador
	// para aninhar todas as `plant`s sob `<parent><child>...`
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
