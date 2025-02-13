# 等待组

本次挑战要解决的问题是启动多个 goroutine，并为每个 goroutine 增加等待组计数器。然后，我们需要等待所有启动的 goroutine 完成。

## 要求

- 具备 Go 语言的基础知识。
- 理解 Go 语言中的并发。
- 熟悉 `sync` 包。

## 示例

```sh
$ go run waitgroups.go
Worker 5 starting
Worker 3 starting
Worker 4 starting
Worker 1 starting
Worker 2 starting
Worker 4 done
Worker 1 done
Worker 2 done
Worker 5 done
Worker 3 done

# 每次调用时，工作线程启动和完成的顺序
# 可能会有所不同。
```
