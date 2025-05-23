# チャネル

このチャレンジでは、新しいチャネルを作成し、新しい goroutine から値を送信するよう求められます。その後、チャネルから値を受信して表示します。

## 要件

- 新しいチャネルを作成するには、`make(chan val-type)` 構文を使用する必要があります。
- チャネルは、それが伝える値によって型付けする必要があります。
- チャネルに値を送信するには、`channel <-` 構文を使用する必要があります。
- チャネルから値を受信するには、`<-channel` 構文を使用する必要があります。
- チャネルに値を送信するために、新しい goroutine を使用する必要があります。

## 例

```sh
# プログラムを実行すると、"ping" メッセージが
# チャネルを介して 1 つの goroutine から別の goroutine に
# 正常に渡されます。
$ go run channels.go
ping

# 既定では、送信と受信は、送信者と受信者の両方が準備できるまでブロックされます。この特性により、
# プログラムの最後で "ping" メッセージを待つことができ、
# 他の同期方法を使用する必要がありません。
```
