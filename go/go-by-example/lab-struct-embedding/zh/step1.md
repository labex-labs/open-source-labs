# 结构体嵌入

创建一个名为 `container` 的结构体，它嵌入一个名为 `base` 的结构体。`base` 结构体应该有一个名为 `num` 的 `int` 类型字段和一个名为 `describe()` 的方法，该方法返回一个字符串。`container` 结构体应该有一个名为 `str` 的 `string` 类型字段。`container` 结构体应该能够访问 `base` 结构体的 `num` 字段和 `describe()` 方法。

- `base` 结构体应该有一个名为 `num` 的 `int` 类型字段。
- `base` 结构体应该有一个名为 `describe()` 的方法，该方法返回一个字符串。
- `container` 结构体应该有一个名为 `str` 的 `string` 类型字段。
- `container` 结构体应该嵌入 `base` 结构体。
- `container` 结构体应该能够访问 `base` 结构体的 `num` 字段和 `describe()` 方法。

```sh
$ go run struct-embedding.go
co={num: 1, str: some name}
also num: 1
describe: base with num=1
describer: base with num=1
```

以下是完整代码：

```go
// Go 支持结构体和接口的 _嵌入_，
// 以表达更无缝的类型 _组合_。
// 这不要与[`//go:embed`](embed-directive)混淆，
// 它是 Go 1.16+ 版本中引入的一个 Go 指令，用于将
// 文件和文件夹嵌入到应用程序二进制文件中。

package main

import "fmt"

type base struct {
	num int
}

func (b base) describe() string {
	return fmt.Sprintf("base with num=%v", b.num)
}

// `container` _嵌入_ 了一个 `base`。嵌入看起来
// 像一个没有名字的字段。
type container struct {
	base
	str string
}

func main() {

	// 使用字面量创建结构体时，我们必须
	// 显式初始化嵌入；这里
	// 嵌入类型充当字段名。
	co := container{
		base: base{
			num: 1,
		},
		str: "some name",
	}

	// 我们可以直接在 `co` 上访问 `base` 的字段，
	// 例如 `co.num`。
	fmt.Printf("co={num: %v, str: %v}\n", co.num, co.str)

	// 或者，我们可以使用
	// 嵌入类型名称拼写出完整路径。
	fmt.Println("also num:", co.base.num)

	// 由于 `container` 嵌入了 `base`，`base` 的方法
	// 也成为了 `container` 的方法。这里
	// 我们直接在 `co` 上调用从 `base` 嵌入的方法。
	fmt.Println("describe:", co.describe())

	type describer interface {
		describe() string
	}

	// 嵌入带有方法的结构体可用于将
	// 接口实现赋予其他结构体。这里
	// 我们看到一个 `container` 现在实现了
	// `describer` 接口，因为它嵌入了 `base`。
	var d describer = co
	fmt.Println("describer:", d.describe())
}

```
