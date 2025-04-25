# ポインタ

2 つの関数`zeroval`と`zeroptr`を使って、値と比べてポインタがどのように機能するかを理解する問題です。`zeroval`は`int`型のパラメータを持っており、引数は値渡しで渡されます。`zeroval`は呼び出し元の関数にある`ival`とは別のコピーを取得します。一方、`zeroptr`は`*int`型のパラメータを持っており、`int`型のポインタを受け取ることを意味します。関数本体の`*iptr`コードは、そのポインタをそのメモリアドレスからそのアドレスにある現在の値に解引用する（dereferences）ものです。解引用されたポインタに値を代入すると、参照されたアドレスの値が変更されます。

- Go 言語の基本的な理解が必要です。
- Go 言語で関数を定義して使用する方法を知っている必要があります。
- Go 言語でポインタを使用する方法を知っている必要があります。

```sh
# `zeroval`は `main`内の`i` を変更しませんが、
# `zeroptr` はその変数のメモリアドレスを参照しているため変更します。
$ go run pointers.go
初期値: 1
zeroval: 1
zeroptr: 0
ポインタ: 0x42131100
```

以下が完全なコードです。

```go
// Go 言語は<em><a href="https://en.wikipedia.org/wiki/Pointer_(computer_programming)">ポインタ</a></em>をサポートしており、
// プログラム内の値やレコードへの参照を渡すことができます。

package main

import "fmt"

// 2 つの関数 `zeroval`と`zeroptr`を使って、値と比べてポインタがどのように機能するかを示します。`zeroval`は`int`型のパラメータを持っており、引数は値渡しで渡されます。`zeroval`は呼び出し元の関数にある`ival` とは別のコピーを取得します。
func zeroval(ival int) {
	ival = 0
}

// 一方、`zeroptr`は `*int`型のパラメータを持っており、`int`型のポインタを受け取ることを意味します。関数本体の`*iptr` コードは、そのポインタをそのメモリアドレスからそのアドレスにある現在の値に解引用する（dereferences）ものです。解引用されたポインタに値を代入すると、参照されたアドレスの値が変更されます。
func zeroptr(iptr *int) {
	*iptr = 0
}

func main() {
	i := 1
	fmt.Println("初期値：", i)

	zeroval(i)
	fmt.Println("zeroval:", i)

	// `&i`の構文は `i`のメモリアドレス、つまり`i` へのポインタを与えます。
	zeroptr(&i)
	fmt.Println("zeroptr:", i)

	// ポインタも表示できます。
	fmt.Println("ポインタ：", &i)
}

```
