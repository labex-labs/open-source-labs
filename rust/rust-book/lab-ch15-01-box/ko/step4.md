# Cons List 에 대한 추가 정보

*Cons list*는 Lisp 프로그래밍 언어와 그 방언에서 유래된 데이터 구조로, 중첩된 쌍으로 구성되며, 연결 리스트의 Lisp 버전입니다. 이름은 Lisp 의 `cons` 함수 ( *construct function*의 약자) 에서 유래되었으며, 이 함수는 두 인수를 사용하여 새로운 쌍을 구성합니다. 값과 다른 쌍으로 구성된 쌍에 `cons`를 호출함으로써 재귀적 쌍으로 구성된 cons list 를 구성할 수 있습니다.

예를 들어, `1, 2, 3` 목록을 포함하는 cons list 의 의사 코드 표현은 다음과 같습니다 (각 쌍은 괄호 안에 있음):

```rust
(1, (2, (3, Nil)))
```

cons list 의 각 항목은 두 개의 요소를 포함합니다: 현재 항목의 값과 다음 항목입니다. 목록의 마지막 항목은 다음 항목 없이 `Nil`이라는 값만 포함합니다. cons list 는 `cons` 함수를 재귀적으로 호출하여 생성됩니다. 재귀의 기본 사례를 나타내는 표준 이름은 `Nil`입니다. 이는 6 장에서 다룬 "null" 또는 "nil" 개념과는 다르며, 이는 유효하지 않거나 부재하는 값입니다.

Cons list 는 Rust 에서 일반적으로 사용되는 데이터 구조는 아닙니다. Rust 에서 항목 목록이 있는 경우 대부분의 경우 `Vec<T>`를 사용하는 것이 더 나은 선택입니다. 다른, 더 복잡한 재귀적 데이터 타입은 다양한 상황에서 *유용*하지만, 이 장에서 cons list 로 시작함으로써 box 를 사용하여 재귀적 데이터 타입을 방해 없이 정의할 수 있는 방법을 탐구할 수 있습니다.

Listing 15-2 는 cons list 에 대한 enum 정의를 포함합니다. 이 코드는 아직 컴파일되지 않습니다. `List` 타입이 알려진 크기를 갖지 않기 때문이며, 이를 시연할 것입니다.

Filename: `src/main.rs`

```rust
enum List {
    Cons(i32, List),
    Nil,
}
```

Listing 15-2: `i32` 값을 갖는 cons list 데이터 구조를 나타내는 enum 을 정의하려는 첫 번째 시도

> 참고: 이 예제를 위해 `i32` 값만 저장하는 cons list 를 구현하고 있습니다. 10 장에서 논의한 것처럼 제네릭을 사용하여 모든 타입의 값을 저장할 수 있는 cons list 타입을 정의할 수도 있습니다.

`List` 타입을 사용하여 목록 `1, 2, 3`을 저장하는 것은 Listing 15-3 의 코드와 같습니다.

Filename: `src/main.rs`

```rust
--snip--

use crate::List::{Cons, Nil};

fn main() {
    let list = Cons(1, Cons(2, Cons(3, Nil)));
}
```

Listing 15-3: `List` enum 을 사용하여 목록 `1, 2, 3`을 저장하기

첫 번째 `Cons` 값은 `1`과 다른 `List` 값을 저장합니다. 이 `List` 값은 `2`와 다른 `List` 값을 저장하는 또 다른 `Cons` 값입니다. 이 `List` 값은 `3`과 `List` 값을 저장하는 또 다른 `Cons` 값이며, 마지막으로 목록의 끝을 알리는 비재귀적 변형인 `Nil`입니다.

Listing 15-3 의 코드를 컴파일하려고 하면 Listing 15-4 에 표시된 오류가 발생합니다.

```bash
error[E0072]: recursive type `List` has infinite size
 --> src/main.rs:1:1
  |
1 | enum List {
  | ^^^^^^^^^ recursive type has infinite size
2 |     Cons(i32, List),
  |               ---- recursive without indirection
  |
help: insert some indirection (e.g., a `Box`, `Rc`, or `&`) to make `List`
representable
  |
2 |     Cons(i32, Box<List>),
  |               ++++    +
```

Listing 15-4: 재귀적 enum 을 정의하려고 할 때 발생하는 오류

오류는 이 타입이 "무한한 크기"를 갖는다고 표시합니다. 그 이유는 `List`를 재귀적인 변형으로 정의했기 때문입니다: 자체의 다른 값을 직접 저장합니다. 결과적으로 Rust 는 `List` 값을 저장하는 데 필요한 공간의 크기를 파악할 수 없습니다. 이 오류가 발생하는 이유를 자세히 살펴보겠습니다. 먼저 Rust 가 비재귀적 타입의 값을 저장하는 데 필요한 공간의 크기를 어떻게 결정하는지 살펴보겠습니다.
