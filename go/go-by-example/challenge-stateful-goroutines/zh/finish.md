# 总结

此挑战演示了如何使用通道（channels）和 goroutine 来同步对共享状态的访问。通过让单个 goroutine 拥有状态，并使用通道来发出读取和写入请求，我们可以避免竞态条件和数据损坏。
