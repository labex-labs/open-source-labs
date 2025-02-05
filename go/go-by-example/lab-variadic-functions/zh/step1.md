# 可变参数函数

在本实验中，你需要实现一个名为 `max` 的函数，该函数接受任意数量的整数作为参数，并返回最大值。

- 函数 `max` 应接受任意数量的整数作为参数。
- 函数 `max` 应返回作为参数传递的整数中的最大值。

```sh
$ go run variadic-functions.go
[1 2] 3
[1 2 3] 6
[1 2 3 4] 10

# Go 语言中函数的另一个关键特性是它们能够形成闭包，我们将在下文中探讨。
```

以下是完整代码：

```go
// [_可变参数函数_](https://en.wikipedia.org/wiki/Variadic_function)
// 可以使用任意数量的尾随参数进行调用。
// 例如，`fmt.Println` 是一个常见的可变参数函数。

package main

import "fmt"

// 这是一个将接受任意数量的 `int` 作为参数的函数。
func sum(nums...int) {
	fmt.Print(nums, " ")
	total := 0
	// 在函数内部，`nums` 的类型等同于 `[]int`。我们可以调用 `len(nums)`，
	// 使用 `range` 对其进行迭代等操作。
	for _, num := range nums {
		total += num
	}
	fmt.Println(total)
}

func main() {

	// 可变参数函数可以以通常的方式使用单个参数进行调用。
	sum(1, 2)
	sum(1, 2, 3)

	// 如果你已经在一个切片中有多个参数，
	// 可以像这样使用 `func(slice...)` 将它们应用于可变参数函数。
	nums := []int{1, 2, 3, 4}
	sum(nums...)
}

```
