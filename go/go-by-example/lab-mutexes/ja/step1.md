# ミューテックス

この実験で解決する問題は、複数の goroutine を使用してループ内で名前付きのカウンタをインクリメントし、カウンタへのアクセスを同期させることです。

- `Container` 構造体を使用して、カウンタのマップを保持します。
- `Mutex` を使用して、`counters` マップへのアクセスを同期させます。
- `Container` 構造体には、`name` という文字列を受け取り、`counters` マップ内の対応するカウンタをインクリメントする `inc` メソッドが必要です。
- `inc` メソッドは、`counters` マップにアクセスする前にミューテックスをロックし、関数の終了時に `defer` 文を使用してアンロックします。
- `sync.WaitGroup` 構造体を使用して、goroutine が終了するのを待ちます。
- `fmt.Println` 関数を使用して、`counters` マップを出力します。

```sh
# プログラムを実行すると、カウンタが予想通りに更新されることがわかります。
$ go run mutexes.go
map[a:20000 b:10000]

# 次に、goroutine とチャネルのみを使用して同じ状態管理タスクを実装する方法を見てみましょう。

```

以下が完全なコードです：

```go
// 前の例では、[原子操作](atomic-counters)を使用して簡単なカウンタ状態を管理する方法を見ました。
// より複雑な状態では、複数の goroutine 間で安全にデータにアクセスするために、[ミューテックス](https://en.wikipedia.org/wiki/Mutual_exclusion)を使用できます。

package main

import (
	"fmt"
	"sync"
)

// Container はカウンタのマップを保持します。複数の goroutine から同時に更新するため、
// アクセスを同期させるために `Mutex` を追加します。
// ミューテックスはコピーできないことに注意してください。この `struct` を渡す場合は、
// ポインタで行う必要があります。
type Container struct {
	mu       sync.Mutex
	counters map[string]int
}

func (c *Container) inc(name string) {
	// `counters` にアクセスする前にミューテックスをロックします。関数の終了時に
	// [defer](defer) 文を使用してアンロックします。
	c.mu.Lock()
	defer c.mu.Unlock()
	c.counters[name]++
}

func main() {
	c := Container{
		// ミューテックスのゼロ値はそのまま使用可能です。ここでは初期化は不要です。
		counters: map[string]int{"a": 0, "b": 0},
	}

	var wg sync.WaitGroup

	// この関数は、名前付きのカウンタをループ内でインクリメントします。
	doIncrement := func(name string, n int) {
		for i := 0; i < n; i++ {
			c.inc(name)
		}
		wg.Done()
	}

	// 複数の goroutine を同時に実行します。すべてが同じ `Container` にアクセスし、
	// 2つは同じカウンタにアクセスすることに注意してください。
	wg.Add(3)
	go doIncrement("a", 10000)
	go doIncrement("a", 10000)
	go doIncrement("b", 10000)

	// goroutine が終了するのを待ちます。
	wg.Wait()
	fmt.Println(c.counters)
}

```
