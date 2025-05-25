# 문제점

컨테이너 유형에 대한 제네릭 `trait`에는 유형 지정 요구 사항이 있습니다. `trait` 사용자는 모든 제네릭 유형을 반드시 지정해야 합니다.

아래 예제에서 `Contains` `trait`은 제네릭 유형 `A`와 `B`를 사용할 수 있도록 허용합니다. 그런 다음 `trait`은 `Container` 유형에 대해 `A`와 `B`에 `i32`를 지정하여 `fn difference()`와 함께 사용할 수 있도록 구현됩니다.

`Contains`가 제네릭이기 때문에 `fn difference()`에 대한 모든 제네릭 유형을 명시적으로 지정해야 합니다. 실제로는 `A`와 `B`가 _입력_ `C`에 의해 결정된다는 것을 표현하는 방법이 필요합니다. 다음 섹션에서 볼 수 있듯이 연관된 유형은 정확히 이러한 기능을 제공합니다.

```rust
struct Container(i32, i32);

// 컨테이너 내에 2 개의 항목이 있는지 확인하는 trait.
// 또한 첫 번째 또는 마지막 값을 검색합니다.
trait Contains<A, B> {
    fn contains(&self, _: &A, _: &B) -> bool; // 명시적으로 `A` 와 `B` 를 요구합니다.
    fn first(&self) -> i32; // 명시적으로 `A` 또는 `B` 를 요구하지 않습니다.
    fn last(&self) -> i32;  // 명시적으로 `A` 또는 `B` 를 요구하지 않습니다.
}

impl Contains<i32, i32> for Container {
    // 저장된 숫자가 같은지 확인합니다.
    fn contains(&self, number_1: &i32, number_2: &i32) -> bool {
        (&self.0 == number_1) && (&self.1 == number_2)
    }

    // 첫 번째 숫자를 가져옵니다.
    fn first(&self) -> i32 { self.0 }

    // 마지막 숫자를 가져옵니다.
    fn last(&self) -> i32 { self.1 }
}

// `C` 는 `A` 와 `B` 를 포함합니다. 이에 따라 `A` 와 `B` 를 다시 표현해야 하는 것은 번거롭습니다.
fn difference<A, B, C>(container: &C) -> i32 where
    C: Contains<A, B> {
    container.last() - container.first()
}

fn main() {
    let number_1 = 3;
    let number_2 = 10;

    let container = Container(number_1, number_2);

    println!("Does container contain {} and {}: {}",
        &number_1, &number_2,
        container.contains(&number_1, &number_2));
    println!("First number: {}", container.first());
    println!("Last number: {}", container.last());

    println!("The difference is: {}", difference(&container));
}
```
