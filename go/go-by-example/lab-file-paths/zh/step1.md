# 文件路径

在本实验中，你需要使用 `filepath` 包对文件路径执行各种操作，例如以可移植的方式构建路径、将路径拆分为目录和文件组件、检查路径是否为绝对路径、查找文件的扩展名以及查找两条路径之间的相对路径。

- 使用 `Join` 以可移植的方式构建路径。
- 使用 `Dir` 和 `Base` 将路径拆分为目录和文件组件。
- 使用 `IsAbs` 检查路径是否为绝对路径。
- 使用 `Ext` 查找文件的扩展名。
- 使用 `TrimSuffix` 从文件名中移除扩展名。
- 使用 `Rel` 查找两条路径之间的相对路径。

```sh
$ go run file-paths.go
p: dir1/dir2/filename
dir1/filename
dir1/filename
Dir(p): dir1/dir2
Base(p): filename
false
true
.json
config
t/file
../c/t/file

```

以下是完整代码：

```go
// `filepath` 包提供了一些函数，用于以一种在不同操作系统之间可移植的方式解析和构建 *文件路径*；例如，在 Linux 上是 `dir/file`，在 Windows 上是 `dir\file`。
package main

import (
	"fmt"
	"path/filepath"
	"strings"
)

func main() {

	// 应该使用 `Join` 以可移植的方式构建路径。它接受任意数量的参数，并从这些参数构建一个分层路径。
	p := filepath.Join("dir1", "dir2", "filename")
	fmt.Println("p:", p)

	// 你应该始终使用 `Join`，而不是手动拼接 `/` 或 `\`。除了提供可移植性之外，`Join` 还会通过移除多余的分隔符和目录更改来规范化路径。
	fmt.Println(filepath.Join("dir1//", "filename"))
	fmt.Println(filepath.Join("dir1/../dir1", "filename"))

	// `Dir` 和 `Base` 可用于将路径拆分为目录和文件。或者，`Split` 将在一次调用中返回两者。
	fmt.Println("Dir(p):", filepath.Dir(p))
	fmt.Println("Base(p):", filepath.Base(p))

	// 我们可以检查路径是否为绝对路径。
	fmt.Println(filepath.IsAbs("dir/file"))
	fmt.Println(filepath.IsAbs("/dir/file"))

	filename := "config.json"

	// 有些文件名在点之后有扩展名。我们可以使用 `Ext` 从这样的文件名中拆分出扩展名。
	ext := filepath.Ext(filename)
	fmt.Println(ext)

	// 要找到移除扩展名后的文件名，使用 `strings.TrimSuffix`。
	fmt.Println(strings.TrimSuffix(filename, ext))

	// `Rel` 查找 *基准* 路径和 *目标* 路径之间的相对路径。如果目标路径无法相对于基准路径变为相对路径，它将返回一个错误。
	rel, err := filepath.Rel("a/b", "a/b/t/file")
	if err!= nil {
		panic(err)
	}
	fmt.Println(rel)

	rel, err = filepath.Rel("a/b", "a/c/t/file")
	if err!= nil {
		panic(err)
	}
	fmt.Println(rel)
}

```
