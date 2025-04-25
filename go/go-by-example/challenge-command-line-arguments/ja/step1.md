# コマンドライン引数

現在のプログラムは、それに渡された生のコマンドライン引数を出力します。ただし、インデックスに基づいて特定の引数を出力するように修正する必要があります。

## 要件

- Go 言語の基本的な知識
- コマンドライン引数に慣れていること

## 例

```sh
# コマンドライン引数を試すには、まず `go build` でバイナリをビルドするのが最善です。
$ go build command-line-arguments.go
$./command-line-arguments a b c d
[./command-line-arguments a b c d]
[a b c d]
c

# 次に、フラグを使った高度なコマンドライン処理を見てみましょう。
```
