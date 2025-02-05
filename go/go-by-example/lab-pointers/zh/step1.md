# 指针

问题在于通过两个函数 `zeroval` 和 `zeroptr` 来理解指针与值相比是如何工作的。`zeroval` 有一个 `int` 类型的参数，所以参数会按值传递给它。`zeroval` 会得到 `ival` 的一个副本，这个副本与调用函数中的那个不同。相比之下，`zeroptr` 有一个 `*int` 类型的参数，这意味着它接受一个 `int` 指针。函数体中的 `*iptr` 代码随后会将指针从其内存地址解引用到该地址处的当前值。给解引用后的指针赋值会改变被引用地址处的值。

- 你应该对 Go 语言有基本的了解。
- 你应该知道如何在 Go 语言中定义和使用函数。
- 你应该知道如何在 Go 语言中使用指针。

```sh
# `zeroval` 不会改变 `main` 函数中的 `i`，但
# `zeroptr` 会，因为它引用了那个变量的内存地址。
$ go run pointers.go
初始值: 1
zeroval: 1
zeroptr: 0
指针: 0x42131100
```

下面是完整代码：

```go
// Go 语言支持 <em><a href="https://en.wikipedia.org/wiki/Pointer_(computer_programming)">指针</a></em>，
// 允许你在程序中传递对值和记录的引用。

package main

import "fmt"

// 我们将通过两个函数 `zeroval` 和 `zeroptr` 展示指针与值相比是如何工作的。`zeroval` 有一个
// `int` 类型的参数，所以参数会按值传递给它。`zeroval` 会得到 `ival` 的一个副本，这个副本与调用函数中的那个不同。
func zeroval(ival int) {
	ival = 0
}

// 相比之下，`zeroptr` 有一个 `*int` 类型的参数，这意味着它接受一个 `int` 指针。函数体中的 `*iptr` 代码随后会将指针从其
// 内存地址解引用到该地址处的当前值。给解引用后的指针赋值会改变被引用地址处的值。
func zeroptr(iptr *int) {
	*iptr = 0
}

func main() {
	i := 1
	fmt.Println("初始值:", i)

	zeroval(i)
	fmt.Println("zeroval:", i)

	// `&i` 语法给出 `i` 的内存地址，
	// 即指向 `i` 的指针。
	zeroptr(&i)
	fmt.Println("zeroptr:", i)

	// 指针也可以打印出来。
	fmt.Println("指针:", &i)
}

```
