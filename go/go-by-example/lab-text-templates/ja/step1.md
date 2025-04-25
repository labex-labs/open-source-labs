# テキストテンプレート

この実験では、動的なコンテンツを生成するために`text/template`パッケージを使用する方法を示す必要があります。

- `text/template`パッケージを使用して動的なコンテンツを生成します。
- `template.Must`関数を使用して、`Parse`がエラーを返した場合にパニックを起こします。
- `{{.FieldName}}`アクションを使用して構造体のフィールドにアクセスします。
- `{{if.. -}} yes {{else -}} no {{end}}\n`アクションを使用して、テンプレートの条件付き実行を行います。
- `{{range.}}{{.}} {{end}}\n`アクションを使用して、スライス、配列、マップ、またはチャネルをループ処理します。

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

以下が完全なコードです：

```go
// Go は、`text/template`パッケージを使って、動的なコンテンツを作成したり、ユーザーにカスタマイズされた出力を表示したりするための組み込みのサポートを提供しています。兄弟パッケージである `html/template` は同じ API を提供していますが、追加のセキュリティ機能があり、HTML を生成するために使用する必要があります。

package main

import (
	"os"
	"text/template"
)

func main() {

	// 新しいテンプレートを作成し、その本文を文字列から解析することができます。
	// テンプレートは、静的なテキストと `{{...}}` で囲まれた「アクション」の混合であり、動的にコンテンツを挿入するために使用されます。
	t1 := template.New("t1")
	t1, err := t1.Parse("Value is {{.}}\n")
	if err!= nil {
		panic(err)
	}

	// 代替として、`template.Must`関数を使用して、`Parse` がエラーを返した場合にパニックを起こすことができます。これは、グローバルスコープで初期化されたテンプレートに特に役立ちます。
	t1 = template.Must(t1.Parse("Value: {{.}}\n"))

	// テンプレートを「実行」することで、そのアクションに特定の値を与えてテキストを生成します。`{{.}}`アクションは、`Execute` に渡されるパラメータとして渡される値に置き換えられます。
	t1.Execute(os.Stdout, "some text")
	t1.Execute(os.Stdout, 5)
	t1.Execute(os.Stdout, []string{
		"Go",
		"Rust",
		"C++",
		"C#",
	})

	// 以下で使用するヘルパー関数。
	Create := func(name, t string) *template.Template {
		return template.Must(template.New(name).Parse(t))
	}

	// データが構造体の場合、`{{.FieldName}}` アクションを使用してそのフィールドにアクセスできます。テンプレートが実行されるときにアクセス可能にするためには、フィールドはエクスポートされている必要があります。
	t2 := Create("t2", "Name: {{.Name}}\n")

	t2.Execute(os.Stdout, struct {
		Name string
	}{"Jane Doe"})

	// マップの場合も同様です。マップでは、キー名のケースに制限はありません。
	t2.Execute(os.Stdout, map[string]string{
		"Name": "Mickey Mouse",
	})

	// if/elseは、テンプレートの条件付き実行を提供します。値が型のデフォルト値（たとえば0、空文字列、nilポインタなど）の場合、その値は偽と見なされます。
	// このサンプルは、テンプレートの別の機能を示しています：アクションで `-` を使用して空白をトリミングすること。
	t3 := Create("t3",
		"{{if.. -}} yes {{else -}} no {{end}}\n")
	t3.Execute(os.Stdout, "not empty")
	t3.Execute(os.Stdout, "")

	// range ブロックを使うと、スライス、配列、マップ、またはチャネルをループ処理できます。range ブロックの中では、`{{.}}` は反復の現在の項目に設定されます。
	t4 := Create("t4",
		"Range: {{range.}}{{.}} {{end}}\n")
	t4.Execute(os.Stdout,
		[]string{
			"Go",
			"Rust",
			"C++",
			"C#",
		})
}

```
