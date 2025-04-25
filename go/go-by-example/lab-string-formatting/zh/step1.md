# 字符串格式化

你需要在 Go 语言中使用各种格式化动词来格式化不同类型的数据。

- 你必须使用 `fmt` 包来格式化数据。
- 对于每种数据类型，你必须使用正确的格式化动词。
- 你必须能够格式化整数、浮点数、字符串和结构体。
- 你必须能够控制输出的宽度和精度。
- 你必须能够使输出左对齐或右对齐。

```sh
$ go run string-formatting.go
struct1: {1 2}
struct2: {x:1 y:2}
struct3: main.point{x:1, y:2}
type: main.point
bool: true
int: 123
bin: 1110
char:!
hex: 1c8
float1: 78.900000
float2: 1.234000e+08
float3: 1.234000E+08
str1: "string"
str2: "\"string\""
str3: 6865782074686973
pointer: 0xc0000ba000
width1: | 12 | 345 \
  | width2: | 1.20 | 3.45 \
  | width3: | 1.20 | 3.45 \
  | width4: | foo | b \
  | width5: | foo | b \
  | sprintf: a string
io: an error
```

以下是完整代码：

```go
// Go 在 `printf` 传统中对字符串格式化提供了出色的支持。
// 以下是一些常见字符串格式化任务的示例。

package main

import (
	"fmt"
	"os"
)

type point struct {
	x, y int
}

func main() {

	// Go 提供了几个用于格式化一般 Go 值的打印“动词”。
	// 例如，这会打印我们 `point` 结构体的一个实例。
	p := point{1, 2}
	fmt.Printf("struct1: %v\n", p)

	// 如果值是一个结构体，`%+v` 变体将包含结构体的字段名。
	fmt.Printf("struct2: %+v\n", p)

	// `%#v` 变体打印值的 Go 语法表示形式，
	// 即会生成该值的源代码片段。
	fmt.Printf("struct3: %#v\n", p)

	// 要打印值的类型，使用 `%T`。
	fmt.Printf("type: %T\n", p)

	// 格式化布尔值很简单。
	fmt.Printf("bool: %t\n", true)

	// 格式化整数有很多选项。
	// 使用 `%d` 进行标准的十进制格式化。
	fmt.Printf("int: %d\n", 123)

	// 这会打印二进制表示形式。
	fmt.Printf("bin: %b\n", 14)

	// 这会打印与给定整数对应的字符。
	fmt.Printf("char: %c\n", 33)

	// `%x` 提供十六进制编码。
	fmt.Printf("hex: %x\n", 456)

	// 对于浮点数也有几个格式化选项。
	// 对于基本的十进制格式化，使用 `%f`。
	fmt.Printf("float1: %f\n", 78.9)

	// `%e` 和 `%E` 以（略有不同版本的）科学记数法格式化浮点数。
	fmt.Printf("float2: %e\n", 123400000.0)
	fmt.Printf("float3: %E\n", 123400000.0)

	// 对于基本的字符串打印，使用 `%s`。
	fmt.Printf("str1: %s\n", "\"string\"")

	// 要像在 Go 源代码中那样对字符串进行双引号括起来，使用 `%q`。
	fmt.Printf("str2: %q\n", "\"string\"")

	// 与前面看到的整数一样，`%x` 以十六进制渲染字符串，
	// 输入的每个字节输出两个字符。
	fmt.Printf("str3: %x\n", "hex this")

	// 要打印指针的表示形式，使用 `%p`。
	fmt.Printf("pointer: %p\n", &p)

	// 格式化数字时，你通常会希望控制结果数字的宽度和精度。
	// 要指定整数的宽度，在动词中的 `%` 后面使用一个数字。
	// 默认情况下，结果将右对齐并用空格填充。
	fmt.Printf("width1: |%6d|%6d|\n", 12, 345)

	// 你也可以指定打印浮点数的宽度，
	// 不过通常你还会希望同时使用 width.precision 语法限制十进制精度。
	fmt.Printf("width2: |%6.2f|%6.2f|\n", 1.2, 3.45)

	// 要左对齐，使用 `-` 标志。
	fmt.Printf("width3: |%-6.2f|%-6.2f|\n", 1.2, 3.45)

	// 格式化字符串时，你可能还希望控制宽度，
	// 特别是为了确保它们在类似表格的输出中对齐。
	// 对于基本的右对齐宽度。
	fmt.Printf("width4: |%6s|%6s|\n", "foo", "b")

	// 要左对齐，与数字一样使用 `-` 标志。
	fmt.Printf("width5: |%-6s|%-6s|\n", "foo", "b")

	// 到目前为止，我们看到了 `Printf`，它将格式化后的字符串打印到 `os.Stdout`。
	// `Sprintf` 格式化并返回一个字符串，而不将其打印到任何地方。
	s := fmt.Sprintf("sprintf: a %s", "string")
	fmt.Println(s)

	// 你可以使用 `Fprintf` 将格式化后的内容打印到除 `os.Stdout` 之外的 `io.Writers`。
	fmt.Fprintf(os.Stderr, "io: an %s\n", "error")
}

```
