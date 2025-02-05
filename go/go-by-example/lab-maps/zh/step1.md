# 映射

在本实验中，你需要创建一个映射，用于存储给定字符串中每个单词出现的次数。你需要将字符串拆分成单词，然后遍历每个单词，如果单词不存在于映射中，则将其添加到映射中；如果单词已存在，则增加其计数。

- 你必须使用映射来存储单词计数。
- 你必须将输入字符串拆分成单词。
- 你必须遍历输入字符串中的每个单词。
- 如果单词不存在于映射中，你必须将其添加到映射中；如果单词已存在，则增加其计数。

```sh
# 注意，当使用 `fmt.Println` 打印映射时，映射会以 `map[k:v k:v]` 的形式显示。
$ go run maps.go
map: map[k1:7 k2:13]
v1: 7
v3: 0
len: 2
map: map[k1:7]
prs: false
map: map[bar:2 foo:1]
```

以下是完整代码：

```go
// 映射是 Go 语言内置的 [关联数据类型](https://en.wikipedia.org/wiki/Associative_array)
// （在其他语言中有时称为 _哈希表_ 或 _字典_）。

package main

import "fmt"

func main() {

	// 要创建一个空映射，使用内置的 `make`：
	// `make(map[key-type]val-type)`。
	m := make(map[string]int)

	// 使用典型的 `name[key] = val` 语法设置键值对。
	m["k1"] = 7
	m["k2"] = 13

	// 使用 `fmt.Println` 打印映射将显示其所有键值对。
	fmt.Println("map:", m)

	// 使用 `name[key]` 获取键对应的值。
	v1 := m["k1"]
	fmt.Println("v1:", v1)

	// 如果键不存在，则返回值类型的
	// [零值](https://go.dev/ref/spec#The_zero_value)。
	v3 := m["k3"]
	fmt.Println("v3:", v3)

	// 对映射调用内置的 `len` 会返回键值对的数量。
	fmt.Println("len:", len(m))

	// 内置的 `delete` 从映射中删除键值对。
	delete(m, "k2")
	fmt.Println("map:", m)

	// 从映射中获取值时的可选第二个返回值表示键是否存在于映射中。
	// 这可用于区分缺失的键和值为零值（如 `0` 或 `""`）的键。
	// 这里我们不需要值本身，因此使用 _空白标识符_ `_` 忽略它。
	_, prs := m["k2"]
	fmt.Println("prs:", prs)

	// 你也可以使用此语法在同一行声明并初始化一个新映射。
	n := map[string]int{"foo": 1, "bar": 2}
	fmt.Println("map:", n)
}

```
