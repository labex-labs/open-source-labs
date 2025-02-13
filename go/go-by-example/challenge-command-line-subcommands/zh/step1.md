# 命令行子命令

你需要创建一个支持两个子命令 `foo` 和 `bar` 的程序，每个子命令都有自己的一组标志。`foo` 子命令应该有两个标志 `enable` 和 `name`，而 `bar` 子命令应该有一个标志 `level`。

## 要求

- 程序应使用 `flag` 包来定义和解析标志。
- `foo` 子命令应具有两个类型为字符串的标志 `enable` 和 `name`。
- `bar` 子命令应具有一个类型为整数的标志 `level`。
- 如果提供了无效的子命令，程序应打印错误消息。
- 程序应打印所调用子命令的标志值。

## 示例

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
标志已提供但未定义: -enable
bar 的用法:
-level int
level

# 接下来我们将看看环境变量，这是另一种常见的
# 对程序进行参数化的方法。
```
