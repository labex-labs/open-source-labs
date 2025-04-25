# 排序

本实验要解决的问题是使用 `sort` 包对字符串和整数切片进行排序。

- 必须导入 `sort` 包。
- 必须使用 `sort.Strings()` 函数对字符串切片进行排序。
- 必须使用 `sort.Ints()` 函数对整数切片进行排序。
- 必须使用 `sort.IntsAreSorted()` 函数检查整数切片是否已经排好序。

```sh
# 运行我们的程序会打印出已排序的字符串和整数
# 切片，以及作为 `AreSorted` 测试结果的 `true`。
$ go run sorting.go
字符串: [a b c]
整数: [2 4 7]
已排序: true
```

以下是完整代码：

```go
// Go 的 `sort` 包实现了对内置类型
// 和用户定义类型的排序。我们先来看对
// 内置类型的排序。

package main

import (
	"fmt"
	"sort"
)

func main() {

	// 排序方法特定于内置类型；
	// 这里是字符串的示例。请注意，排序是
	// 原地进行的，所以它会改变给定的切片，而不
	// 返回新的切片。
	strs := []string{"c", "a", "b"}
	sort.Strings(strs)
	fmt.Println("字符串：", strs)

	// 对 `int` 进行排序的示例。
	ints := []int{7, 2, 4}
	sort.Ints(ints)
	fmt.Println("整数：  ", ints)

	// 我们还可以使用 `sort` 检查切片是否
	// 已经按顺序排列。
	s := sort.IntsAreSorted(ints)
	fmt.Println("已排序：", s)
}

```
