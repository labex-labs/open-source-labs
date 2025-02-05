# 闭包

你需要创建一个返回另一个函数的函数。返回的函数每次被调用时，都应将一个变量的值加 1。该变量对于每个返回的函数来说应该是唯一的。

- 函数 `intSeq` 应返回另一个函数。
- 返回的函数每次被调用时，都应将一个变量的值加 1。
- 该变量对于每个返回的函数来说应该是唯一的。

```sh
$ go run closures.go
1
2
3
1

# 目前我们要研究的函数的最后一个特性是
# 递归。
```

以下是完整代码：

```go
// Go 支持 [_匿名函数_](https://en.wikipedia.org/wiki/Anonymous_function)，
// 它可以形成 <a href="https://en.wikipedia.org/wiki/Closure_(computer_science)"><em>闭包</em></a>。
// 当你想在代码中内联定义一个函数而无需为其命名时，匿名函数很有用。

package main

import "fmt"

// 函数 `intSeq` 返回另一个函数，
// 我们在 `intSeq` 的函数体中匿名定义它。返回的函数
// 通过变量 `i` 形成一个闭包。
func intSeq() func() int {
	i := 0
	return func() int {
		i++
		return i
	}
}

func main() {

	// 我们调用 `intSeq`，将结果（一个函数）
	// 赋给 `nextInt`。这个函数值捕获了它自己的
	// `i` 值，每次我们调用 `nextInt` 时，该值都会更新。
	nextInt := intSeq()

	// 通过多次调用 `nextInt` 来查看闭包的效果。
	fmt.Println(nextInt())
	fmt.Println(nextInt())
	fmt.Println(nextInt())

	// 为了确认状态对于那个特定函数是唯一的，
	// 创建并测试一个新的函数。
	newInts := intSeq()
	fmt.Println(newInts())
}

```
