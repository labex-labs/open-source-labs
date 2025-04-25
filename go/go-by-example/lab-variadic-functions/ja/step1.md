# 可変長関数

この実験では、任意の数の整数を引数として受け取り、最大値を返す `max` という名前の関数を実装する必要があります。

- 関数 `max` は、任意の数の整数を引数として受け取る必要があります。
- 関数 `max` は、引数として渡された整数の最大値を返す必要があります。

```sh
$ go run variadic-functions.go
[1 2] 3
[1 2 3] 6
[1 2 3 4] 10

# Go 言語における関数のもう一つの重要な側面は、クロージャを形成する能力であり、次にこれを見ていきます。
```

以下に完全なコードがあります：

```go
// [_可変長関数_](https://en.wikipedia.org/wiki/Variadic_function)
// は、任意の数の末尾引数で呼び出すことができます。
// たとえば、`fmt.Println` は一般的な可変長関数です。

package main

import "fmt"

// ここには、任意の数の `int` を引数として受け取る関数があります。
func sum(nums...int) {
	fmt.Print(nums, " ")
	total := 0
	// 関数内では、`nums` の型は `[]int` に相当します。
	// `len(nums)` を呼び出したり、`range` で反復処理したりできます。
	for _, num := range nums {
		total += num
	}
	fmt.Println(total)
}

func main() {

	// 可変長関数は通常の方法で個々の引数で呼び出すことができます。
	sum(1, 2)
	sum(1, 2, 3)

	// すでにスライスに複数の引数がある場合、
	// このように `func(slice...)` を使って可変長関数に適用します。
	nums := []int{1, 2, 3, 4}
	sum(nums...)
}

```
