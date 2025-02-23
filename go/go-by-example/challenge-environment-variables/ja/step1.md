# 環境変数

このチャレンジでは、環境変数を設定、取得、一覧表示する必要があります。

## 要件

- `os.Setenv` を使用してキー/値のペアを設定します。
- `os.Getenv` を使用してキーに対する値を取得します。
- `os.Environ` を使用して環境にあるすべてのキー/値のペアを一覧表示します。
- `strings.SplitN` を使用してキーと値を分割します。

## 例

```sh
# プログラムを実行すると、プログラム内で設定した `FOO` の値が取得されることがわかりますが、
# `BAR` は空です。
$ go run environment-variables.go
FOO: 1
BAR:

# 環境にあるキーの一覧は、特定のマシンに依存します。
TERM_PROGRAM
PATH
SHELL
...
FOO

# 最初に環境で `BAR` を設定すると、実行中のプログラムがその値を取得します。
$ BAR=2 go run environment-variables.go
FOO: 1
BAR: 2
...
```
