# HTTP 클라이언트 (Client)

서버에 HTTP GET 요청을 보내고 HTTP 응답 상태와 응답 본문의 처음 5 줄을 출력하는 프로그램을 작성해야 합니다.

- 프로그램은 `net/http` 패키지를 사용하여 HTTP GET 요청을 발행해야 합니다.
- 프로그램은 HTTP 응답 상태를 출력해야 합니다.
- 프로그램은 응답 본문의 처음 5 줄을 출력해야 합니다.
- 프로그램은 오류를 적절하게 처리해야 합니다.

```sh
$ go run http-clients.go
Response status: 200 OK
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Go by Example</title>

```

전체 코드는 다음과 같습니다.

```go
// The Go standard library comes with excellent support
// for HTTP clients and servers in the `net/http`
// package. In this example we'll use it to issue simple
// HTTP requests.
package main

import (
	"bufio"
	"fmt"
	"net/http"
)

func main() {

	// Issue an HTTP GET request to a server. `http.Get` is a
	// convenient shortcut around creating an `http.Client`
	// object and calling its `Get` method; it uses the
	// `http.DefaultClient` object which has useful default
	// settings.
	resp, err := http.Get("https://gobyexample.com")
	if err != nil {
		panic(err)
	}
	defer resp.Body.Close()

	// Print the HTTP response status.
	fmt.Println("Response status:", resp.Status)

	// Print the first 5 lines of the response body.
	scanner := bufio.NewScanner(resp.Body)
	for i := 0; scanner.Scan() && i < 5; i++ {
		fmt.Println(scanner.Text())
	}

	if err := scanner.Err(); err != nil {
		panic(err)
	}
}
```
