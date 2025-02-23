# ファイルの書き込み

文字列とバイト列をファイルに書き込み、バッファ付きライターを使用するGoプログラムを書かなければなりません。

- プログラムは、文字列とバイト列をファイルに書き込む必要があります。
- プログラムは、バッファ付きライターを使用する必要があります。

```sh
# ファイル書き込みコードを実行してみましょう。
$ go run writing-files.go
wrote 5 bytes
wrote 7 bytes
wrote 9 bytes

# 次に、書き込まれたファイルの内容を確認します。
$ cat /tmp/dat1
hello
go
$ cat /tmp/dat2
some
writes
buffered

# 次に、これまで見てきたファイルI/Oの考え方を
# `stdin` と `stdout` ストリームに適用してみましょう。
```

以下が完全なコードです。

```go
// Go言語でファイルを書き込む方法は、
// 先ほど読み取りに使ったものと同じパターンになります。

package main

import (
	"bufio"
	"fmt"
	"os"
)

func check(e error) {
	if e!= nil {
		panic(e)
	}
}

func main() {

	// まずは、文字列を（または単にバイト列を）
	// ファイルに書き出す方法を見てみましょう。
	d1 := []byte("hello\ngo\n")
	err := os.WriteFile("/tmp/dat1", d1, 0644)
	check(err)

	// より細かい書き込みを行うには、書き込み用に
	// ファイルを開きます。
	f, err := os.Create("/tmp/dat2")
	check(err)

	// ファイルを開いた直後に `Close` を呼び出すのが
	// 慣例です。
	defer f.Close()

	// 予想通り、バイト列を `Write` できます。
	d2 := []byte{115, 111, 109, 101, 10}
	n2, err := f.Write(d2)
	check(err)
	fmt.Printf("wrote %d bytes\n", n2)

	// `WriteString` も利用できます。
	n3, err := f.WriteString("writes\n")
	check(err)
	fmt.Printf("wrote %d bytes\n", n3)

	// 書き込みを安定したストレージにフラッシュするには、
	// `Sync` を呼び出します。
	f.Sync()

	// `bufio` は、先ほど見たバッファ付きリーダーに加えて、
	// バッファ付きライターも提供しています。
	w := bufio.NewWriter(f)
	n4, err := w.WriteString("buffered\n")
	check(err)
	fmt.Printf("wrote %d bytes\n", n4)

	// すべてのバッファ操作が基礎となるライターに
	// 適用されることを確認するには、`Flush` を呼び出します。
	w.Flush()

}

```
