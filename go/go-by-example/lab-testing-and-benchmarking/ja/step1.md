# テストとベンチマーキング

この実験で解決する問題は、`IntMin`という名前の整数の最小値関数の単純な実装をテストし、ベンチマークを測定することです。

- `testing`パッケージをインポートする必要があります。
- `IntMin`関数は2つの整数パラメータを取り、整数を返す必要があります。
- `TestIntMinBasic`関数は、基本的な入力値に対して`IntMin`関数をテストする必要があります。
- `TestIntMinTableDriven`関数は、テーブル駆動スタイルを使って`IntMin`関数をテストする必要があります。
- `BenchmarkIntMin`関数は、`IntMin`関数のベンチマークを測定する必要があります。

```sh
# 現在のプロジェクト内のすべてのテストを詳細モードで実行します。

# 現在のプロジェクト内のすべてのベンチマークを実行します。すべてのテストは、
# ベンチマークの前に実行されます。`bench`フラグは、正規表現でベンチマーク関数名を
# フィルタリングします。
```

以下が完全なコードです：

```go
// 原則正しいGoプログラムを書く際の重要な部分であるユニットテスト。`testing`パッケージは、
// ユニットテストを書くために必要なツールを提供し、`go test`コマンドはテストを実行します。

// 示すために、このコードは`main`パッケージにありますが、任意のパッケージでもかまいません。
// テストコードは通常、テスト対象のコードと同じパッケージにあります。
package main

import (
	"fmt"
	"testing"
)

// この整数の最小値の単純な実装をテストします。通常、テスト対象のコードは
// `intutils.go`のような名前のソースファイルにあり、そのテストファイルは
// `intutils_test.go`と名付けられます。
func IntMin(a, b int) int {
	if a < b {
		return a
	}
	return b
}

// 名前が`Test`で始まる関数を書くことでテストを作成します。
func TestIntMinBasic(t *testing.T) {
	ans := IntMin(2, -2)
	if ans!= -2 {
		// `t.Error*`はテストの失敗を報告しますが、テストの実行を続行します。
		// `t.Fatal*`はテストの失敗を報告し、テストを即座に停止します。
		t.Errorf("IntMin(2, -2) = %d; want -2", ans)
	}
}

// テストを書くことは反復的な場合があるため、慣例的に*テーブル駆動スタイル*を使います。
// ここでは、テスト入力と期待される出力をテーブルに列挙し、単一のループがそれらを
// 走査してテストロジックを実行します。
func TestIntMinTableDriven(t *testing.T) {
	var tests = []struct {
		a, b int
		want int
	}{
		{0, 1, 0},
		{1, 0, 0},
		{2, -2, -2},
		{0, -1, -1},
		{-1, 0, -1},
	}

	for _, tt := range tests {
		// t.Runは、各テーブルエントリに対して1つの「サブテスト」を実行します。
		// `go test -v`を実行すると、これらは個別に表示されます。
		testname := fmt.Sprintf("%d,%d", tt.a, tt.b)
		t.Run(testname, func(t *testing.T) {
			ans := IntMin(tt.a, tt.b)
			if ans!= tt.want {
				t.Errorf("got %d, want %d", ans, tt.want)
			}
		})
	}
}

// ベンチマークテストは通常、`_test.go`ファイルに記述され、`Benchmark`で始まる名前を持ちます。
// `testing`ランナーは、各ベンチマーク関数を何度も実行し、各実行で`b.N`を増やして
// 精密な測定値を収集します。
func BenchmarkIntMin(b *testing.B) {
	// 通常、ベンチマークは、ベンチマーク対象の関数を`b.N`回ループで実行します。
	for i := 0; i < b.N; i++ {
		IntMin(1, 2)
	}
}

```
