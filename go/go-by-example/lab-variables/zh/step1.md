# 变量

你需要完成代码，以在 Go 语言中声明并初始化不同类型的变量。

- 具备 Go 语言语法的基础知识
- 熟悉 Go 语言中的变量声明和初始化

```sh
$ go run variables.go
初始值
1 2
true
0
苹果
```

以下是完整代码：

```go
// 在 Go 语言中，_变量_ 是被显式声明并由编译器使用的，
// 例如用于检查函数调用的类型正确性。

package main

import "fmt"

func main() {

	// `var` 声明一个或多个变量。
	var a = "初始值"
	fmt.Println(a)

	// 你可以一次性声明多个变量。
	var b, c int = 1, 2
	fmt.Println(b, c)

	// Go 语言会推断初始化变量的类型。
	var d = true
	fmt.Println(d)

	// 未进行相应初始化而声明的变量会被赋予 _零值_。例如，
	// `int` 类型的零值是 `0`。
	var e int
	fmt.Println(e)

	// `:=` 语法是声明并初始化变量的简写形式，例如在这种情况下
	// 等同于 `var f string = "苹果"`。
	// 此语法仅在函数内部可用。
	f := "苹果"
	fmt.Println(f)
}

```
