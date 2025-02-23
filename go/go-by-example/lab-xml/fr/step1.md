# XML

Vous devrez créer une structure nommée `Plant` qui peut être mappée sur XML. La structure devrait avoir les champs suivants :

- `Id` (int) - un attribut XML
- `Name` (string) - un élément XML imbriqué
- `Origin` ([]string) - un élément XML imbriqué

Vous devriez également créer une structure nommée `Nesting` qui contient une slice de structs `Plant`. La structure `Nesting` devrait être mappée sur un élément XML nommé `nesting`, et les structs `Plant` devraient être imbriqués sous `<parent><child>...`.

Vous devriez ensuite écrire du code pour sérialiser les structs `Plant` et `Nesting` en XML, et désérialiser des données XML dans la structure `Plant`.

- La structure `Plant` devrait être mappée sur un élément XML nommé `plant`.
- Le champ `Id` de la structure `Plant` devrait être mappé sur un attribut XML nommé `id`.
- Le champ `Name` de la structure `Plant` devrait être mappé sur un élément XML imbriqué nommé `name`.
- Le champ `Origin` de la structure `Plant` devrait être mappé sur un élément XML imbriqué nommé `origin`.
- La structure `Nesting` devrait être mappée sur un élément XML nommé `nesting`.
- Les structs `Plant` dans la slice `Nesting` devraient être imbriqués sous `<parent><child>...`.

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

Voici le code complet ci-dessous :

```go
// Go offre une prise en charge intégrée pour XML et des formats similaires à XML
// avec le package `encoding.xml`.

package main

import (
	"encoding/xml"
	"fmt"
)

// Plant sera mappé sur XML. De manière similaire aux
// exemples JSON, les balises de champ contiennent des directives pour l'
// encodeur et le décodeur. Ici, nous utilisons quelques fonctionnalités
// spéciales du package XML : le nom de champ `XMLName` détermine
// le nom de l'élément XML représentant cette structure ;
// `id,attr` signifie que le champ `Id` est un XML
// _attribut_ plutôt qu'un élément imbriqué.
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

	// Génère XML représentant notre plante ; en utilisant
	// `MarshalIndent` pour produire une sortie plus
	// lisible pour l'homme.
	out, _ := xml.MarshalIndent(coffee, " ", "  ")
	fmt.Println(string(out))

	// Pour ajouter un en-tête XML générique à la sortie, ajoutez-le
	// explicitement.
	fmt.Println(xml.Header + string(out))

	// Utilisez `Unmarshal` pour analyser un flux de bytes avec XML
	// dans une structure de données. Si l'XML est mal formé ou
	// ne peut pas être mappé sur Plant, une erreur descriptive
	// sera renvoyée.
	var p Plant
	if err := xml.Unmarshal(out, &p); err!= nil {
		panic(err)
	}
	fmt.Println(p)

	tomato := &Plant{Id: 81, Name: "Tomato"}
	tomato.Origin = []string{"Mexico", "California"}

	// La balise de champ `parent>child>plant` indique à l'encodeur
	// de plonger tous les `plant` sous `<parent><child>...`
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
