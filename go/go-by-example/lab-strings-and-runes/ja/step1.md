# 文字列とルーン

この実験で解決する問題は、Go言語で文字列とルーンを扱う方法を理解することです。具体的には、文字列の長さを取得する方法、文字列のインデックスにアクセスする方法、文字列内のルーンの数をカウントする方法、および文字列内のルーンを反復処理する方法をカバーします。

この実験を完了するには、以下が必要です。

- Go言語の構文の基本的な理解
- Go言語の文字列とルーンの知識
- Go言語の標準ライブラリ

```sh
$ go run strings-and-runes.go
Len: 18
e0 b8 aa e0 b8 a7 e0 b8 b1 e0 b8 aa e0 b8 94 e0 b8 b5
Rune count: 6
U+0E2A 'ส' starts at 0
U+0E27 'ว' starts at 3
U+0E31 'ั' starts at 6
U+0E2A 'ส' starts at 9
U+0E14 'ด' starts at 12
U+0E35 'ี' starts at 15

Using DecodeRuneInString
U+0E2A 'ส' starts at 0
found so sua
U+0E27 'ว' starts at 3
U+0E31 'ั' starts at 6
U+0E2A 'ส' starts at 9
found so sua
U+0E14 'ด' starts at 12
U+0E35 'ี' starts at 15
```

以下に完全なコードがあります。

```go
// Go言語の文字列は、バイトの読み取り専用スライスです。この言語と
// 標準ライブラリは、文字列に特別な扱いを行います。
// [UTF-8](https://en.wikipedia.org/wiki/UTF-8)でエンコードされた
// テキストのコンテナとしてです。
// 他の言語では、文字列は「文字」で構成されています。
// Go言語では、文字の概念は`rune`と呼ばれます。これは、
// Unicodeコードポイントを表す整数です。
// [このGo言語のブログ記事](https://go.dev/blog/strings)は、
// このトピックの良い紹介になっています。

package main

import (
	"fmt"
	"unicode/utf8"
)

func main() {

	// `s`は、タイ語の「こんにちは」を表すリテラル値が割り当てられた
	// `string`です。Go言語の文字列リテラルはUTF-8でエンコードされた
	// テキストです。
	const s = "สวัสดี"

	// 文字列は`[]byte`に等しいため、これは格納されている生のバイトの
	// 長さを生成します。
	fmt.Println("Len:", len(s))

	// 文字列にインデックスを付けると、各インデックスにある生のバイト値が
	// 生成されます。このループは、`s`のコードポイントを構成するすべての
	// バイトの16進数値を生成します。
	for i := 0; i < len(s); i++ {
		fmt.Printf("%x ", s[i])
	}
	fmt.Println()

	// 文字列内のルーンの数をカウントするには、`utf8`パッケージを使用できます。
	// ただし、`RuneCountInString`の実行時間は文字列のサイズに依存します。
	// なぜなら、各UTF-8ルーンを順次デコードする必要があるからです。
	// 一部のタイ文字は複数のUTF-8コードポイントで表されるため、
	// このカウントの結果は予想外になる場合があります。
	fmt.Println("Rune count:", utf8.RuneCountInString(s))

	// `range`ループは、文字列を特別に扱い、各`rune`とその文字列内の
	// オフセットをデコードします。
	for idx, runeValue := range s {
		fmt.Printf("%#U starts at %d\n", runeValue, idx)
	}

	// 明示的に`utf8.DecodeRuneInString`関数を使用することで、
	// 同じ反復処理を達成できます。
	fmt.Println("\nUsing DecodeRuneInString")
	for i, w := 0, 0; i < len(s); i += w {
		runeValue, width := utf8.DecodeRuneInString(s[i:])
		fmt.Printf("%#U starts at %d\n", runeValue, i)
		w = width

		// これは、`rune`値を関数に渡すことを示しています。
		examineRune(runeValue)
	}
}

func examineRune(r rune) {

	// シングルクォートで囲まれた値は、「ルーンリテラル」です。
	// 直接、`rune`値とルーンリテラルを比較できます。
	if r == 't' {
		fmt.Println("found tee")
	} else if r == 'ส' {
		fmt.Println("found so sua")
	}
}

```
