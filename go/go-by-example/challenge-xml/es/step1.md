# XML

Se te pide crear una estructura llamada `Plant` que se pueda mapear a XML. La estructura debe tener los siguientes campos:

- `Id` (int) - un atributo XML
- `Name` (string) - un elemento XML anidado
- `Origin` ([]string) - un elemento XML anidado

También debes crear una estructura llamada `Nesting` que contiene una slice de estructuras `Plant`. La estructura `Nesting` debe ser mapeada a un elemento XML llamado `nesting`, y las estructuras `Plant` deben estar anidadas bajo `<parent><child>...`.

Luego debes escribir código para serializar las estructuras `Plant` y `Nesting` a XML, y deserializar datos XML en la estructura `Plant`.

## Requisitos

- La estructura `Plant` debe ser mapeada a un elemento XML llamado `plant`.
- El campo `Id` de la estructura `Plant` debe ser mapeado a un atributo XML llamado `id`.
- El campo `Name` de la estructura `Plant` debe ser mapeado a un elemento XML anidado llamado `name`.
- El campo `Origin` de la estructura `Plant` debe ser mapeado a un elemento XML anidado llamado `origin`.
- La estructura `Nesting` debe ser mapeada a un elemento XML llamado `nesting`.
- Las estructuras `Plant` en la slice `Nesting` deben estar anidadas bajo `<parent><child>...`.

## Ejemplo

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
