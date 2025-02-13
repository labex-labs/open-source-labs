# 总结

在这个挑战中，我们学习了如何使用互斥锁在多个 goroutine 之间安全地访问数据。我们创建了一个 `Container` 结构体来保存计数器的映射，并使用一个 `Mutex` 来同步对 `counters` 映射的访问。我们还实现了一个 `inc` 方法来递增命名计数器，并使用 `sync.WaitGroup` 结构体来等待 goroutine 完成。最后，我们使用 `fmt.Println` 函数打印了 `counters` 映射。
