# 正規表現

このチャレンジでは、Go言語で様々な正規表現関連のタスクを実行するコードを完成させる必要があります。

## 要件

- `regexp` パッケージを使用して正規表現関連のタスクを実行します。
- `MatchString` を使用してパターンが文字列と一致するかどうかをテストします。
- `Compile` を使用して `Regexp` 構造体を最適化します。
- `MatchString` を使用して `Compile` と同じように一致をテストします。
- `FindString` を使用して正規表現の一致を見つけます。
- `FindStringIndex` を使用して最初の一致を見つけ、一致するテキストではなく一致の開始と終了インデックスを返します。
- `FindStringSubmatch` を使用して `p([a-z]+)ch` と `([a-z]+)` の両方に関する情報を返します。
- `FindStringSubmatchIndex` を使用して一致と部分一致のインデックスに関する情報を返します。
- `FindAllString` を使用して正規表現のすべての一致を見つけます。
- `FindAllStringSubmatchIndex` を使用して入力のすべての一致に適用し、最初の一致に限定しません。
- `Match` を使用して `[]byte` 引数で一致をテストし、関数名から `String` を削除します。
- `MustCompile` を使用して正規表現を持つグローバル変数を作成します。
- `ReplaceAllString` を使用して文字列を他の値で置き換える部分集合を置き換えます。
- `ReplaceAllFunc` を使用して与えられた関数で一致したテキストを変換します。

## 例

```sh
# Go正規表現の完全なリファレンスについては
# [`regexp`](https://pkg.go.dev/regexp) パッケージのドキュメントを参照してください。
```
