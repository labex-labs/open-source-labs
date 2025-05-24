# チャネルの反復処理

整数のチャネルを引数に取り、チャネルから受け取ったすべての整数の合計を返す関数を書く必要があります。

- 関数名は`sumInts`とする。
- 関数は`chan int`型の単一のパラメータを取る。
- 関数は単一の整数値を返す。
- 関数本体の中でループや再帰を使ってはいけない。
- 外部パッケージを使ってはいけない。

```sh
$ go run range-over-channels.go
one
two

# この例はまた、空でないチャネルを閉じても、残りの値を受け取ることができることを示しています。
```

以下に完全なコードがあります：

```go
// [前の](range) 例では、`for` と `range` が基本的なデータ構造の反復処理をどのように提供するかを見ました。
// この構文を使って、チャネルから受け取った値を反復処理することもできます。

package main

import "fmt"

func main() {

	// `queue` チャネルの 2 つの値を反復処理します。
	queue := make(chan string, 2)
	queue <- "one"
	queue <- "two"
	close(queue)

	// この `range` は、`queue` から受け取った各要素を反復処理します。上でチャネルを `close` したので、2 つの要素を受け取った後に反復処理は終了します。
	for elem := range queue {
		fmt.Println(elem)
	}
}

```
