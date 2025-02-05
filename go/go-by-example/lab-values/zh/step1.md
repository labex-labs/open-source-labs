# 值类型

你的任务是完成 `calculate` 函数，该函数接受两个整数并返回它们的和与积。

- `calculate` 函数应接受两个整数作为参数。
- `calculate` 函数应返回两个整数，即输入参数的和与积。

```sh
$ go run values.go
golang
1+1 = 2
7.0/3.0 = 2.3333333333333335
false
true
false
```

以下是完整代码：

```go
// Go 有各种值类型，包括字符串、
// 整数、浮点数、布尔值等。这里有一些
// 基本示例。

package main

import "fmt"

func main() {

	// 字符串，可以用 `+` 连接。
	fmt.Println("go" + "lang")

	// 整数和浮点数。
	fmt.Println("1+1 =", 1+1)
	fmt.Println("7.0/3.0 =", 7.0/3.0)

	// 布尔值，有你期望的布尔运算符。
	fmt.Println(true && false)
	fmt.Println(true || false)
	fmt.Println(!true)
}

```
