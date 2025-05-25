# Rc`<T>`{=html}를 사용하여 데이터 공유하기

Listing 15-5 의 cons list 예제로 돌아가 보겠습니다. `Box<T>`를 사용하여 정의했음을 기억하세요. 이번에는 세 번째 리스트를 모두 공유하는 두 개의 리스트를 만들 것입니다. 개념적으로, 이것은 그림 15-3 과 유사합니다.

그림 15-3: 세 번째 리스트 `a`를 공유하는 두 개의 리스트 `b`와 `c`

`5`와 `10`을 포함하는 리스트 `a`를 만들 것입니다. 그런 다음 `3`으로 시작하는 `b`와 `4`로 시작하는 `c`의 두 개의 리스트를 더 만들 것입니다. `b`와 `c` 리스트는 모두 `5`와 `10`을 포함하는 첫 번째 `a` 리스트로 이어집니다. 즉, 두 리스트 모두 `5`와 `10`을 포함하는 첫 번째 리스트를 공유합니다.

Listing 15-17 에 표시된 것처럼 `Box<T>`를 사용하여 `List`를 정의하여 이 시나리오를 구현하려고 하면 작동하지 않습니다.

파일 이름: `src/main.rs`

```rust
enum List {
    Cons(i32, Box<List>),
    Nil,
}

use crate::List::{Cons, Nil};

fn main() {
    let a = Cons(5, Box::new(Cons(10, Box::new(Nil))));
  1 let b = Cons(3, Box::new(a));
  2 let c = Cons(4, Box::new(a));
}
```

Listing 15-17: 세 번째 리스트의 소유권을 공유하려는 `Box<T>`를 사용하는 두 개의 리스트를 가질 수 없음을 보여줍니다.

이 코드를 컴파일하면 다음과 같은 오류가 발생합니다.

```bash
error[E0382]: use of moved value: `a`
  --> src/main.rs:11:30
   |
9  |     let a = Cons(5, Box::new(Cons(10, Box::new(Nil))));
   |         - move occurs because `a` has type `List`, which
does not implement the `Copy` trait
10 |     let b = Cons(3, Box::new(a));
   |                              - value moved here
11 |     let c = Cons(4, Box::new(a));
   |                              ^ value used here after move
```

`Cons` 변형은 자신이 보유한 데이터를 소유하므로 `b` 리스트 \[1]를 만들 때 `a`가 `b`로 이동하고 `b`가 `a`를 소유합니다. 그런 다음 `c` \[2]를 만들 때 `a`를 다시 사용하려고 하면 `a`가 이동되었기 때문에 사용할 수 없습니다.

`Cons`의 정의를 참조를 보유하도록 변경할 수 있지만, 그러면 lifetime 매개변수를 지정해야 합니다. lifetime 매개변수를 지정하면 리스트의 모든 요소가 전체 리스트만큼 오래 지속될 것이라고 지정하는 것입니다. 이것은 Listing 15-17 의 요소와 리스트의 경우이지만 모든 시나리오에서 그런 것은 아닙니다.

대신, Listing 15-18 에 표시된 것처럼 `Box<T>` 대신 `Rc<T>`를 사용하도록 `List`의 정의를 변경할 것입니다. 이제 각 `Cons` 변형은 값과 `List`를 가리키는 `Rc<T>`를 보유합니다. `b`를 만들 때 `a`의 소유권을 가져가는 대신, `a`가 보유하고 있는 `Rc<List>`를 복제하여 참조 수를 1 에서 2 로 늘리고 `a`와 `b`가 해당 `Rc<List>`의 데이터를 공유하도록 합니다. 또한 `c`를 만들 때 `a`를 복제하여 참조 수를 2 에서 3 으로 늘립니다. `Rc::clone`을 호출할 때마다 `Rc<List>` 내의 데이터에 대한 참조 카운트가 증가하고, 해당 데이터에 대한 참조가 0 개가 아닌 한 데이터는 정리되지 않습니다.

파일 이름: `src/main.rs`

```rust
enum List {
    Cons(i32, Rc<List>),
    Nil,
}

use crate::List::{Cons, Nil};
1 use std::rc::Rc;

fn main() {
  2 let a = Rc::new(Cons(5, Rc::new(Cons(10, Rc::new(Nil)))));
  3 let b = Cons(3, Rc::clone(&a));
  4 let c = Cons(4, Rc::clone(&a));
}
```

Listing 15-18: `Rc<T>`를 사용하는 `List`의 정의

`Rc<T>`를 범위 내로 가져오기 위해 `use` 문을 추가해야 합니다 \[1] (prelude 에 없기 때문입니다). `main`에서 `5`와 `10`을 보유하는 리스트를 만들고 `a` \[2]의 새로운 `Rc<List>`에 저장합니다. 그런 다음 `b` \[3]와 `c` \[4]를 만들 때 `Rc::clone` 함수를 호출하고 `a`의 `Rc<List>`에 대한 참조를 인수로 전달합니다.

`Rc::clone(&a)` 대신 `a.clone()`을 호출할 수도 있었지만, Rust 의 규칙은 이 경우 `Rc::clone`을 사용하는 것입니다. `Rc::clone`의 구현은 대부분의 타입의 `clone` 구현과 같이 모든 데이터를 깊이 복사하지 않습니다. `Rc::clone` 호출은 참조 카운트만 증가시키며, 이는 많은 시간이 걸리지 않습니다. 데이터의 깊은 복사는 많은 시간이 걸릴 수 있습니다. 참조 카운팅에 `Rc::clone`을 사용함으로써, 깊이 복사 종류의 clone 과 참조 카운트를 증가시키는 종류의 clone 을 시각적으로 구별할 수 있습니다. 코드에서 성능 문제를 찾을 때, 깊이 복사 clone 만 고려하면 되고 `Rc::clone` 호출은 무시할 수 있습니다.
