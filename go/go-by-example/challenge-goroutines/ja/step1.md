# Goroutine

このチャレンジで解くべき問題は、関数を並列実行するためのgoroutineを作成して実行することです。

## 要件

- `f`関数は、入力文字列とカウンタ変数を3回表示する必要があります。
- `main`関数は、`f`関数を同期的に呼び出し、「direct」とカウンタ変数を3回表示する必要があります。
- `main`関数は、goroutineを使用して`f`関数を非同期的に呼び出し、「goroutine」とカウンタ変数を3回表示する必要があります。
- `main`関数は、メッセージを表示する匿名関数を実行するgoroutineを起動する必要があります。
- `main`関数は、「done」を表示する前に、goroutineが実行を終了するのを待つ必要があります。

## 例

```sh
# このプログラムを実行すると、
# ブロッキング呼び出しの出力が最初に表示され、
# その後2つのgoroutineの出力が表示されます。
# goroutineはGo実行時に並列実行されるため、
# goroutineの出力は入れ替わって表示される場合があります。
$ go run goroutines.go
direct : 0
direct : 1
direct : 2
goroutine : 0
going
goroutine : 1
goroutine : 2
done

# 次に、並列Goプログラムにおけるgoroutineの補完機能である
# チャネルについて見てみましょう。

```
