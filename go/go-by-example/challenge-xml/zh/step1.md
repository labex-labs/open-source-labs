# XML

你需要创建一个名为 `Plant` 的结构体，该结构体能够映射到 XML。该结构体应具有以下字段：

- `Id` (int) - 一个 XML 属性
- `Name` (string) - 一个嵌套的 XML 元素
- `Origin` ([]string) - 一个嵌套的 XML 元素

你还应创建一个名为 `Nesting` 的结构体，该结构体包含一个 `Plant` 结构体切片。`Nesting` 结构体应映射到一个名为 `nesting` 的 XML 元素，并且 `Plant` 结构体应嵌套在 `<parent><child>...</child></parent>` 之下。

然后，你需要编写代码将 `Plant` 和 `Nesting` 结构体编组为 XML，并将 XML 数据解组到 `Plant` 结构体中。

## 要求

- `Plant` 结构体应映射到一个名为 `plant` 的 XML 元素。
- `Plant` 结构体的 `Id` 字段应映射到一个名为 `id` 的 XML 属性。
- `Plant` 结构体的 `Name` 字段应映射到一个名为 `name` 的嵌套 XML 元素。
- `Plant` 结构体的 `Origin` 字段应映射到一个名为 `origin` 的嵌套 XML 元素。
- `Nesting` 结构体应映射到一个名为 `nesting` 的 XML 元素。
- `Nesting` 切片中的 `Plant` 结构体应嵌套在 `<parent><child>...</child></parent>` 之下。

## 示例

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
