# 方法

提供的代码定义了一个名为 `rect` 的结构体类型，它有两个字段：`width` 和 `height`。为这个结构体类型定义了两个方法：`area` 和 `perim`。`area` 方法计算矩形的面积，`perim` 方法计算矩形的周长。主函数调用这两个方法并打印结果。

- `area` 方法的接收者类型应为 `*rect`。
- `perim` 方法的接收者类型应为 `rect`。
- `area` 方法应返回矩形的面积。
- `perim` 方法应返回矩形的周长。
- `main` 函数应调用这两个方法并打印结果。

```sh
$ go run methods.go
面积: 50
周长: 30
面积: 50
周长: 30

# 接下来我们将看看 Go 语言用于对相关方法集进行分组和命名的机制：接口。
```

以下是完整代码：

```go
// Go 语言支持在结构体类型上定义 _方法_。

package main

import "fmt"

type rect struct {
	width, height int
}

// 这个 `area` 方法的 _接收者类型_ 是 `*rect`。
func (r *rect) area() int {
	return r.width * r.height
}

// 方法可以为指针或值接收者类型定义。这里是一个值接收者的示例。
func (r rect) perim() int {
	return 2*r.width + 2*r.height
}

func main() {
	r := rect{width: 10, height: 5}

	// 这里我们调用为我们的结构体定义的两个方法。
	fmt.Println("面积：", r.area())
	fmt.Println("周长：", r.perim())

	// Go 语言会自动处理方法调用时的值和指针之间的转换。你可能希望使用指针接收者类型，以避免在方法调用时进行复制，或者允许方法修改接收的结构体。
	rp := &r
	fmt.Println("面积：", rp.area())
	fmt.Println("周长：", rp.perim())
}

```
