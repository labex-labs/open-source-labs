# Rc`<T>` 및 RefCell`<T>`을 사용하여 가변 데이터의 다중 소유자 허용하기

`RefCell<T>`를 사용하는 일반적인 방법은 `Rc<T>`와 함께 사용하는 것입니다. `Rc<T>`를 사용하면 일부 데이터의 여러 소유자를 가질 수 있지만 해당 데이터에 대한 불변 액세스만 제공한다는 것을 기억하세요. `RefCell<T>`를 포함하는 `Rc<T>`가 있는 경우 여러 소유자를 가질 수 있고 변경할 수 있는 값을 얻을 수 있습니다!

예를 들어, 여러 목록이 다른 목록의 소유권을 공유할 수 있도록 `Rc<T>`를 사용했던 Listing 15-18 의 cons 목록 예제를 기억하세요. `Rc<T>`는 불변 값만 포함하므로 목록을 생성한 후에는 목록의 값을 변경할 수 없습니다. 목록의 값을 변경할 수 있는 기능을 위해 `RefCell<T>`를 추가해 보겠습니다. Listing 15-24 는 `Cons` 정의에서 `RefCell<T>`를 사용하면 모든 목록에 저장된 값을 수정할 수 있음을 보여줍니다.

파일 이름: `src/main.rs`

```rust
#[derive(Debug)]
enum List {
    Cons(Rc<RefCell<i32>>, Rc<List>),
    Nil,
}

use crate::List::{Cons, Nil};
use std::cell::RefCell;
use std::rc::Rc;

fn main() {
  1 let value = Rc::new(RefCell::new(5));

  2 let a = Rc::new(Cons(Rc::clone(&value), Rc::new(Nil)));

    let b = Cons(Rc::new(RefCell::new(3)), Rc::clone(&a));
    let c = Cons(Rc::new(RefCell::new(4)), Rc::clone(&a));

  3 *value.borrow_mut() += 10;

    println!("a after = {:?}", a);
    println!("b after = {:?}", b);
    println!("c after = {:?}", c);
}
```

Listing 15-24: `Rc<RefCell<i32>>`를 사용하여 변경할 수 있는 `List` 생성

`Rc<RefCell<i32>>`의 인스턴스인 값을 생성하고 나중에 직접 액세스할 수 있도록 `value`라는 변수에 저장합니다 \[1]. 그런 다음 `value` \[2]를 포함하는 `Cons` 변형을 사용하여 `a`에서 `List`를 생성합니다. `value`에서 `a`로 소유권을 이전하거나 `a`가 `value`에서 차용하는 대신, `a`와 `value` 모두 내부 `5` 값의 소유권을 갖도록 `value`를 복제해야 합니다.

Listing 15-18 에서 했던 것처럼, `b`와 `c` 목록을 생성할 때 모두 `a`를 참조할 수 있도록 `a` 목록을 `Rc<T>`로 래핑합니다.

`a`, `b`, `c`에서 목록을 생성한 후 `value` \[3]의 값에 10 을 더하고 싶습니다. "-\> 연산자는 어디에 있습니까?"에서 논의한 자동 역참조 기능을 사용하여 `Rc<T>`를 내부 `RefCell<T>` 값으로 역참조하는 `value`에서 `borrow_mut`을 호출하여 이 작업을 수행합니다. `borrow_mut` 메서드는 `RefMut<T>` 스마트 포인터를 반환하고, 역참조 연산자를 사용하여 내부 값을 변경합니다.

`a`, `b`, `c`를 출력하면 모두 `5` 대신 수정된 값 `15`를 갖는 것을 볼 수 있습니다.

    a after = Cons(RefCell { value: 15 }, Nil)
    b after = Cons(RefCell { value: 3 }, Cons(RefCell { value: 15 }, Nil))
    c after = Cons(RefCell { value: 4 }, Cons(RefCell { value: 15 }, Nil))

이 기술은 매우 훌륭합니다! `RefCell<T>`를 사용하면 겉으로는 불변인 `List` 값을 갖게 됩니다. 그러나 필요할 때 데이터를 수정할 수 있도록 내부 가변성에 대한 액세스를 제공하는 `RefCell<T>`의 메서드를 사용할 수 있습니다. 차용 규칙의 런타임 검사는 데이터 경합으로부터 보호하며, 데이터 구조에서 이러한 유연성을 위해 약간의 속도를 희생할 가치가 있는 경우도 있습니다. `RefCell<T>`는 다중 스레드 코드에서는 작동하지 않습니다! `Mutex<T>`는 `RefCell<T>`의 스레드 안전 버전이며, 16 장에서 `Mutex<T>`에 대해 논의할 것입니다.
