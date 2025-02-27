# 定数

Rust には、グローバルを含む任意のスコープで宣言できる 2 種類の異なる定数があります。どちらも明示的な型注釈が必要です。

- `const`：変更不可能な値（一般的なケース）。
- `static`：`'static` 寿命を持つ場合には `mut` 可能な変数。静的寿命は推論され、指定する必要はありません。可変静的変数にアクセスまたは変更することは `unsafe` です。

```rust
// グローバルは他のすべてのスコープの外で宣言されます。
static LANGUAGE: &str = "Rust";
const THRESHOLD: i32 = 10;

fn is_big(n: i32) -> bool {
    // ある関数内で定数にアクセスする
    n > THRESHOLD
}

fn main() {
    let n = 16;

    // メインスレッドで定数にアクセスする
    println!("This is {}", LANGUAGE);
    println!("The threshold is {}", THRESHOLD);
    println!("{} is {}", n, if is_big(n) { "big" } else { "small" });

    // エラー！`const` を変更することはできません。
    THRESHOLD = 5;
    // FIXME ^ この行をコメントアウトしてください
}
```
