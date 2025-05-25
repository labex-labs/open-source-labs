# 트레이트

물론 `trait`도 제네릭일 수 있습니다. 여기서는 `Drop` `trait`을 재구현하여 자신과 입력값을 제거하는 제네릭 메서드로 정의합니다.

```rust
// 복사 불가능한 타입들.
struct Empty;
struct Null;

// `T` 에 대한 제네릭 트레이트.
trait DoubleDrop<T> {
    // 호출자 타입에 메서드를 정의하여 추가적인 단일 매개변수 `T` 를 받고 아무것도 하지 않습니다.
    fn double_drop(self, _: T);
}

// 모든 제네릭 매개변수 `T` 와 호출자 `U` 에 대해 `DoubleDrop<T>` 를 구현합니다.
impl<T, U> DoubleDrop<T> for U {
    // 이 메서드는 전달된 두 개의 인수 모두를 소유하여 두 개 모두를 할당 해제합니다.
    fn double_drop(self, _: T) {}
}

fn main() {
    let empty = Empty;
    let null  = Null;

    // `empty` 와 `null` 을 할당 해제합니다.
    empty.double_drop(null);

    //empty;
    //null;
    // ^ TODO: 이 줄들을 주석 해제해 보세요.
}
```
