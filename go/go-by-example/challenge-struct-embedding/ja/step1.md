# 構造体の埋め込み

`base` という名前の構造体を埋め込む `container` という名前の構造体を作成します。`base` 構造体は、型 `int` の `num` という名前のフィールドと、文字列を返す `describe()` という名前のメソッドを持つ必要があります。`container` 構造体は、型 `string` の `str` という名前のフィールドを持つ必要があります。`container` 構造体は、`base` 構造体の `num` フィールドと `describe()` メソッドにアクセスできる必要があります。

## 要件

- `base` 構造体は、型 `int` の `num` という名前のフィールドを持つ必要があります。
- `base` 構造体は、文字列を返す `describe()` という名前のメソッドを持つ必要があります。
- `container` 構造体は、型 `string` の `str` という名前のフィールドを持つ必要があります。
- `container` 構造体は、`base` 構造体を埋め込む必要があります。
- `container` 構造体は、`base` 構造体の `num` フィールドと `describe()` メソッドにアクセスできる必要があります。

## 例

```sh
$ go run struct-embedding.go
co={num: 1, str: some name}
also num: 1
describe: base with num=1
describer: base with num=1
```
