# クロージャ

あなたは、もう一つの関数を返す関数を作成する必要があります。返される関数は、呼び出されるたびに変数を 1 増やすようにする必要があります。この変数は、返される各関数に固有でなければなりません。

## 要件

- 関数 `intSeq` は、もう一つの関数を返す必要があります。
- 返される関数は、呼び出されるたびに変数を 1 増やす必要があります。
- この変数は、返される各関数に固有でなければなりません。

## 例

```sh
$ go run closures.go
1
2
3
1

# 今見ている関数の最後の機能は
# 再帰です。
```
