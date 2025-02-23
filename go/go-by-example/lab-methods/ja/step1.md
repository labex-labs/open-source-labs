# メソッド

提供されたコードは、`width` と `height` の2つのフィールドを持つ `rect` と呼ばれる構造体型を定義します。この構造体型に対して、`area` と `perim` の2つのメソッドが定義されています。`area` メソッドは長方形の面積を計算し、`perim` メソッドは長方形の周りの長さを計算します。メイン関数はこれら2つのメソッドを呼び出し、その結果を出力します。

- `area` メソッドのレシーバ型は `*rect` でなければなりません。
- `perim` メソッドのレシーバ型は `rect` でなければなりません。
- `area` メソッドは長方形の面積を返す必要があります。
- `perim` メソッドは長方形の周りの長さを返す必要があります。
- `main` 関数は両方のメソッドを呼び出し、その結果を出力する必要があります。

```sh
$ go run methods.go
area: 50
perim: 30
area: 50
perim: 30

# 次に、Goの関連するメソッドのグループ化と命名のメカニズムである
# インターフェイスを見てみましょう。
```

以下が完全なコードです。

```go
// Goは構造体型に定義された _メソッド_ をサポートしています。

package main

import "fmt"

type rect struct {
	width, height int
}

// この `area` メソッドの _レシーバ型_ は `*rect` です。
func (r *rect) area() int {
	return r.width * r.height
}

// メソッドはポインタまたは値の
// レシーバ型のどちらでも定義できます。ここに値レシーバの例があります。
func (r rect) perim() int {
	return 2*r.width + 2*r.height
}

func main() {
	r := rect{width: 10, height: 5}

	// ここでは、構造体に定義された2つのメソッドを呼び出します。
	fmt.Println("area: ", r.area())
	fmt.Println("perim:", r.perim())

	// Goはメソッド呼び出し時の値とポインタの間の変換を自動的に処理します。
	// メソッド呼び出し時のコピーを避けるため、またはメソッドが受け取る構造体を変更できるようにするために、
	// ポインタレシーバ型を使用することができます。
	rp := &r
	fmt.Println("area: ", rp.area())
	fmt.Println("perim:", rp.perim())
}

```
