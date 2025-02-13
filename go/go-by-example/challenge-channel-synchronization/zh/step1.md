# 通道同步

在此挑战中要解决的问题是创建一个 goroutine，它执行一些工作，并在工作完成时通过通道通知另一个 goroutine。

## 要求

要完成此挑战，你需要：

- 创建一个名为 `worker` 的函数，该函数将一个 `bool` 类型的通道作为参数。
- 在 `worker` 函数内部，执行一些工作，然后向通道发送一个值，以通知工作已完成。
- 在 `main` 函数中，创建一个缓冲区大小为 1 的 `bool` 类型通道。
- 启动一个调用 `worker` 函数并将通道作为参数传递的 goroutine。
- 阻塞 `main` 函数，直到从通道接收到一个值。

## 示例

```sh
$ go run channel-synchronization.go
working...done

# 如果你从这个程序中删除了 `<- done` 这一行，
# 程序会在 `worker` 甚至还未启动之前就退出。
```
