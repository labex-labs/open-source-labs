# 環境変数

この実験では、環境変数を設定、取得、一覧表示する必要があります。

- `os.Setenv` を使用してキー/値のペアを設定します。
- `os.Getenv` を使用してキーの値を取得します。
- `os.Environ` を使用して環境にあるすべてのキー/値のペアを一覧表示します。
- `strings.SplitN` を使用してキーと値を分割します。

```sh
# プログラムを実行すると、プログラム内で設定した `FOO` の値が取得できますが、
# `BAR` は空になっています。
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

以下に完全なコードがあります。

```go
// [環境変数](https://en.wikipedia.org/wiki/Environment_variable)
// は、[Unix プログラムに構成情報を伝える](https://www.12factor.net/config) ための一般的なメカニズムです。
// 環境変数を設定、取得、一覧表示する方法を見てみましょう。

package main

import (
	"fmt"
	"os"
	"strings"
)

func main() {

	// キー/値のペアを設定するには、`os.Setenv` を使用します。キーの値を取得するには、`os.Getenv` を使用します。
	// キーが環境に存在しない場合、これは空の文字列を返します。
	os.Setenv("FOO", "1")
	fmt.Println("FOO:", os.Getenv("FOO"))
	fmt.Println("BAR:", os.Getenv("BAR"))

	// `os.Environ` を使用して環境にあるすべてのキー/値のペアを一覧表示します。
	// これは `KEY=value` の形式の文字列をスライスとして返します。
	// キーと値を取得するには、`strings.SplitN` で分割できます。
	// ここではすべてのキーを表示します。
	fmt.Println()
	for _, e := range os.Environ() {
		pair := strings.SplitN(e, "=", 2)
		fmt.Println(pair[0])
	}
}

```
