# コマンドライン引数

現在のプログラムは、それに渡された生のコマンドライン引数を出力します。ただし、インデックスに基づいて特定の引数を出力するように修正する必要があります。

- Go 言語の基本知識
- コマンドライン引数に慣れていること

```sh
# コマンドライン引数を実験するには、まず `go build` でバイナリをビルドするのが最善です。
$ go build command-line-arguments.go
$./command-line-arguments a b c d
[./command-line-arguments a b c d]
[a b c d]
c

# 次に、フラグを使った高度なコマンドライン処理を見てみましょう。
```

以下が完全なコードです。

```go
// [_コマンドライン引数_](https://en.wikipedia.org/wiki/Command-line_interface#Arguments)
// は、プログラムの実行をパラメータ化する一般的な方法です。
// たとえば、`go run hello.go` は `go` プログラムに対して `run` と
// `hello.go` の引数を使っています。

package main

import (
	"fmt"
	"os"
)

func main() {

	// `os.Args` を使うと、生のコマンドライン引数にアクセスできます。
	// このスライスの最初の値はプログラムのパスであり、`os.Args[1:]` は
	// プログラムの引数を保持しています。
	argsWithProg := os.Args
	argsWithoutProg := os.Args[1:]

	// 通常のインデックス付けで個々の引数を取得できます。
	arg := os.Args[3]

	fmt.Println(argsWithProg)
	fmt.Println(argsWithoutProg)
	fmt.Println(arg)
}

```
