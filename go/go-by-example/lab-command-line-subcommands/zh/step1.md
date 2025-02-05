# 命令行子命令

你需要创建一个支持两个子命令 `foo` 和 `bar` 的程序，每个子命令都有自己的一组标志。`foo` 子命令应该有两个标志 `enable` 和 `name`，而 `bar` 子命令应该有一个标志 `level`。

- 程序应使用 `flag` 包来定义和解析标志。
- `foo` 子命令应该有两个类型为字符串的标志 `enable` 和 `name`。
- `bar` 子命令应该有一个类型为整数的标志 `level`。
- 如果提供了无效的子命令，程序应打印错误消息。
- 程序应打印所调用子命令的标志值。

```sh
$ go build command-line-subcommands.go

# 首先调用 foo 子命令。
$./command-line-subcommands foo -enable -name=joe a1 a2
子命令 'foo'
enable: true
name: joe
tail: [a1 a2]

# 现在尝试 bar。
$./command-line-subcommands bar -level 8 a1
子命令 'bar'
level: 8
tail: [a1]

# 但是 bar 不接受 foo 的标志。
$./command-line-subcommands bar -enable a1
标志已提供但未定义：-enable
bar 的用法：
-level int
level

# 接下来我们将看看环境变量，这是另一种常见的
# 为程序参数化的方法。
```

以下是完整代码：

```go
// 一些命令行工具，如 `go` 工具或 `git`
// 有许多 *子命令*，每个子命令都有自己的一组
// 标志。例如，`go build` 和 `go get` 是 `go` 工具的两个
// 不同子命令。
// `flag` 包让我们能够轻松定义具有自己标志的简单
// 子命令。

package main

import (
	"flag"
	"fmt"
	"os"
)

func main() {

	// 我们使用 `NewFlagSet` 函数声明一个子命令，并继续定义
	// 此子命令特有的新标志。
	fooCmd := flag.NewFlagSet("foo", flag.ExitOnError)
	fooEnable := fooCmd.Bool("enable", false, "enable")
	fooName := fooCmd.String("name", "", "name")

	// 对于不同的子命令，我们可以定义不同的
	// 支持的标志。
	barCmd := flag.NewFlagSet("bar", flag.ExitOnError)
	barLevel := barCmd.Int("level", 0, "level")

	// 子命令预期作为程序的第一个参数。
	if len(os.Args) < 2 {
		fmt.Println("预期 'foo' 或 'bar' 子命令")
		os.Exit(1)
	}

	// 检查调用了哪个子命令。
	switch os.Args[1] {

	// 对于每个子命令，我们解析其自己的标志并
	// 可以访问尾随的位置参数。
	case "foo":
		fooCmd.Parse(os.Args[2:])
		fmt.Println("子命令 'foo'")
		fmt.Println("  enable:", *fooEnable)
		fmt.Println("  name:", *fooName)
		fmt.Println("  tail:", fooCmd.Args())
	case "bar":
		barCmd.Parse(os.Args[2:])
		fmt.Println("子命令 'bar'")
		fmt.Println("  level:", *barLevel)
		fmt.Println("  tail:", barCmd.Args())
	default:
		fmt.Println("预期 'foo' 或 'bar' 子命令")
		os.Exit(1)
	}
}

```
