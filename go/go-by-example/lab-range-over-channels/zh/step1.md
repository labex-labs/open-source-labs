# 通道上的遍历

你需要编写一个函数，该函数接收一个整数通道，并返回从该通道接收到的所有整数的总和。

- 该函数应命名为 `sumInts`。
- 该函数应接收一个 `chan int` 类型的单个参数。
- 该函数应返回一个整数值。
- 不允许在函数体内使用任何循环或递归。
- 不允许使用任何外部包。

```sh
$ go run range-over-channels.go
一
二

# 此示例还表明，可以关闭一个非空通道，但仍能接收剩余的值。
```

以下是完整代码：

```go
// 在 [之前](range) 的示例中，我们看到了 `for` 和
// `range` 如何对基本数据结构进行迭代。
// 我们也可以使用此语法来迭代从通道接收的值。

package main

import "fmt"

func main() {

	// 我们将遍历 `queue` 通道中的 2 个值。
	queue := make(chan string, 2)
	queue <- "一"
	queue <- "二"
	close(queue)

	// 这个 `range` 会在从 `queue` 接收到每个元素时对其进行迭代。由于我们在上面关闭了通道，所以在接收到 2 个元素后迭代就会终止。
	for elem := range queue {
		fmt.Println(elem)
	}
}

```
