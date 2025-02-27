# パラメータとしての文字列スライス

リテラルと`String`値のスライスを取得できることがわかったので、`first_word`に対するさらなる改善点があります。それは、そのシグネチャです。

```rust
fn first_word(s: &String) -> &str {
```

もっと経験豊富なRustプログラマは、代わりにリスト4-9に示すシグネチャを書くでしょう。なぜなら、これにより、`&String`値と`&str`値の両方で同じ関数を使用できるようになるからです。

```rust
fn first_word(s: &str) -> &str {
```

リスト4-9: `s`パラメータの型として文字列スライスを使用することで`first_word`関数を改善する

文字列スライスがあれば、それを直接渡すことができます。`String`があれば、`String`のスライスまたは`String`への参照を渡すことができます。この柔軟性は、「関数とメソッドによる暗黙的な参照強制」で説明する機能である参照強制を利用しています。

`String`への参照ではなく文字列スライスを受け取るように関数を定義することで、APIをより汎用的で便利にすることができます。機能を失うことなくです。

ファイル名: `src/main.rs`

```rust
fn main() {
    let my_string = String::from("hello world");

    // `first_word`は、部分的または全体的な`String`のスライスに対して機能します
    let word = first_word(&my_string[0..6]);
    let word = first_word(&my_string[..]);
    // `first_word`は、`String`への参照にも機能します。これは、`String`の全体のスライスと同等です
    let word = first_word(&my_string);

    let my_string_literal = "hello world";

    // `first_word`は、部分的または全体的な文字列リテラルのスライスに対して機能します
    let word = first_word(&my_string_literal[0..6]);
    let word = first_word(&my_string_literal[..]);

    // 文字列リテラルはすでに文字列スライスなので、スライス構文なしでもこれが機能します！
    let word = first_word(my_string_literal);
}
```
