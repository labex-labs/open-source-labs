# + 構文を使った複数のトレイト境界の指定

複数のトレイト境界を指定することもできます。`notify` が `item` に対して `summarize` の他に表示形式を使用するようにしたい場合、`notify` の定義で `item` が `Display` と `Summary` の両方を実装する必要があることを指定します。これは `+` 構文を使って行うことができます。

```rust
pub fn notify(item: &(impl Summary + Display)) {
```

`+` 構文は、ジェネリック型のトレイト境界でも有効です。

```rust
pub fn notify<T: Summary + Display>(item: &T) {
```

2 つのトレイト境界が指定されると、`notify` の本体は `summarize` を呼び出し、`{}` を使って `item` をフォーマットすることができます。
