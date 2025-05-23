# ポインタ/参照

ポインタに関しては、構文分解と参照解除を区別する必要があります。これらは異なる概念であり、C/C++ のような言語とは異なる方法で使用されます。

- 参照解除には `*` を使用します
- 構文分解には `&`、`ref`、および `ref mut` を使用します

```rust
fn main() {
    // `i32` 型の参照を割り当てます。`&` は、割り当てられている参照があることを示しています。
    let reference = &4;

    match reference {
        // `reference` が `&val` とパターンマッチする場合、次のような比較が行われます。
        // `&i32`
        // `&val`
        // ^ 一致する `&` を削除すると、`i32` が `val` に割り当てられるはずです。
        &val => println!("構文分解を通じて値を取得しました：{:?}", val),
    }

    // `&` を回避するには、マッチングする前に参照解除します。
    match *reference {
        val => println!("参照解除を通じて値を取得しました：{:?}", val),
    }

    // 参照で始まらない場合どうなるでしょうか。`reference` は `&` でした
    // 右辺が既に参照だったためです。これは参照ではありません
    // 右辺が参照ではないためです。
    let _not_a_reference = 3;

    // Rust はまさにこの目的のために `ref` を提供しています。これは割り当てを変更して
    // 要素に対して参照が作成されるようにします。この参照が割り当てられます。
    let ref _is_a_reference = 3;

    // したがって、参照なしで 2 つの値を定義することで、
    // `ref` と `ref mut` を使用して参照を取得できます。
    let value = 5;
    let mut mut_value = 6;

    // `ref` キーワードを使用して参照を作成します。
    match value {
        ref r => println!("値への参照を取得しました：{:?}", r),
    }

    // 同様に `ref mut` を使用します。
    match mut_value {
        ref mut m => {
            // 参照を取得しました。何かを追加する前に参照解除する必要があります。
            *m += 10;
            println!("10 を追加しました。`mut_value`: {:?}", m);
        },
    }
}
```
