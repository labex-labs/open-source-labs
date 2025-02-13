# 恢复

提供的代码中的 `mayPanic` 函数在被调用时会引发恐慌（panic）。你的任务是修改 `main` 函数，从恐慌中恢复并打印错误信息。

## 要求

- 使用 `recover` 函数处理 `mayPanic` 函数中的恐慌。
- 当发生恐慌时打印错误信息。

## 示例

```sh
$ go run recover.go
Recovered. Error:
a problem
```
