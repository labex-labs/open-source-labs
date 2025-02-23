# HTTP クライアント

サーバーにHTTP GETリクエストを送信し、HTTPレスポンスのステータスとレスポンスボディの最初の5行を表示するプログラムを作成する必要があります。

- プログラムは`net/http`パッケージを使用してHTTP GETリクエストを発行する必要があります。
- プログラムはHTTPレスポンスのステータスを表示する必要があります。
- プログラムはレスポンスボディの最初の5行を表示する必要があります。
- プログラムはエラーを適切に処理する必要があります。

```sh
$ go run http-clients.go
レスポンスステータス: 200 OK
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Go by Example</title>

```

以下に完全なコードがあります。

```go
// Goの標準ライブラリは、`net/http`パッケージにおいてHTTPクライアントとサーバーに対する優れたサポートを備えています。この例では、簡単なHTTPリクエストを発行するためにそれを使用します。
package main

import (
	"bufio"
	"fmt"
	"net/http"
)

func main() {

	// サーバーにHTTP GETリクエストを発行します。`http.Get`は、`http.Client`オブジェクトを作成してその`Get`メソッドを呼び出すことの便利なショートカットです。これは、便利なデフォルト設定を持つ`http.DefaultClient`オブジェクトを使用します。
	resp, err := http.Get("https://gobyexample.com")
	if err!= nil {
		panic(err)
	}
	defer resp.Body.Close()

	// HTTPレスポンスのステータスを表示します。
	fmt.Println("レスポンスステータス:", resp.Status)

	// レスポンスボディの最初の5行を表示します。
	scanner := bufio.NewScanner(resp.Body)
	for i := 0; scanner.Scan() && i < 5; i++ {
		fmt.Println(scanner.Text())
	}

	if err := scanner.Err(); err!= nil {
		panic(err)
	}
}

```
