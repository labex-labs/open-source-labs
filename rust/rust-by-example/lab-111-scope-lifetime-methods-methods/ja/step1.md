# メソッド

メソッドは関数と同様にアノテーション付けされます。

```rust
struct Owner(i32);

impl Owner {
    // 独立した関数と同じように寿命をアノテートします。
    fn add_one<'a>(&'a mut self) { self.0 += 1; }
    fn print<'a>(&'a self) {
        println!("`print`: {}", self.0);
    }
}

fn main() {
    let mut owner = Owner(18);

    owner.add_one();
    owner.print();
}
```
