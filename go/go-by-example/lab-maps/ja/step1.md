# マップ

この実験では、与えられた文字列における各単語の出現回数を格納するマップを作成する必要があります。文字列を単語に分割し、その後各単語を反復処理して、既に存在しない場合はマップに追加し、存在する場合はそのカウントをインクリメントする必要があります。

- 単語のカウントを格納するためにマップを使用する必要があります。
- 入力文字列を単語に分割する必要があります。
- 入力文字列の各単語を反復処理する必要があります。
- 既に存在しない場合は各単語をマップに追加し、存在する場合はそのカウントをインクリメントする必要があります。

```sh
# マップは `fmt.Println` で出力すると `map[k:v k:v]` の形式で表示されます。
$ go run maps.go
map: map[k1:7 k2:13]
v1: 7
v3: 0
len: 2
map: map[k1:7]
prs: false
map: map[bar:2 foo:1]
```

以下が完全なコードです：

```go
// マップは Go の組み込みの [連想データ型](https://en.wikipedia.org/wiki/Associative_array) です
// （他の言語では時々「ハッシュ」または「辞書」と呼ばれます）。

package main

import "fmt"

func main() {

	// 空のマップを作成するには、組み込みの `make` を使用します：
	// `make(map[key-type]val-type)`。
	m := make(map[string]int)

	// 通常の `name[key] = val` 構文を使用してキー/値ペアを設定します。
	m["k1"] = 7
	m["k2"] = 13

	// `fmt.Println` などを使用してマップを出力すると、そのすべてのキー/値ペアが表示されます。
	fmt.Println("map:", m)

	// `name[key]` を使用してキーの値を取得します。
	v1 := m["k1"]
	fmt.Println("v1:", v1)

	// キーが存在しない場合、値型の [ゼロ値](https://go.dev/ref/spec#The_zero_value) が返されます。
	v3 := m["k3"]
	fmt.Println("v3:", v3)

	// 組み込みの `len` をマップに対して呼び出すと、キー/値ペアの数が返されます。
	fmt.Println("len:", len(m))

	// 組み込みの `delete` は、マップからキー/値ペアを削除します。
	delete(m, "k2")
	fmt.Println("map:", m)

	// マップから値を取得する際のオプションの 2 番目の戻り値は、キーがマップに存在するかどうかを示します。これは、欠落したキーとゼロ値（たとえば `0` または `""`）を持つキーを区別するために使用できます。ここでは値自体が必要なかったので、ブランク識別子 `_` を使用して無視しました。
	_, prs := m["k2"]
	fmt.Println("prs:", prs)

	// この構文を使用すると、同じ行で新しいマップを宣言および初期化することもできます。
	n := map[string]int{"foo": 1, "bar": 2}
	fmt.Println("map:", n)
}

```
