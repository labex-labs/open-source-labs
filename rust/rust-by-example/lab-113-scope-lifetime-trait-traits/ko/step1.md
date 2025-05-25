# 트레이트 (Traits)

트레이트 메서드에서 생명주기 (lifetime) 주석은 기본적으로 함수와 유사합니다. `impl` 역시 생명주기 주석을 가질 수 있다는 점에 유의하십시오.

```rust
// 생명주기 주석이 있는 구조체입니다.
#[derive(Debug)]
struct Borrowed<'a> {
    x: &'a i32,
}

// impl 에 생명주기를 주석 처리합니다.
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
