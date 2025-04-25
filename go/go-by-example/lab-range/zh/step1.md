# Range

本实验要解决的问题是演示如何在切片、数组、映射和字符串中使用 `range`。

要完成本实验，你需要：

- 具备 Golang 语法的基础知识
- 你的机器上安装了 Golang

```sh
$ go run range.go
总和: 9
索引: 1
a - > 苹果
b - > 香蕉
键: a
键: b
0 103
1 111
```

以下是完整代码：

```go
// _range_ 用于遍历各种数据结构中的元素。让我们看看如何在一些我们已经学过的数据结构中使用 `range`。

package main

import "fmt"

func main() {

	// 这里我们使用 `range` 来计算切片中数字的总和。
	// 数组的操作方式也是如此。
	nums := []int{2, 3, 4}
	sum := 0
	for _, num := range nums {
		sum += num
	}
	fmt.Println("总和：", sum)

	// 对数组和切片使用 `range` 会为每个元素提供索引和值。
	// 上面我们不需要索引，所以用下划线标识符 `_` 忽略了它。
	// 但有时我们实际上需要索引。
	for i, num := range nums {
		if num == 3 {
			fmt.Println("索引：", i)
		}
	}

	// 对映射使用 `range` 会遍历键值对。
	kvs := map[string]string{"a": "苹果", "b": "香蕉"}
	for k, v := range kvs {
		fmt.Printf("%s -> %s\n", k, v)
	}

	// `range` 也可以只遍历映射的键。
	for k := range kvs {
		fmt.Println("键：", k)
	}

	// 对字符串使用 `range` 会遍历 Unicode 码点。
	// 第一个值是 `rune` 的起始字节索引，第二个值是 `rune` 本身。
	// 更多细节请参阅 [字符串和符文](strings-and-runes)。
	for i, c := range "go" {
		fmt.Println(i, c)
	}
}

```
