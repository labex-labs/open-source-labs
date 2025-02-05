# 函数

在给定的代码中，我们有两个函数 `plus` 和 `plusPlus`。`plus` 函数接受两个整数作为参数，并返回它们的和。`plusPlus` 函数接受三个整数作为参数，并返回它们的和。你的任务是通过将第三个整数加到前两个整数的和中来完成 `plusPlus` 函数。

- `plus` 函数应接受两个整数作为参数，并返回它们的和作为一个整数。
- `plusPlus` 函数应接受三个整数作为参数，并返回它们的和作为一个整数。
- `plusPlus` 函数应使用 `plus` 函数来计算前两个整数的和。

```sh
$ go run functions.go
1+2 = 3
1+2+3 = 6

# Go 函数还有其他几个特性。其中一个是
# 多个返回值，我们将在下一节中介绍。
```

以下是完整代码：

```go
// _函数_ 在 Go 中至关重要。我们将通过几个不同的示例来学习
// 函数。

package main

import "fmt"

// 这是一个接受两个 `int` 并返回
// 它们的和作为一个 `int` 的函数。
func plus(a int, b int) int {

	// Go 需要显式返回，即它不会
	// 自动返回最后一个表达式的值。
	return a + b
}

// 当你有多个连续的相同类型的参数时，你可以省略
// 相同类型参数的类型名称，直到最后一个声明类型的参数。
func plusPlus(a, b, c int) int {
	return a + b + c
}

func main() {

	// 像你期望的那样调用函数，使用
	// `name(args)`。
	res := plus(1, 2)
	fmt.Println("1+2 =", res)

	res = plusPlus(1, 2, 3)
	fmt.Println("1+2+3 =", res)
}

```
