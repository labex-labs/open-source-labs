# 変数

Go 言語でさまざまな型の変数を宣言して初期化するコードを完成させる必要があります。

- Go 言語の構文に関する基本知識
- Go 言語における変数の宣言と初期化に慣れていること

```sh
$ go run variables.go
初期化
1 2
true
0
りんご
```

以下に完全なコードがあります。

```go
// Go 言語では、_変数_は明示的に宣言され、コンパイラによって関数呼び出しの型の正しさをチェックするために使用されます。

package main

import "fmt"

func main() {

	// `var` は 1 つ以上の変数を宣言します。
	var a = "初期化"
	fmt.Println(a)

	// 一度に複数の変数を宣言することができます。
	var b, c int = 1, 2
	fmt.Println(b, c)

	// Go 言語は初期化された変数の型を推論します。
	var d = true
	fmt.Println(d)

	// 対応する初期化なしで宣言された変数は_ゼロ値_になります。たとえば、`int` 型のゼロ値は `0` です。
	var e int
	fmt.Println(e)

	// `:=` 構文は変数を宣言して初期化するための省略形で、この場合、`var f string = "りんご"`と同じです。この構文は関数内でのみ使用できます。
	f := "りんご"
	fmt.Println(f)
}

```
