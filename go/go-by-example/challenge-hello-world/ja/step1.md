# ハローワールド

コンソールに「hello world」というメッセージを表示するプログラムを書きましょう。

## 要件

- プログラムはメッセージを表示するために `fmt` パッケージを使用する必要があります。
- プログラムは Golang で書かれる必要があります。

## 例

```sh
# プログラムを実行するには、コードを `hello-world.go` に入れて
# `go run` を使用します。
$ go run hello-world.go
hello world

# 時々、プログラムをバイナリにビルドしたい場合があります。
# これは `go build` を使用して行うことができます。
$ go build hello-world.go
$ ls
hello-world hello-world.go

# その後、ビルド済みのバイナリを直接実行することができます。
$./hello-world
hello world

# これで基本的な Go プログラムを実行してビルドできるようになりましたので、
# この言語についてもっと学びましょう。
```
