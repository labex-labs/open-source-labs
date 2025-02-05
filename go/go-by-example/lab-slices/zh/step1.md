# 切片

本实验要解决的问题是在 Go 语言中创建和操作切片。你需要创建一个长度不为零的空切片，在切片中设置和获取值，使用 `len` 函数获取切片的长度，使用 `append` 函数向切片中添加新值，使用 `copy` 函数复制切片，以及使用切片运算符从现有切片中获取一部分元素。

要完成本实验，你需要对 Go 语言的语法和切片数据类型有基本的了解。你还需要熟悉 `make`、`append` 和 `copy` 函数，以及切片运算符。

```sh
# 请注意，虽然切片与数组是不同的类型，
# 但 `fmt.Println` 对它们的呈现方式类似。
$ go run slices.go
emp: [ ]
set: [a b c]
get: c
len: 3
apd: [a b c d e f]
cpy: [a b c d e f]
sl1: [c d e]
sl2: [a b c d e]
sl3: [c d e f]
dcl: [g h i]
2d: [[0] [1 2] [2 3 4]]

# 查看 Go 团队的这篇 [精彩博客文章](https://go.dev/blog/slices-intro)，
# 以获取有关 Go 语言中切片设计和实现的更多详细信息。

# 既然我们已经了解了数组和切片，接下来我们将看看
# Go 语言的另一个关键内置数据结构：映射。
```

以下是完整代码：

```go
// 切片是 Go 语言中的一种重要数据类型，它为序列提供了比数组更强大的接口。

package main

import "fmt"

func main() {

	// 与数组不同，切片仅由它们包含的元素类型（而非元素数量）来定义类型。
	// 要创建一个长度不为零的空切片，请使用内置的 `make` 函数。
	// 这里我们创建一个长度为 `3` 的 `string` 类型切片（初始值为零值）。
	s := make([]string, 3)
	fmt.Println("emp:", s)

	// 我们可以像操作数组一样设置和获取切片中的元素。
	s[0] = "a"
	s[1] = "b"
	s[2] = "c"
	fmt.Println("set:", s)
	fmt.Println("get:", s[2])

	// `len` 函数按预期返回切片的长度。
	fmt.Println("len:", len(s))

	// 除了这些基本操作外，切片还支持一些其他操作，这使得它们比数组更丰富。
	// 其中一个是内置的 `append` 函数，它返回一个包含一个或多个新值的切片。
	// 请注意，我们需要接受 `append` 的返回值，因为我们可能会得到一个新的切片值。
	s = append(s, "d")
	s = append(s, "e", "f")
	fmt.Println("apd:", s)

	// 切片也可以被复制。这里我们创建一个与 `s` 长度相同的空切片 `c`，并将 `s` 复制到 `c` 中。
	c := make([]string, len(s))
	copy(c, s)
	fmt.Println("cpy:", c)

	// 切片支持一种 “切片” 运算符，语法为 `slice[low:high]`。
	// 例如，这将获取元素 `s[2]`、`s[3]` 和 `s[4]` 组成的切片。
	l := s[2:5]
	fmt.Println("sl1:", l)

	// 这将切片到（但不包括）`s[5]`。
	l = s[:5]
	fmt.Println("sl2:", l)

	// 这将从（并包括）`s[2]` 开始切片。
	l = s[2:]
	fmt.Println("sl3:", l)

	// 我们也可以在一行中声明并初始化一个切片变量。
	t := []string{"g", "h", "i"}
	fmt.Println("dcl:", t)

	// 切片可以组成多维数据结构。与多维数组不同，内部切片的长度可以不同。
	twoD := make([][]int, 3)
	for i := 0; i < 3; i++ {
		innerLen := i + 1
		twoD[i] = make([]int, innerLen)
		for j := 0; j < innerLen; j++ {
			twoD[i][j] = i + j
		}
	}
	fmt.Println("2d: ", twoD)
}

```
