# 方法

方法的注释方式与函数类似：

```rust
struct Owner(i32);

impl Owner {
    // 像在独立函数中一样注释生命周期。
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
