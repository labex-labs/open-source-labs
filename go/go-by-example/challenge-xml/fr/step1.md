# XML

Vous êtes requis de créer une structure nommée `Plant` qui peut être mappée sur XML. La structure devrait avoir les champs suivants :

- `Id` (int) - un attribut XML
- `Name` (string) - un élément XML imbriqué
- `Origin` ([]string) - un élément XML imbriqué

Vous devriez également créer une structure nommée `Nesting` qui contient une slice de structs `Plant`. La structure `Nesting` devrait être mappée sur un élément XML nommé `nesting`, et les structs `Plant` devraient être imbriqués sous `<parent><child>...`.

Vous devriez ensuite écrire du code pour sérialiser les structs `Plant` et `Nesting` en XML, et désérialiser des données XML dans la struct `Plant`.

## Exigences

- La structure `Plant` devrait être mappée sur un élément XML nommé `plant`.
- Le champ `Id` de la structure `Plant` devrait être mappé sur un attribut XML nommé `id`.
- Le champ `Name` de la structure `Plant` devrait être mappé sur un élément XML imbriqué nommé `name`.
- Le champ `Origin` de la structure `Plant` devrait être mappé sur un élément XML imbriqué nommé `origin`.
- La structure `Nesting` devrait être mappée sur un élément XML nommé `nesting`.
- Les structs `Plant` dans la slice `Nesting` devraient être imbriqués sous `<parent><child>...`.

## Exemple

```sh
$ go run xml.go
 <plant id="27">
   <name>Café</name>
   <origin>Éthiopie</origin>
   <origin>Brésil</origin>
 </plant>
<?xml version="1.0" encoding="UTF-8"?>
 <plant id="27">
   <name>Café</name>
   <origin>Éthiopie</origin>
   <origin>Brésil</origin>
 </plant>
Plant id=27, name=Café, origin=[Éthiopie Brésil]
 <nesting>
   <parent>
     <child>
       <plant id="27">
         <name>Café</name>
         <origin>Éthiopie</origin>
         <origin>Brésil</origin>
       </plant>
       <plant id="81">
         <name>Tomate</name>
         <origin>Mexique</origin>
         <origin>Californie</origin>
       </plant>
     </child>
   </parent>
 </nesting>

```
