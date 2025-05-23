# スライス

この実験で解くべき問題は、Go でスライスを作成して操作することです。ゼロではない長さの空のスライスを作成し、スライス内の値を設定および取得し、`len` 関数を使用してスライスの長さを取得し、`append` 関数を使用して新しい値をスライスに追加し、`copy` 関数を使用してスライスをコピーし、スライス演算子を使用して既存のスライスから要素のスライスを取得する必要があります。

この実験を完了するには、Go の構文とスライスデータ型の基本的な理解が必要です。また、`make`、`append`、`copy` 関数、およびスライス演算子にも慣れている必要があります。

```sh
# スライスは配列とは異なる型ですが、
# `fmt.Println` によって同様にレンダリングされます。
$ go run slices.go
emp: [ ]
set: [a b c]
get: c
len: 3
apd: [a b c d e f]
cpy: [a b c d e f]
sl1: [c d e]
sl2: [a b c d e]
sl3: [c d e f]
dcl: [g h i]
2d: [[0] [1 2] [2 3 4]]

# Go チームによるこの [素晴らしいブログ記事](https://go.dev/blog/slices-intro) を
# 参照して、Go のスライスの設計と実装に関する詳細を確認してください。

# これまで配列とスライスを見てきましたので、
# Go の他の重要な組み込みデータ構造である
# マップを見てみましょう。
```

以下に完全なコードがあります。

```go
// _スライス_ は Go の重要なデータ型であり、
// 配列よりもシーケンスに対するより強力なインターフェイスを提供します。

package main

import "fmt"

func main() {

	// 配列とは異なり、スライスは含まれる要素のみで型付けされます
	// （要素の数ではありません）。ゼロではない長さの空のスライスを作成するには、
	// 組み込みの `make` を使用します。ここでは、長さ `3` の
	// `string` のスライスを作成します（最初はゼロ値）。
	s := make([]string, 3)
	fmt.Println("emp:", s)

	// 配列と同じように、設定と取得ができます。
	s[0] = "a"
	s[1] = "b"
	s[2] = "c"
	fmt.Println("set:", s)
	fmt.Println("get:", s[2])

	// `len` は予想通りスライスの長さを返します。
	fmt.Println("len:", len(s))

	// これらの基本的な操作に加えて、スライスは配列よりも豊富な
	// 操作をいくつかサポートしています。1 つは組み込みの `append` で、
	// 1 つ以上の新しい値を含むスライスを返します。
	// `append` からの返り値を受け取る必要があることに注意してください。
	// 新しいスライス値が返される場合があるためです。
	s = append(s, "d")
	s = append(s, "e", "f")
	fmt.Println("apd:", s)

	// スライスも `copy` することができます。ここでは、
	// 長さが `s` と同じ空のスライス `c` を作成し、
	// `s` から `c` にコピーします。
	c := make([]string, len(s))
	copy(c, s)
	fmt.Println("cpy:", c)

	// スライスは、構文 `slice[low:high]` の "スライス" 演算子をサポートします。
	// たとえば、これは要素 `s[2]`、`s[3]`、および `s[4]` のスライスを取得します。
	l := s[2:5]
	fmt.Println("sl1:", l)

	// これは `s[5]` まで（ただし含まない）をスライスします。
	l = s[:5]
	fmt.Println("sl2:", l)

	// そして、これは `s[2]` 以降（そして含む）をスライスします。
	l = s[2:]
	fmt.Println("sl3:", l)

	// スライス用の変数を 1 行で宣言および初期化することもできます。
	t := []string{"g", "h", "i"}
	fmt.Println("dcl:", t)

	// スライスを使用して多次元データ構造を構築できます。
	// 多次元配列とは異なり、内部のスライスの長さは変化させることができます。
	twoD := make([][]int, 3)
	for i := 0; i < 3; i++ {
		innerLen := i + 1
		twoD[i] = make([]int, innerLen)
		for j := 0; j < innerLen; j++ {
			twoD[i][j] = i + j
		}
	}
	fmt.Println("2d: ", twoD)
}

```
