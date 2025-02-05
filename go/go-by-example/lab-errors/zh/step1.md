# 错误

本实验提供了两个函数，如果输入参数为 42，则返回一个错误。第一个函数返回一个基本的错误值，而第二个函数使用自定义类型来表示错误。

- 必须导入 `errors` 包。
- 如果输入参数为 42，`f1` 函数必须返回一个错误。
- 如果输入参数为 42，`f2` 函数必须返回一个 `argError` 类型的错误。
- `argError` 类型必须有两个字段：`arg` 和 `prob`。
- `argError` 类型必须实现 `Error()` 方法。
- `main` 函数必须使用 7 和 42 作为输入参数调用 `f1` 和 `f2`。
- `main` 函数必须打印每个函数调用的结果以及返回的任何错误。
- `main` 函数必须演示如何以编程方式使用自定义错误中的数据。

```sh
$ go run errors.go
f1 运行成功: 10
f1 运行失败: 不能处理 42
f2 运行成功: 10
f2 运行失败: 42 - 不能处理它
42
不能处理它

# 请参阅 Go 博客上的这篇 [精彩文章](https://go.dev/blog/error-handling-and-go)
# 以了解更多关于错误处理的内容。
```

以下是完整代码：

```go
// 在 Go 语言中，通过显式的、单独的返回值来传递错误是一种惯用方式。这与 Java 和 Ruby 等语言中使用的异常形成对比，
// 也与 C 语言中有时使用的重载单结果/错误值不同。Go 语言的方法使得很容易看出哪些函数返回错误，并使用与处理任何其他非错误任务相同的语言结构来处理它们。

package main

import (
	"errors"
	"fmt"
)

// 按照惯例，错误是最后一个返回值，类型为 `error`，这是一个内置接口。
func f1(arg int) (int, error) {
	if arg == 42 {

		// `errors.New` 使用给定的错误消息构造一个基本的 `error` 值。
		return -1, errors.New("不能处理 42")

	}

	// 错误位置的 `nil` 值表示没有错误。
	return arg + 3, nil
}

// 通过在自定义类型上实现 `Error()` 方法，可以将其用作 `error`。以下是上述示例的一个变体，它使用自定义类型来显式表示参数错误。
type argError struct {
	arg  int
	prob string
}

func (e *argError) Error() string {
	return fmt.Sprintf("%d - %s", e.arg, e.prob)
}

func f2(arg int) (int, error) {
	if arg == 42 {

		// 在这种情况下，我们使用 `&argError` 语法来构建一个新的结构体，为两个字段 `arg` 和 `prob` 提供值。
		return -1, &argError{arg, "不能处理它"}
	}
	return arg + 3, nil
}

func main() {

	// 下面的两个循环测试我们的每个返回错误的函数。请注意，在 `if` 行上使用内联错误检查是 Go 代码中的常见习惯用法。
	for _, i := range []int{7, 42} {
		if r, e := f1(i); e!= nil {
			fmt.Println("f1 运行失败:", e)
		} else {
			fmt.Println("f1 运行成功:", r)
		}
	}
	for _, i := range []int{7, 42} {
		if r, e := f2(i); e!= nil {
			fmt.Println("f2 运行失败:", e)
		} else {
			fmt.Println("f2 运行成功:", r)
		}
	}

	// 如果你想以编程方式使用自定义错误中的数据，需要通过类型断言将错误获取为自定义错误类型的实例。
	_, e := f2(42)
	if ae, ok := e.(*argError); ok {
		fmt.Println(ae.arg)
		fmt.Println(ae.prob)
	}
}

```
