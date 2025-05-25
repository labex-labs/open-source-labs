# 테스트 케이스: List

요소가 각각 순차적으로 처리되어야 하는 구조체에 대해 `fmt::Display`를 구현하는 것은 까다롭습니다. 문제는 각 `write!`가 `fmt::Result`를 생성한다는 것입니다. 이를 제대로 처리하려면 _모든_ 결과를 처리해야 합니다. Rust 는 정확히 이러한 목적으로 `?` 연산자를 제공합니다.

`write!`에 `?`를 사용하는 것은 다음과 같습니다.

```rust
// Try `write!` to see if it errors. If it errors, return
// the error. Otherwise continue.
write!(f, "{}", value)?;
```

`?`를 사용할 수 있으므로, `Vec`에 대해 `fmt::Display`를 구현하는 것은 간단합니다.

```rust
use std::fmt; // `fmt` 모듈을 가져옵니다.

// `Vec` 을 포함하는 `List` 라는 구조체를 정의합니다.
struct List(Vec<i32>);

impl fmt::Display for List {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        // 튜플 인덱싱을 사용하여 값을 추출하고,
        // `vec` 에 대한 참조를 생성합니다.
        let vec = &self.0;

        write!(f, "[")?;

        // `count` 에서 반복 횟수를 열거하면서 `vec` 에서 `v` 를 반복합니다.
        for (count, v) in vec.iter().enumerate() {
            // 첫 번째 요소를 제외한 모든 요소에 쉼표를 추가합니다.
            // 오류 발생 시 `?` 연산자를 사용하여 반환합니다.
            if count != 0 { write!(f, ", ")?; }
            write!(f, "{}", v)?;
        }

        // 열린 대괄호를 닫고 fmt::Result 값을 반환합니다.
        write!(f, "]")
    }
}

fn main() {
    let v = List(vec![1, 2, 3]);
    println!("{}", v);
}
```

## 활동

벡터의 각 요소의 인덱스도 인쇄되도록 프로그램을 변경해 보세요. 새로운 출력은 다음과 같아야 합니다.

```rust
[0: 1, 1: 2, 2: 3]
```
