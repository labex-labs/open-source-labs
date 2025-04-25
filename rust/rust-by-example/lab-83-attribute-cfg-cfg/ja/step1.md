# `cfg`

構成条件付きチェックは、2 つの異なる演算子を通じて可能です。

- `cfg` 属性：属性位置に `#[cfg(...)]`
- `cfg!` マクロ：ブール式に `cfg!(...)`

前者は条件付きコンパイルを可能にする一方、後者は実行時のチェックを可能にするために、条件付きで `true` または `false` のリテラルに評価されます。両方とも同じ引数構文を使用します。

`cfg!` は `#[cfg]` とは異なり、コードを削除せず、真偽値のみを評価します。たとえば、条件に `cfg!` を使用する場合、if/else 式のすべてのブロックは、`cfg!` が評価する内容に関係なく、有効でなければなりません。

```rust
// この関数は、対象の OS が linux の場合のみコンパイルされます
#[cfg(target_os = "linux")]
fn are_you_on_linux() {
    println!("You are running linux!");
}

// この関数は、対象の OS が linux でない場合のみコンパイルされます
#[cfg(not(target_os = "linux"))]
fn are_you_on_linux() {
    println!("You are *not* running linux!");
}

fn main() {
    are_you_on_linux();

    println!("Are you sure?");
    if cfg!(target_os = "linux") {
        println!("Yes. It's definitely linux!");
    } else {
        println!("Yes. It's definitely *not* linux!");
    }
}
```
