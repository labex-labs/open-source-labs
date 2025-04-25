# 関数によるソート

この実験で解くべき問題は、Go 言語で文字列を長さでソートするカスタムソート関数を実装することです。

- `byLength` 型を `[]string` 型のエイリアスとして作成します。
- `sort.Interface` を `byLength` 型で実装します。
- `Len` 関数と `Swap` 関数を `byLength` 型で実装します。
- `Less` 関数を `byLength` 型で実装して、実際のカスタムソートロジックを保持します。
- `main` 関数では、元の `fruits` スライスを `byLength` に変換し、その型付きのスライスに対して `sort.Sort` を使用します。

```sh
# プログラムを実行すると、望ましいように文字列の長さでソートされたリストが表示されます。
$ go run sorting-by-functions.go
[kiwi peach banana]

# このようにカスタム型を作成し、その型で 3 つの `Interface` メソッドを実装し、そのカスタム型のコレクションに対して `sort.Sort` を呼び出すことで、Go 言語のスライスを任意の関数でソートすることができます。
```

以下が完全なコードです。

```go
// 時々、コレクションを自然順序以外の基準でソートしたい場合があります。たとえば、文字列をアルファベット順ではなく、長さでソートしたいとしましょう。ここでは、Go 言語におけるカスタムソートの例を示します。

package main

import (
	"fmt"
	"sort"
)

// Go 言語でカスタム関数によるソートを行うには、対応する型が必要です。ここでは、組み込みの `[]string` 型のエイリアスである `byLength` 型を作成しました。
type byLength []string

// 型に `sort.Interface` の `Len`、`Less`、`Swap` を実装することで、`sort` パッケージの汎用的な `Sort` 関数を使用できます。`Len` と `Swap` は通常、型によらず似通っており、`Less` に実際のカスタムソートロジックが含まれます。この場合、文字列の長さが短い順にソートしたいので、ここでは `len(s[i])` と `len(s[j])` を使用しています。
func (s byLength) Len() int {
	return len(s)
}
func (s byLength) Swap(i, j int) {
	s[i], s[j] = s[j], s[i]
}
func (s byLength) Less(i, j int) bool {
	return len(s[i]) < len(s[j])
}

// これらの準備が整えば、元の `fruits` スライスを `byLength` に変換し、その型付きのスライスに対して `sort.Sort` を使用することで、カスタムソートを実装できます。
func main() {
	fruits := []string{"peach", "banana", "kiwi"}
	sort.Sort(byLength(fruits))
	fmt.Println(fruits)
}

```
