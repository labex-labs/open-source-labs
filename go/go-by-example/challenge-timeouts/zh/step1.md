# 超时处理

当程序连接到外部资源或需要限制执行时间时，超时处理非常重要。本次挑战是要在 Go 语言中使用通道（channels）和 `select` 来实现超时处理。

## 要求

- 使用通道（channels）和 `select` 在 Go 语言中实现超时处理。
- 使用带缓冲的通道（buffered channel），以防通道从未被读取而导致 goroutine 泄漏。
- 使用 `time.After` 来等待在超时后发送的值。
- 使用 `select` 来处理第一个准备好的接收操作。

## 示例

```sh
# 运行此程序会显示第一个操作超时，而第二个操作成功。
$ go run timeouts.go
timeout 1
result 2
```
