# 非阻塞通道操作

在此挑战中要解决的问题是使用带有 `default` 子句的 `select` 语句来实现非阻塞通道操作。

## 要求

- 使用带有 `default` 子句的 `select` 语句在通道上实现非阻塞接收。
- 使用带有 `default` 子句的 `select` 语句在通道上实现非阻塞发送。
- 使用带有多个 `case` 子句和一个 `default` 子句的 `select` 语句实现多路非阻塞选择。

## 示例

```sh
$ go run non-blocking-channel-operations.go
未接收到消息
未发送消息
无活动
```
