# if-else

整数を入力として受け取り、文字列を返す`checkNumber`関数を完成させる必要があります。数が偶数の場合は「even」を返し、そうでない場合は「odd」を返します。

- 関数名は`checkNumber`でなければなりません。
- 関数は整数を入力として受け取る必要があります。
- 関数は文字列を返す必要があります。
- 数が偶数の場合は「even」を返します。
- 数が奇数の場合は「odd」を返します。

```sh
$ go run if-else.go
7は奇数
8は4で割り切れる
9は1桁である

# Goには[三項演算子](https://en.wikipedia.org/wiki/%3F:)(ternary if)はありません。
# したがって、基本的な条件でも完全な`if`文を使用する必要があります。
```

以下に完全なコードがあります。

```go
// Goにおける`if`文と`else`文による分岐は
// 簡単です。

package main

import "fmt"

func main() {

	// 基本的な例を示します。
	if 7%2 == 0 {
		fmt.Println("7は偶数")
	} else {
		fmt.Println("7は奇数")
	}

	// `else`なしの`if`文もあります。
	if 8%4 == 0 {
		fmt.Println("8は4で割り切れる")
	}

	// 条件文の前に文を置くことができます。この文で宣言された変数は
	// 現在のブランチとその後のすべてのブランチで利用可能です。
	if num := 9; num < 0 {
		fmt.Println(num, "は負の数")
	} else if num < 10 {
		fmt.Println(num, "は1桁")
	} else {
		fmt.Println(num, "は複数桁")
	}
}

// Goでは条件の周りに丸括弧は必要ありませんが、
// 波括弧は必要です。

```
