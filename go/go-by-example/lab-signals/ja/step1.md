# シグナル

場合によっては、Go プログラムが Unix シグナルを賢く扱うようにしたいと思うことがあります。たとえば、サーバーが `SIGTERM` を受け取ったときにグレースフルにシャットダウンするようにしたり、コマンドラインツールが `SIGINT` を受け取ったときに入力の処理を停止するようにしたりします。

- `os.Signal` の通知を受け取るためのバッファ付きチャネルを作成します。
- `signal.Notify` を使用して、指定されたシグナルの通知を受け取るようにチャネルを登録します。
- シグナルのブロッキング受信を実行するための goroutine を作成します。
- 受信したシグナルを出力し、プログラムが終了できることを通知します。
- 期待されるシグナルを待ち、その後終了します。

```sh
# このプログラムを実行すると、シグナルを待ち続けます。
# `ctrl-C` を入力することで（端末では `^C` と表示されます）
# `SIGINT` シグナルを送信し、プログラムが `interrupt` を出力してから終了します。
$ go run signals.go
awaiting signal
^C
interrupt
exiting
```

以下が完全なコードです：

```go
// 時々、私たちは Go プログラムが [Unix シグナル](https://en.wikipedia.org/wiki/Unix_signal) を賢く扱うようにしたいと思います。
// たとえば、サーバーが `SIGTERM` を受け取ったときにグレースフルにシャットダウンするようにしたり、
// コマンドラインツールが `SIGINT` を受け取ったときに入力の処理を停止するようにしたりします。
// ここでは、チャネルを使って Go でシグナルを扱う方法を示します。

package main

import (
	"fmt"
	"os"
	"os/signal"
	"syscall"
)

func main() {

	// Go のシグナル通知は、チャネルに `os.Signal` 値を送信することで機能します。
	// これらの通知を受け取るためのチャネルを作成します。このチャネルはバッファ付きである必要があります。
	sigs := make(chan os.Signal, 1)

	// `signal.Notify` は、指定されたチャネルに指定されたシグナルの通知を受け取るように登録します。
	signal.Notify(sigs, syscall.SIGINT, syscall.SIGTERM)

	// ここではメイン関数内で `sigs` から受信できますが、
	// グレースフルシャットダウンのより現実的なシナリオを示すために、
	// 別の goroutine でどのように行うかを見てみましょう。
	done := make(chan bool, 1)

	go func() {
		// この goroutine はシグナルのブロッキング受信を実行します。
		// シグナルを受け取ると、それを出力してから、
		// プログラムが終了できることを通知します。
		sig := <-sigs
		fmt.Println()
		fmt.Println(sig)
		done <- true
	}()

	// プログラムはここで待機し、期待されるシグナルを受け取るまで（上記の goroutine が `done` に値を送信することによって示される）、その後終了します。
	fmt.Println("awaiting signal")
	<-done
	fmt.Println("exiting")
}

```
