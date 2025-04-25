# HTTP クライアント

サーバーに HTTP GET リクエストを送信し、HTTP レスポンスのステータスとレスポンスボディの最初の 5 行を表示するプログラムを作成するよう求められています。

## 要件

- プログラムは、HTTP GET リクエストを発行するために`net/http`パッケージを使用する必要があります。
- プログラムは、HTTP レスポンスのステータスを表示する必要があります。
- プログラムは、レスポンスボディの最初の 5 行を表示する必要があります。
- プログラムは、エラーを適切に処理する必要があります。

## 例

```sh
$ go run http-clients.go
Response status: 200 OK
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Go by Example</title>

```
