# ソート

この実験で解くべき問題は、`sort` パッケージを使って文字列と整数のスライスをソートすることです。

- `sort` パッケージをインポートする必要があります。
- 文字列のスライスをソートするには `sort.Strings()` 関数を使用します。
- 整数のスライスをソートするには `sort.Ints()` 関数を使用します。
- 整数のスライスが既にソートされているかどうかを確認するには `sort.IntsAreSorted()` 関数を使用します。

```sh
# プログラムを実行すると、ソートされた文字列と整数の
# スライスと、`AreSorted` テストの結果として `true` が表示されます。
$ go run sorting.go
Strings: [a b c]
Ints: [2 4 7]
Sorted: true
```

以下に完全なコードがあります。

```go
// Goの`sort`パッケージは、組み込み型と
// ユーザー定義型のソートを実装しています。
// まずは組み込み型のソートを見てみましょう。

package main

import (
	"fmt"
	"sort"
)

func main() {

	// ソートメソッドは組み込み型に固有です。
	// ここでは文字列を例に挙げます。
	// ソートは破壊的であることに注意してください。
	// つまり、与えられたスライスを変更し、新しいスライスを返しません。
	strs := []string{"c", "a", "b"}
	sort.Strings(strs)
	fmt.Println("Strings:", strs)

	// 整数をソートする例です。
	ints := []int{7, 2, 4}
	sort.Ints(ints)
	fmt.Println("Ints:   ", ints)

	// スライスが既にソートされているかどうかを
	// 確認するためにも`sort`を使うことができます。
	s := sort.IntsAreSorted(ints)
	fmt.Println("Sorted: ", s)
}

```
