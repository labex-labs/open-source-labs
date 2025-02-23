# テストとベンチマーク

このチャレンジで解くべき問題は、`IntMin`という名前の整数の最小値関数の単純な実装をテストし、ベンチマークを行うことです。

## 要件

- `testing`パッケージをインポートする必要があります。
- `IntMin`関数は2つの整数型のパラメータを取り、整数型を返す必要があります。
- `TestIntMinBasic`関数は、基本的な入力値に対して`IntMin`関数をテストする必要があります。
- `TestIntMinTableDriven`関数は、テーブル駆動スタイルを使って`IntMin`関数をテストする必要があります。
- `BenchmarkIntMin`関数は、`IntMin`関数のベンチマークを行う必要があります。

## 例

```sh
# 現在のプロジェクト内のすべてのテストを詳細モードで実行します。
$ go test -v
== RUN   TestIntMinBasic
--- PASS: TestIntMinBasic (0.00s)
=== RUN   TestIntMinTableDriven
=== RUN   TestIntMinTableDriven/0,1
=== RUN   TestIntMinTableDriven/1,0
=== RUN   TestIntMinTableDriven/2,-2
=== RUN   TestIntMinTableDriven/0,-1
=== RUN   TestIntMinTableDriven/-1,0
--- PASS: TestIntMinTableDriven (0.00s)
    --- PASS: TestIntMinTableDriven/0,1 (0.00s)
    --- PASS: TestIntMinTableDriven/1,0 (0.00s)
    --- PASS: TestIntMinTableDriven/2,-2 (0.00s)
    --- PASS: TestIntMinTableDriven/0,-1 (0.00s)
    --- PASS: TestIntMinTableDriven/-1,0 (0.00s)
PASS
ok  	examples/testing-and-benchmarking	0.023s

# 現在のプロジェクト内のすべてのベンチマークを実行します。すべてのテストは、
# ベンチマークの前に実行されます。`bench`フラグは、正規表現でベンチマーク関数名を
# フィルタリングします。
$ go test -bench=.
goos: darwin
goarch: arm64
pkg: examples/testing
BenchmarkIntMin-8 1000000000 0.3136 ns/op
PASS
ok  	examples/testing-and-benchmarking	0.351s

```
