# 참조 사이클 생성하기

참조 사이클이 어떻게 발생할 수 있는지, 그리고 이를 방지하는 방법을 살펴보겠습니다. Listing 15-25 의 `List` enum 정의와 `tail` 메서드부터 시작합니다.

파일 이름: `src/main.rs`

```rust
use crate::List::{Cons, Nil};
use std::cell::RefCell;
use std::rc::Rc;

#[derive(Debug)]
enum List {
  1 Cons(i32, RefCell<Rc<List>>),
    Nil,
}

impl List {
  2 fn tail(&self) -> Option<&RefCell<Rc<List>>> {
        match self {
            Cons(_, item) => Some(item),
            Nil => None,
        }
    }
}
```

Listing 15-25: `Cons` 변형이 참조하는 것을 수정할 수 있도록 `RefCell<T>`를 포함하는 cons list 정의

Listing 15-5 의 `List` 정의의 또 다른 변형을 사용하고 있습니다. `Cons` 변형의 두 번째 요소는 이제 `RefCell<Rc<List>>` \[1]입니다. 즉, Listing 15-24 에서 했던 것처럼 `i32` 값을 수정하는 대신, `Cons` 변형이 가리키는 `List` 값을 수정하려고 합니다. 또한 `Cons` 변형이 있는 경우 두 번째 항목에 편리하게 접근할 수 있도록 `tail` 메서드 \[2]를 추가하고 있습니다.

Listing 15-26 에서는 Listing 15-25 의 정의를 사용하는 `main` 함수를 추가하고 있습니다. 이 코드는 `a`에 리스트를 생성하고, `a`의 리스트를 가리키는 `b`에 리스트를 생성합니다. 그런 다음 `a`의 리스트를 `b`를 가리키도록 수정하여 참조 사이클을 생성합니다. 이 과정에서 참조 횟수가 어떻게 되는지 보여주기 위해 `println!` 문이 사용됩니다.

파일 이름: `src/main.rs`

```rust
fn main() {
  1 let a = Rc::new(Cons(5, RefCell::new(Rc::new(Nil))));

    println!("a initial rc count = {}", Rc::strong_count(&a));
    println!("a next item = {:?}", a.tail());

  2 let b = Rc::new(Cons(10, RefCell::new(Rc::clone(&a))));

    println!(
        "a rc count after b creation = {}",
        Rc::strong_count(&a)
    );
    println!("b initial rc count = {}", Rc::strong_count(&b));
    println!("b next item = {:?}", b.tail());

  3 if let Some(link) = a.tail() {
      4 *link.borrow_mut() = Rc::clone(&b);
    }

    println!(
        "b rc count after changing a = {}",
        Rc::strong_count(&b)
    );
    println!(
        "a rc count after changing a = {}",
        Rc::strong_count(&a)
    );

    // Uncomment the next line to see that we have a cycle;
    // it will overflow the stack
    // println!("a next item = {:?}", a.tail());
}
```

Listing 15-26: 서로를 가리키는 두 개의 `List` 값의 참조 사이클 생성

`5, Nil`의 초기 리스트를 가진 `List` 값을 포함하는 `Rc<List>` 인스턴스를 변수 `a`에 생성합니다 \[1]. 그런 다음 값 `10`을 포함하고 `a`의 리스트를 가리키는 또 다른 `List` 값을 포함하는 `Rc<List>` 인스턴스를 변수 `b`에 생성합니다 \[2].

`a`가 `Nil` 대신 `b`를 가리키도록 수정하여 사이클을 생성합니다. `tail` 메서드를 사용하여 `a`의 `RefCell<Rc<List>>`에 대한 참조를 가져와 변수 `link`에 넣습니다 \[3]. 그런 다음 `RefCell<Rc<List>>`에서 `borrow_mut` 메서드를 사용하여 내부 값을 `Nil` 값을 포함하는 `Rc<List>`에서 `b`의 `Rc<List>`로 변경합니다 \[4].

