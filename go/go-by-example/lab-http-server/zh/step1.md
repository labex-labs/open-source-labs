# HTTP 服务器

你需要编写一个简单的 HTTP 服务器，它能够处理两条路由：`/hello` 和 `/headers`。`/hello` 路由应返回一个简单的“hello”响应，而 `/headers` 路由应返回所有的 HTTP 请求头。

- 服务器应使用 `net/http` 包。
- `/hello` 路由应返回“hello”响应。
- `/headers` 路由应返回所有的 HTTP 请求头。
- 服务器应监听端口 `8090`。

```sh
# 在后台运行服务器。
$ go run http-servers.go &

# 访问 `/hello` 路由。
$ curl localhost:8090/hello
hello
```

以下是完整代码：

```go
// 使用 `net/http` 包编写一个基本的 HTTP 服务器很容易。
package main

import (
	"fmt"
	"net/http"
)

// `net/http` 服务器中的一个基本概念是 *处理器*。处理器是一个实现了 `http.Handler` 接口的对象。编写处理器的一种常见方式是在具有适当签名的函数上使用 `http.HandlerFunc` 适配器。
func hello(w http.ResponseWriter, req *http.Request) {

	// 用作处理器的函数接受一个 `http.ResponseWriter` 和一个 `http.Request` 作为参数。响应写入器用于填充 HTTP 响应。在这里，我们简单的响应只是 "hello\n"。
	fmt.Fprintf(w, "hello\n")
}

func headers(w http.ResponseWriter, req *http.Request) {

	// 这个处理器做了一些更复杂的事情，它读取所有的 HTTP 请求头并将它们回显到响应体中。
	for name, headers := range req.Header {
		for _, h := range headers {
			fmt.Fprintf(w, "%v: %v\n", name, h)
		}
	}
}

func main() {

	// 我们使用 `http.HandleFunc` 便利函数在服务器路由上注册我们的处理器。它在 `net/http` 包中设置了 *默认路由器*，并接受一个函数作为参数。
	http.HandleFunc("/hello", hello)
	http.HandleFunc("/headers", headers)

	// 最后，我们使用端口和一个处理器调用 `ListenAndServe`。`nil` 告诉它使用我们刚刚设置的默认路由器。
	http.ListenAndServe(":8090", nil)
}

```
