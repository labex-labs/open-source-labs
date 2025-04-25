# select

この実験では、2 つのチャネル`c1`と`c2`が与えられており、ある時間の経過後に値を受け取ります。あなたのタスクは、`select`を使用してこれら 2 つの値を同時に待ち、それぞれの値が到着するたびに表示することです。

- `select`文を使用して 2 つのチャネルを待つ必要があります。
- 各チャネルから受け取った値を到着するたびに表示する必要があります。

```sh
# 予想通り、値 `"one"` とその後 `"two"` を受け取ります。
$ time go run select.go
received one
received two

# 1 秒と 2 秒の `Sleep` が同時に実行されるため、合計実行時間は約 2 秒だけです。
real 0m2.245s
```

以下が完全なコードです：

```go
// Go の _select_ を使うと、複数のチャネル操作を待つことができます。
// goroutine とチャネルを select と組み合わせることは、Go の強力な機能です。

package main

import (
	"fmt"
	"time"
)

func main() {

	// この例では、2 つのチャネルをまたいで select します。
	c1 := make(chan string)
	c2 := make(chan string)

	// 各チャネルは、ある時間の経過後に値を受け取ります。
	// たとえば、並行した goroutine で実行されるブロッキング RPC 操作をシミュレートするためです。
	go func() {
		time.Sleep(1 * time.Second)
		c1 <- "one"
	}()
	go func() {
		time.Sleep(2 * time.Second)
		c2 <- "two"
	}()

	// これら 2 つの値を同時に待ち、それぞれの値が到着するたびに表示するために、`select` を使用します。
	for i := 0; i < 2; i++ {
		select {
		case msg1 := <-c1:
			fmt.Println("received", msg1)
		case msg2 := <-c2:
			fmt.Println("received", msg2)
		}
	}
}

```
