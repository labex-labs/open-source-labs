# Supertrait 사용하기

때로는 다른 트레이트에 의존하는 트레이트 정의를 작성할 수 있습니다. 첫 번째 트레이트를 구현하려면 해당 타입이 두 번째 트레이트도 구현하도록 요구하고 싶을 것입니다. 이렇게 하면 트레이트 정의에서 두 번째 트레이트의 연관 항목을 사용할 수 있습니다. 트레이트 정의가 의존하는 트레이트를 해당 트레이트의 *supertrait*라고 합니다.

예를 들어, 별표로 프레임이 지정되도록 주어진 값을 출력하는 `outline_print` 메서드가 있는 `OutlinePrint` 트레이트를 만들고 싶다고 가정해 보겠습니다. 즉, 표준 라이브러리 트레이트 `Display`를 구현하여 `(x, y)`가 되도록 하는 `Point` 구조체가 주어지면, `x`가 `1`이고 `y`가 `3`인 `Point` 인스턴스에서 `outline_print`를 호출하면 다음과 같이 출력되어야 합니다.

    **********
    *        *
    * (1, 3) *
    *        *
    **********

`outline_print` 메서드의 구현에서 `Display` 트레이트의 기능을 사용하고 싶습니다. 따라서 `OutlinePrint` 트레이트가 `Display`도 구현하고 `OutlinePrint`에 필요한 기능을 제공하는 타입에 대해서만 작동하도록 지정해야 합니다. `OutlinePrint: Display`를 지정하여 트레이트 정의에서 이를 수행할 수 있습니다. 이 기술은 트레이트 바운드를 트레이트에 추가하는 것과 유사합니다. Listing 19-22 는 `OutlinePrint` 트레이트의 구현을 보여줍니다.

Filename: `src/main.rs`

```rust
use std::fmt;

trait OutlinePrint: fmt::Display {
    fn outline_print(&self) {
        let output = self.to_string();
        let len = output.len();
        println!("{}", "*".repeat(len + 4));
        println!("*{}*", " ".repeat(len + 2));
        println!("* {} *", output);
        println!("*{}*", " ".repeat(len + 2));
        println!("{}", "*".repeat(len + 4));
    }
}
```

Listing 19-22: `Display`의 기능을 요구하는 `OutlinePrint` 트레이트 구현

`OutlinePrint`가 `Display` 트레이트를 요구하도록 지정했으므로, `Display`를 구현하는 모든 타입에 대해 자동으로 구현되는 `to_string` 함수를 사용할 수 있습니다. 트레이트 이름 뒤에 콜론을 추가하고 `Display` 트레이트를 지정하지 않고 `to_string`을 사용하려고 하면, 현재 범위에서 `&Self` 타입에 대해 `to_string`이라는 메서드가 발견되지 않았다는 오류가 발생합니다.

`Point` 구조체와 같이 `Display`를 구현하지 않는 타입에 대해 `OutlinePrint`를 구현하려고 할 때 어떤 일이 발생하는지 살펴보겠습니다.

Filename: `src/main.rs`

```rust
struct Point {
    x: i32,
    y: i32,
}

impl OutlinePrint for Point {}
```

`Display`가 필요하지만 구현되지 않았다는 오류가 발생합니다.

```bash
error[E0277]: `Point` doesn't implement `std::fmt::Display`
  --> src/main.rs:20:6
   |
20 | impl OutlinePrint for Point {}
   |      ^^^^^^^^^^^^ `Point` cannot be formatted with the default formatter
   |
   = help: the trait `std::fmt::Display` is not implemented for `Point`
   = note: in format strings you may be able to use `{:?}` (or {:#?} for
pretty-print) instead
note: required by a bound in `OutlinePrint`
  --> src/main.rs:3:21
   |
3  | trait OutlinePrint: fmt::Display {
   |                     ^^^^^^^^^^^^ required by this bound in `OutlinePrint`
```

이를 해결하려면, `Point`에 `Display`를 구현하고 `OutlinePrint`가 요구하는 제약 조건을 충족합니다.

Filename: `src/main.rs`

```rust
use std::fmt;

impl fmt::Display for Point {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "({}, {})", self.x, self.y)
    }
}
```

그런 다음, `Point`에 `OutlinePrint` 트레이트를 구현하면 성공적으로 컴파일되고, `Point` 인스턴스에서 `outline_print`를 호출하여 별표 윤곽선 내에 표시할 수 있습니다.
