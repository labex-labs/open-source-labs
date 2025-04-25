# goroutine

この実験で解くべき問題は、関数を並列実行するための goroutine を作成して実行することです。

- `f`関数は、入力文字列とカウンタ変数を 3 回出力する必要があります。
- `main`関数は、`f`関数を同期的に呼び出し、「direct」とカウンタ変数を 3 回出力する必要があります。
- `main`関数は、goroutine を使用して`f`関数を非同期的に呼び出し、「goroutine」とカウンタ変数を 3 回出力する必要があります。
- `main`関数は、メッセージを出力する匿名関数を実行する goroutine を起動する必要があります。
- `main`関数は、「done」を出力する前に、goroutine が実行を終了するのを待つ必要があります。

```sh
# このプログラムを実行すると、ブロッキング呼び出しの出力が最初に表示され、その後 2 つの goroutine の出力が表示されます。goroutine の出力は、Go 実行時に並列実行されているため、入れ子になっている場合があります。

# 次に、並列 Go プログラムにおける goroutine の補完機能であるチャネルを見てみましょう。
```

以下に完全なコードがあります。

```go
// _goroutine_は、軽量の実行スレッドです。

package main

import (
	"fmt"
	"time"
)

func f(from string) {
	for i := 0; i < 3; i++ {
		fmt.Println(from, ":", i)
	}
}

func main() {

	// 関数呼び出し `f(s)` があるとしましょう。通常の方法でそれを呼び出し、同期的に実行するには、次のようになります。
	f("direct")

	// goroutine でこの関数を呼び出すには、`go f(s)`を使用します。この新しい goroutine は、呼び出し元の goroutine と並列に実行されます。
	go f("goroutine")

	// 匿名関数呼び出しのための goroutine も起動できます。
	go func(msg string) {
		fmt.Println(msg)
	}("going")

	// これら 2 つの関数呼び出しは、現在別々の goroutine で非同期に実行されています。完了するのを待ちます（より堅牢なアプローチとして、[WaitGroup](waitgroups) を使用します）。
	time.Sleep(time.Second)
	fmt.Println("done")
}

```
