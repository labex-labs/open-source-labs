# オーバーロード

マクロは、さまざまな引数の組み合わせを受け付けるようにオーバーロードすることができます。その点で、`macro_rules!` は `match` ブロックと同じように機能します。

```rust
// `test!` は、呼び出し方に応じて
// `$left` と `$right` を異なる方法で比較します。
macro_rules! test {
    // 引数はコンマで区切る必要はありません。
    // 任意のテンプレートを使うことができます！
    ($left:expr; and $right:expr) => {
        println!("{:?} and {:?} is {:?}",
                 stringify!($left),
                 stringify!($right),
                 $left && $right)
    };
    // ^ 各アームはセミコロンで終わる必要があります。
    ($left:expr; or $right:expr) => {
        println!("{:?} or {:?} is {:?}",
                 stringify!($left),
                 stringify!($right),
                 $left || $right)
    };
}

fn main() {
    test!(1i32 + 1 == 2i32; and 2i32 * 2 == 4i32);
    test!(true; or false);
}
```
