# 乱数

指定された範囲内の乱数の整数と浮動小数点数を生成するプログラムを作成する必要があります。また、シードを変更することで、様々な数のシーケンスを生成できるようにする必要があります。

## 要件

- プログラムは、乱数を生成するために`math/rand`パッケージを使用する必要があります。
- プログラムは、指定された範囲内の乱数の整数を生成する必要があります。
- プログラムは、指定された範囲内の乱数の浮動小数点数を生成する必要があります。
- プログラムは、シードを変更することで、様々な数のシーケンスを生成できる必要があります。

## 例

```sh
# このサンプルを実行する場所によっては、
# 生成される一部の数が異なる場合があります。
# Go のプレイグラウンドでは、`time.Now()` でシードを設定しても、
# プレイグラウンドの実装方法のため、依然として決定的な結果が得られます。
$ go run random-numbers.go
81,87
0.6645600532184904
7.123187485356329,8.434115364335547
0,28
5,87
5,87

# Go が提供できる他の乱数に関する参照については、
# [`math/rand`](https://pkg.go.dev/math/rand)
# パッケージのドキュメントを参照してください。
```
