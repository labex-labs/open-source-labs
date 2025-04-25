# ワーカープール

`jobs` チャネルで作業を受け取り、対応する結果を `results` チャネルに送信するワーカープールを実装します。ワーカープールは複数の並行インスタンスを持ち、各ワーカーは 1 つの作業につき 1 秒間スリープして、高負荷なタスクをシミュレートします。

## 要件

- goroutine とチャネルを使ってワーカープールを実装します。
- ワーカープールは複数の並行インスタンスを持つ必要があります。
- 各ワーカーは 1 つの作業につき 1 秒間スリープして、高負荷なタスクをシミュレートします。
- ワーカープールは `jobs` チャネルで作業を受け取り、対応する結果を `results` チャネルに送信します。

## 例

```sh
# 実行中のプログラムでは、さまざまなワーカーによって 5 つの作業が実行されています。
# 合計で約 5 秒間の作業を行っているにもかかわらず、3 つのワーカーが並行して動作しているため、
# プログラム全体の実行時間は約 2 秒です。
$ time go run worker-pools.go
worker 1 started job 1
worker 2 started job 2
worker 3 started job 3
worker 1 finished job 1
worker 1 started job 4
worker 2 finished job 2
worker 2 started job 5
worker 3 finished job 3
worker 1 finished job 4
worker 2 finished job 5

real 0m2.358s
```
