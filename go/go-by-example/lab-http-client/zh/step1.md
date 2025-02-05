# HTTP 客户端

你需要编写一个程序，向服务器发送 HTTP GET 请求，并打印 HTTP 响应状态以及响应体的前 5 行。

- 程序应使用 `net/http` 包发出 HTTP GET 请求。
- 程序应打印 HTTP 响应状态。
- 程序应打印响应体的前 5 行。
- 程序应妥善处理错误。

```sh
$ go run http-clients.go
响应状态: 200 OK
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Go by Example</title>

```

以下是完整代码：

```go
// Go 标准库在 `net/http` 包中对 HTTP 客户端和服务器提供了出色的支持。
// 在这个示例中，我们将使用它来发出简单的 HTTP 请求。
package main

import (
	"bufio"
	"fmt"
	"net/http"
)

func main() {

	// 向服务器发出 HTTP GET 请求。`http.Get` 是创建 `http.Client`
	// 对象并调用其 `Get` 方法的便捷捷径；它使用具有有用默认设置的
	// `http.DefaultClient` 对象。
	resp, err := http.Get("https://gobyexample.com")
	if err!= nil {
		panic(err)
	}
	defer resp.Body.Close()

	// 打印 HTTP 响应状态。
	fmt.Println("响应状态:", resp.Status)

	// 打印响应体的前 5 行。
	scanner := bufio.NewScanner(resp.Body)
	for i := 0; scanner.Scan() && i < 5; i++ {
		fmt.Println(scanner.Text())
	}

	if err := scanner.Err(); err!= nil {
		panic(err)
	}
}

```
