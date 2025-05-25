# 연관된 타입 (Associated types)

"연관된 타입"을 사용하면 내부 타입을 트레이트 내에서 _출력_ 타입으로 로컬하게 이동하여 코드 가독성을 향상시킬 수 있습니다. `trait` 정의의 구문은 다음과 같습니다.

```rust
// `A` 와 `B` 는 `type` 키워드를 통해 트레이트 내에서 정의됩니다.
// (참고: 이 맥락에서의 `type` 은 별칭으로 사용되는 `type` 과 다릅니다).
trait Contains {
    type A;
    type B;

    // 이 새로운 타입을 일반적으로 참조하기 위한 업데이트된 구문.
    fn contains(&self, _: &Self::A, _: &Self::B) -> bool;
}
```

`Contains` `trait`를 사용하는 함수는 더 이상 `A` 또는 `B`를 전혀 표현할 필요가 없습니다.

```rust
// 연관된 타입을 사용하지 않을 경우
fn difference<A, B, C>(container: &C) -> i32 where
    C: Contains<A, B> { ... }

// 연관된 타입을 사용할 경우
fn difference<C: Contains>(container: &C) -> i32 { ... }
```

이전 섹션의 예제를 연관된 타입을 사용하여 다시 작성해 보겠습니다.

```rust
struct Container(i32, i32);

// 컨테이너 내에 2 개의 항목이 있는지 확인하고, 첫 번째 또는 마지막 값을 가져오는 트레이트.
trait Contains {
    // 메서드가 활용할 수 있는 일반 타입을 여기에 정의합니다.
    type A;
    type B;

    fn contains(&self, _: &Self::A, _: &Self::B) -> bool;
    fn first(&self) -> i32;
    fn last(&self) -> i32;
}

impl Contains for Container {
    // `A` 와 `B` 가 어떤 타입인지 지정합니다. 입력 타입이 `Container(i32, i32)`이면 출력 타입은 `i32` 와 `i32` 로 결정됩니다.
    type A = i32;
    type B = i32;

    // `&Self::A` 와 `&Self::B` 도 여기서 유효합니다.
    fn contains(&self, number_1: &i32, number_2: &i32) -> bool {
        (&self.0 == number_1) && (&self.1 == number_2)
    }
    // 첫 번째 숫자를 가져옵니다.
    fn first(&self) -> i32 { self.0 }

    // 마지막 숫자를 가져옵니다.
    fn last(&self) -> i32 { self.1 }
}

fn difference<C: Contains>(container: &C) -> i32 {
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
