# 자식에서 부모로의 참조 추가하기

자식 노드가 부모를 인식하게 하려면 `Node` 구조체 정의에 `parent` 필드를 추가해야 합니다. 문제는 `parent`의 타입을 결정하는 것입니다. `Rc<T>`를 포함할 수 없다는 것을 알고 있습니다. 그렇게 하면 `leaf.parent`가 `branch`를 가리키고 `branch.children`이 `leaf`를 가리키는 참조 사이클이 생성되어 `strong_count` 값이 0 이 되지 않기 때문입니다.

관계를 다른 방식으로 생각해보면, 부모 노드는 자식을 소유해야 합니다. 부모 노드가 drop 되면 자식 노드도 drop 되어야 합니다. 그러나 자식은 부모를 소유해서는 안 됩니다. 자식 노드를 drop 하면 부모는 여전히 존재해야 합니다. 이것이 약한 참조의 경우입니다!

따라서 `Rc<T>` 대신 `parent`의 유형을 `Weak<T>`를 사용하도록, 특히 `RefCell<Weak<Node>>`를 사용하도록 만들 것입니다. 이제 `Node` 구조체 정의는 다음과 같습니다.

파일 이름: `src/main.rs`

```rust
use std::cell::RefCell;
use std::rc::{Rc, Weak};

#[derive(Debug)]
struct Node {
    value: i32,
    parent: RefCell<Weak<Node>>,
    children: RefCell<Vec<Rc<Node>>>,
}
```

노드는 부모 노드를 참조할 수 있지만 부모를 소유하지 않습니다. Listing 15-28 에서 `main`을 업데이트하여 이 새로운 정의를 사용하므로 `leaf` 노드는 부모인 `branch`를 참조할 수 있습니다.

파일 이름: `src/main.rs`

```rust
fn main() {
    let leaf = Rc::new(Node {
        value: 3,
      1 parent: RefCell::new(Weak::new()),
        children: RefCell::new(vec![]),
    });

  2 println!(
        "leaf parent = {:?}",
        leaf.parent.borrow().upgrade()
    );

    let branch = Rc::new(Node {
        value: 5,
      3 parent: RefCell::new(Weak::new()),
        children: RefCell::new(vec![Rc::clone(&leaf)]),
    });

  4 *leaf.parent.borrow_mut() = Rc::downgrade(&branch);

  5 println!(
        "leaf parent = {:?}",
        leaf.parent.borrow().upgrade()
    );
}
```

Listing 15-28: 부모 노드인 `branch`에 대한 약한 참조가 있는 `leaf` 노드

`leaf` 노드를 생성하는 것은 `parent` 필드를 제외하고 Listing 15-27 과 유사합니다. `leaf`는 부모가 없는 상태로 시작하므로 새롭고 비어 있는 `Weak<Node>` 참조 인스턴스를 생성합니다 \[1].

이 시점에서 `upgrade` 메서드를 사용하여 `leaf`의 부모에 대한 참조를 얻으려고 하면 `None` 값을 얻습니다. 첫 번째 `println!` 문 \[2]의 출력에서 이를 확인할 수 있습니다.

```rust
leaf parent = None
```

`branch` 노드를 생성할 때 `branch`에는 부모 노드가 없으므로 `parent` 필드에 새로운 `Weak<Node>` 참조가 있습니다 \[3]. 여전히 `leaf`를 `branch`의 자식 중 하나로 가지고 있습니다. `branch`에 `Node` 인스턴스가 있으면 `leaf`를 수정하여 부모에 대한 `Weak<Node>` 참조를 제공할 수 있습니다 \[4]. `leaf`의 `parent` 필드에서 `RefCell<Weak<Node>>`에 대해 `borrow_mut` 메서드를 사용한 다음, `Rc::downgrade` 함수를 사용하여 `branch`의 `Rc<Node>`에서 `branch`에 대한 `Weak<Node>` 참조를 생성합니다.

`leaf`의 부모를 다시 출력하면 \[5], 이번에는 `branch`를 포함하는 `Some` 변형을 얻게 됩니다. 이제 `leaf`는 부모에 접근할 수 있습니다! `leaf`를 출력할 때 Listing 15-26 에서와 같이 스택 오버플로로 끝나는 사이클도 방지합니다. `Weak<Node>` 참조는 `(Weak)`로 출력됩니다.

    leaf parent = Some(Node { value: 5, parent: RefCell { value: (Weak) },
    children: RefCell { value: [Node { value: 3, parent: RefCell { value: (Weak) },
    children: RefCell { value: [] } }] } })

무한 출력이 없다는 것은 이 코드가 참조 사이클을 생성하지 않았음을 나타냅니다. `Rc::strong_count` 및 `Rc::weak_count`를 호출하여 얻는 값을 보면 이를 알 수도 있습니다.
