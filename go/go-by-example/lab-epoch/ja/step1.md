# Epoch

この実験で解くべき問題は、Unix エポック以降の秒数、ミリ秒数、またはナノ秒数を計算できる Golang プログラムを書くことです。

この実験を完了するには、Golang の基本的な理解と次の要件が必要です。

- Golang の `time` パッケージに慣れていること。
- `time` パッケージの `Unix`、`UnixMilli`、および `UnixNano` 関数の使い方を知っていること。

```sh
$ go run epoch.go
2012-10-31 16:13:58.292387 +0000 UTC
1351700038
1351700038292
1351700038292387000
2012-10-31 16:13:58 +0000 UTC
2012-10-31 16:13:58.292387 +0000 UTC

# 次に、別の時間関連のタスクである時間の解析とフォーマットについて見ていきましょう。
```

以下に完全なコードがあります。

```go
// プログラムで一般的な要件は、[Unix エポック](https://en.wikipedia.org/wiki/Unix_time) 以降の秒数、ミリ秒数、またはナノ秒数を取得することです。
// これは Go で行う方法です。

package main

import (
	"fmt"
	"time"
)

func main() {

	// `time.Now` を `Unix`、`UnixMilli` または `UnixNano` とともに使用して、
	// Unix エポック以降の経過時間をそれぞれ秒、ミリ秒、またはナノ秒で取得します。
	now := time.Now()
	fmt.Println(now)

	fmt.Println(now.Unix())
	fmt.Println(now.UnixMilli())
	fmt.Println(now.UnixNano())

	// エポック以降の整数秒またはナノ秒を対応する `time` に変換することもできます。
	fmt.Println(time.Unix(now.Unix(), 0))
	fmt.Println(time.Unix(0, now.UnixNano()))
}

```
