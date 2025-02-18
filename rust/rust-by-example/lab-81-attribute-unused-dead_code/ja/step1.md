# `dead_code`

コンパイラは、未使用の関数について警告する `dead_code` リント（静的解析警告）を提供しています。属性（_attribute_）を使用すると、このリントを無効にすることができます。

```rust
fn used_function() {}

// `#[allow(dead_code)]` は `dead_code` リントを無効にする属性です
#[allow(dead_code)]
fn unused_function() {}

fn noisy_unused_function() {}
// FIXME ^ 警告を抑制する属性を追加してください

fn main() {
    used_function();
}
```

実際のプログラムでは、未使用のコード（デッドコード）を削除する必要があります。これらの例では、例の対話的な性質上、一部の場所でデッドコードを許可しています。
