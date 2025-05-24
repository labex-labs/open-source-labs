# 再帰

`sum`関数は整数のスライスを受け取り、そのスライス内のすべての整数の合計を返します。ただし、この関数は不完全であり、再帰を使って実装する必要があります。

- `sum`関数は再帰を使って実装する必要があります。
- この関数は整数のスライスを入力として受け取る必要があります。
- この関数はスライス内のすべての整数の合計を返す必要があります。

```sh
$ go run recursion.go
5040
13
```

以下に完全なコードがあります。

```go
// Go 言語は
// <a href="https://en.wikipedia.org/wiki/Recursion_(computer_science)"><em>再帰関数</em></a>をサポートしています。
// ここに典型的な例を示します。

package main

import "fmt"

// この `fact` 関数は、`fact(0)` のベースケースに到達するまで自分自身を呼び出します。
func fact(n int) int {
	if n == 0 {
		return 1
	}
	return n * fact(n-1)
}

func main() {
	fmt.Println(fact(7))

	// クロージャも再帰的になることができますが、これにはクロージャを定義する前に明示的に型付きの `var` で宣言する必要があります。
	var fib func(n int) int

	fib = func(n int) int {
		if n < 2 {
			return n
		}

		// `fib` が以前に `main` で宣言されていたので、Go 言語はここで `fib` を使ってどの関数を呼び出すかを知っています。
		return fib(n-1) + fib(n-2)
	}

	fmt.Println(fib(7))
}

```
