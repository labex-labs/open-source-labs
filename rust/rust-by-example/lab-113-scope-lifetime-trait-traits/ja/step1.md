# トレイト

トレイトメソッドにおける寿命注釈は基本的に関数と同じです。`impl` にも寿命注釈があることに注意してください。

```rust
// 寿命注釈のある構造体。
#[derive(Debug)]
struct Borrowed<'a> {
    x: &'a i32,
}

// impl に寿命を注釈付けする。
impl<'a> Default for Borrowed<'a> {
    fn default() -> Self {
        Self {
            x: &10,
        }
    }
}

fn main() {
    let b: Borrowed = Default::default();
    println!("b is {:?}", b);
}
```
