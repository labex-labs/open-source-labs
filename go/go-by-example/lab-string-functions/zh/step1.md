# 字符串函数

完成以下代码，以打印`strings`包提供的各种字符串函数的输出。

- 使用`strings`包来完成本实验。
- 使用`fmt.Println`函数来打印输出。
- 不要修改函数名或参数。

```sh
$ go run string-functions.go
包含：true
计数：2
有前缀：true
有后缀：true
索引：1
连接：a-b
重复：aaaaa
替换：f00
替换：f0o
分割：[a b c d e]
转换为小写：test
转换为大写：TEST
```

以下是完整代码：

```go
// 标准库的 `strings` 包提供了许多
// 与字符串相关的实用函数。以下是一些示例
// 让你了解这个包。

package main

import (
	"fmt"
	s "strings"
)

// 我们将 `fmt.Println` 别名到一个更短的名字，因为我们将在下面
// 大量使用它。
var p = fmt.Println

func main() {

	// 以下是 `strings` 包中可用函数的一个示例。由于这些是包中的函数，
	// 而不是字符串对象本身的方法，我们需要将相关字符串作为第一个
	// 参数传递给函数。你可以在 [`strings`](https://pkg.go.dev/strings)
	// 包文档中找到更多函数。
	p("包含：  ", s.Contains("test", "es"))
	p("计数：     ", s.Count("test", "t"))
	p("有前缀： ", s.HasPrefix("test", "te"))
	p("有后缀： ", s.HasSuffix("test", "st"))
	p("索引：     ", s.Index("test", "e"))
	p("连接：      ", s.Join([]string{"a", "b"}, "-"))
	p("重复：    ", s.Repeat("a", 5))
	p("替换：   ", s.Replace("foo", "o", "0", -1))
	p("替换：   ", s.Replace("foo", "o", "0", 1))
	p("分割：     ", s.Split("a-b-c-d-e", "-"))
	p("转换为小写：   ", s.ToLower("TEST"))
	p("转换为大写：   ", s.ToUpper("test"))
}

```
