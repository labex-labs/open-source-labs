# インターフェイス

問題は、Go言語でインターフェイスを実装することです。インターフェイス内のすべてのメソッドを実装すればよいのです。ここでは、`rect`と`circle`に対して`geometry`を実装します。

- Go言語でインターフェイスを実装する。
- インターフェイス内のすべてのメソッドを実装する。
- 汎用的な`measure`関数を使って、任意の`geometry`に対して動作させる。
- `circle`と`rect`構造体のインスタンスを`measure`の引数として使う。

```sh
$ go run interfaces.go
{3 4}
12
14
{5}
78.53981633974483
31.41592653589793

# Goのインターフェイスに関する詳細を学ぶには、この
# [素晴らしいブログ記事](https://jordanorelli.tumblr.com/post/32665860244/how-to-use-interfaces-in-go) を参照してください。
```

以下が完全なコードです：

```go
// _インターフェイス_ は、メソッド
// シグネチャの名前付きコレクションです。

package main

import (
	"fmt"
	"math"
)

// ここには、幾何学的形状のための基本的なインターフェイスがあります。
type geometry interface {
	area() float64
	perim() float64
}

// 私たちの例では、このインターフェイスを
// `rect` と `circle` の型で実装します。
type rect struct {
	width, height float64
}
type circle struct {
	radius float64
}

// Go言語でインターフェイスを実装するには、
// インターフェイス内のすべてのメソッドを
// 実装するだけです。ここでは、`rect` に対して
// `geometry` を実装します。
func (r rect) area() float64 {
	return r.width * r.height
}
func (r rect) perim() float64 {
	return 2*r.width + 2*r.height
}

// `circle` に対する実装です。
func (c circle) area() float64 {
	return math.Pi * c.radius * c.radius
}
func (c circle) perim() float64 {
	return 2 * math.Pi * c.radius
}

// 変数がインターフェイス型を持っている場合、
// その名前付きインターフェイスに含まれる
// メソッドを呼び出すことができます。ここには、
// 任意の `geometry` に対して動作させるために
// これを利用した汎用的な `measure` 関数があります。
func measure(g geometry) {
	fmt.Println(g)
	fmt.Println(g.area())
	fmt.Println(g.perim())
}

func main() {
	r := rect{width: 3, height: 4}
	c := circle{radius: 5}

	// `circle` と `rect` の構造体型は両方とも
	// `geometry` インターフェイスを実装しているので、
	// これらの構造体のインスタンスを
	// `measure` の引数として使うことができます。
	measure(r)
	measure(c)
}

```
