# 埋め込みディレクティブ

あなたの課題は、与えられたコードを修正して、ファイルとフォルダを Go バイナリに埋め込み、それらの内容を表示することです。

## 要件

- ファイルとフォルダを埋め込むには、`embed`パッケージを使用する必要があります。
- 埋め込まれたファイルの内容を格納するには、`string`型と`[]byte`型を使用する必要があります。
- ワイルドカードを使って複数のファイルやフォルダを埋め込むには、`embed.FS`型を使用する必要があります。
- 埋め込まれたファイルの内容を表示する必要があります。

## 例

```sh
# これらのコマンドを使って例を実行します。
# （注：Go Playground の制限により、
# この例はローカルマシンでのみ実行できます。）
$ mkdir -p folder
$ echo "hello go" > folder/single_file.txt
$ echo "123" > folder/file1.hash
$ echo "456" > folder/file2.hash

$ go run embed-directive.go
hello go
hello go
123
456
```
