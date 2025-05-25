# 여러 바운드

하나의 타입에 여러 바운드를 적용하려면 `+` 연산자를 사용합니다. 일반적인 방식과 마찬가지로, 서로 다른 타입은 `,`로 구분됩니다.

```rust
use std::fmt::{Debug, Display};

fn compare_prints<T: Debug + Display>(t: &T) {
    println!("Debug: `{:?}`", t);
    println!("Display: `{}`", t);
}

fn compare_types<T: Debug, U: Debug>(t: &T, u: &U) {
    println!("t: `{:?}`", t);
    println!("u: `{:?}`", u);
}

fn main() {
    let string = "words";
    let array = [1, 2, 3];
    let vec = vec![1, 2, 3];

    compare_prints(&string);
    //compare_prints(&array);
    // TODO ^ 이 부분을 주석 해제해 보세요.

    compare_types(&array, &vec);
}
```
