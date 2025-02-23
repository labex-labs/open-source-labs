# 状態を持つ goroutine

並列プログラミングにおいて、共有状態へのアクセスを同期させることは、競合条件やデータの破損を回避するために不可欠です。この実験では、単一の goroutine が状態を所有し、他の goroutine が状態を読み書きするためのメッセージを送信するシナリオを提示します。

- 状態を所有する goroutine に対して読み書き要求を発行するためにチャネルを使用します。
- 要求と応答をカプセル化するために `readOp` と `writeOp` 構造体を使用します。
- 状態を格納するために map を使用します。
- 成功と返却値を示すために `resp` チャネルを使用します。
- 読み書き操作の回数をカウントするために `atomic` パッケージを使用します。
- 操作間に遅延を追加するために `time` パッケージを使用します。

```sh
# 私たちのプログラムを実行すると、goroutine ベースの
# 状態管理の例が約80,000回の合計操作を完了することがわかります。
$ go run stateful-goroutines.go
readOps: 71708
writeOps: 7177

# この特定のケースでは、goroutine ベースのアプローチは
# ミューテックスベースのアプローチよりも少し複雑でした。
# ただし、特定のケースでは役立つ場合があります。たとえば、
# 他のチャネルが関係している場合や、複数のこのようなミューテックスを管理するのが
# エラーが発生しやすい場合です。プログラムの正しさを理解することに関して、
# 特に自然に感じられるアプローチをどちらでも使用する必要があります。
```

以下に完全なコードがあります：

```go
// 前の例では、明示的なロックを使用して
// [ミューテックス](mutexes) を使って、複数の goroutine 間で共有状態へのアクセスを同期させました。
// 別のオプションは、goroutine とチャネルの組み込みの同期機能を使用して、同じ結果を達成することです。
// このチャネルベースのアプローチは、コミュニケーションによるメモリの共有と、
// 各データを正確に1つの goroutine が所有する Go の考え方と一致しています。

package main

import (
	"fmt"
	"math/rand"
	"sync/atomic"
	"time"
)

// この例では、私たちの状態は単一の goroutine によって所有されます。
// これにより、データが同時アクセスによって破損することがないことが保証されます。
// その状態を読み書きするには、他の goroutine が所有する goroutine にメッセージを送信し、
// 対応する応答を受け取ります。これらの `readOp` と `writeOp` 構造体は、
// それらの要求と、所有する goroutine が応答する方法をカプセル化します。
type readOp struct {
	key  int
	resp chan int
}
type writeOp struct {
	key  int
	val  int
	resp chan bool
}

func main() {

	// 前と同じように、私たちは実行する操作の数をカウントします。
	var readOps uint64
	var writeOps uint64

	// `reads` と `writes` チャネルは、それぞれ他の goroutine によって
	// 読み書き要求を発行するために使用されます。
	reads := make(chan readOp)
	writes := make(chan writeOp)

	// ここには、`state` を所有する goroutine があります。
	// これは、前の例と同じように map ですが、
	// 今回は状態を持つ goroutine 専用になっています。
	// この goroutine は、`reads` と `writes` チャネルを繰り返し選択し、
	// 要求が到着するたびに応答します。応答は、まず要求された操作を実行し、
	// その後応答チャネル `resp` に値を送信して成功を示すことによって実行されます
	// （`reads` の場合、望ましい値も含みます）。
	go func() {
		var state = make(map[int]int)
		for {
			select {
			case read := <-reads:
				read.resp <- state[read.key]
			case write := <-writes:
				state[write.key] = write.val
				write.resp <- true
			}
		}
	}()

	// これは、`reads` チャネルを介して状態を所有する goroutine に対して読みを発行する
	// 100個の goroutine を開始します。
	// 各読み取りには、`readOp` を構築し、`reads` チャネルを介して送信し、
	// その後提供された `resp` チャネルを介して結果を受け取る必要があります。
	for r := 0; r < 100; r++ {
		go func() {
			for {
				read := readOp{
					key:  rand.Intn(5),
					resp: make(chan int)}
				reads <- read
				<-read.resp
				atomic.AddUint64(&readOps, 1)
				time.Sleep(time.Millisecond)
			}
		}()
	}

	// 同じアプローチを使用して、10個の書き込みも開始します。
	for w := 0; w < 10; w++ {
		go func() {
			for {
				write := writeOp{
					key:  rand.Intn(5),
					val:  rand.Intn(100),
					resp: make(chan bool)}
				writes <- write
				<-write.resp
				atomic.AddUint64(&writeOps, 1)
				time.Sleep(time.Millisecond)
			}
		}()
	}

	// goroutine が1秒間動作するようにします。
	time.Sleep(time.Second)

	// 最後に、操作回数を取得して報告します。
	readOpsFinal := atomic.LoadUint64(&readOps)
	fmt.Println("readOps:", readOpsFinal)
	writeOpsFinal := atomic.LoadUint64(&writeOps)
	fmt.Println("writeOps:", writeOpsFinal)
}

```
