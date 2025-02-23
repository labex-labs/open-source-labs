# HTTPサーバ

2つのルート：`/hello` と `/headers` を処理できる簡単なHTTPサーバを書くように求められています。`/hello` ルートは単純な "hello" レスポンスを返す必要があり、`/headers` ルートはすべてのHTTPリクエストヘッダを返す必要があります。

- サーバは `net/http` パッケージを使用する必要があります。
- `/hello` ルートは "hello" レスポンスを返す必要があります。
- `/headers` ルートはすべてのHTTPリクエストヘッダを返す必要があります。
- サーバはポート `8090` で待ち受ける必要があります。

```sh
# サーバをバックグラウンドで実行します。
$ go run http-servers.go &

# `/hello` ルートにアクセスします。
$ curl localhost:8090/hello
hello
```

以下が完全なコードです：

```go
// `net/http` パッケージを使えば、基本的なHTTPサーバを書くのは簡単です。
package main

import (
	"fmt"
	"net/http"
)

// `net/http` サーバにおける基本的な概念は
// *ハンドラ* です。ハンドラは `http.Handler` インターフェイスを実装するオブジェクトです。
// ハンドラを書く一般的な方法は、適切なシグネチャの関数に対して `http.HandlerFunc` アダプタを使うことです。
func hello(w http.ResponseWriter, req *http.Request) {

	// ハンドラとして機能する関数は
	// `http.ResponseWriter` と `http.Request` を引数に取ります。
	// レスポンスライタはHTTPレスポンスを埋めるために使用されます。
	// ここでの単純なレスポンスはただ "hello\n" です。
	fmt.Fprintf(w, "hello\n")
}

func headers(w http.ResponseWriter, req *http.Request) {

	// このハンドラは、すべてのHTTPリクエストヘッダを読み取り、
	// それらをレスポンスボディにエコーすることで、もう少し洗練されたことを行います。
	for name, headers := range req.Header {
		for _, h := range headers {
			fmt.Fprintf(w, "%v: %v\n", name, h)
		}
	}
}

func main() {

	// サーバルートにハンドラを登録する際には、
	// `http.HandleFunc` という便利な関数を使います。
	// これは `net/http` パッケージ内の *デフォルトルータ* を設定し、
	// 関数を引数に取ります。
	http.HandleFunc("/hello", hello)
	http.HandleFunc("/headers", headers)

	// 最後に、ポートとハンドラを指定して `ListenAndServe` を呼び出します。
	// `nil` は、先ほど設定したデフォルトルータを使用することを示しています。
	http.ListenAndServe(":8090", nil)
}

```
