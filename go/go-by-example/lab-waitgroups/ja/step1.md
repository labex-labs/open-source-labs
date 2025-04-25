# waitgroups

この実験で解決する問題は、複数のゴルーチンを起動し、それぞれに対して WaitGroup のカウンタをインクリメントすることです。その後、起動したすべてのゴルーチンが終了するのを待つ必要があります。

- Golang の基本知識。
- Golang における並行処理の理解。
- `sync`パッケージに慣れていること。

```sh
$ go run waitgroups.go
Worker 5 starting
Worker 3 starting
Worker 4 starting
Worker 1 starting
Worker 2 starting
Worker 4 done
Worker 1 done
Worker 2 done
Worker 5 done
Worker 3 done

# 各起動時におけるワーカーの起動と終了の順序は
# おそらく異なります。
```

以下に完全なコードがあります：

```go
// 複数のゴルーチンが終了するのを待つには、
// *ウェイトグループ* を使用できます。

package main

import (
	"fmt"
	"sync"
	"time"
)

// これは、各ゴルーチンで実行する関数です。
func worker(id int) {
	fmt.Printf("Worker %d starting\n", id)

	// 高負荷なタスクをシミュレートするために Sleep します。
	time.Sleep(time.Second)
	fmt.Printf("Worker %d done\n", id)
}

func main() {

	// この WaitGroup は、ここで起動したすべてのゴルーチンが終了するのを待つために使用されます。
	// 注：WaitGroup を明示的に関数に渡す場合は、*ポインタ* で行う必要があります。
	var wg sync.WaitGroup

	// 複数のゴルーチンを起動し、それぞれに対して WaitGroup のカウンタをインクリメントします。
	for i := 1; i <= 5; i++ {
		wg.Add(1)
		// 各ゴルーチンクロージャで同じ `i` 値を再利用しないようにします。
		// 詳細については、[FAQ](https://golang.org/doc/faq#closures_and_goroutines) を参照してください。
		i := i

		// worker 呼び出しをクロージャでラップし、このワーカーが完了したことを WaitGroup に伝えるようにします。
		// このようにすることで、ワーカー自体はその実行に関与する並行処理のプリミティブを意識する必要がありません。
		go func() {
			defer wg.Done()
			worker(i)
		}()
	}

	// WaitGroup のカウンタが 0 に戻るまでブロックします。
	// すべてのワーカーが完了したことを通知されます。
	wg.Wait()

	// このアプローチには、ワーカーからのエラーを伝播させる簡単な方法はありません。
	// より高度なユースケースの場合は、[errgroup パッケージ](https://pkg.go.dev/golang.org/x/sync/errgroup) を使用することを検討してください。
}

```
