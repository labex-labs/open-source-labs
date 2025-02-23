# 値型

あなたの課題は、2つの整数を受け取り、それらの和と積を返す `calculate` 関数を完成させることです。

- `calculate` 関数は、2つの整数をパラメータとして受け取る必要があります。
- `calculate` 関数は、入力パラメータの和と積である2つの整数を返す必要があります。

```sh
$ go run values.go
golang
1+1 = 2
7.0/3.0 = 2.3333333333333335
false
true
false
```

以下に完全なコードがあります。

```go
// Goには、文字列、整数、浮動小数点数、ブール値など、さまざまな値型があります。
// 以下は、いくつかの基本的な例です。

package main

import "fmt"

func main() {

	// `+` で文字列を連結できます。
	fmt.Println("go" + "lang")

	// 整数と浮動小数点数。
	fmt.Println("1+1 =", 1+1)
	fmt.Println("7.0/3.0 =", 7.0/3.0)

	// ブール値は、期待通りのブール演算子があります。
	fmt.Println(true && false)
	fmt.Println(true || false)
	fmt.Println(!true)
}

```
