# チャネルのクローズ

この実験では、与えられたコードを修正して、ワーカーに対してもう作業がない場合に`jobs`チャネルをクローズする必要があります。また、すべての作業が完了したことを通知するために`done`チャネルを使用する必要があります。

- バッファ付きチャネル`jobs`を使用して、`main()`ゴルーチンからワーカーゴルーチンに処理すべき作業を伝えます。
- すべての作業が完了したことを通知するために`done`チャネルを使用します。
- ワーカーゴルーチンを使用して、`j, more := <-jobs`で`jobs`から繰り返し受信します。
- すべての作業が完了したときに、受信の特殊な2値形式を使用して`done`に通知します。
- `jobs`チャネルを介してワーカーに3つの作業を送信し、その後クローズします。
- [同期](channel-synchronization)アプローチを使用してワーカーを待ちます。

```sh
$ go run closing-channels.go
sent job 1
received job 1
sent job 2
received job 2
sent job 3
received job 3
sent all jobs
received all jobs

# クローズされたチャネルの考え方は、次の例に自然につながります。
# チャネルの`range`。
```

以下に完全なコードがあります。

```go
// チャネルを _クローズ_ すると、そのチャネルにはもう値が送信されなくなります。
// これは、チャネルの受信側に完了を通知するのに役立ちます。

package main

import "fmt"

// この例では、`jobs`チャネルを使用して、
// `main()`ゴルーチンからワーカーゴルーチンに処理すべき作業を伝えます。
// ワーカーに対してもう作業がない場合、`jobs`チャネルを`close`します。
func main() {
	jobs := make(chan int, 5)
	done := make(chan bool)

	// ここがワーカーゴルーチンです。
	// `j, more := <-jobs`で`jobs`から繰り返し受信します。
	// この受信の特殊な2値形式では、`jobs`が`close`され、
	// チャネル内のすべての値が既に受信されている場合、`more`値は`false`になります。
	// すべての作業を終えたときに、これを使って`done`に通知します。
	go func() {
		for {
			j, more := <-jobs
			if more {
				fmt.Println("received job", j)
			} else {
				fmt.Println("received all jobs")
				done <- true
				return
			}
		}
	}()

	// これは、`jobs`チャネルを介してワーカーに3つの作業を送信し、その後クローズします。
	for j := 1; j <= 3; j++ {
		jobs <- j
		fmt.Println("sent job", j)
	}
	close(jobs)
	fmt.Println("sent all jobs")

	// 前に見た [同期](channel-synchronization) アプローチを使ってワーカーを待ちます。
	<-done
}

```
