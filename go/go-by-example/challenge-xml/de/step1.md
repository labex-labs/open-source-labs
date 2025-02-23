# XML

Sie müssen eine Struktur namens `Plant` erstellen, die in XML abgebildet werden kann. Die Struktur sollte die folgenden Felder haben:

- `Id` (int) - ein XML-Attribut
- `Name` (string) - ein geschachtelter XML-Element
- `Origin` ([]string) - ein geschachtelter XML-Element

Sie sollten auch eine Struktur namens `Nesting` erstellen, die eine Liste von `Plant`-Strukturen enthält. Die `Nesting`-Struktur sollte einem XML-Element namens `nesting` zugeordnet werden, und die `Plant`-Strukturen sollten unter `<parent><child>...` geschachtelt sein.

Anschließend sollten Sie Code schreiben, um die `Plant`- und `Nesting`-Strukturen in XML zu marshalisieren und XML-Daten in die `Plant`-Struktur zu unmarshalieren.

## Anforderungen

- Die `Plant`-Struktur sollte einem XML-Element namens `plant` zugeordnet werden.
- Das `Id`-Feld der `Plant`-Struktur sollte einem XML-Attribut namens `id` zugeordnet werden.
- Das `Name`-Feld der `Plant`-Struktur sollte einem geschachtelten XML-Element namens `name` zugeordnet werden.
- Das `Origin`-Feld der `Plant`-Struktur sollte einem geschachtelten XML-Element namens `origin` zugeordnet werden.
- Die `Nesting`-Struktur sollte einem XML-Element namens `nesting` zugeordnet werden.
- Die `Plant`-Strukturen in der `Nesting`-Liste sollten unter `<parent><child>...` geschachtelt sein.

## Beispiel

```sh
$ go run xml.go
 <plant id="27">
   <name>Kaffee</name>
   <origin>Äthiopien</origin>
   <origin>Brasilien</origin>
 </plant>
<?xml version="1.0" encoding="UTF-8"?>
 <plant id="27">
   <name>Kaffee</name>
   <origin>Äthiopien</origin>
   <origin>Brasilien</origin>
 </plant>
Plant id=27, name=Kaffee, origin=[Äthiopien Brasilien]
 <nesting>
   <parent>
     <child>
       <plant id="27">
         <name>Kaffee</name>
         <origin>Äthiopien</origin>
         <origin>Brasilien</origin>
       </plant>
       <plant id="81">
         <name>Tomate</name>
         <origin>Mexiko</origin>
         <origin>Kalifornien</origin>
       </plant>
     </child>
   </parent>
 </nesting>

```
