# ファイルの読み取り

Go プログラムでは、ファイルを読み取り、ファイル内のデータに対してさまざまな操作を行う必要があります。

- Go の基本的なプログラミング概念に慣れている必要があります。
- コンピュータに Go がインストールされている必要があります。

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

# 次に、ファイルの書き込みについて見てみましょう。
```

以下に完全なコードがあります。

```go
// 多くの Go プログラムで必要な基本的なタスクは、ファイルの読み書きです。まずは、
// ファイルの読み取りのいくつかの例を見てみましょう。

package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
)

// ファイルを読み取るには、ほとんどの呼び出しでエラーをチェックする必要があります。
// このヘルパー関数により、以下のエラーチェックを簡略化できます。
func check(e error) {
	if e!= nil {
		panic(e)
	}
}

func main() {

	// おそらく最も基本的なファイル読み取りタスクは、
	// ファイルの内容全体をメモリに読み込むことです。
	dat, err := os.ReadFile("/tmp/dat")
	check(err)
	fmt.Print(string(dat))

	// ファイルの読み取り方法や読み取る部分をより細かく制御したい場合が多いです。
	// これらのタスクでは、まず `Open` を使ってファイルを開き、`os.File` 値を取得します。
	f, err := os.Open("/tmp/dat")
	check(err)

	// ファイルの先頭からいくつかのバイトを読み取ります。
	// 最大 5 バイトを読み取るようにしますが、実際に読み取ったバイト数もメモします。
	b1 := make([]byte, 5)
	n1, err := f.Read(b1)
	check(err)
	fmt.Printf("%d bytes: %s\n", n1, string(b1[:n1]))

	// また、ファイル内の既知の位置に `Seek` して、そこから `Read` することもできます。
	o2, err := f.Seek(6, 0)
	check(err)
	b2 := make([]byte, 2)
	n2, err := f.Read(b2)
	check(err)
	fmt.Printf("%d bytes @ %d: ", n2, o2)
	fmt.Printf("%v\n", string(b2[:n2]))

	// `io` パッケージには、ファイル読み取りに役立つ関数がいくつかあります。
	// たとえば、上記のような読み取りは `ReadAtLeast` を使ってより堅牢に実装できます。
	o3, err := f.Seek(6, 0)
	check(err)
	b3 := make([]byte, 2)
	n3, err := io.ReadAtLeast(f, b3, 2)
	check(err)
	fmt.Printf("%d bytes @ %d: %s\n", n3, o3, string(b3))

	// 巻き戻しの機能は組み込みではありませんが、`Seek(0, 0)` でこれを実現できます。
	_, err = f.Seek(0, 0)
	check(err)

	// `bufio` パッケージは、バッファ付きのリーダーを実装しており、
	// 多数の小さな読み取りに対する効率性と、追加の読み取りメソッドのために役立ちます。
	r4 := bufio.NewReader(f)
	b4, err := r4.Peek(5)
	check(err)
	fmt.Printf("5 bytes: %s\n", string(b4))

	// 終了後はファイルを閉じます (通常は、`Open` の直後に `defer` を使って
	// スケジュールされます)。
	f.Close()
}

```
