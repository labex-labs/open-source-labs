# 変数束縛

Rust は静的型付けによって型安全性を提供します。変数束縛は宣言時に型注釈を付けることができます。ただし、ほとんどの場合、コンパイラはコンテキストから変数の型を推論することができ、注釈の負担を大幅に軽減します。

値（リテラルなど）は、`let` 束縛を使って変数に束縛することができます。

```rust
fn main() {
    let an_integer = 1u32;
    let a_boolean = true;
    let unit = ();

    // `an_integer` を `copied_integer` にコピーする
    let copied_integer = an_integer;

    println!("An integer: {:?}", copied_integer);
    println!("A boolean: {:?}", a_boolean);
    println!("Meet the unit value: {:?}", unit);

    // コンパイラは未使用の変数束縛について警告します。これらの警告は、
    // 変数名の前にアンダースコアを付けることで無効にすることができます
    let _unused_variable = 3u32;

    let noisy_unused_variable = 2u32;
    // FIXME ^ 警告を抑制するためにアンダースコアで接頭辞を付ける
    // ブラウザでは警告が表示されない場合があることに注意してください
}
```
