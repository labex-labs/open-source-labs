# 信号

在某些情况下，我们希望我们的 Go 程序能够智能地处理 Unix 信号。例如，我们可能希望服务器在接收到 `SIGTERM` 时优雅地关闭，或者命令行工具在接收到 `SIGINT` 时停止处理输入。

## 要求

- 创建一个带缓冲的通道来接收 `os.Signal` 通知。
- 使用 `signal.Notify` 注册该通道以接收指定信号的通知。
- 创建一个 goroutine 来执行对信号的阻塞接收。
- 打印接收到的信号并通知程序可以结束。
- 等待预期的信号，然后退出。

## 示例

```sh
# 当我们运行这个程序时，它将阻塞等待一个
# 信号。通过输入 `ctrl-C`（终端显示为 `^C`），我们可以发送一个 `SIGINT` 信号，
# 使程序打印 `interrupt` 然后退出。
$ go run signals.go
awaiting signal
^C
interrupt
exiting
```
