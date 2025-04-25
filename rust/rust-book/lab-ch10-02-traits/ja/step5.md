# パラメータとしてのトレイト

トレイトの定義と実装方法を学んだので、トレイトを使って多くの異なる型を受け付ける関数を定義する方法を探ってみましょう。リスト 10-13 で `NewsArticle` 型と `Tweet` 型に対して実装した `Summary` トレイトを使って、`notify` 関数を定義します。この関数は、`Summary` トレイトを実装したある型の `item` パラメータに対して `summarize` メソッドを呼び出します。これを行うには、次のように `impl Trait` 構文を使います。

```rust
pub fn notify(item: &impl Summary) {
    println!("Breaking news! {}", item.summarize());
}
```

`item` パラメータの具体的な型の代わりに、`impl` キーワードとトレイト名を指定します。このパラメータは、指定されたトレイトを実装する任意の型を受け付けます。`notify` の本体では、`Summary` トレイトに属する `item` の任意のメソッド、たとえば `summarize` を呼び出すことができます。`notify` を呼び出して、`NewsArticle` または `Tweet` の任意のインスタンスを渡すことができます。`String` や `i32` などの他の型で関数を呼び出すコードはコンパイルされません。なぜなら、それらの型は `Summary` を実装していないからです。
