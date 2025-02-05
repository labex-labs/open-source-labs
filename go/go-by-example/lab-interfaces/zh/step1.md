# 接口

问题在于如何在Go语言中实现一个接口，我们只需要实现接口中的所有方法即可。在这里，我们在`rect`（矩形）和`circle`（圆形）上实现`geometry`（几何图形）接口。

- 在Go语言中实现一个接口。
- 实现接口中的所有方法。
- 使用一个通用的`measure`函数来处理任何`geometry`。
- 使用`circle`和`rect`结构体的实例作为`measure`的参数。

```sh
$ go run interfaces.go
{3 4}
12
14
{5}
78.53981633974483
31.41592653589793

# 要了解更多关于Go语言接口的内容，请查看这篇
# [很棒的博客文章](https://jordanorelli.tumblr.com/post/32665860244/how-to-use-interfaces-in-go)。
```

以下是完整代码：

```go
// _接口_ 是命名的方法签名集合。

package main

import (
	"fmt"
	"math"
)

// 这是一个几何形状的基本接口。
type geometry interface {
	area() float64
	perim() float64
}

// 对于我们的示例，我们将在
// `rect`（矩形）和 `circle`（圆形）类型上实现这个接口。
type rect struct {
	width, height float64
}
type circle struct {
	radius float64
}

// 要在Go语言中实现一个接口，我们只需要
// 实现接口中的所有方法。在这里，我们在
// `rect`（矩形）上实现 `geometry`（几何图形）接口。
func (r rect) area() float64 {
	return r.width * r.height
}
func (r rect) perim() float64 {
	return 2*r.width + 2*r.height
}

// `circle`（圆形）的实现。
func (c circle) area() float64 {
	return math.Pi * c.radius * c.radius
}
func (c circle) perim() float64 {
	return 2 * math.Pi * c.radius
}

// 如果一个变量具有接口类型，那么我们可以调用
// 命名接口中的方法。这是一个通用的 `measure` 函数，
// 利用这一点来处理任何 `geometry`（几何图形）。
func measure(g geometry) {
	fmt.Println(g)
	fmt.Println(g.area())
	fmt.Println(g.perim())
}

func main() {
	r := rect{width: 3, height: 4}
	c := circle{radius: 5}

	// `circle`（圆形）和 `rect`（矩形）结构体类型都
	// 实现了 `geometry`（几何图形）接口，所以我们可以使用
	// 这些结构体的实例作为 `measure` 的参数。
	measure(r)
	measure(c)
}

```
