# 环境变量

在本实验中，你需要设置、获取和列出环境变量。

- 使用 `os.Setenv` 设置键值对。
- 使用 `os.Getenv` 获取键对应的值。
- 使用 `os.Environ` 列出环境中的所有键值对。
- 使用 `strings.SplitN` 分割键和值。

```sh
# 运行该程序会显示我们获取到了在程序中设置的 `FOO` 的值，但 `BAR` 为空。
$ go run environment-variables.go
FOO: 1
BAR:

# 环境中的键列表取决于你的特定机器。
TERM_PROGRAM
PATH
SHELL
...
FOO

# 如果我们先在环境中设置 `BAR`，运行的程序会获取到该值。
$ BAR=2 go run environment-variables.go
FOO: 1
BAR: 2
...
```

以下是完整代码：

```go
// [环境变量](https://en.wikipedia.org/wiki/Environment_variable)
// 是一种向 Unix 程序 [传递配置信息](https://www.12factor.net/config) 的通用机制。
// 让我们看看如何设置、获取和列出环境变量。

package main

import (
	"fmt"
	"os"
	"strings"
)

func main() {

	// 要设置键值对，使用 `os.Setenv`。要获取键对应的值，使用 `os.Getenv`。
	// 如果环境中不存在该键，这将返回一个空字符串。
	os.Setenv("FOO", "1")
	fmt.Println("FOO:", os.Getenv("FOO"))
	fmt.Println("BAR:", os.Getenv("BAR"))

	// 使用 `os.Environ` 列出环境中的所有键值对。
	// 这将返回一个字符串切片，形式为 `KEY=value`。
	// 你可以使用 `strings.SplitN` 来获取键和值。
	// 这里我们打印所有的键。
	fmt.Println()
	for _, e := range os.Environ() {
		pair := strings.SplitN(e, "=", 2)
		fmt.Println(pair[0])
	}
}

```
