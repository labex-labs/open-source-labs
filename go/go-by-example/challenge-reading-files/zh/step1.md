# 读取文件

你需要在 Go 程序中读取文件，并对文件中的数据执行不同的操作。

## 要求

- 你应该熟悉基本的 Go 编程概念。
- 你的计算机上应安装了 Go。

## 示例

```sh
$ echo "hello" > /tmp/dat
$ echo "go" >> /tmp/dat
$ go run reading-files.go
hello
go
5 字节: hello
2 字节 @ 6: go
2 字节 @ 6: go
5 字节: hello

# 接下来我们将学习写入文件。
```
