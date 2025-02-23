# ラインフィルター

この実験で解くべき問題は、stdin から入力テキストを読み取り、そのテキストのすべての文字を大文字に変換してから、変更されたテキストを stdout に出力する Go プログラムを作成することです。

- プログラムは stdin から入力テキストを読み取らなければなりません。
- プログラムは入力テキストのすべての文字を大文字に変換しなければなりません。
- プログラムは変更されたテキストを stdout に出力しなければなりません。

```sh
# ラインフィルターを試すには、まずいくつかの小文字の行が記載されたファイルを作成します。
$ echo 'hello' > /tmp/lines
$ echo 'filter' >> /tmp/lines

# 次に、ラインフィルターを使用して大文字の行を取得します。
$ cat /tmp/lines | go run line-filters.go
HELLO
FILTER
```

以下が完全なコードです。

```go
// _ラインフィルター_ は、stdin から入力を読み取り、それを処理してから、いくつかの派生結果を stdout に出力する一般的なタイプのプログラムです。`grep` や `sed` は一般的なラインフィルターです。

// 以下は、すべての入力テキストの大文字バージョンを書き出す Go のラインフィルターの例です。独自の Go のラインフィルターを書く際にこのパターンを使用できます。
package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {

	// バッファ付きのスキャナで無バッファの `os.Stdin` をラップすることで、スキャナを次のトークンに進める便利な `Scan` メソッドが得られます。これは、デフォルトのスキャナでは次の行になります。
	scanner := bufio.NewScanner(os.Stdin)

	for scanner.Scan() {
		// `Text` は、ここでは入力からの次の行である現在のトークンを返します。
		ucl := strings.ToUpper(scanner.Text())

		// 大文字に変換された行を出力します。
		fmt.Println(ucl)
	}

	// `Scan` 中のエラーをチェックします。ファイルの終端は予想され、`Scan` によってエラーとして報告されません。
	if err := scanner.Err(); err!= nil {
		fmt.Fprintln(os.Stderr, "error:", err)
		os.Exit(1)
	}
}

```
