# XML

你需要创建一个名为 `Plant` 的结构体，该结构体能够映射到 XML。该结构体应具有以下字段：

- `Id` (int) - 一个 XML 属性
- `Name` (string) - 一个嵌套的 XML 元素
- `Origin` ([]string) - 一个嵌套的 XML 元素

你还需要创建一个名为 `Nesting` 的结构体，该结构体包含一个 `Plant` 结构体的切片。`Nesting` 结构体应映射到一个名为 `nesting` 的 XML 元素，并且 `Plant` 结构体应嵌套在 `<parent><child>...</child></parent>` 之下。

然后，你需要编写代码将 `Plant` 和 `Nesting` 结构体编组为 XML，并将 XML 数据解组到 `Plant` 结构体中。

- `Plant` 结构体应映射到一个名为 `plant` 的 XML 元素。
- `Plant` 结构体的 `Id` 字段应映射到一个名为 `id` 的 XML 属性。
- `Plant` 结构体的 `Name` 字段应映射到一个名为 `name` 的嵌套 XML 元素。
- `Plant` 结构体的 `Origin` 字段应映射到一个名为 `origin` 的嵌套 XML 元素。
- `Nesting` 结构体应映射到一个名为 `nesting` 的 XML 元素。
- `Nesting` 切片中的 `Plant` 结构体应嵌套在 `<parent><child>...</child></parent>` 之下。

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

以下是完整代码：

```go
// Go 通过 `encoding.xml` 包对 XML 及类似 XML 的格式提供了内置支持。

package main

import (
	"encoding/xml"
	"fmt"
)

// Plant 将被映射到 XML。与 JSON 示例类似，字段标签包含了编码器和解码器的指令。
// 在这里我们使用了 XML 包的一些特殊功能：`XMLName` 字段名决定了表示这个结构体的 XML 元素的名称；
// `id,attr` 表示 `Id` 字段是一个 XML _属性_ 而不是一个嵌套元素。
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

	// 生成表示我们的植物的 XML；使用 `MarshalIndent` 来生成更易读的输出。
	out, _ := xml.MarshalIndent(coffee, " ", "  ")
	fmt.Println(string(out))

	// 要在输出中添加通用的 XML 头部，需显式追加。
	fmt.Println(xml.Header + string(out))

	// 使用 `Unmarshal` 将包含 XML 的字节流解析为数据结构。
	// 如果 XML 格式错误或无法映射到 Plant，将返回一个描述性错误。
	var p Plant
	if err := xml.Unmarshal(out, &p); err!= nil {
		panic(err)
	}
	fmt.Println(p)

	tomato := &Plant{Id: 81, Name: "Tomato"}
	tomato.Origin = []string{"Mexico", "California"}

	// `parent>child>plant` 字段标签告诉编码器将所有 `plant` 嵌套在 `<parent><child>...</child></parent>` 之下
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
