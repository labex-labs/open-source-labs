# strong_count 및 weak_count 변경 시각화

새로운 내부 범위를 생성하고 `branch`의 생성을 해당 범위로 이동하여 `Rc<Node>` 인스턴스의 `strong_count` 및 `weak_count` 값이 어떻게 변경되는지 살펴보겠습니다. 이렇게 하면 `branch`가 생성된 다음 범위에서 벗어날 때 어떻게 되는지 확인할 수 있습니다. 수정 사항은 Listing 15-29 에 나와 있습니다.

파일 이름: `src/main.rs`

```rust
fn main() {
    let leaf = Rc::new(Node {
        value: 3,
        parent: RefCell::new(Weak::new()),
        children: RefCell::new(vec![]),
    });

  1 println!(
        "leaf strong = {}, weak = {}",
        Rc::strong_count(&leaf),
        Rc::weak_count(&leaf),
    );

  2 {
        let branch = Rc::new(Node {
            value: 5,
            parent: RefCell::new(Weak::new()),
            children: RefCell::new(vec![Rc::clone(&leaf)]),
        });

        *leaf.parent.borrow_mut() = Rc::downgrade(&branch);

      3 println!(
            "branch strong = {}, weak = {}",
            Rc::strong_count(&branch),
            Rc::weak_count(&branch),
        );

      4 println!(
            "leaf strong = {}, weak = {}",
            Rc::strong_count(&leaf),
            Rc::weak_count(&leaf),
        );
  5 }

  6 println!(
        "leaf parent = {:?}",
        leaf.parent.borrow().upgrade()
    );
  7 println!(
        "leaf strong = {}, weak = {}",
        Rc::strong_count(&leaf),
        Rc::weak_count(&leaf),
    );
}
```

Listing 15-29: 내부 범위에서 `branch`를 생성하고 강하고 약한 참조 횟수 검사

`leaf`가 생성된 후 해당 `Rc<Node>`는 strong count 가 1 이고 weak count 가 0 입니다 \[1]. 내부 범위 \[2]에서 `branch`를 생성하고 `leaf`와 연결합니다. 이 시점에서 카운트를 출력하면 \[3], `branch`의 `Rc<Node>`는 strong count 가 1 이고 weak count 가 1( `leaf.parent`가 `Weak<Node>`로 `branch`를 가리키는 경우) 이 됩니다. `leaf`에서 카운트를 출력하면 \[4], `branch`가 이제 `branch.children`에 저장된 `leaf`의 `Rc<Node>` 복사본을 가지고 있기 때문에 strong count 가 2 가 되지만 weak count 는 여전히 0 이 됩니다.

내부 범위가 종료되면 \[5], `branch`가 범위를 벗어나고 `Rc<Node>`의 strong count 가 0 으로 감소하므로 해당 `Node`가 drop 됩니다. `leaf.parent`의 weak count 1 은 `Node`가 drop 되는지 여부와 관련이 없으므로 메모리 누수가 발생하지 않습니다!

범위가 끝난 후 `leaf`의 부모에 접근하려고 하면 다시 `None`을 얻게 됩니다 \[6]. 프로그램이 종료될 때 \[7], `leaf`의 `Rc<Node>`는 strong count 가 1 이고 weak count 가 0 입니다. 왜냐하면 변수 `leaf`가 이제 다시 `Rc<Node>`에 대한 유일한 참조이기 때문입니다.

카운트 및 값 drop 을 관리하는 모든 로직은 `Rc<T>` 및 `Weak<T>`와 `Drop` 트레이트의 구현에 내장되어 있습니다. `Node`의 정의에서 자식에서 부모로의 관계가 `Weak<T>` 참조여야 한다고 지정하면, 참조 사이클과 메모리 누수를 생성하지 않고 부모 노드가 자식 노드를 가리키고 그 반대로도 가리킬 수 있습니다.
