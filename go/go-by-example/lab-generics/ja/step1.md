# ジェネリクス

この実験で解決しようとする問題は、Go言語でジェネリック関数と型をどのように定義して使用するかを理解することです。

- Go言語におけるジェネリクスの概念を理解する。
- 型パラメータと制約を持つジェネリック関数を定義する方法を知る。
- 型パラメータを持つジェネリック型を定義する方法を知る。
- ジェネリック型にメソッドを定義する方法を理解する。
- 型推論を使ってジェネリック関数を呼び出す方法を知る。

```sh
$ go run generics.go
keys: [4 1 2]
list: [10 13 23]
```

以下が完全なコードです：

```go
// 1.18バージョンから、Goは _ジェネリクス_、すなわち _型パラメータ_ のサポートを追加しました。

package main

import "fmt"

// ジェネリック関数の例として、`MapKeys` は任意の型のマップを取り、そのキーのスライスを返します。
// この関数には2つの型パラメータ - `K` と `V` があります。
// `K` は `comparable` 制約を持ち、この型の値を `==` と `!=` 演算子で比較できることを意味します。
// これはGoのマップのキーに必要です。
// `V` は `any` 制約を持ち、何ら制限されないことを意味します（`any` は `interface{}` のエイリアスです）。
func MapKeys[K comparable, V any](m map[K]V) []K {
	r := make([]K, 0, len(m))
	for k := range m {
		r = append(r, k)
	}
	return r
}

// ジェネリック型の例として、`List` は任意の型の値を持つ単方向リンクリストです。
type List[T any] struct {
	head, tail *element[T]
}

type element[T any] struct {
	next *element[T]
	val  T
}

// 通常の型と同じように、ジェネリック型にメソッドを定義することができますが、型パラメータをそのままに保たなければなりません。
// 型は `List[T]` で、`List` ではありません。
func (lst *List[T]) Push(v T) {
	if lst.tail == nil {
		lst.head = &element[T]{val: v}
		lst.tail = lst.head
	} else {
		lst.tail.next = &element[T]{val: v}
		lst.tail = lst.tail.next
	}
}

func (lst *List[T]) GetAll() []T {
	var elems []T
	for e := lst.head; e!= nil; e = e.next {
		elems = append(elems, e.val)
	}
	return elems
}

func main() {
	var m = map[int]string{1: "2", 2: "4", 4: "8"}

	// ジェネリック関数を呼び出すとき、多くの場合 _型推論_ に依存できます。
	// 注意：`MapKeys` を呼び出すとき、`K` と `V` の型を明示的に指定する必要はありません。
	// コンパイラが自動的に型を推論します。
	fmt.Println("keys:", MapKeys(m))

	//... ただし、明示的に指定することもできます。
	_ = MapKeys[int, string](m)

	lst := List[int]{}
	lst.Push(10)
	lst.Push(13)
	lst.Push(23)
	fmt.Println("list:", lst.GetAll())
}

```
