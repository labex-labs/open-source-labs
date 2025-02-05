# 通道方向

本实验要解决的问题是修改给定代码，以确保用作函数参数的通道被指定为仅用于发送或接收值。

- 具备 Go 语言的基础知识
- 理解通道及其在 Go 语言中的用法

```sh
$ go run channel-directions.go
passed message
```

以下是完整代码：

```go
// 当使用通道作为函数参数时，你可以
// 指定一个通道是仅用于发送还是接收
// 值。这种特定性提高了程序的类型安全性。

package main

import "fmt"

// 这个 `ping` 函数只接受一个用于发送
// 值的通道。尝试在这个通道上接收值会导致编译时错误。
func ping(pings chan<- string, msg string) {
	pings <- msg
}

// `pong` 函数接受一个用于接收的通道 (`pings`) 和另一个用于发送的通道 (`pongs`)。
func pong(pings <-chan string, pongs chan<- string) {
	msg := <-pings
	pongs <- msg
}

func main() {
	pings := make(chan string, 1)
	pongs := make(chan string, 1)
	ping(pings, "passed message")
	pong(pings, pongs)
	fmt.Println(<-pongs)
}

```
