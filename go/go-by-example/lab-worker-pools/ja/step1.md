# ワーカープール

`jobs` チャネルを介して作業を受け取り、`results` チャネルを介して対応する結果を送信するワーカープールを実装します。ワーカープールは複数の並行インスタンスを持ち、各ワーカーは1つの作業につき1秒間スリープして、高負荷なタスクをシミュレートします。

- goroutine とチャネルを使ってワーカープールを実装します。
- ワーカープールは複数の並行インスタンスを持つ必要があります。
- 各ワーカーは1つの作業につき1秒間スリープして、高負荷なタスクをシミュレートします。
- ワーカープールは `jobs` チャネルを介して作業を受け取り、`results` チャネルを介して対応する結果を送信する必要があります。

```sh
# 実行中のプログラムでは、さまざまなワーカーによって5つの作業が実行されています。
# 合計で約5秒間の作業を行っているにもかかわらず、プログラムは約2秒しかかかりません。
# なぜなら、3つのワーカーが並行して動作しているからです。
$ time go run worker-pools.go
worker 1 started job 1
worker 2 started job 2
worker 3 started job 3
worker 1 finished job 1
worker 1 started job 4
worker 2 finished job 2
worker 2 started job 5
worker 3 finished job 3
worker 1 finished job 4
worker 2 finished job 5

real 0m2.358s
```

以下が完全なコードです：

```go
// この例では、goroutine とチャネルを使って _ワーカープール_ を実装する方法を見てみます。

package main

import (
	"fmt"
	"time"
)

// ここにワーカーがあり、複数の並行インスタンスを実行します。
// これらのワーカーは `jobs` チャネルを介して作業を受け取り、
// `results` に対応する結果を送信します。
// 1つの作業につき1秒間スリープして、高負荷なタスクをシミュレートします。
func worker(id int, jobs <-chan int, results chan<- int) {
	for j := range jobs {
		fmt.Println("worker", id, "started  job", j)
		time.Sleep(time.Second)
		fmt.Println("worker", id, "finished job", j)
		results <- j * 2
	}
}

func main() {

	// ワーカープールを使用するには、作業を送信して結果を収集する必要があります。
	// このために2つのチャネルを作成します。
	const numJobs = 5
	jobs := make(chan int, numJobs)
	results := make(chan int, numJobs)

	// これは3つのワーカーを起動します。最初はブロックされます。
	// まだ作業がないためです。
	for w := 1; w <= 3; w++ {
		go worker(w, jobs, results)
	}

	// ここでは5つの `jobs` を送信し、その後 `close` して、
	// これがすべての作業であることを示します。
	for j := 1; j <= numJobs; j++ {
		jobs <- j
	}
	close(jobs)

	// 最後に、すべての作業の結果を収集します。
	// これにより、ワーカー goroutine が終了することも保証されます。
	// 複数の goroutine を待つ別の方法は、[WaitGroup](waitgroups) を使用することです。
	for a := 1; a <= numJobs; a++ {
		<-results
	}
}

```
