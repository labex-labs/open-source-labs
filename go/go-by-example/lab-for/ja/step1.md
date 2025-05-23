# `for`

以下のコードには、さまざまな種類の`for`ループが含まれています。ただし、コードの一部は不完全であり、コードが正しく機能するように欠落している部分を埋める必要があります。

- Go 言語の構文に関する基本知識
- Go 言語における`for`ループの使い方に慣れていること

```sh
$ go run for.go
1
2
3
7
8
9
loop
1
3
5

# 後で、`range` 文、チャネル、その他のデータ構造を見る際に、
# 他の `for` の形式を見ます。
```

以下が完全なコードです。

```go
// `for` は Go の唯一のループ構文です。以下に、
// `for` ループのいくつかの基本的な種類を示します。

package main

import "fmt"

func main() {

	// 最も基本的な型で、単一の条件を持つものです。
	i := 1
	for i <= 3 {
		fmt.Println(i)
		i = i + 1
	}

	// 古典的な初期化/条件/繰り返し後の `for` ループです。
	for j := 7; j <= 9; j++ {
		fmt.Println(j)
	}

	// 条件がない `for` は、`break` 文でループを抜けるか、
	// 囲まれた関数から `return` するまで、繰り返し実行されます。
	for {
		fmt.Println("loop")
		break
	}

	// また、`continue` 文を使って、次のループの反復に移ることもできます。
	for n := 0; n <= 5; n++ {
		if n%2 == 0 {
			continue
		}
		fmt.Println(n)
	}
}

```
