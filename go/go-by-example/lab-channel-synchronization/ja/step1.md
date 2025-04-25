# チャネルによる同期

この実験で解決する問題は、ある作業を行う goroutine を作成し、その作業が完了したときにチャネルを使って別の goroutine に通知することです。

この実験を完了するには、以下のことが必要になります。

- `worker`という名前の関数を作成し、`bool`型のチャネルをパラメータとして取ります。
- `worker`関数の中で、ある作業を行い、その作業が完了したことを通知するためにチャネルに値を送信します。
- `main`関数の中で、バッファサイズが 1 の`bool`型のチャネルを作成します。
- `worker`関数を呼び出し、そのチャネルをパラメータとして渡す goroutine を起動します。
- `main`関数をブロックして、チャネルから値が受信されるまで待ちます。

```sh
$ go run channel-synchronization.go
working...done

# このプログラムから`<- done`行を削除すると、
# `worker` が開始される前にプログラムが終了します。
```

以下が完全なコードです。

```go
// チャネルを使って goroutine 間での実行を同期できます。
// ここでは、ブロッキング受信を使って goroutine が終了するのを待つ例を示します。
// 複数の goroutine が終了するのを待つ場合、
// [WaitGroup](waitgroups) を使う方が好ましい場合があります。

package main

import (
	"fmt"
	"time"
)

// これは goroutine で実行する関数です。
// `done` チャネルは、この関数の作業が完了したことを
// 別の goroutine に通知するために使われます。
func worker(done chan bool) {
	fmt.Print("working...")
	time.Sleep(time.Second)
	fmt.Println("done")

	// 作業が完了したことを通知するために値を送信します。
	done <- true
}

func main() {

	// ワーカーgoroutine を起動し、通知用のチャネルを渡します。
	done := make(chan bool, 1)
	go worker(done)

	// ワーカーからチャネルを通じての通知を受信するまでブロックします。
	<-done
}

```
