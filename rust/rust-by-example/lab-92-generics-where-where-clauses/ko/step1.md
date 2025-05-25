# Where 절

제약 조건은 타입의 첫 번째 언급 대신 `{` 열기 전에 바로 `where` 절을 사용하여 표현할 수 있습니다. 또한 `where` 절은 타입 매개변수뿐만 아니라 임의의 타입에 제약 조건을 적용할 수 있습니다.

`where` 절이 유용한 경우:

- 제네릭 타입과 제약 조건을 별도로 명시하여 더 명확하게 표현할 때:

```rust
impl <A: TraitB + TraitC, D: TraitE + TraitF> MyTrait<A, D> for YourType {}

// where 절을 사용하여 제약 조건 표현
impl <A, D> MyTrait<A, D> for YourType where
    A: TraitB + TraitC,
    D: TraitE + TraitF {}
```

- `where` 절을 사용하는 것이 일반적인 구문보다 더 표현력이 풍부할 때. 이 예제의 `impl`은 `where` 절 없이 직접 표현할 수 없습니다.

```rust
use std::fmt::Debug;

trait PrintInOption {
    fn print_in_option(self);
}

// 그렇지 않으면 `T: Debug`로 표현해야 하거나
// 다른 간접적인 방법을 사용해야 하므로, 이 경우 `where` 절이 필요합니다.
impl<T> PrintInOption for T where
    Option<T>: Debug {
    // 출력되는 것이 `Option<T>: Debug`이므로 이것을 제약 조건으로 사용하고 싶습니다.
    // 그렇지 않으면 잘못된 제약 조건을 사용하는 것입니다.
    fn print_in_option(self) {
        println!("{:?}", Some(self));
    }
}

fn main() {
    let vec = vec![1, 2, 3];

    vec.print_in_option();
}
```
