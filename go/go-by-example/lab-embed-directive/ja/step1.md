# 埋め込みディレクティブ

与えられたコードを修正して、ファイルとフォルダをGoバイナリに埋め込み、その内容を表示することがあなたの課題です。

- ファイルとフォルダを埋め込むには、`embed`パッケージを使用する必要があります。
- 埋め込まれたファイルの内容を格納するには、`string`型と`[]byte`型を使用する必要があります。
- ワイルドカードを使って複数のファイルやフォルダを埋め込むには、`embed.FS`型を使用する必要があります。
- 埋め込まれたファイルの内容を表示する必要があります。

```sh
# これらのコマンドを使ってサンプルを実行します。
# （注：Go Playgroundの制限により、
# このサンプルはローカルマシン上でのみ実行できます。）
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

以下に完全なコードがあります。

```go
// `//go:embed`は、プログラムがビルド時にGoバイナリに任意のファイルやフォルダを含めることを可能にする
// [コンパイラディレクティブ](https://pkg.go.dev/cmd/compile#hdr-Compiler_Directives)です。
// 埋め込みディレクティブに関する詳細は、
// [ここ](https://pkg.go.dev/embed)を参照してください。
package main

// `embed`パッケージをインポートします。このパッケージからエクスポートされた識別子を使わない場合、
// `_ "embed"`でブランクインポートを行うことができます。
import (
	"embed"
)

// `embed`ディレクティブは、Goソースファイルが含まれるディレクトリに対する相対パスを受け付けます。
// このディレクティブは、その直後に続く`string`変数にファイルの内容を埋め込みます。
//
//go:embed folder/single_file.txt
var fileString string

// または、ファイルの内容を`[]byte`に埋め込むこともできます。
//
//go:embed folder/single_file.txt
var fileByte []byte

// ワイルドカードを使って複数のファイルやフォルダを埋め込むこともできます。
// これは、[embed.FS型](https://pkg.go.dev/embed#FS)の変数を使い、
// 簡単な仮想ファイルシステムを実装します。
//
//go:embed folder/single_file.txt
//go:embed folder/*.hash
var folder embed.FS

func main() {

	// `single_file.txt`の内容を表示します。
	print(fileString)
	print(string(fileByte))

	// 埋め込まれたフォルダからいくつかのファイルを取得します。
	content1, _ := folder.ReadFile("folder/file1.hash")
	print(string(content1))

	content2, _ := folder.ReadFile("folder/file2.hash")
	print(string(content2))
}

```
