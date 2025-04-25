# ファイルの読み取り

Go 言語のプログラムでは、ファイルを読み取り、ファイル内のデータに対してさまざまな操作を行う必要があります。

## 要件

- Go 言語の基本的なプログラミング概念に精通している必要があります。
- コンピュータに Go 言語がインストールされている必要があります。

## 例

```sh
$ echo "hello" > /tmp/dat
$ echo "go" >> /tmp/dat
$ go run reading-files.go
hello
go
5 bytes: hello
2 bytes @ 6: go
2 bytes @ 6: go
5 bytes: hello

# 次に、ファイルの書き込みについて見ていきます。
```
