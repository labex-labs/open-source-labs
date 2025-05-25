# 더 많은 매개변수를 가진 메서드

`Rectangle` 구조체에 두 번째 메서드를 구현하여 메서드 사용을 연습해 보겠습니다. 이번에는 `Rectangle`의 인스턴스가 다른 `Rectangle`의 인스턴스를 받아들이고 두 번째 `Rectangle`이 `self` (첫 번째 `Rectangle`) 내부에 완전히 들어갈 수 있으면 `true`를 반환하고, 그렇지 않으면 `false`를 반환하도록 합니다. 즉, `can_hold` 메서드를 정의하면 Listing 5-14 에 표시된 프로그램을 작성할 수 있습니다.

파일 이름: `src/main.rs`

```rust
fn main() {
    let rect1 = Rectangle {
        width: 30,
        height: 50,
    };
    let rect2 = Rectangle {
        width: 10,
        height: 40,
    };
    let rect3 = Rectangle {
        width: 60,
        height: 45,
    };

    println!("Can rect1 hold rect2? {}", rect1.can_hold(&rect2));
    println!("Can rect1 hold rect3? {}", rect1.can_hold(&rect3));
}
```

Listing 5-14: 아직 작성되지 않은 `can_hold` 메서드 사용

예상되는 출력은 다음과 같습니다. `rect2`의 두 치수 모두 `rect1`의 치수보다 작지만, `rect3`는 `rect1`보다 넓기 때문입니다.

```rust
Can rect1 hold rect2? true
Can rect1 hold rect3? false
```

메서드를 정의하려는 것을 알고 있으므로, `impl Rectangle` 블록 내에 있을 것입니다. 메서드 이름은 `can_hold`이고, 다른 `Rectangle`의 불변 빌림을 매개변수로 받습니다. 메서드를 호출하는 코드를 보면 매개변수의 타입을 알 수 있습니다: `rect1.can_hold(&rect2)`는 `&rect2`를 전달하는데, 이는 `Rectangle`의 인스턴스인 `rect2`에 대한 불변 빌림입니다. `rect2`를 읽기만 하면 되기 때문에 (쓰는 것은 가변 빌림이 필요하므로) 말이 되고, `main`이 `can_hold` 메서드를 호출한 후에도 `rect2`의 소유권을 유지하여 다시 사용할 수 있도록 하려고 합니다. `can_hold`의 반환 값은 부울 (Boolean) 이 될 것이고, 구현은 `self`의 너비와 높이가 다른 `Rectangle`의 너비와 높이보다 각각 큰지 여부를 확인합니다. Listing 5-15 에 표시된 Listing 5-13 의 `impl` 블록에 새로운 `can_hold` 메서드를 추가해 보겠습니다.

파일 이름: `src/main.rs`

```rust
impl Rectangle {
    fn area(&self) -> u32 {
        self.width * self.height
    }

    fn can_hold(&self, other: &Rectangle) -> bool {
        self.width > other.width && self.height > other.height
    }
}
```

Listing 5-15: 다른 `Rectangle` 인스턴스를 매개변수로 받는 `Rectangle`에 `can_hold` 메서드 구현하기

Listing 5-14 의 `main` 함수로 이 코드를 실행하면 원하는 출력을 얻을 수 있습니다. 메서드는 `self` 매개변수 뒤의 시그니처에 추가하는 여러 매개변수를 가질 수 있으며, 이러한 매개변수는 함수의 매개변수와 마찬가지로 작동합니다.
