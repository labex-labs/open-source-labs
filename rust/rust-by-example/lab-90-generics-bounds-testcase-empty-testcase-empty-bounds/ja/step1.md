# テストケース：空の境界

境界が機能する仕組みの結果として、`trait` に機能が含まれていなくても、依然として境界として使用できます。`Eq` と `Copy` は、`std` ライブラリにあるそのような `trait` の例です。

```rust
struct Cardinal;
struct BlueJay;
struct Turkey;

trait Red {}
trait Blue {}

impl Red for Cardinal {}
impl Blue for BlueJay {}

// これらの関数は、これらの
// trait を実装する型に対してのみ有効です。trait が空であることは関係ありません。
fn red<T: Red>(_: &T)   -> &'static str { "red" }
fn blue<T: Blue>(_: &T) -> &'static str { "blue" }

fn main() {
    let cardinal = Cardinal;
    let blue_jay = BlueJay;
    let _turkey   = Turkey;

    // 境界のため、`red()` はブルージェイでは機能せず、逆も同様です。
    println!("A cardinal is {}", red(&cardinal));
    println!("A blue jay is {}", blue(&blue_jay));
    //println!("A turkey is {}", red(&_turkey));
    // ^ TODO: この行のコメントを外してみてください。
}
```
