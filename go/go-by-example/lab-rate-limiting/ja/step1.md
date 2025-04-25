# レート制限

問題は、サービス品質を維持し、リソースの利用を制御するために、着信リクエストの処理を制限することです。

- Go 言語
- goroutine、チャネル、およびタイカーに関する基本的な理解

```sh
# プログラムを実行すると、最初のバッチのリクエストが
# 約 200 ミリ秒ごとに 1 回ずつ処理されることがわかります。
$ go run rate-limiting.go
request 1 2012-10-19 00:38:18.687438 +0000 UTC
request 2 2012-10-19 00:38:18.887471 +0000 UTC
request 3 2012-10-19 00:38:19.087238 +0000 UTC
request 4 2012-10-19 00:38:19.287338 +0000 UTC
request 5 2012-10-19 00:38:19.487331 +0000 UTC

# 2 番目のバッチのリクエストに対しては、バースト可能なレート制限のため、
# 最初の 3 つのリクエストをすぐに処理し、その後、残りの 2 つのリクエストを
# それぞれ約 200ms の遅延で処理します。
request 1 2012-10-19 00:38:20.487578 +0000 UTC
request 2 2012-10-19 00:38:20.487645 +0000 UTC
request 3 2012-10-19 00:38:20.487676 +0000 UTC
request 4 2012-10-19 00:38:20.687483 +0000 UTC
request 5 2012-10-19 00:38:20.887542 +0000 UTC
```

以下に完全なコードがあります：

```go
// [_レート制限_](https://en.wikipedia.org/wiki/Rate_limiting)
// は、リソースの利用を制御し、サービス品質を維持するための
// 重要なメカニズムです。Go 言語は、goroutine、チャネル、および
// [タイカー](tickers) を使って、レート制限を簡潔にサポートしています。

package main

import (
	"fmt"
	"time"
)

func main() {

	// まずは基本的なレート制限を見てみましょう。
	// 着信リクエストの処理を制限したいとします。
	// これらのリクエストは同じ名前のチャネルから処理されます。
	requests := make(chan int, 5)
	for i := 1; i <= 5; i++ {
		requests <- i
	}
	close(requests)

	// この `limiter` チャネルは 200 ミリ秒ごとに値を受け取ります。
	// これが私たちのレート制限方式の調整装置です。
	limiter := time.Tick(200 * time.Millisecond)

	// 各リクエストを処理する前に `limiter` チャネルからの受信をブロックすることで、
	// 200 ミリ秒ごとに 1 つのリクエストに制限します。
	for req := range requests {
		<-limiter
		fmt.Println("request", req, time.Now())
	}

	// 全体的なレート制限を維持しながら、レート制限方式で短時間のバーストを許可したい場合があります。
	// これは、`limiter` チャネルをバッファリングすることで達成できます。
	// この `burstyLimiter` チャネルは最大 3 つのイベントのバーストを許可します。
	burstyLimiter := make(chan time.Time, 3)

	// 許可されたバーストを表すためにチャネルを満たします。
	for i := 0; i < 3; i++ {
		burstyLimiter <- time.Now()
	}

	// 200 ミリ秒ごとに、`burstyLimiter` に新しい値を追加しようとします。
	// その制限は 3 つです。
	go func() {
		for t := range time.Tick(200 * time.Millisecond) {
			burstyLimiter <- t
		}
	}()

	// 今度はさらに 5 つの着信リクエストをシミュレートします。
	// これらの最初の 3 つは、`burstyLimiter` のバースト機能の恩恵を受けます。
	burstyRequests := make(chan int, 5)
	for i := 1; i <= 5; i++ {
		burstyRequests <- i
	}
	close(burstyRequests)
	for req := range burstyRequests {
		<-burstyLimiter
		fmt.Println("request", req, time.Now())
	}
}

```
