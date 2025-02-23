# テキスト テンプレート

このチャレンジでは、`text/template` パッケージを使って動的なコンテンツを生成する方法を示すよう求められます。

## 要件

- `text/template` パッケージを使って動的なコンテンツを生成する。
- `Parse` がエラーを返した場合にパニックになるように `template.Must` 関数を使う。
- `{{.FieldName}}` アクションを使って構造体のフィールドにアクセスする。
- `{{if..}} yes {{else..}} no {{end}}\n` アクションを使ってテンプレートの条件付き実行を行う。
- `{{range.}}{{.}} {{end}}\n` アクションを使ってスライス、配列、マップ、またはチャネルをループ処理する。

## 例

```sh
$ go run templates.go
Value: some text
Value: 5
Value: [Go Rust C++ C#]
Name: Jane Doe
Name: Mickey Mouse
yes
no
Range: Go Rust C++ C#
```
