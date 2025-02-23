# タイマーとタイマー

この実験では、500msごとにタイマーを発生させるタイマーを作成する必要があります。値が到着するのを待つためにチャネルを使用します。

- `time` パッケージを使用してタイマーを作成します。
- 値が到着するのを待つためにチャネルを使用します。
- `select` 文を使用してチャネルから値を受け取ります。
- 1600ms後にタイマーを停止します。

```sh
# このプログラムを実行すると、タイマーは停止する前に3回タイマーを発生させるはずです。
$ go run tickers.go
Tick at 2012-09-23 11:29:56.487625 -0700 PDT
Tick at 2012-09-23 11:29:56.988063 -0700 PDT
Tick at 2012-09-23 11:29:57.488076 -0700 PDT
Ticker stopped
```

以下に完全なコードがあります：

```go
// [タイマー](timers) は、将来一度何かを行いたい場合に使用します。- _タイマー_ は、定期的に何かを繰り返し行いたい場合に使用します。ここでは、停止するまで定期的にタイマーを発生させるタイマーの例を示します。

package main

import (
	"fmt"
	"time"
)

func main() {

	// タイマーはタイマーと同じようなメカニズムを使用します。値が送信されるチャネルです。ここでは、チャネル上の `select` 組み込みを使用して、500msごとに値が到着するのを待ちます。
	ticker := time.NewTicker(500 * time.Millisecond)
	done := make(chan bool)

	go func() {
		for {
			select {
			case <-done:
				return
			case t := <-ticker.C:
				fmt.Println("Tick at", t)
			}
		}
	}()

	// タイマーと同じように、タイマーを停止できます。タイマーが停止すると、そのチャネル上で値を受け取らなくなります。1600ms後に停止します。
	time.Sleep(1600 * time.Millisecond)
	ticker.Stop()
	done <- true
	fmt.Println("Ticker stopped")
}

```
