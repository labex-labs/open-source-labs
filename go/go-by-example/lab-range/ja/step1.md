# Range

この実験で解決する問題は、スライス、配列、マップ、および文字列で `range` を使用する方法を示すことです。

この実験を完了するには、以下が必要です。

- Go 言語の構文に関する基本的な知識
- あなたのマシンに Go 言語がインストールされていること

```sh
$ go run range.go
sum: 9
index: 1
a - > apple
b - > banana
key: a
key: b
0 103
1 111
```

以下に完全なコードがあります。

```go
// _range_ は、さまざまなデータ構造の要素を反復処理します。
// 既に学んだいくつかのデータ構造で `range` をどのように使用するか見てみましょう。

package main

import "fmt"

func main() {

	// ここでは、`range` を使ってスライス内の数値を合計します。
	// 配列も同じように機能します。
	nums := []int{2, 3, 4}
	sum := 0
	for _, num := range nums {
		sum += num
	}
	fmt.Println("sum:", sum)

	// 配列とスライスでの `range` は、各エントリのインデックスと値の両方を提供します。
	// 上ではインデックスは必要なかったので、ブランク識別子 `_` で無視しました。
	// ただし、時には実際にインデックスが必要な場合もあります。
	for i, num := range nums {
		if num == 3 {
			fmt.Println("index:", i)
		}
	}

	// マップでの `range` は、キー/値のペアを反復処理します。
	kvs := map[string]string{"a": "apple", "b": "banana"}
	for k, v := range kvs {
		fmt.Printf("%s -> %s\n", k, v)
	}

	// `range` は、マップのキーだけを反復処理することもできます。
	for k := range kvs {
		fmt.Println("key:", k)
	}

	// 文字列での `range` は、Unicode コードポイントを反復処理します。
	// 最初の値は `rune` の開始バイトインデックスで、2 番目の値は `rune` 自体です。
	// 詳細については、[Strings and Runes](strings-and-runes) を参照してください。
	for i, c := range "go" {
		fmt.Println(i, c)
	}
}

```
