# 構造体

この実験では、与えられた名前で新しい人間の構造体を構築する `newPerson` 関数を完成させる必要があります。`person` 構造体型には `name` と `age` のフィールドがあります。

- `person` 構造体型には必ず `name` と `age` のフィールドがある必要があります。
- `newPerson` 関数は、与えられた名前で新しい人間の構造体を構築する必要があります。
- `newPerson` 関数は、新しく作成された人間の構造体へのポインタを返す必要があります。
- `main` 関数は、以下の内容を出力する必要があります。
  - 名前が "Bob" で年齢が20歳の新しい構造体。
  - 名前が "Alice" で年齢が30歳の新しい構造体。
  - 名前が "Fred" で年齢が0歳の新しい構造体。
  - 名前が "Ann" で年齢が40歳の新しい構造体へのポインタ。
  - `newPerson` 関数を使用して構築された名前が "Jon" で年齢が42歳の新しい構造体。
  - 名前が "Sean" で年齢が50歳の構造体の `name` フィールド。
  - 名前が "Sean" で年齢が50歳の構造体への構造体ポインタの `age` フィールド。
  - `age` フィールドが51に更新された後の、名前が "Sean" で年齢が50歳の構造体への構造体ポインタの `age` フィールド。

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

以下が完全なコードです。

```go
// Go言語の _構造体_ は、フィールドの型付きコレクションです。
// データをまとめてレコードを形成するのに役立ちます。

package main

import "fmt"

// この `person` 構造体型には `name` と `age` のフィールドがあります。
type person struct {
	name string
	age  int
}

// `newPerson` は、与えられた名前で新しい人間の構造体を構築します。
func newPerson(name string) *person {
	// ローカル変数へのポインタを安全に返すことができます。
	// ローカル変数は関数のスコープを超えて生存します。
	p := person{name: name}
	p.age = 42
	return &p
}

func main() {

	// この構文で新しい構造体を作成します。
	fmt.Println(person{"Bob", 20})

	// 構造体を初期化する際にフィールド名を指定することができます。
	fmt.Println(person{name: "Alice", age: 30})

	// 省略されたフィールドはゼロ値になります。
	fmt.Println(person{name: "Fred"})

	// `&` 接頭辞は構造体へのポインタを生成します。
	fmt.Println(&person{name: "Ann", age: 40})

	// コンストラクタ関数に新しい構造体の作成をカプセル化するのは慣例です。
	fmt.Println(newPerson("Jon"))

	// ドットを使って構造体のフィールドにアクセスします。
	s := person{name: "Sean", age: 50}
	fmt.Println(s.name)

	// 構造体ポインタでもドットを使うことができます。
	// ポインタは自動的に参照解除されます。
	sp := &s
	fmt.Println(sp.age)

	// 構造体は可変です。
	sp.age = 51
	fmt.Println(sp.age)
}

```
