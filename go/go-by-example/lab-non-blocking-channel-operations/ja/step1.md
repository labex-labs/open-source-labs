# 非ブロッキングチャネル操作

この実験で解くべき問題は、`default` 句を含む `select` 文を使用して非ブロッキングチャネル操作を実装することです。

- `default` 句を含む `select` 文を使用して、チャネル上で非ブロッキング受信を実装する。
- `default` 句を含む `select` 文を使用して、チャネル上で非ブロッキング送信を実装する。
- 複数の `case` 句と `default` 句を持つ `select` 文を使用して、マルチウェイ非ブロッキングセレクトを実装する。

```sh
$ go run non-blocking-channel-operations.go
メッセージは受信されませんでした
メッセージは送信されませんでした
活動はありません
```

以下に完全なコードがあります。

```go
// チャネル上の基本的な送信と受信はブロッキングです。
// ただし、`default` 句を持つ `select` を使用することで、
// 非ブロッキングの送信、受信、さらには非ブロッキングのマルチウェイ `select` を実装できます。

package main

import "fmt"

func main() {
	messages := make(chan string)
	signals := make(chan bool)

	// ここに非ブロッキング受信があります。`messages` 上に値がある場合、
	// `select` はその値を持つ `<-messages` の `case` を選択します。
	// そうでない場合は、すぐに `default` の `case` を選択します。
	select {
	case msg := <-messages:
		fmt.Println("受信したメッセージ", msg)
	default:
		fmt.Println("メッセージは受信されませんでした")
	}

	// 非ブロッキング送信も同様に機能します。ここでは `msg` を
	// `messages` チャネルに送信できません。なぜなら、チャネルには
	// バッファがなく、受信側もいないからです。したがって、
	// `default` の `case` が選択されます。
	msg := "hi"
	select {
	case messages <- msg:
		fmt.Println("送信したメッセージ", msg)
	default:
		fmt.Println("メッセージは送信されませんでした")
	}

	// `default` 句の上に複数の `case` を使用することで、
	// マルチウェイ非ブロッキングセレクトを実装できます。
	// ここでは、`messages` と `signals` の両方で非ブロッキング受信を試みます。
	select {
	case msg := <-messages:
		fmt.Println("受信したメッセージ", msg)
	case sig := <-signals:
		fmt.Println("受信した信号", sig)
	default:
		fmt.Println("活動はありません")
	}
}

```
