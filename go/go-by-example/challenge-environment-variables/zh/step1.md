# 环境变量

在这个挑战中，你需要设置、获取和列出环境变量。

## 要求

- 使用 `os.Setenv` 设置键值对。
- 使用 `os.Getenv` 获取键对应的值。
- 使用 `os.Environ` 列出环境中的所有键值对。
- 使用 `strings.SplitN` 拆分键和值。

## 示例

```sh
# 运行程序显示我们获取到了在程序中设置的 `FOO` 的值，但 `BAR` 为空。
$ go run environment-variables.go
FOO: 1
BAR:

# 环境中的键列表将取决于你的特定机器。
TERM_PROGRAM
PATH
SHELL
...
FOO

# 如果我们先在环境中设置 `BAR`，运行的程序会获取到那个值。
$ BAR=2 go run environment-variables.go
FOO: 1
BAR: 2
...
```
