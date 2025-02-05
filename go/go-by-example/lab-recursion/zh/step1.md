# 递归

`sum` 函数接受一个整数切片，并返回该切片中所有整数的总和。然而，该函数并不完整，需要使用递归来实现。

- `sum` 函数必须使用递归来实现。
- 该函数必须接受一个整数切片作为输入。
- 该函数必须返回切片中所有整数的总和。

```sh
$ go run recursion.go
5040
13
```

以下是完整代码：

```go
// Go 支持
// <a href="https://en.wikipedia.org/wiki/Recursion_(computer_science)"><em>递归函数</em></a>。
// 这是一个经典示例。

package main

import "fmt"

// 这个 `fact` 函数会不断调用自身，直到达到
// `fact(0)` 这个基准情况。
func fact(n int) int {
	if n == 0 {
		return 1
	}
	return n * fact(n-1)
}

func main() {
	fmt.Println(fact(7))

	// 闭包也可以是递归的，但这需要在定义闭包之前
	// 用带类型的 `var` 显式声明闭包。
	var fib func(n int) int

	fib = func(n int) int {
		if n < 2 {
			return n
		}

		// 由于 `fib` 之前在 `main` 中声明过，Go
		// 知道在这里调用哪个函数作为 `fib`。
		return fib(n-1) + fib(n-2)
	}

	fmt.Println(fib(7))
}

```
