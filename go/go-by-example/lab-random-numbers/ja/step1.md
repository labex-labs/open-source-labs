# 乱数

指定された範囲内の乱数の整数と浮動小数点数を生成するプログラムを作成する必要があります。また、シードを変更することで、様々な数字のシーケンスを生成できるようにする必要があります。

- プログラムは`math/rand`パッケージを使用して乱数を生成する必要があります。
- プログラムは指定された範囲内の乱数の整数を生成する必要があります。
- プログラムは指定された範囲内の乱数の浮動小数点数を生成する必要があります。
- プログラムはシードを変更することで、様々な数字のシーケンスを生成できる必要があります。

```sh
# このサンプルを実行する場所によっては、
# 生成される一部の数字が異なる場合があります。
# Goのプレイグラウンドでは、`time.Now()`でシードを設定しても、
# プレイグラウンドの実装方法のため、決定論的な結果が得られます。
$ go run random-numbers.go
81,87
0.6645600532184904
7.123187485356329,8.434115364335547
0,28
5,87
5,87

# Goが提供できる他の乱数に関する参照については、
# [`math/rand`](https://pkg.go.dev/math/rand)
# パッケージのドキュメントを参照してください。
```

以下に完全なコードがあります。

```go
// Goの`math/rand`パッケージは、
// [疑似乱数](https://en.wikipedia.org/wiki/Pseudorandom_number_generator)
// の生成を提供します。

package main

import (
	"fmt"
	"math/rand"
	"time"
)

func main() {

	// たとえば、`rand.Intn`は0以上100未満の乱数の`int` nを返します。
	fmt.Print(rand.Intn(100), ",")
	fmt.Print(rand.Intn(100))
	fmt.Println()

	// `rand.Float64`は0.0以上1.0未満の`float64` `f`を返します。
	fmt.Println(rand.Float64())

	// これを使って、たとえば5.0以上10.0未満の乱数の浮動小数点数を生成できます。
	fmt.Print((rand.Float64()*5)+5, ",")
	fmt.Print((rand.Float64() * 5) + 5)
	fmt.Println()

	// デフォルトの乱数生成器は決定論的であるため、
	// デフォルトでは毎回同じ数字のシーケンスを生成します。
	// 様々なシーケンスを生成するには、変更するシードを与えます。
	// これは、秘密にする予定の乱数には安全ではありません。
	// その場合は`crypto/rand`を使用してください。
	s1 := rand.NewSource(time.Now().UnixNano())
	r1 := rand.New(s1)

	// 結果として得られる`rand.Rand`を、
	// `rand`パッケージの関数と同じように呼び出します。
	fmt.Print(r1.Intn(100), ",")
	fmt.Print(r1.Intn(100))
	fmt.Println()

	// 同じ数字でシードを設定すると、
	// 同じ乱数のシーケンスが生成されます。
	s2 := rand.NewSource(42)
	r2 := rand.New(s2)
	fmt.Print(r2.Intn(100), ",")
	fmt.Print(r2.Intn(100))
	fmt.Println()
	s3 := rand.NewSource(42)
	r3 := rand.New(s3)
	fmt.Print(r3.Intn(100), ",")
	fmt.Print(r3.Intn(100))
}

```
