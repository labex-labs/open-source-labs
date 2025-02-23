# 構造体の埋め込み

`base` という名前の構造体を埋め込む `container` という名前の構造体を作成します。`base` 構造体は、型 `int` の `num` という名前のフィールドと、文字列を返す `describe()` という名前のメソッドを持つ必要があります。`container` 構造体は、型 `string` の `str` という名前のフィールドを持つ必要があります。`container` 構造体は、`base` 構造体の `num` フィールドと `describe()` メソッドにアクセスできる必要があります。

- `base` 構造体は、型 `int` の `num` という名前のフィールドを持つ必要があります。
- `base` 構造体は、文字列を返す `describe()` という名前のメソッドを持つ必要があります。
- `container` 構造体は、型 `string` の `str` という名前のフィールドを持つ必要があります。
- `container` 構造体は、`base` 構造体を埋め込む必要があります。
- `container` 構造体は、`base` 構造体の `num` フィールドと `describe()` メソッドにアクセスできる必要があります。

```sh
$ go run struct-embedding.go
co={num: 1, str: some name}
also num: 1
describe: base with num=1
describer: base with num=1
```

以下が完全なコードです：

```go
// Go言語は、型のよりシームレスな _コンポジション_ を表現するために、構造体とインターフェイスの _埋め込み_ をサポートしています。
// これは、Go 1.16以降で導入された `//go:embed` と混同しないでください。これは、アプリケーションバイナリにファイルとフォルダを埋め込むためのGoディレクティブです。

package main

import "fmt"

type base struct {
	num int
}

func (b base) describe() string {
	return fmt.Sprintf("base with num=%v", b.num)
}

// `container` は `base` を _埋め込み_ します。埋め込みは、名前のないフィールドのように見えます。
type container struct {
	base
	str string
}

func main() {

	// リテラルを使って構造体を作成する場合、埋め込みを明示的に初期化する必要があります。ここでは、埋め込まれた型がフィールド名として機能します。
	co := container{
		base: base{
			num: 1,
		},
		str: "some name",
	}

	// 直接 `co` で `base` のフィールドにアクセスできます。たとえば、`co.num` のように。
	fmt.Printf("co={num: %v, str: %v}\n", co.num, co.str)

	// あるいは、埋め込まれた型名を使って完全なパスを記述することもできます。
	fmt.Println("also num:", co.base.num)

	// `container` は `base` を埋め込んでいるため、`base` のメソッドも `container` のメソッドになります。ここでは、`base` から埋め込まれたメソッドを直接 `co` で呼び出しています。
	fmt.Println("describe:", co.describe())

	type describer interface {
		describe() string
	}

	// メソッドを持つ構造体を埋め込むことで、他の構造体にインターフェイスの実装を与えることができます。ここでは、`container` が `base` を埋め込んでいるため、`describer` インターフェイスを実装していることがわかります。
	var d describer = co
	fmt.Println("describer:", d.describe())
}

```
