# 트리 데이터 구조 생성하기: 자식 노드가 있는 노드

먼저, 자식 노드에 대해 아는 노드로 트리를 구성합니다. 자체 `i32` 값과 자식 `Node` 값에 대한 참조를 모두 저장하는 `Node`라는 구조체를 생성합니다.

파일 이름: `src/main.rs`

```rust
use std::cell::RefCell;
use std::rc::Rc;

#[derive(Debug)]
struct Node {
    value: i32,
    children: RefCell<Vec<Rc<Node>>>,
}
```

`Node`가 자식을 소유하고, 각 `Node`에 직접 접근할 수 있도록 해당 소유권을 변수와 공유하려고 합니다. 이를 위해 `Vec<T>` 항목을 `Rc<Node>` 타입의 값으로 정의합니다. 또한 다른 노드의 자식 노드를 수정하고 싶으므로, `Vec<Rc<Node>>` 주위에 `children`에 `RefCell<T>`를 사용합니다.

다음으로, 구조체 정의를 사용하여 `value`가 `3`이고 자식이 없는 `leaf`라는 `Node` 인스턴스와, `value`가 `5`이고 `leaf`를 자식 중 하나로 갖는 `branch`라는 또 다른 인스턴스를 생성합니다. Listing 15-27 에 나와 있습니다.

파일 이름: `src/main.rs`

```rust
fn main() {
    let leaf = Rc::new(Node {
        value: 3,
        children: RefCell::new(vec![]),
    });

    let branch = Rc::new(Node {
        value: 5,
        children: RefCell::new(vec![Rc::clone(&leaf)]),
    });
}
```

Listing 15-27: 자식이 없는 `leaf` 노드와 `leaf`를 자식 중 하나로 갖는 `branch` 노드 생성

`leaf`에서 `Rc<Node>`를 복제하여 `branch`에 저장합니다. 즉, `leaf`의 `Node`는 이제 `leaf`와 `branch` 두 개의 소유자를 갖습니다. `branch.children`을 통해 `branch`에서 `leaf`로 이동할 수 있지만, `leaf`에서 `branch`로 이동할 방법은 없습니다. 그 이유는 `leaf`가 `branch`에 대한 참조가 없고, 그들이 관련되어 있다는 것을 알지 못하기 때문입니다. `leaf`가 `branch`가 자신의 부모라는 것을 알기를 원합니다. 다음 단계에서 그렇게 할 것입니다.
