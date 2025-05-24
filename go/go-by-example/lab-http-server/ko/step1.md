# HTTP 서버

두 개의 경로 `/hello`와 `/headers`를 처리할 수 있는 간단한 HTTP 서버를 작성해야 합니다. `/hello` 경로는 간단한 "hello" 응답을 반환해야 하며, `/headers` 경로는 모든 HTTP 요청 헤더를 반환해야 합니다.

- 서버는 `net/http` 패키지를 사용해야 합니다.
- `/hello` 경로는 "hello" 응답을 반환해야 합니다.
- `/headers` 경로는 모든 HTTP 요청 헤더를 반환해야 합니다.
- 서버는 포트 `8090`에서 리스닝해야 합니다.

```sh
# Run the server in the background.
$ go run http-servers.go &

# Access the `/hello` route.
$ curl localhost:8090/hello
hello
```

전체 코드는 다음과 같습니다.

```go
// Writing a basic HTTP server is easy using the
// `net/http` package.
package main

import (
	"fmt"
	"net/http"
)

// A fundamental concept in `net/http` servers is
// *handlers*. A handler is an object implementing the
// `http.Handler` interface. A common way to write
// a handler is by using the `http.HandlerFunc` adapter
// on functions with the appropriate signature.
func hello(w http.ResponseWriter, req *http.Request) {

	// Functions serving as handlers take a
	// `http.ResponseWriter` and a `http.Request` as
	// arguments. The response writer is used to fill in the
	// HTTP response. Here our simple response is just
	// "hello\n".
	fmt.Fprintf(w, "hello\n")
}

func headers(w http.ResponseWriter, req *http.Request) {

	// This handler does something a little more
	// sophisticated by reading all the HTTP request
	// headers and echoing them into the response body.
	for name, headers := range req.Header {
		for _, h := range headers {
			fmt.Fprintf(w, "%v: %v\n", name, h)
		}
	}
}

func main() {

	// We register our handlers on server routes using the
	// `http.HandleFunc` convenience function. It sets up
	// the *default router* in the `net/http` package and
	// takes a function as an argument.
	http.HandleFunc("/hello", hello)
	http.HandleFunc("/headers", headers)

	// Finally, we call the `ListenAndServe` with the port
	// and a handler. `nil` tells it to use the default
	// router we've just set up.
	http.ListenAndServe(":8090", nil)
}
```
