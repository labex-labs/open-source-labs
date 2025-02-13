# 互斥锁

在此挑战中要解决的问题是，使用多个 goroutine 在循环中递增一个命名计数器，并确保对计数器的访问是同步的。

## 要求

- 使用 `Container` 结构体来保存计数器的映射。
- 使用 `Mutex` 来同步对 `counters` 映射的访问。
- `Container` 结构体应该有一个 `inc` 方法，该方法接受一个字符串 `name`，并递增 `counters` 映射中相应的计数器。
- `inc` 方法应该在访问 `counters` 映射之前锁定互斥锁，并在函数结束时使用 `defer` 语句解锁。
- 使用 `sync.WaitGroup` 结构体来等待 goroutine 完成。
- 使用 `fmt.Println` 函数来打印 `counters` 映射。

## 示例

```sh
# 运行程序会显示计数器
# 按预期更新。
$ go run mutexes.go
map[a:20000 b:10000]

# 接下来我们将看看如何仅使用 goroutine 和通道来实现相同的状态
# 管理任务。

```
