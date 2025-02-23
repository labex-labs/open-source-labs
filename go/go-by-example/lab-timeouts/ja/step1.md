# タイムアウト

プログラムが外部リソースに接続する場合や、実行時間を制限する必要がある場合、タイムアウトは重要です。この実験では、チャネルと `select` を使って Go でタイムアウトを実装します。

- チャネルと `select` を使って Go でタイムアウトを実装する。
- チャネルが読み取られない場合にゴルーチンリークを防ぐために、バッファ付きチャネルを使用する。
- タイムアウト後に値が送信されるのを待つために `time.After` を使用する。
- `select` を使って最初に準備ができた受信を行う。

```sh
# このプログラムを実行すると、最初の操作がタイムアウトし、2番目の操作が成功することが示されます。
$ go run timeouts.go
timeout 1
result 2
```

以下に完全なコードがあります。

```go
// _タイムアウト_ は、外部リソースに接続するプログラムや、それ以外の場合に実行時間を制限する必要があるプログラムにとって重要です。チャネルと `select` のおかげで、Go でタイムアウトを実装するのは簡単でエレガントです。

package main

import (
	"fmt"
	"time"
)

func main() {

	// 私たちの例では、外部呼び出しを実行しており、2秒後にチャネル `c1` でその結果を返すとします。チャネルはバッファ付きであることに注意してください。したがって、ゴルーチン内の送信はブロックされません。これは、チャネルが読み取られない場合にゴルーチンリークを防ぐための一般的なパターンです。
	c1 := make(chan string, 1)
	go func() {
		time.Sleep(2 * time.Second)
		c1 <- "result 1"
	}()

	// ここにタイムアウトを実装する `select` があります。
	// `res := <-c1` は結果を待ち、`<-time.After` は1秒のタイムアウト後に送信される値を待ちます。`select` は最初に準備ができた受信を行うため、操作が許可された1秒以上かかる場合、タイムアウトのケースを選択します。
	select {
	case res := <-c1:
		fmt.Println(res)
	case <-time.After(1 * time.Second):
		fmt.Println("timeout 1")
	}

	// 3秒の長いタイムアウトを許可する場合、`c2` からの受信は成功し、結果が表示されます。
	c2 := make(chan string, 1)
	go func() {
		time.Sleep(2 * time.Second)
		c2 <- "result 2"
	}()
	select {
	case res := <-c2:
		fmt.Println(res)
	case <-time.After(3 * time.Second):
		fmt.Println("timeout 2")
	}
}

```
