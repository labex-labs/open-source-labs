# switch

この実験では、入力値に基づいて対応するメッセージを出力するように `switch` 文を完成させる必要があります。

- 問題を解くために `switch` 文を使用する必要があります。
- 予期しない入力値を処理するために `default` ケースを使用する必要があります。

```sh
$ go run switch.go
Write 2 as two
It's a weekday
It's after noon
I'm a bool
I'm an int
Don't know type string

```

以下に完全なコードがあります。

```go
// _Switch文_ は、多くのブランチに渡る条件分岐を表現します。

package main

import (
	"fmt"
	"time"
)

func main() {

	// 基本的な `switch` です。
	i := 2
	fmt.Print("Write ", i, " as ")
	switch i {
	case 1:
		fmt.Println("one")
	case 2:
		fmt.Println("two")
	case 3:
		fmt.Println("three")
	}

	// 同じ `case` 文で複数の式を区切るためにコンマを使用できます。この例では、オプションの `default` ケースも使用しています。
	switch time.Now().Weekday() {
	case time.Saturday, time.Sunday:
		fmt.Println("It's the weekend")
	default:
		fmt.Println("It's a weekday")
	}

	// 式のない `switch` は、if/else ロジックを表現する別の方法です。ここでは、`case` 式が定数でない場合も示しています。
	t := time.Now()
	switch {
	case t.Hour() < 12:
		fmt.Println("It's before noon")
	default:
		fmt.Println("It's after noon")
	}

	// 型 `switch` は値ではなく型を比較します。これを使用して、インターフェイス値の型を見つけることができます。この例では、変数 `t` はその句に対応する型を持つことになります。
	whatAmI := func(i interface{}) {
		switch t := i.(type) {
		case bool:
			fmt.Println("I'm a bool")
		case int:
			fmt.Println("I'm an int")
		default:
			fmt.Printf("Don't know type %T\n", t)
		}
	}
	whatAmI(true)
	whatAmI(1)
	whatAmI("hey")
}

```
