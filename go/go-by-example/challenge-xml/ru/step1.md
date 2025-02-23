# XML

Требуется создать структуру под названием `Plant`, которая может быть сопоставлена с XML. Структура должна иметь следующие поля:

- `Id` (int) - XML-атрибут
- `Name` (string) - вложенный XML-элемент
- `Origin` ([]string) - вложенный XML-элемент

Также необходимо создать структуру под названием `Nesting`, которая содержит срез структур `Plant`. Структура `Nesting` должна быть сопоставлена с XML-элементом под названием `nesting`, а структуры `Plant` должны быть вложены под `<parent><child>...`.

Затем необходимо написать код для маршалинга структур `Plant` и `Nesting` в XML и демаршалинга XML-данных в структуру `Plant`.

## Требования

- Структура `Plant` должна быть сопоставлена с XML-элементом под названием `plant`.
- Поле `Id` структуры `Plant` должно быть сопоставлено с XML-атрибутом под названием `id`.
- Поле `Name` структуры `Plant` должно быть сопоставлено с вложенным XML-элементом под названием `name`.
- Поле `Origin` структуры `Plant` должно быть сопоставлено с вложенным XML-элементом под названием `origin`.
- Структура `Nesting` должна быть сопоставлена с XML-элементом под названием `nesting`.
- Структуры `Plant` в срезе `Nesting` должны быть вложены под `<parent><child>...`.

## Пример

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
