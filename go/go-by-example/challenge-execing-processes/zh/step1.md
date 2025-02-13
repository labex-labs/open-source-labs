# 执行进程

问题在于用另一个进程（比如非 Go 进程）替换当前的 Go 进程。

## 要求

- Go 编程语言
- 了解 Go 的 `exec` 函数的基本知识
- 熟悉环境变量

## 示例

```sh
# 当我们运行程序时，它会被 `ls` 替换。
$ go run execing-processes.go
total 16
drwxr-xr-x 4 mark 136B Oct 3 16:29.
drwxr-xr-x 91 mark 3.0K Oct 3 12:50..
-rw-r--r-- 1 mark 1.3K Oct 3 16:28 execing-processes.go

# 注意，Go 没有提供经典的 Unix `fork` 函数。不过通常这不是问题，因为启动 goroutine、生成进程以及执行进程涵盖了 `fork` 的大多数用例。
```
