# 字符串与符文（rune）

本实验要解决的问题是理解如何在 Go 语言中处理字符串和符文。具体来说，本实验将涵盖如何获取字符串的长度、如何对字符串进行索引、如何计算字符串中的符文数量以及如何遍历字符串中的符文。

要完成本实验，你需要：

- 对 Go 语言语法有基本的了解
- 掌握 Go 语言中的字符串和符文
- 了解 Go 标准库

```sh
$ go run strings-and-runes.go
长度：18
e0 b8 aa e0 b8 a7 e0 b8 b1 e0 b8 aa e0 b8 94 e0 b8 b5
符文数量：6
U+0E2A 'ส' 起始位置为0
U+0E27 'ว' 起始位置为3
U+0E31 'ั' 起始位置为6
U+0E2A 'ส' 起始位置为9
U+0E14 'ด' 起始位置为12
U+0E35 'ี' 起始位置为15

使用DecodeRuneInString
U+0E2A 'ส' 起始位置为0
找到 so sua
U+0E27 'ว' 起始位置为3
U+0E31 'ั' 起始位置为6
U+0E2A 'ส' 起始位置为9
找到 so sua
U+0E14 'ด' 起始位置为12
U+0E35 'ี' 起始位置为15
```

以下是完整代码：

```go
// Go 语言中的字符串是只读的字节切片。该语言
// 和标准库对字符串有特殊处理 - 它们被视为
// 以 [UTF-8](https://en.wikipedia.org/wiki/UTF-8) 编码的文本容器。
// 在其他语言中，字符串由“字符”组成。
// 在 Go 语言中，字符的概念称为 `rune` - 它是
// 一个表示 Unicode 码点的整数。
// [这篇 Go 语言博客文章](https://go.dev/blog/strings) 是
// 关于该主题的很好的介绍。

package main

import (
	"fmt"
	"unicode/utf8"
)

func main() {

	// `s` 是一个 `string` 类型，被赋予一个字面量值
	// 它表示泰语中的“你好”一词。Go 语言的字符串字面量是
	// UTF-8 编码的文本。
	const s = "สวัสดี"

	// 由于字符串等同于 `[]byte`，这将产生存储在其中的原始字节的长度。
	fmt.Println("长度：", len(s))

	// 对字符串进行索引会产生每个索引处的原始字节值。
	// 这个循环生成构成 `s` 中码点的所有字节的十六进制值。
	for i := 0; i < len(s); i++ {
		fmt.Printf("%x ", s[i])
	}
	fmt.Println()

	// 要计算字符串中有多少个 _符文_，我们可以使用
	// `utf8` 包。请注意，`RuneCountInString` 的运行时
	// 取决于字符串的大小，因为它必须按顺序解码每个 UTF-8 符文。
	// 一些泰语字符由多个 UTF-8 码点表示，所以这个计数的结果可能会令人惊讶。
	fmt.Println("符文数量：", utf8.RuneCountInString(s))

	// `range` 循环对字符串有特殊处理，并会解码
	// 每个 `rune` 及其在字符串中的偏移量。
	for idx, runeValue := range s {
		fmt.Printf("%#U 起始位置为 %d\n", runeValue, idx)
	}

	// 我们可以通过显式使用
	// `utf8.DecodeRuneInString` 函数来实现相同的迭代。
	fmt.Println("\n使用 DecodeRuneInString")
	for i, w := 0, 0; i < len(s); i += w {
		runeValue, width := utf8.DecodeRuneInString(s[i:])
		fmt.Printf("%#U 起始位置为 %d\n", runeValue, i)
		w = width

		// 这展示了将一个 `rune` 值传递给一个函数。
		examineRune(runeValue)
	}
}

func examineRune(r rune) {

	// 用单引号括起来的值是 _符文字面量_。我们
	// 可以直接将一个 `rune` 值与一个符文字面量进行比较。
	if r == 't' {
		fmt.Println("找到 tee")
	} else if r == 'ส' {
		fmt.Println("找到 so sua")
	}
}

```