이 코드를 실행하면, 마지막 `println!`을 잠시 주석 처리해두면 다음과 같은 출력을 얻게 됩니다.

    a initial rc count = 1
    a next item = Some(RefCell { value: Nil })
    a rc count after b creation = 2
    b initial rc count = 1
    b next item = Some(RefCell { value: Cons(5, RefCell { value: Nil }) })
    b rc count after changing a = 2
    a rc count after changing a = 2

`a`와 `b` 모두에서 `Rc<List>` 인스턴스의 참조 횟수는 `a`의 리스트를 `b`를 가리키도록 변경한 후 2 입니다. `main`의 끝에서 Rust 는 변수 `b`를 drop 하며, 이는 `b` `Rc<List>` 인스턴스의 참조 횟수를 2 에서 1 로 감소시킵니다. `Rc<List>`가 힙에 가지고 있는 메모리는 이 시점에서 drop 되지 않습니다. 왜냐하면 참조 횟수가 1 이지 0 이 아니기 때문입니다. 그런 다음 Rust 는 `a`를 drop 하며, 이는 `a` `Rc<List>` 인스턴스의 참조 횟수를 2 에서 1 로 감소시킵니다. 이 인스턴스의 메모리도 drop 될 수 없습니다. 왜냐하면 다른 `Rc<List>` 인스턴스가 여전히 이를 참조하고 있기 때문입니다. 리스트에 할당된 메모리는 영원히 수집되지 않은 상태로 남게 됩니다. 이 참조 사이클을 시각화하기 위해 그림 15-4 에 다이어그램을 만들었습니다.

그림 15-4: 서로를 가리키는 리스트 `a`와 `b`의 참조 사이클

마지막 `println!`의 주석을 해제하고 프로그램을 실행하면 Rust 는 `a`가 `b`를 가리키고, `b`가 `a`를 가리키는 등의 사이클을 출력하려고 시도하여 스택 오버플로우가 발생합니다.

실제 프로그램과 비교했을 때, 이 예제에서 참조 사이클을 생성하는 결과는 그다지 심각하지 않습니다. 참조 사이클을 생성한 직후 프로그램이 종료됩니다. 그러나 더 복잡한 프로그램이 사이클에서 많은 메모리를 할당하고 오랫동안 유지하는 경우, 프로그램은 필요 이상으로 많은 메모리를 사용하고 시스템을 압도하여 사용 가능한 메모리가 부족하게 될 수 있습니다.

참조 사이클을 생성하는 것은 쉽지 않지만, 불가능한 것도 아닙니다. `Rc<T>` 값을 포함하는 `RefCell<T>` 값 또는 내부 가변성 및 참조 횟수가 있는 유사한 중첩된 유형 조합이 있는 경우, 사이클을 생성하지 않도록 해야 합니다. Rust 가 이를 감지하도록 의존할 수 없습니다. 참조 사이클을 생성하는 것은 프로그램의 논리적 버그이며, 자동화된 테스트, 코드 검토 및 기타 소프트웨어 개발 관행을 사용하여 최소화해야 합니다.

참조 사이클을 피하는 또 다른 해결책은 일부 참조가 소유권을 표현하고 일부 참조는 그렇지 않도록 데이터 구조를 재구성하는 것입니다. 결과적으로, 일부 소유권 관계와 일부 비소유권 관계로 구성된 사이클을 가질 수 있으며, 소유권 관계만 값이 drop 될 수 있는지 여부에 영향을 미칩니다. Listing 15-25 에서 우리는 항상 `Cons` 변형이 자신의 리스트를 소유하기를 원하므로, 데이터 구조를 재구성하는 것은 불가능합니다. 비소유권 관계가 참조 사이클을 방지하는 적절한 방법인 경우를 보기 위해 부모 노드와 자식 노드로 구성된 그래프를 사용하는 예를 살펴보겠습니다.
