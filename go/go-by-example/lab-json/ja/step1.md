# JSON

Go言語でJSONデータをエンコードおよびデコードするために提供されたコードの完成が求められます。このコードには、基本データ型のエンコードとデコードの例のほか、カスタムデータ型のエンコードとデコードの例も含まれています。

- Go言語の基本的な知識
- Go言語でJSONデータをエンコードおよびデコードすることに慣れていること
- 既存のGo言語のコードを読み解く能力

```sh
$ go run json.go
true
1
2.34
"gopher"
["apple","peach","pear"]
{"apple":5,"lettuce":7}
{"Page":1,"Fruits":["apple","peach","pear"]}
{"page":1,"fruits":["apple","peach","pear"]}
map[num:6.13 strs:[a b]]
6.13
a
{1 [apple peach]}
apple
{"apple":5,"lettuce":7}


# ここではGoにおけるJSONの基本について説明しましたが、詳細については
# [JSON and Go](https://go.dev/blog/json)
# のブログ記事と[JSONパッケージのドキュメント](https://pkg.go.dev/encoding/json)
# を参照してください。

```

以下が完全なコードです。

```go
// GoはJSONエンコードとデコードに対する組み込みのサポートを提供しており、
// 組み込み型とカスタムデータ型の両方に対応しています。

package main

import (
	"encoding/json"
	"fmt"
	"os"
)

// 以下ではカスタム型のエンコードとデコードを示すために、この2つの構造体を使用します。
type response1 struct {
	Page   int
	Fruits []string
}

// JSONでエンコード/デコードされるのはエクスポートされたフィールドのみです。
// フィールドはエクスポートするために大文字で始める必要があります。
type response2 struct {
	Page   int      `json:"page"`
	Fruits []string `json:"fruits"`
}

func main() {

	// まずは基本データ型をJSON文字列にエンコードする方法を見てみましょう。
	// ここには原子値のいくつかの例があります。
	bolB, _ := json.Marshal(true)
	fmt.Println(string(bolB))

	intB, _ := json.Marshal(1)
	fmt.Println(string(intB))

	fltB, _ := json.Marshal(2.34)
	fmt.Println(string(fltB))

	strB, _ := json.Marshal("gopher")
	fmt.Println(string(strB))

	// 以下はスライスとマップの例で、期待通りJSON配列とオブジェクトにエンコードされます。
	slcD := []string{"apple", "peach", "pear"}
	slcB, _ := json.Marshal(slcD)
	fmt.Println(string(slcB))

	mapD := map[string]int{"apple": 5, "lettuce": 7}
	mapB, _ := json.Marshal(mapD)
	fmt.Println(string(mapB))

	// JSONパッケージはカスタムデータ型を自動的にエンコードできます。
	// エンコードされた出力にはエクスポートされたフィールドのみが含まれ、
	// デフォルトではそれらの名前がJSONキーとして使用されます。
	res1D := &response1{
		Page:   1,
		Fruits: []string{"apple", "peach", "pear"}}
	res1B, _ := json.Marshal(res1D)
	fmt.Println(string(res1B))

	// 構造体フィールド宣言にタグを使用することで、
	// エンコードされたJSONキー名をカスタマイズできます。
	// 上の`response2`の定義を見ると、そのようなタグの例がわかります。
	res2D := &response2{
		Page:   1,
		Fruits: []string{"apple", "peach", "pear"}}
	res2B, _ := json.Marshal(res2D)
	fmt.Println(string(res2B))

	// 次にJSONデータをGoの値にデコードする方法を見てみましょう。
	// ここには汎用的なデータ構造の例があります。
	byt := []byte(`{"num":6.13,"strs":["a","b"]}`)

	// JSONパッケージがデコードされたデータを格納できる変数を用意する必要があります。
	// この`map[string]interface{}`は、文字列から任意のデータ型へのマップを保持します。
	var dat map[string]interface{}

	// ここが実際のデコード処理であり、関連するエラーのチェックも行っています。
	if err := json.Unmarshal(byt, &dat); err!= nil {
		panic(err)
	}
	fmt.Println(dat)

	// デコードされたマップ内の値を使用するには、
	// それらを適切な型に変換する必要があります。
	// たとえばここでは`num`の値を期待される`float64`型に変換しています。
	num := dat["num"].(float64)
	fmt.Println(num)

	// ネストされたデータにアクセスするには、一連の変換が必要です。
	strs := dat["strs"].([]interface{})
	str1 := strs[0].(string)
	fmt.Println(str1)

	// また、JSONをカスタムデータ型にデコードすることもできます。
	// これには、プログラムに追加の型安全性を付与し、
	// デコードされたデータにアクセスする際の型アサーションの必要をなくすという利点があります。
	str := `{"page": 1, "fruits": ["apple", "peach"]}`
	res := response2{}
	json.Unmarshal([]byte(str), &res)
	fmt.Println(res)
	fmt.Println(res.Fruits[0])

	// 上の例では、常にバイトと文字列をデータと標準出力上のJSON表現の間の中間データとして使用していました。
	// また、JSONエンコードを`os.Stdout`のような`os.Writer`に直接ストリーミングしたり、
	// さらにはHTTPレスポンスボディに直接ストリーミングすることもできます。
	enc := json.NewEncoder(os.Stdout)
	d := map[string]int{"apple": 5, "lettuce": 7}
	enc.Encode(d)
}

```
