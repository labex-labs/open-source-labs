# プレイグラウンド

[Rust Playground](https://play.rust-lang.org/) は、Web インターフェイスを通じて Rust コードを試すための方法です。

## `mdbook` との併用

`mdbook` では、コード例を実行可能かつ編集可能にすることができます。

```rust
fn main() {
    println!("Hello World!");
}
```

これにより、読者はコードサンプルを実行するだけでなく、変更して調整することもできます。ここでのキーは、コードフェンスブロックに `editable` という単語をカンマで区切って追加することです。

````markdown
```rust
//...place your code here
```
````

また、`mdbook` がビルドおよびテスト時にコードをスキップする場合は、`ignore` を追加できます。

````markdown
```rust
//...place your code here
```
````

## ドキュメントとの併用

公式の Rust ドキュメントの一部では、「実行」と表示されるボタンがあることに気付いたかもしれません。このボタンを押すと、Rust Playground の新しいタブでコードサンプルが開きます。この機能は、`html_playground_url` と呼ばれる #\[doc\] 属性を使用することで有効になります。
