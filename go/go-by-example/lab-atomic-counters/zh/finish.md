# 总结

在本实验中，我们学习了如何在Go语言中使用`sync/atomic`包来管理状态，即通过多个goroutine递增一个计数器。我们使用`AddUint64`函数来原子地递增计数器，并使用WaitGroup来等待所有goroutine完成它们的工作。
