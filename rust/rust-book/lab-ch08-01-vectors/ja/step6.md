# 複数の型を格納するための列挙型の使用

ベクトルは同じ型の値のみを格納できます。これは不便な場合があります。異なる型の項目のリストを格納する必要があるケースは確かにあります。幸いなことに、列挙型のバリアントは同じ列挙型の下で定義されているため、異なる型の要素を表すために 1 つの型が必要な場合、列挙型を定義して使用することができます！

たとえば、スプレッドシートの行から値を取得したいとしましょう。その行の一部の列には整数が含まれ、一部には浮動小数点数が含まれ、一部には文字列が含まれています。列挙型のバリアントが異なる値型を保持する列挙型を定義することができ、すべての列挙型のバリアントは同じ型（列挙型の型）と見なされます。そして、その列挙型を保持するベクトルを作成することができ、最終的には異なる型を保持することができます。これをリスト 8-9 で示しています。

```rust
enum SpreadsheetCell {
    Int(i32),
    Float(f64),
    Text(String),
}

let row = vec![
    SpreadsheetCell::Int(3),
    SpreadsheetCell::Text(String::from("blue")),
    SpreadsheetCell::Float(10.12),
];
```

リスト 8-9:1 つのベクトルに異なる型の値を格納するための`enum`を定義する

Rust はコンパイル時にベクトルにどの型が含まれるかを知る必要があります。そうすることで、各要素を格納するためにヒープ上にどれだけのメモリが必要かを正確に把握できます。また、このベクトルに許可される型も明示する必要があります。Rust がベクトルに任意の型を保持できるようにした場合、ベクトルの要素に対して行われる操作で 1 つ以上の型がエラーを引き起こす可能性があります。列挙型と`match`式を使うことで、Rust はコンパイル時にすべての可能なケースが処理されることを保証します。これについては、第 6 章で説明しています。

実行時にベクトルに格納するための型の網羅的なセットを知らない場合、列挙型の手法は機能しません。代わりに、トレイトオブジェクトを使用することができます。これについては、第 17 章で説明します。

ここで、ベクトルを使用する最も一般的な方法のいくつかについて説明しましたが、標準ライブラリによって`Vec<T>`に定義されている多くの便利なメソッドの API ドキュメントを必ず確認してください。たとえば、`push`に加えて、`pop`メソッドは最後の要素を削除して返します。
