# Golang Challenge: XML

## Introduction

This challenge aims to test your knowledge of working with XML in Golang. You will be required to create a struct that can be mapped to XML, marshal and unmarshal XML data, and use field tags to define the structure of the XML output.

## Problem

You are required to create a struct named `Plant` that can be mapped to XML. The struct should have the following fields:

- `Id` (int) - an XML attribute
- `Name` (string) - a nested XML element
- `Origin` ([]string) - a nested XML element

You should also create a struct named `Nesting` that contains a slice of `Plant` structs. The `Nesting` struct should be mapped to an XML element named `nesting`, and the `Plant` structs should be nested under `<parent><child>...`.

You should then write code to marshal the `Plant` and `Nesting` structs to XML, and unmarshal XML data into the `Plant` struct.

## Requirements

- The `Plant` struct should be mapped to an XML element named `plant`.
- The `Id` field of the `Plant` struct should be mapped to an XML attribute named `id`.
- The `Name` field of the `Plant` struct should be mapped to a nested XML element named `name`.
- The `Origin` field of the `Plant` struct should be mapped to a nested XML element named `origin`.
- The `Nesting` struct should be mapped to an XML element named `nesting`.
- The `Plant` structs in the `Nesting` slice should be nested under `<parent><child>...`.

## TODO

You need to complete the following code blocks:

```go
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

type Nesting struct {
	XMLName xml.Name `xml:"nesting"`
	Plants  []*Plant `xml:"parent>child>plant"`
}

func main() {
	coffee := &Plant{Id: 27, Name: "Coffee"}
	coffee.Origin = []string{"Ethiopia", "Brazil"}

	out, _ := xml.MarshalIndent(coffee, " ", "  ")
	fmt.Println(string(out))

	fmt.Println(xml.Header + string(out))

	var p Plant
	if err := xml.Unmarshal(out, &p); err != nil {
		panic(err)
	}
	fmt.Println(p)

	tomato := &Plant{Id: 81, Name: "Tomato"}
	tomato.Origin = []string{"Mexico", "California"}

	nesting := &Nesting{}
	nesting.Plants = []*Plant{coffee, tomato}

	out, _ = xml.MarshalIndent(nesting, " ", "  ")
	fmt.Println(string(out))
}
```

## Example

```
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

## Summary

In this challenge, you learned how to work with XML in Golang. You created a struct that can be mapped to XML, marshaled and unmarshaled XML data, and used field tags to define the structure of the XML output.
