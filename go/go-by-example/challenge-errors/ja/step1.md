# エラー

このチャレンジでは、入力引数が42の場合にエラーを返す2つの関数が提供されています。最初の関数は基本的なエラー値を返し、2番目の関数はエラーを表すためにカスタム型を使用します。

## 要件

- `errors` パッケージをインポートする必要があります。
- `f1` 関数は、入力引数が42の場合にエラーを返す必要があります。
- `f2` 関数は、入力引数が42の場合に `argError` 型のエラーを返す必要があります。
- `argError` 型は2つのフィールド `arg` と `prob` を持たなければなりません。
- `argError` 型は `Error()` メソッドを実装する必要があります。
- `main` 関数は、入力引数として7と42を使って `f1` と `f2` の両方を呼び出す必要があります。
- `main` 関数は、各関数呼び出しの結果と、返されたエラーを一緒に出力する必要があります。
- `main` 関数は、カスタムエラーのデータをプログラム的にどのように使うかを示す必要があります。

## 例

```sh
$ go run errors.go
f1 worked: 10
f1 failed: can't work with 42
f2 worked: 10
f2 failed: 42 - can't work with it
42
can't work with it

# See this [great post](https://go.dev/blog/error-handling-and-go)
# on the Go blog for more on error handling.

```
