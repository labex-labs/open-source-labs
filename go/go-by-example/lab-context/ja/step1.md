# コンテキスト

`hello` 関数は、サーバーが行っている作業をシミュレートします。これは、クライアントに応答を送信する前に数秒間待機することで行われます。作業中は、コンテキストの `Done()` チャネルを監視して、作業をキャンセルしてできるだけ早く返す信号があるかどうかを確認します。

- Golang 1.13 以上のバージョンが必要です。

```sh
# サーバーをバックグラウンドで実行します。
$ go run context-in-http-servers.go &

# `/hello` に対するクライアント要求をシミュレートします。
# 開始直後に Ctrl+C を押してキャンセル信号を送信します。
$ curl localhost:8090/hello
server: hello handler started
^C
server: context canceled
server: hello handler ended
```

以下が完全なコードです：

```go
// 前の例では、簡単な [HTTP サーバー](http-servers) を設定する方法を見てきました。
// HTTP サーバーは、キャンセル制御に対する `context.Context` の使用方法を示すのに便利です。
// `Context` は、API 境界と goroutine をまたいで期限付き、キャンセル信号、およびその他の要求スコープの値を保持します。
package main

import (
	"fmt"
	"net/http"
	"time"
)

func hello(w http.ResponseWriter, req *http.Request) {

	// `net/http` メカニズムによって各要求に対して `context.Context` が作成され、
	// `Context()` メソッドで利用できます。
	ctx := req.Context()
	fmt.Println("server: hello handler started")
	defer fmt.Println("server: hello handler ended")

	// クライアントに応答を送信する前に数秒間待機します。
	// これは、サーバーが行っている作業をシミュレートできます。
	// 作業中は、コンテキストの `Done()` チャネルを監視して、
	// 作業をキャンセルしてできるだけ早く返す信号があるかどうかを確認します。
	select {
	case <-time.After(10 * time.Second):
		fmt.Fprintf(w, "hello\n")
	case <-ctx.Done():
		// コンテキストの `Err()` メソッドは、`Done()` チャネルが
		// クローズされた理由を説明するエラーを返します。
		err := ctx.Err()
		fmt.Println("server:", err)
		internalError := http.StatusInternalServerError
		http.Error(w, err.Error(), internalError)
	}
}

func main() {

	// 前と同じように、"/hello" ルートにハンドラを登録し、サービングを開始します。
	http.HandleFunc("/hello", hello)
	http.ListenAndServe(":8090", nil)
}

```
