# 자체 스마트 포인터 정의하기

기본적으로 스마트 포인터가 참조와 어떻게 다르게 동작하는지 경험하기 위해 표준 라이브러리에서 제공하는 `Box<T>` 타입과 유사한 스마트 포인터를 만들어 보겠습니다. 그런 다음 역참조 연산자를 사용할 수 있는 기능을 추가하는 방법을 살펴보겠습니다.

`Box<T>` 타입은 궁극적으로 하나의 요소를 가진 튜플 구조체로 정의되므로 Listing 15-8 은 동일한 방식으로 `MyBox<T>` 타입을 정의합니다. 또한 `Box<T>`에 정의된 `new` 함수와 일치하는 `new` 함수도 정의합니다.

파일 이름: `src/main.rs`

```rust
 1 struct MyBox<T>(T);

impl<T> MyBox<T> {
  2 fn new(x: T) -> MyBox<T> {
      3 MyBox(x)
    }
}
```

Listing 15-8: `MyBox<T>` 타입 정의하기

`MyBox`라는 구조체를 정의하고 제네릭 매개변수 `T`를 선언합니다 \[1]. 이는 모든 타입의 값을 저장하려는 것이기 때문입니다. `MyBox` 타입은 `T` 타입의 단일 요소를 가진 튜플 구조체입니다. `MyBox::new` 함수는 `T` 타입의 매개변수 하나를 받아서 \[2] 전달된 값을 저장하는 `MyBox` 인스턴스를 반환합니다 \[3].

Listing 15-7 의 `main` 함수를 Listing 15-8 에 추가하고 `Box<T>` 대신 정의한 `MyBox<T>` 타입을 사용하도록 변경해 보겠습니다. Listing 15-9 의 코드는 Rust 가 `MyBox`를 역참조하는 방법을 모르기 때문에 컴파일되지 않습니다.

파일 이름: `src/main.rs`

```rust
fn main() {
    let x = 5;
    let y = MyBox::new(x);

    assert_eq!(5, x);
    assert_eq!(5, *y);
}
```

Listing 15-9: 참조 및 `Box<T>`를 사용했던 방식과 동일하게 `MyBox<T>`를 사용하려는 시도

다음은 결과 컴파일 오류입니다.

```bash
error[E0614]: type `MyBox<{integer}>` cannot be dereferenced
  --> src/main.rs:14:19
   |
14 |     assert_eq!(5, *y);
   |                   ^^
```

`MyBox<T>` 타입은 해당 기능을 타입에 구현하지 않았기 때문에 역참조할 수 없습니다. `*` 연산자를 사용하여 역참조를 활성화하려면 `Deref` 트레이트를 구현합니다.
