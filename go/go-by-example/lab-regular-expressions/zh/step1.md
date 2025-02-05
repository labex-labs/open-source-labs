# 正则表达式

本实验要求你完成代码，以在 Go 语言中执行各种与正则表达式相关的任务。

- 使用 `regexp` 包来执行与正则表达式相关的任务。
- 使用 `MatchString` 来测试一个模式是否与字符串匹配。
- 使用 `Compile` 来优化 `Regexp` 结构体。
- 使用 `MatchString` 来像 `Compile` 那样测试匹配。
- 使用 `FindString` 来查找正则表达式的匹配项。
- 使用 `FindStringIndex` 来查找第一个匹配项，并返回匹配项的起始和结束索引，而不是匹配的文本。
- 使用 `FindStringSubmatch` 来返回 `p([a-z]+)ch` 和 `([a-z]+)` 的信息。
- 使用 `FindStringSubmatchIndex` 来返回关于匹配项和子匹配项索引的信息。
- 使用 `FindAllString` 来查找正则表达式的所有匹配项。
- 使用 `FindAllStringSubmatchIndex` 来应用于输入中的所有匹配项，而不仅仅是第一个。
- 使用 `Match` 来使用 `[]byte` 参数测试匹配，并从函数名中去掉 `String`。
- 使用 `MustCompile` 来创建带有正则表达式的全局变量。
- 使用 `ReplaceAllString` 用其他值替换字符串的子集。
- 使用 `ReplaceAllFunc` 用给定函数转换匹配的文本。

```sh
$ go run regular-expressions.go
true
true
peach
idx: [0 5]
[peach ea]
[0 5 1 3]
[peach punch pinch]
all: [[0 5 1 3] [6 11 7 9] [12 17 13 15]]
[peach punch]
true
regexp: p([a-z]+)ch
a <fruit>
a PEACH

# 有关 Go 正则表达式的完整参考，请查看
# [`regexp`](https://pkg.go.dev/regexp) 包文档。

```

以下是完整代码：

```go
// Go 为 [正则表达式](https://en.wikipedia.org/wiki/Regular_expression) 提供了内置支持。
// 以下是 Go 中一些常见的与正则表达式相关任务的示例。

package main

import (
	"bytes"
	"fmt"
	"regexp"
)

func main() {

	// 这测试一个模式是否与字符串匹配。
	match, _ := regexp.MatchString("p([a-z]+)ch", "peach")
	fmt.Println(match)

	// 上面我们直接使用了字符串模式，但对于
	// 其他正则表达式任务，你需要 `Compile` 一个
	// 优化后的 `Regexp` 结构体。
	r, _ := regexp.Compile("p([a-z]+)ch")

	// 这些结构体上有许多方法。这是一个像我们之前看到的匹配测试。
	fmt.Println(r.MatchString("peach"))

	// 这找到正则表达式的匹配项。
	fmt.Println(r.FindString("peach punch"))

	// 这也找到第一个匹配项，但返回
	// 匹配项的起始和结束索引，而不是
	// 匹配的文本。
	fmt.Println("idx:", r.FindStringIndex("peach punch"))

	// `Submatch` 变体包括关于
	// 整个模式匹配以及这些匹配中的子匹配的信息。例如，这将返回
	// `p([a-z]+)ch` 和 `([a-z]+)` 的信息。
	fmt.Println(r.FindStringSubmatch("peach punch"))

	// 类似地，这将返回关于匹配项和子匹配项索引的信息。
	fmt.Println(r.FindStringSubmatchIndex("peach punch"))

	// 这些函数的 `All` 变体适用于输入中的所有
	// 匹配项，而不仅仅是第一个。例如，要找到正则表达式的所有匹配项。
	fmt.Println(r.FindAllString("peach punch pinch", -1))

	// 上述其他函数也有这些 `All` 变体。
	fmt.Println("all:", r.FindAllStringSubmatchIndex(
		"peach punch pinch", -1))

	// 向这些函数提供非负整数作为第二个
	// 参数将限制匹配项的数量。
	fmt.Println(r.FindAllString("peach punch pinch", 2))

	// 我们上面的示例有字符串参数并使用
	// 像 `MatchString` 这样的名称。我们也可以提供
	// `[]byte` 参数并从函数名中去掉 `String`。
	fmt.Println(r.Match([]byte("peach")))

	// 当用正则表达式创建全局变量时，你可以使用 `Compile` 的 `MustCompile` 变体。`MustCompile` 会引发恐慌而不是
	// 返回错误，这使得它在用于全局变量时更安全。
	r = regexp.MustCompile("p([a-z]+)ch")
	fmt.Println("regexp:", r)

	// `regexp` 包还可用于用其他值替换
	// 字符串的子集。
	fmt.Println(r.ReplaceAllString("a peach", "<fruit>"))

	// `Func` 变体允许你用给定函数转换匹配的
	// 文本。
	in := []byte("a peach")
	out := r.ReplaceAllFunc(in, bytes.ToUpper)
	fmt.Println(string(out))
}

```
