# 命令行参数

该程序目前会打印出传递给它的原始命令行参数。不过，需要对其进行修改，以便根据参数的索引打印出特定的参数。

## 要求

- 具备 Go 语言的基础知识
- 熟悉命令行参数

## 示例

```sh
# 要试验命令行参数，最好先使用 `go build` 构建一个二进制文件。
$ go build command-line-arguments.go
$./command-line-arguments a b c d
[./command-line-arguments a b c d]
[a b c d]
c

# 接下来，我们将研究使用标志进行更高级的命令行处理。
```
