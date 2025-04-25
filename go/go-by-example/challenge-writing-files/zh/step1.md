# 写入文件

你需要编写一个 Go 程序，将字符串和字节写入文件，并使用带缓冲的写入器。

## 要求

- 程序应将字符串和字节写入文件。
- 程序应使用带缓冲的写入器。

## 示例

```sh
# 尝试运行写入文件的代码。
$ go run writing-files.go
写入了5个字节
写入了7个字节
写入了9个字节

# 然后检查写入文件的内容。
$ cat /tmp/dat1
hello
go
$ cat /tmp/dat2
some
writes
buffered

# 接下来，我们将看看如何将刚刚学到的一些文件 I/O 概念
# 应用到 `stdin` 和 `stdout` 流上。
```
