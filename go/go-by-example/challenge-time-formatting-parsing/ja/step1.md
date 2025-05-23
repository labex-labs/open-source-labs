# 日付と時刻のフォーマットと解析

この課題では、提供されたレイアウトを使用して Go 言語で日付と時刻をフォーマットし、解析することが求められます。

## 要件

- `time` パッケージを使用して日付と時刻をフォーマットし、解析します。
- `time.RFC3339` レイアウトを使用して日付と時刻をフォーマットし、解析します。
- `Mon Jan 2 15:04:05 MST 2006` の参照日付を使用して、与えられた日付/文字列のフォーマット/解析に使用するパターンを示します。
- `Parse` 関数を使用して日付と時刻を解析します。
- `Format` 関数を使用して日付と時刻をフォーマットします。
- `fmt.Println` 関数を使用してフォーマットされた日付と時刻を出力します。
- `fmt.Printf` 関数を使用して抽出されたコンポーネント付きのフォーマットされた日付と時刻を出力します。

## 例

```sh
$ go run time-formatting-parsing.go
2014-04-15T18:00:15-07:00
2012-11-01 22:08:41 +0000 +0000
6:00PM
Tue Apr 15 18:00:15 2014
2014-04-15T18:00:15.161182-07:00
0000-01-01 20:41:00 +0000 UTC
2014-04-15T18:00:15-00:00
parsing time "8:41PM" as "Mon Jan _2 15:04:05 2006":...
```
