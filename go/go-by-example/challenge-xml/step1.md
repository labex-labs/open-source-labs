# XML

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

## Example

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
