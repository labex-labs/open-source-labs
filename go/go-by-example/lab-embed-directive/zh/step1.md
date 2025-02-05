# 嵌入指令

你的任务是修改给定代码，将文件和文件夹嵌入到 Go 二进制文件中并打印其内容。

- 你必须使用 `embed` 包来嵌入文件和文件夹。
- 你必须使用 `string` 和 `[]byte` 类型来存储嵌入文件的内容。
- 你必须使用 `embed.FS` 类型来通过通配符嵌入多个文件或文件夹。
- 你必须打印嵌入文件的内容。

```sh
# 使用这些命令运行示例。
# （注意：由于 Go 语言游乐场的限制，
# 此示例只能在你的本地机器上运行。）
$ mkdir -p folder
$ echo "hello go" > folder/single_file.txt
$ echo "123" > folder/file1.hash
$ echo "456" > folder/file2.hash

$ go run embed-directive.go
hello go
hello go
123
456
```

以下是完整代码：

```go
// `//go:embed` 是一个 [编译器指令](https://pkg.go.dev/cmd/compile#hdr-Compiler_Directives)，
// 它允许程序在构建时将任意文件和文件夹包含到 Go 二进制文件中。
// 在此处阅读有关嵌入指令的更多信息 [此处](https://pkg.go.dev/embed)。
package main

// 导入 `embed` 包；如果你不使用此包中的任何导出标识符，
// 则可以使用 `_ "embed"` 进行空白导入。
import (
	"embed"
)

// `embed` 指令接受相对于包含 Go 源文件的目录的路径。
// 此指令将文件内容嵌入到紧随其后的 `string` 变量中。
//
//go:embed folder/single_file.txt
var fileString string

// 或者将文件内容嵌入到 `[]byte` 中。
//
//go:embed folder/single_file.txt
var fileByte []byte

// 我们还可以使用通配符嵌入多个文件甚至文件夹。
// 这使用了 [embed.FS 类型](https://pkg.go.dev/embed#FS) 的变量，
// 它实现了一个简单的虚拟文件系统。
//
//go:embed folder/single_file.txt
//go:embed folder/*.hash
var folder embed.FS

func main() {

	// 打印 `single_file.txt` 的内容。
	print(fileString)
	print(string(fileByte))

	// 从嵌入的文件夹中检索一些文件。
	content1, _ := folder.ReadFile("folder/file1.hash")
	print(string(content1))

	content2, _ := folder.ReadFile("folder/file2.hash")
	print(string(content2))
}

```
