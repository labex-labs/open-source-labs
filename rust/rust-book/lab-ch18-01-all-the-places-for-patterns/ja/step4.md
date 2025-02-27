# while let 条件付きループ

`if let` と構造が似ていますが、`while let` 条件付きループは、パターンが引き続き一致する限り、`while` ループを実行できるようにします。リスト18-2では、`while let` ループをコード化しています。このループでは、ベクトルをスタックとして使用し、ベクトルに格納された値を押し込まれた順序とは逆の順序で表示します。

ファイル名: `src/main.rs`

```rust
let mut stack = Vec::new();

stack.push(1);
stack.push(2);
stack.push(3);

while let Some(top) = stack.pop() {
    println!("{top}");
}
```

リスト18-2: `stack.pop()` が `Some` を返す限り、`while let` ループを使用して値を表示する

この例では、`3`、`2`、そして `1` が表示されます。`pop` メソッドはベクトルから最後の要素を取り出し、`Some(value)` を返します。ベクトルが空の場合、`pop` は `None` を返します。`while` ループは、`pop` が `Some` を返す限り、そのブロック内のコードを継続して実行します。`pop` が `None` を返すと、ループは停止します。`while let` を使用することで、スタックからすべての要素を取り出すことができます。
