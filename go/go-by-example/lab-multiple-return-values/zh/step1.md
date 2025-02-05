# 多个返回值

完成 `swap` 函数，使其以相反顺序返回两个输入参数。

- `swap` 函数应将两个整数作为输入参数。
- `swap` 函数应以相反顺序返回两个整数。

```sh
$ go run multiple-return-values.go
3
7
7

# 接受可变数量的参数是 Go 函数的另一个不错的
# 特性；我们接下来会探讨这一点。
```

以下是完整代码：

```go
// Go 对 _多个返回值_ 提供了内置支持。
// 此特性在地道的 Go 代码中经常使用，例如
// 从函数中同时返回结果和错误值。

package main

import "fmt"

// 此函数签名中的 `(int, int)` 表明
// 该函数返回两个 `int` 类型的值。
func vals() (int, int) {
	return 3, 7
}

func main() {

	// 在这里，我们通过 _多重赋值_ 使用调用返回的两个不同返回值。
	a, b := vals()
	fmt.Println(a)
	fmt.Println(b)

	// 如果你只想要返回值的一个子集，
	// 可以使用空白标识符 `_`。
	_, c := vals()
	fmt.Println(c)
}

```
