# 오버로드 (Overload)

매크로는 다양한 조합의 인수를 허용하도록 오버로드될 수 있습니다. 이러한 측면에서 `macro_rules!`는 match 블록과 유사하게 작동할 수 있습니다.

```rust
// `test!` 는 `$left` 와 `$right` 를 비교합니다.
// 호출 방식에 따라 다르게 비교합니다.
macro_rules! test {
    // 인수는 쉼표로 구분할 필요가 없습니다.
    // 어떤 템플릿도 사용할 수 있습니다!
    ($left:expr; and $right:expr) => {
        println!("{:?} and {:?} is {:?}",
                 stringify!($left),
                 stringify!($right),
                 $left && $right)
    };
    // ^ 각 arm 은 세미콜론으로 끝나야 합니다.
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
