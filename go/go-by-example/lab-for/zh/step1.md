# `for`

以下代码包含了不同类型的 `for` 循环。不过，代码的某些部分不完整，你需要填空以使代码正确运行。

- 具备 Go 语言语法的基础知识
- 熟悉 Go 语言中的 `for` 循环

```sh
$ go run for.go
1
2
3
7
8
9
loop
1
3
5

# 稍后在我们查看 `range` 语句、通道和其他数据
# 结构时，我们会看到一些其他的 `for` 形式。
```

以下是完整代码：

```go
// `for` 是 Go 语言唯一的循环结构。以下是
// `for` 循环的一些基本类型。

package main

import "fmt"

func main() {

	// 最基本的类型，只有一个条件。
	i := 1
	for i <= 3 {
		fmt.Println(i)
		i = i + 1
	}

	// 经典的初始化/条件/后置 `for` 循环。
	for j := 7; j <= 9; j++ {
		fmt.Println(j)
	}

	// 没有条件的 `for` 循环会一直重复
	// 直到你从循环中 `break` 出来或者从
	// 封闭函数中 `return`。
	for {
		fmt.Println("loop")
		break
	}

	// 你也可以 `continue` 到循环的下一次迭代。
	for n := 0; n <= 5; n++ {
		if n%2 == 0 {
			continue
		}
		fmt.Println(n)
	}
}

```
