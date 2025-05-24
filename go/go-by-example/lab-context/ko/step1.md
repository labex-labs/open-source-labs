# Context (컨텍스트)

`hello` 함수는 클라이언트에 응답을 보내기 전에 몇 초 동안 대기하여 서버가 수행하는 일부 작업을 시뮬레이션합니다. 작업하는 동안, 작업을 취소하고 가능한 한 빨리 반환해야 함을 알리는 신호에 대한 컨텍스트의 `Done()` 채널을 주시하십시오.

- Golang 버전 1.13 이상.

```sh
# Run the server in the background.
$ go run context-in-http-servers.go &

# Simulate a client request to `/hello`, hitting
# Ctrl+C shortly after starting to signal
# cancellation.
$ curl localhost:8090/hello
server: hello handler started
^C
server: context canceled
server: hello handler ended
```

전체 코드는 다음과 같습니다.

```go
// In the previous example we looked at setting up a simple
// [HTTP server](http-servers). HTTP servers are useful for
// demonstrating the usage of `context.Context` for
// controlling cancellation. A `Context` carries deadlines,
// cancellation signals, and other request-scoped values
// across API boundaries and goroutines.
package main

import (
	"fmt"
	"net/http"
	"time"
)

func hello(w http.ResponseWriter, req *http.Request) {

	// A `context.Context` is created for each request by
	// the `net/http` machinery, and is available with
	// the `Context()` method.
	ctx := req.Context()
	fmt.Println("server: hello handler started")
	defer fmt.Println("server: hello handler ended")

	// Wait for a few seconds before sending a reply to the
	// client. This could simulate some work the server is
	// doing. While working, keep an eye on the context's
	// `Done()` channel for a signal that we should cancel
	// the work and return as soon as possible.
	select {
	case <-time.After(10 * time.Second):
		fmt.Fprintf(w, "hello\n")
	case <-ctx.Done():
		// The context's `Err()` method returns an error
		// that explains why the `Done()` channel was
		// closed.
		err := ctx.Err()
		fmt.Println("server:", err)
		internalError := http.StatusInternalServerError
		http.Error(w, err.Error(), internalError)
	}
}

func main() {

	// As before, we register our handler on the "/hello"
	// route, and start serving.
	http.HandleFunc("/hello", hello)
	http.ListenAndServe(":8090", nil)
}
```
