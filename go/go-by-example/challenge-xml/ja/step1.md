# XML

XML にマッピングできる`Plant`という名前の構造体を作成する必要があります。この構造体は以下のフィールドを持つ必要があります。

- `Id` (int) - XML 属性
- `Name` (string) - ネストされた XML 要素
- `Origin` ([]string) - ネストされた XML 要素

また、`Plant`構造体のスライスを含む`Nesting`という名前の構造体も作成する必要があります。`Nesting`構造体は`nesting`という名前の XML 要素にマッピングされ、`Plant`構造体は`<parent><child>...`の下にネストされる必要があります。

その後、`Plant`と`Nesting`構造体を XML にマーシャリングし、XML データを`Plant`構造体にアンマーシャリングするコードを書く必要があります。

## 要件

- `Plant`構造体は`plant`という名前の XML 要素にマッピングされる必要があります。
- `Plant`構造体の`Id`フィールドは`id`という名前の XML 属性にマッピングされる必要があります。
- `Plant`構造体の`Name`フィールドは`name`という名前のネストされた XML 要素にマッピングされる必要があります。
- `Plant`構造体の`Origin`フィールドは`origin`という名前のネストされた XML 要素にマッピングされる必要があります。
- `Nesting`構造体は`nesting`という名前の XML 要素にマッピングされる必要があります。
- `Nesting`スライス内の`Plant`構造体は`<parent><child>...`の下にネストされる必要があります。

## 例

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
