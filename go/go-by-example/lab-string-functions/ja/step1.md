# 文字列関数

`strings`パッケージによって提供される様々な文字列関数の出力を表示するために、以下のコードを完成させます。

- `strings`パッケージを使用して実験を完了させます。
- `fmt.Println`関数を使用して出力を表示します。
- 関数名またはパラメータを変更しないでください。

```sh
$ go run string-functions.go
Contains: true
Count: 2
HasPrefix: true
HasSuffix: true
Index: 1
Join: a-b
Repeat: aaaaa
Replace: f00
Replace: f0o
Split: [a b c d e]
ToLower: test
ToUpper: TEST
```

以下が完全なコードです。

```go
// 標準ライブラリの `strings` パッケージは、多くの便利な文字列関連の関数を提供します。ここにいくつかの例を示しますので、このパッケージの概要を掴んでもらえれば幸いです。

package main

import (
	"fmt"
	s "strings"
)

// 以下で頻繁に使用するので、`fmt.Println` を短い名前でエイリアス化します。
var p = fmt.Println

func main() {

	// ここに `strings` に用意されている関数のサンプルを示します。これらはパッケージ内の関数なので、文字列オブジェクト自体のメソッドではありません。したがって、関数の最初の引数として対象の文字列を渡す必要があります。[`strings`](https://pkg.go.dev/strings) パッケージのドキュメントでさらに多くの関数を見つけることができます。
	p("Contains:  ", s.Contains("test", "es"))
	p("Count:     ", s.Count("test", "t"))
	p("HasPrefix: ", s.HasPrefix("test", "te"))
	p("HasSuffix: ", s.HasSuffix("test", "st"))
	p("Index:     ", s.Index("test", "e"))
	p("Join:      ", s.Join([]string{"a", "b"}, "-"))
	p("Repeat:    ", s.Repeat("a", 5))
	p("Replace:   ", s.Replace("foo", "o", "0", -1))
	p("Replace:   ", s.Replace("foo", "o", "0", 1))
	p("Split:     ", s.Split("a-b-c-d-e", "-"))
	p("ToLower:   ", s.ToLower("TEST"))
	p("ToUpper:   ", s.ToUpper("test"))
}

```
