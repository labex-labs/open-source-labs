# クロージャ

あなたは、もう一つの関数を返す関数を作成する必要があります。返される関数は、呼び出されるたびに変数を 1 増やす必要があります。この変数は、返される各関数に固有でなければなりません。

- 関数 `intSeq` は、もう一つの関数を返す必要があります。
- 返される関数は、呼び出されるたびに変数を 1 増やす必要があります。
- この変数は、返される各関数に固有でなければなりません。

```sh
$ go run closures.go
1
2
3
1

# 今見ている関数の最後の機能は
# 再帰です。
```

以下に完全なコードがあります：

```go
// Go 言語は [匿名関数](https://en.wikipedia.org/wiki/Anonymous_function) をサポートしており、
// これらは <a href="https://en.wikipedia.org/wiki/Closure_(computer_science)"><em>クロージャ</em></a> を形成することができます。
// 匿名関数は、関数を名前付けすることなくインラインで定義したい場合に便利です。

package main

import "fmt"

// この関数 `intSeq` は、もう一つの関数を返します。
// これは、`intSeq` の本体で匿名で定義されています。
// 返される関数は、変数 `i` を _クロージャ_ として使って
// クロージャを形成します。
func intSeq() func() int {
	i := 0
	return func() int {
		i++
		return i
	}
}

func main() {

	// 関数 `intSeq` を呼び出し、結果（関数）を
	// `nextInt` に代入します。この関数値は、
	// それ自身の `i` 値をキャプチャしており、
	// これは `nextInt` を呼び出すたびに更新されます。
	nextInt := intSeq()

	// `nextInt` を何回か呼び出すことで、
	// クロージャの効果を確認します。
	fmt.Println(nextInt())
	fmt.Println(nextInt())
	fmt.Println(nextInt())

	// その特定の関数に固有の状態であることを確認するために、
	// 新しい関数を作成してテストします。
	newInts := intSeq()
	fmt.Println(newInts())
}

```
