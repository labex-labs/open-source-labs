# 使用函数进行排序

本实验要解决的问题是在 Go 语言中实现一个自定义排序函数，该函数按照字符串长度对字符串切片进行排序。

- 应将 `byLength` 类型创建为 `[]string` 类型的别名。
- 应在 `byLength` 类型上实现 `sort.Interface`。
- 应在 `byLength` 类型上实现 `Len` 和 `Swap` 函数。
- 应在 `byLength` 类型上实现 `Less` 函数，以保存实际的自定义排序逻辑。
- `main` 函数应将原始的 `fruits` 切片转换为 `byLength` 类型，然后对该类型化的切片使用 `sort.Sort`。

```sh
# 运行我们的程序会显示一个按字符串长度排序的列表，
# 正如预期的那样。
$ go run sorting-by-functions.go
[kiwi peach banana]

# 通过遵循这种创建自定义类型、在该类型上实现三个
# `Interface` 方法，然后对该自定义类型的集合调用
# sort.Sort 的相同模式，我们可以通过任意函数对 Go 切片
# 进行排序。
```

以下是完整代码：

```go
// 有时我们希望按照非自然顺序对集合进行排序。例如，
// 假设我们希望按字符串长度而不是字母顺序对字符串进行
// 排序。这是 Go 语言中自定义排序的一个示例。

package main

import (
	"fmt"
	"sort"
)

// 为了在 Go 语言中通过自定义函数进行排序，我们需要一个
// 相应的类型。在这里，我们创建了一个 `byLength` 类型，
// 它只是内置 `[]string` 类型的别名。
type byLength []string

// 我们在我们的类型上实现 `sort.Interface` - `Len`、
// `Less` 和 `Swap` - 以便我们可以使用 `sort` 包的通用
// `Sort` 函数。`Len` 和 `Swap` 在不同类型之间通常是
// 相似的，而 `Less` 将保存实际的自定义排序逻辑。在我
// 们的例子中，我们希望按字符串长度递增的顺序进行排序，
// 所以我们在这里使用 `len(s[i])` 和 `len(s[j])`。
func (s byLength) Len() int {
	return len(s)
}
func (s byLength) Swap(i, j int) {
	s[i], s[j] = s[j], s[i]
}
func (s byLength) Less(i, j int) bool {
	return len(s[i]) < len(s[j])
}

// 有了这些，我们现在可以通过将原始的 `fruits` 切片转换
// 为 `byLength` 类型，然后对该类型化的切片使用 `sort.Sort`
// 来实现我们的自定义排序。
func main() {
	fruits := []string{"peach", "banana", "kiwi"}
	sort.Sort(byLength(fruits))
	fmt.Println(fruits)
}

```
