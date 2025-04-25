# 時間

以下のコードには、Go で時間と期間を扱う方法の例が含まれています。ただし、コードの一部が欠けています。あなたのタスクは、コードを完成させて、期待通りに動作させることです。

- Go プログラミング言語の基本知識。
- Go の時間と期間のサポートに慣れていること。

```sh
$ go run time.go
2012-10-31 15:50:13.793654 +0000 UTC
2009-11-17 20:34:58.651387237 +0000 UTC
2009
November
17
20
34
58
651387237
UTC
Tuesday
true
false
false
25891h15m15.142266763s
25891.25420618521
1.5534752523711128e+06
9.320851514226677e+07
93208515142266763
2012-10-31 15:50:13.793654 +0000 UTC
2006-12-05 01:19:43.509120474 +0000 UTC

# 次に、Unix エポックに対する時間の関連する概念を見てみましょう。
```

以下が完全なコードです：

```go
// Go は時間と期間に対して広範なサポートを提供しています。
// 以下にいくつかの例を示します。

package main

import (
	"fmt"
	"time"
)

func main() {
	p := fmt.Println

	// まずは現在の時間を取得します。
	now := time.Now()
	p(now)

	// 年、月、日などを指定して `time` 構造体を作成できます。時間は常に `Location`、つまりタイムゾーンに関連付けられます。
	then := time.Date(
		2009, 11, 17, 20, 34, 58, 651387237, time.UTC)
	p(then)

	// 時間値のさまざまなコンポーネントを期待通りに抽出できます。
	p(then.Year())
	p(then.Month())
	p(then.Day())
	p(then.Hour())
	p(then.Minute())
	p(then.Second())
	p(then.Nanosecond())
	p(then.Location())

	// 月曜日から日曜日までの `Weekday` も利用できます。
	p(then.Weekday())

	// これらのメソッドは 2 つの時間を比較し、最初の時間が 2 番目の時間より前、後、または同時に発生するかどうかをそれぞれテストします。
	p(then.Before(now))
	p(then.After(now))
	p(then.Equal(now))

	// `Sub` メソッドは、2 つの時間の間隔を表す `Duration` を返します。
	diff := now.Sub(then)
	p(diff)

	// 期間の長さをさまざまな単位で計算できます。
	p(diff.Hours())
	p(diff.Minutes())
	p(diff.Seconds())
	p(diff.Nanoseconds())

	// `Add` を使って、与えられた期間だけ時間を進めることができます。または `-` を使って、期間だけ後ろに移動することもできます。
	p(then.Add(diff))
	p(then.Add(-diff))
}

```
