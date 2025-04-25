# 数字解析

在许多程序中，从字符串解析数字是一项常见的任务。本实验要求你使用内置的 `strconv` 包从字符串中解析不同类型的数字。

- 使用 `strconv` 包从字符串中解析数字。
- 使用 `ParseFloat` 解析浮点数。
- 使用 `ParseInt` 解析整数。
- 使用 `ParseInt` 解析十六进制格式的数字。
- 使用 `ParseUint` 解析无符号整数。
- 使用 `Atoi` 解析十进制整数。
- 处理解析函数返回的错误。

```sh
$ go run number-parsing.go
1.234
123
456
789
135
strconv.ParseInt: 解析 "wat": 语法无效

# 接下来我们将看看另一个常见的解析任务：URL。
```

以下是完整代码：

```go
// 从字符串解析数字是许多程序中一项基本但常见的任务
// 以下是在 Go 语言中实现的方法。

package main

// 内置的 `strconv` 包提供数字
// 解析功能。
import (
	"fmt"
	"strconv"
)

func main() {

	// 使用 `ParseFloat` 时，这个 `64` 表示要解析的
	// 精度位数。
	f, _ := strconv.ParseFloat("1.234", 64)
	fmt.Println(f)

	// 对于 `ParseInt`，`0` 表示从字符串推断基数。`64`
	// 要求结果能容纳在 64 位中。
	i, _ := strconv.ParseInt("123", 0, 64)
	fmt.Println(i)

	// `ParseInt` 会识别十六进制格式的数字。
	d, _ := strconv.ParseInt("0x1c8", 0, 64)
	fmt.Println(d)

	// 也有 `ParseUint`。
	u, _ := strconv.ParseUint("789", 0, 64)
	fmt.Println(u)

	// `Atoi` 是用于基本十进制 `int` 解析的便捷函数。
	k, _ := strconv.Atoi("135")
	fmt.Println(k)

	// 解析函数在输入错误时返回错误。
	_, e := strconv.Atoi("wat")
	fmt.Println(e)
}

```
