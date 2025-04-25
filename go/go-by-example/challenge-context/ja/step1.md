# コンテキスト

`hello`関数は、サーバーが行っている作業をシミュレートします。これは、クライアントに応答を送信する前に数秒間待機することで行われます。作業中は、コンテキストの`Done()`チャネルを監視して、作業をキャンセルしてできるだけ早く返す信号があるかどうかを確認します。

## 要件

- Golang 1.13 以上

## 例

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
