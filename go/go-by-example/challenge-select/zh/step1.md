# 选择语句（Select）

在这个挑战中，你会得到两个通道 `c1` 和 `c2`，它们会在一段时间后接收一个值。你的任务是使用 `select` 语句同时等待这两个值，并在每个值到达时打印出来。

## 要求

- 你应该使用 `select` 语句等待两个通道。
- 你应该在每个通道接收到值时打印出来。

## 示例

```sh
# 我们按预期接收到值 `"one"`，然后是 `"two"`。
$ time go run select.go
收到 one
收到 two

# 请注意，总执行时间仅约为 2 秒，因为 1 秒和 2 秒的 `Sleep` 操作是并发执行的。
实际时间 0m2.245s
```
