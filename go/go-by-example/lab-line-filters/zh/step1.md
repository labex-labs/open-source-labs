# 行过滤器

本实验要解决的问题是编写一个Go程序，从标准输入（stdin）读取输入文本，将文本中的所有字母大写，然后将修改后的文本打印到标准输出（stdout）。

- 程序必须从标准输入读取输入文本。
- 程序必须将输入文本中的所有字母大写。
- 程序必须将修改后的文本打印到标准输出。

```sh
# 要测试我们的行过滤器，首先创建一个包含几行小写字母的文件。
$ echo 'hello' > /tmp/lines
$ echo 'filter' >> /tmp/lines

# 然后使用行过滤器获取大写字母的行。
$ cat /tmp/lines | go run line-filters.go
HELLO
FILTER
```

以下是完整代码：

```go
// 一个 _行过滤器_ 是一种常见的程序类型，它从标准输入读取输入，进行处理，然后将一些派生结果打印到标准输出。`grep` 和 `sed` 是常见的行过滤器。

// 这是一个用Go编写的行过滤器示例，它会输出所有输入文本的大写版本。你可以使用这个模式来编写自己的Go行过滤器。
package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {

	// 用一个带缓冲的扫描器包装无缓冲的 `os.Stdin`，为我们提供了一个方便的 `Scan` 方法，该方法将扫描器推进到下一个标记；在默认扫描器中，这是下一行。
	scanner := bufio.NewScanner(os.Stdin)

	for scanner.Scan() {
		// `Text` 返回当前标记，在这里是输入中的下一行。
		ucl := strings.ToUpper(scanner.Text())

		// 输出大写后的行。
		fmt.Println(ucl)
	}

	// 检查 `Scan` 过程中是否有错误。文件结束是预期的，`Scan` 不会将其报告为错误。
	if err := scanner.Err(); err!= nil {
		fmt.Fprintln(os.Stderr, "error:", err)
		os.Exit(1)
	}
}

```
