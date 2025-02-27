# 新しい文字列を作成する

`Vec<T>` で利用可能な多くの操作が、`String` でも利用可能です。なぜなら、`String` は実際、バイトのベクターをラップしたものとして実装されており、追加の保証、制限、機能があるからです。`Vec<T>` と `String` で同じように機能する関数の例として、インスタンスを作成する `new` 関数があります。これはリスト8-11に示されています。

```rust
let mut s = String::new();
```

リスト8-11：新しい空の `String` を作成する

この行は、新しい空の文字列 `s` を作成します。その後、この文字列にデータを読み込むことができます。多くの場合、文字列の最初のデータがあり、それを使って文字列を始めたいと思います。そのためには、文字列リテラルと同じように、`Display` トレイトを実装するすべての型で利用可能な `to_string` メソッドを使います。リスト8-12に2つの例を示します。

```rust
let data = "initial contents";

let s = data.to_string();

// このメソッドは直接のリテラルでも機能します：
let s = "initial contents".to_string();
```

リスト8-12：文字列リテラルから `String` を作成するための `to_string` メソッドの使用

このコードは、`initial contents` を含む文字列を作成します。

また、`String::from` 関数を使って、文字列リテラルから `String` を作成することもできます。リスト8-13のコードは、`to_string` を使ったリスト8-12のコードと同等です。

```rust
let s = String::from("initial contents");
```

リスト8-13：文字列リテラルから `String` を作成するための `String::from` 関数の使用

文字列はたくさんの用途に使われるため、文字列用の多くの異なるジェネリックAPIを使うことができ、多くのオプションが用意されています。それらの一部は冗長に見えるかもしれませんが、すべてにその役割があります！この場合、`String::from` と `to_string` は同じことをしますので、どちらを選ぶかは、スタイルと読みやすさの問題です。

文字列は UTF-8 エンコードされていることを忘れないでください。したがって、正しくエンコードされたデータを含めることができます。これはリスト8-14に示されています。

```rust
let hello = String::from("السلام عليكم");
let hello = String::from("Dobrý den");
let hello = String::from("Hello");
let hello = String::from("שָׁלוֹם");
let hello = String::from("नमस्ते");
let hello = String::from("こんにちは");
let hello = String::from("안녕하세요");
let hello = String::from("你好");
let hello = String::from("Olá");
let hello = String::from("Здравствуйте");
let hello = String::from("Hola");
```

リスト8-14：文字列にさまざまな言語の挨拶を格納する

これらはすべて、有効な `String` 値です。
