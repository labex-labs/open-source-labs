# 上下文

`hello` 函数通过等待几秒钟再向客户端发送回复，来模拟服务器正在进行的一些工作。在工作过程中，留意上下文的 `Done()` 通道，以获取我们应该取消工作并尽快返回的信号。

- Go 语言版本 1.13 或更高。

```sh
# 在后台运行服务器。
$ go run context-in-http-servers.go &

# 模拟对 `/hello` 的客户端请求，在启动后不久按下
# Ctrl+C 以发出取消信号。
$ curl localhost:8090/hello
server: hello handler started
^C
server: context canceled
server: hello handler ended
```

以下是完整代码：

```go
// 在上一个示例中，我们研究了如何设置一个简单的
// [HTTP 服务器](http-servers)。HTTP 服务器对于演示
// 使用 `context.Context` 来控制取消操作很有用。
// `Context` 可携带截止日期、取消信号以及其他跨 API
// 边界和 goroutine 的请求范围值。
package main

import (
	"fmt"
	"net/http"
	"time"
)

func hello(w http.ResponseWriter, req *http.Request) {

	// `net/http` 机制会为每个请求创建一个
	// `context.Context`，并可通过 `Context()` 方法获取。
	ctx := req.Context()
	fmt.Println("server: hello handler started")
	defer fmt.Println("server: hello handler ended")

	// 在向客户端发送回复之前等待几秒钟。这可以模拟
	// 服务器正在进行的一些工作。在工作过程中，留意
	// 上下文的 `Done()` 通道，以获取我们应该取消工作
	// 并尽快返回的信号。
	select {
	case <-time.After(10 * time.Second):
		fmt.Fprintf(w, "hello\n")
	case <-ctx.Done():
		// 上下文的 `Err()` 方法返回一个错误，解释
		// `Done()` 通道关闭的原因。
		err := ctx.Err()
		fmt.Println("server:", err)
		internalError := http.StatusInternalServerError
		http.Error(w, err.Error(), internalError)
	}
}

func main() {

	// 与之前一样，我们在“/hello”路由上注册处理程序，
	// 并开始提供服务。
	http.HandleFunc("/hello", hello)
	http.ListenAndServe(":8090", nil)
}

```
