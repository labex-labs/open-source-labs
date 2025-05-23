# 構造体

このチャレンジでは、与えられた名前で新しい人間の構造体を構築する `newPerson` 関数を完成させる必要があります。`person` 構造体型には `name` と `age` のフィールドがあります。

## 要件

- `person` 構造体型には `name` と `age` のフィールドが必要です。
- `newPerson` 関数は、与えられた名前で新しい人間の構造体を構築する必要があります。
- `newPerson` 関数は、新しく作成された人間の構造体へのポインタを返す必要があります。
- `main` 関数は、以下を出力する必要があります。
  - 名前が "Bob" で年齢が 20 の新しい構造体。
  - 名前が "Alice" で年齢が 30 の新しい構造体。
  - 名前が "Fred" で年齢が 0 の新しい構造体。
  - 名前が "Ann" で年齢が 40 の新しい構造体へのポインタ。
  - `newPerson` 関数を使用して構築された名前が "Jon" で年齢が 42 の新しい構造体。
  - 名前が "Sean" で年齢が 50 の構造体の `name` フィールド。
  - 名前が "Sean" で年齢が 50 の構造体への構造体ポインタの `age` フィールド。
  - 年齢フィールドが 51 に更新された後の、名前が "Sean" で年齢が 50 の構造体への構造体ポインタの `age` フィールド。

## 例

```sh
$ go run structs.go
{Bob 20}
{Alice 30}
{Fred 0}
&{Ann 40}
&{Jon 42}
Sean
50
51
```
