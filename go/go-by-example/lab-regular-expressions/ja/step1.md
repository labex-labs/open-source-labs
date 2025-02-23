# 正規表現

この実験では、Go言語で様々な正規表現関連のタスクを実行するためのコードを完成させる必要があります。

- `regexp` パッケージを使用して正規表現関連のタスクを実行します。
- `MatchString` を使用して、パターンが文字列と一致するかどうかをテストします。
- `Compile` を使用して `Regexp` 構造体を最適化します。
- `MatchString` を使用して、`Compile` と同じように一致をテストします。
- `FindString` を使用して、正規表現の一致を見つけます。
- `FindStringIndex` を使用して、最初の一致を見つけ、一致するテキストではなく、一致の開始と終了インデックスを返します。
- `FindStringSubmatch` を使用して、`p([a-z]+)ch` と `([a-z]+)` の両方に関する情報を返します。
- `FindStringSubmatchIndex` を使用して、一致と部分一致のインデックスに関する情報を返します。
- `FindAllString` を使用して、正規表現のすべての一致を見つけます。
- `FindAllStringSubmatchIndex` を使用して、入力内のすべての一致に適用します。最初の一致だけでなく、すべての一致に適用します。
- `Match` を使用して、`[]byte` 引数で一致をテストし、関数名から `String` を削除します。
- `MustCompile` を使用して、正規表現を持つグローバル変数を作成します。
- `ReplaceAllString` を使用して、文字列を他の値で置き換えます。
- `ReplaceAllFunc` を使用して、与えられた関数で一致するテキストを変換します。

```sh
$ go run regular-expressions.go
true
true
peach
idx: [0 5]
[peach ea]
[0 5 1 3]
[peach punch pinch]
all: [[0 5 1 3] [6 11 7 9] [12 17 13 15]]
[peach punch]
true
regexp: p([a-z]+)ch
a <fruit>
a PEACH

# Goの正規表現の完全なリファレンスについては、
# [「regexp」](https://pkg.go.dev/regexp) パッケージのドキュメントを参照してください。

```

以下が完全なコードです：

```go
// Goは[正規表現](https://en.wikipedia.org/wiki/Regular_expression)に対する組み込みのサポートを提供しています。
// 以下は、Goにおける一般的な正規表現関連のタスクのいくつかの例です。

package main

import (
	"bytes"
	"fmt"
	"regexp"
)

func main() {

	// これは、パターンが文字列と一致するかどうかをテストします。
	match, _ := regexp.MatchString("p([a-z]+)ch", "peach")
	fmt.Println(match)

	// 上では直接文字列パターンを使用しましたが、
	// 他の正規表現タスクでは、最適化された `Regexp` 構造体を `Compile` する必要があります。
	r, _ := regexp.Compile("p([a-z]+)ch")

	// これらの構造体では多くのメソッドが利用可能です。ここでは、
	// 先ほど見たのと同じような一致テストを行います。
	fmt.Println(r.MatchString("peach"))

	// これは、正規表現の一致を見つけます。
	fmt.Println(r.FindString("peach punch"))

	// これも最初の一致を見つけますが、一致するテキストではなく、
	// 一致の開始と終了インデックスを返します。
	fmt.Println("idx:", r.FindStringIndex("peach punch"))

	// `Submatch` のバリアントには、
	// 完全なパターンの一致とそれらの一致内の部分一致の両方に関する情報が含まれています。
	// たとえば、これは `p([a-z]+)ch` と `([a-z]+)` の両方に関する情報を返します。
	fmt.Println(r.FindStringSubmatch("peach punch"))

	// 同様に、これは一致と部分一致のインデックスに関する情報を返します。
	fmt.Println(r.FindStringSubmatchIndex("peach punch"))

	// これらの関数の `All` バリアントは、入力内のすべての一致に適用されます。最初の一致だけでなく、すべての一致に適用されます。
	// たとえば、正規表現のすべての一致を見つけるには。
	fmt.Println(r.FindAllString("peach punch pinch", -1))

	// 上で見た他の関数にもこれらの `All` バリアントが利用可能です。
	fmt.Println("all:", r.FindAllStringSubmatchIndex(
		"peach punch pinch", -1))

	// これらの関数に対して2番目の引数として非負の整数を指定すると、一致の数が制限されます。
	fmt.Println(r.FindAllString("peach punch pinch", 2))

	// 上の例では文字列引数を使用し、`MatchString` のような名前を使っていました。
	// また、`[]byte` 引数を提供し、関数名から `String` を削除することもできます。
	fmt.Println(r.Match([]byte("peach")))

	// 正規表現を持つグローバル変数を作成する際には、`Compile` の `MustCompile` バリエーションを使用できます。
	// `MustCompile` はエラーを返す代わりにパニックを起こします。これは、グローバル変数に対して使用するのが安全です。
	r = regexp.MustCompile("p([a-z]+)ch")
	fmt.Println("regexp:", r)

	// `regexp` パッケージを使用して、文字列を他の値で置き換えることもできます。
	fmt.Println(r.ReplaceAllString("a peach", "<fruit>"))

	// `Func` バリアントを使用すると、与えられた関数で一致するテキストを変換できます。
	in := []byte("a peach")
	out := r.ReplaceAllFunc(in, bytes.ToUpper)
	fmt.Println(string(out))
}

```
