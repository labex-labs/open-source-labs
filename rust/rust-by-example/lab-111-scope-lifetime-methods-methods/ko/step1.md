# 메서드 (Methods)

메서드는 함수와 유사하게 주석 처리됩니다.

```rust
struct Owner(i32);

impl Owner {
    // 독립 실행형 함수와 마찬가지로 생명주기 (lifetimes) 를 주석 처리합니다.
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
