# if-else

你需要完成 `checkNumber` 函数，该函数接受一个整数作为输入并返回一个字符串。如果数字是偶数，则返回 "even"，否则返回 "odd"。

- 函数应命名为 `checkNumber`。
- 函数应接受一个整数作为输入。
- 函数应返回一个字符串。
- 如果数字是偶数，则返回 "even"。
- 如果数字是奇数，则返回 "odd"。

```sh
$ go run if-else.go
7 是奇数
8 能被 4 整除
9 是个一位数

# Go 语言中没有 [三元 if](https://en.wikipedia.org/wiki/%3F:)
# 所以即使是基本条件，你也需要使用完整的 `if` 语句。
```

以下是完整代码：

```go
// 在 Go 语言中使用 `if` 和 `else` 进行分支
// 很简单。

package main

import "fmt"

func main() {

	// 这是一个基本示例。
	if 7%2 == 0 {
		fmt.Println("7 是偶数")
	} else {
		fmt.Println("7 是奇数")
	}

	// 你可以有一个没有 `else` 的 `if` 语句。
	if 8%4 == 0 {
		fmt.Println("8 能被 4 整除")
	}

	// 一条语句可以在条件判断之前；在这条语句中声明的任何变量
	// 在当前以及所有后续分支中都可用。
	if num := 9; num < 0 {
		fmt.Println(num, "是负数")
	} else if num < 10 {
		fmt.Println(num, "是个一位数")
	} else {
		fmt.Println(num, "有多个数位")
	}
}

// 注意，在 Go 语言中条件判断周围不需要括号
// 但花括号是必需的。

```
