# 总结

在本实验中，我们学习了如何在 Go 语言中使用`sync/atomic`包来管理状态，即通过多个 goroutine 递增一个计数器。我们使用`AddUint64`函数来原子地递增计数器，并使用 WaitGroup 来等待所有 goroutine 完成它们的工作。
