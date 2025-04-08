# Goroutine

在此挑战中要解决的问题是创建并运行 goroutine 以并发执行函数。

## 要求

- `f` 函数应将其输入字符串和一个计数器变量打印三次。
- `main` 函数应同步调用 `f` 函数，并将 “direct” 和一个计数器变量打印三次。
- `main` 函数应使用 goroutine 异步调用 `f` 函数，并将 “goroutine” 和一个计数器变量打印三次。
- `main` 函数应启动一个 goroutine 来执行一个打印消息的匿名函数。
- `main` 函数应在打印 “done” 之前等待 goroutine 完成执行。

## 示例

```sh
# 当我们运行此程序时，我们首先看到阻塞调用的输出，然后是两个
# goroutine 的输出。goroutine 的输出可能会交错，因为 goroutine 由
# Go 运行时并发运行。

# 接下来我们将看看并发 Go 程序中 goroutine 的补充：通道。
```
