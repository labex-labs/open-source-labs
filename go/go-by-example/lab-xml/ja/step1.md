# XML

XML にマッピングできる`Plant`という名前の構造体を作成する必要があります。この構造体は以下のフィールドを持つ必要があります。

- `Id` (int) - XML 属性
- `Name` (string) - ネストされた XML 要素
- `Origin` ([]string) - ネストされた XML 要素

また、`Plant`構造体のスライスを含む`Nesting`という名前の構造体も作成する必要があります。`Nesting`構造体は`nesting`という名前の XML 要素にマッピングされ、`Plant`構造体は`<parent><child>...</child></parent>`の下にネストされる必要があります。

次に、`Plant`と`Nesting`構造体を XML にマーシャリングし、XML データを`Plant`構造体にアンマーシャリングするコードを書く必要があります。

- `Plant`構造体は`plant`という名前の XML 要素にマッピングされる必要があります。
- `Plant`構造体の`Id`フィールドは`id`という名前の XML 属性にマッピングされる必要があります。
- `Plant`構造体の`Name`フィールドは`name`という名前のネストされた XML 要素にマッピングされる必要があります。
- `Plant`構造体の`Origin`フィールドは`origin`という名前のネストされた XML 要素にマッピングされる必要があります。
- `Nesting`構造体は`nesting`という名前の XML 要素にマッピングされる必要があります。
- `Nesting`スライス内の`Plant`構造体は`<parent><child>...</child></parent>`の下にネストされる必要があります。

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

以下が完全なコードです。

```go
// Go は `encoding.xml` パッケージを使って XML および XML に似た
// 形式に対する組み込みのサポートを提供しています。

package main

import (
	"encoding/xml"
	"fmt"
)

// Plant は XML にマッピングされます。JSON の例と同様に、フィールドタグには
// エンコーダとデコーダに対する指示が含まれています。ここでは XML パッケージの
// いくつかの特別な機能を使っています。`XMLName` フィールド名はこの構造体を表す
// XML 要素の名前を指定します。`id,attr` は `Id` フィールドが XML の
// _属性_ であり、ネストされた要素ではないことを意味します。
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

	// 私たちの植物を表す XML を生成します。`MarshalIndent` を使って
	// より読みやすい出力を生成します。
	out, _ := xml.MarshalIndent(coffee, " ", "  ")
	fmt.Println(string(out))

	// 出力に汎用的な XML ヘッダを追加するには、明示的に追加します。
	fmt.Println(xml.Header + string(out))

	// `Unmarshal` を使って XML で構成されたバイト列をデータ構造に
	// パースします。XML が不正または Plant にマッピングできない場合、
	// 記述的なエラーが返されます。
	var p Plant
	if err := xml.Unmarshal(out, &p); err!= nil {
		panic(err)
	}
	fmt.Println(p)

	tomato := &Plant{Id: 81, Name: "Tomato"}
	tomato.Origin = []string{"Mexico", "California"}

	// `parent>child>plant` フィールドタグはエンコーダに指示して、
	// すべての `plant` を `<parent><child>...</child></parent>` の下に
	// ネストさせます。
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
