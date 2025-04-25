# 数値の解析

文字列から数値を解析することは、多くのプログラムで一般的なタスクです。この実験では、組み込みの `strconv` パッケージを使用して、文字列からさまざまな種類の数値を解析する必要があります。

- `strconv` パッケージを使用して文字列から数値を解析します。
- `ParseFloat` を使用して浮動小数点数を解析します。
- `ParseInt` を使用して整数を解析します。
- `ParseInt` を使用して 16 進形式の数値を解析します。
- `ParseUint` を使用して符号なし整数を解析します。
- `Atoi` を使用して 10 進数の整数を解析します。
- 解析関数が返すエラーを処理します。

```sh
$ go run number-parsing.go
1.234
123
456
789
135
strconv.ParseInt: parsing "wat": invalid syntax

# 次に、もう一つの一般的な解析タスクである URL を見てみましょう。
```

以下に完全なコードを示します。

```go
// 文字列から数値を解析することは、多くのプログラムで基本的で一般的なタスクです。
// ここでは、Go 言語でそれを行う方法を示します。

package main

// 組み込みのパッケージ `strconv` は数値の解析を提供します。
import (
	"fmt"
	"strconv"
)

func main() {

	// `ParseFloat` では、この `64` は解析する精度のビット数を示します。
	f, _ := strconv.ParseFloat("1.234", 64)
	fmt.Println(f)

	// `ParseInt` の場合、`0` は文字列から基数を推測することを意味します。
	// `64` は結果が 64 ビットに収まることを要求します。
	i, _ := strconv.ParseInt("123", 0, 64)
	fmt.Println(i)

	// `ParseInt` は 16 進形式の数値を認識します。
	d, _ := strconv.ParseInt("0x1c8", 0, 64)
	fmt.Println(d)

	// `ParseUint` も利用可能です。
	u, _ := strconv.ParseUint("789", 0, 64)
	fmt.Println(u)

	// `Atoi` は基本的な 10 進数の `int` 解析のための便利関数です。
	k, _ := strconv.Atoi("135")
	fmt.Println(k)

	// 解析関数は入力が不適切な場合にエラーを返します。
	_, e := strconv.Atoi("wat")
	fmt.Println(e)
}

```
