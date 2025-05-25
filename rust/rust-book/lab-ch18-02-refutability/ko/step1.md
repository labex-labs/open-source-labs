# Refutability: 패턴이 일치하지 않을 수 있는지 여부

패턴은 두 가지 형태로 제공됩니다: 반박 가능 (refutable) 과 반박 불가능 (irrefutable). 전달된 모든 가능한 값에 대해 일치하는 패턴은 *반박 불가능*합니다. 예를 들어, `let x = 5;` 문에서 `x`는 모든 것에 일치하므로 일치하지 못할 수 없기 때문입니다. 일부 가능한 값에 대해 일치하지 못할 수 있는 패턴은 *반박 가능*합니다. 예를 들어, `if let Some(x) = a_value` 표현식에서 `Some(x)`는 `a_value` 변수의 값이 `Some`이 아닌 `None`인 경우 `Some(x)` 패턴이 일치하지 않기 때문에 반박 가능합니다.

함수 매개변수, `let` 문 및 `for` 루프는 값이 일치하지 않을 때 프로그램이 의미 있는 작업을 수행할 수 없으므로 반박 불가능한 패턴만 허용합니다. `if let` 및 `while let` 표현식은 반박 가능 및 반박 불가능 패턴을 모두 허용하지만, 컴파일러는 반박 불가능 패턴에 대해 경고합니다. 이는 정의상, 가능한 실패를 처리하기 위한 것이기 때문입니다: 조건문의 기능은 성공 또는 실패에 따라 다르게 수행하는 능력에 있습니다.

일반적으로 반박 가능 및 반박 불가능 패턴의 차이점에 대해 걱정할 필요는 없습니다. 그러나 오류 메시지에서 이를 볼 때 대응할 수 있도록 반박 가능성 개념에 익숙해져야 합니다. 이러한 경우, 코드의 의도된 동작에 따라 패턴 또는 패턴을 사용하는 구조를 변경해야 합니다.

Rust 가 반박 불가능 패턴을 요구하는 곳에서 반박 가능한 패턴을 사용하려고 시도하는 경우와 그 반대의 경우에 어떤 일이 발생하는지 예시를 살펴보겠습니다. Listing 18-8 은 `let` 문을 보여주지만, 패턴의 경우 반박 가능한 패턴인 `Some(x)`를 지정했습니다. 예상대로 이 코드는 컴파일되지 않습니다.

```rust
let Some(x) = some_option_value;
```

Listing 18-8: `let`과 함께 반박 가능한 패턴을 사용하려는 시도

`some_option_value`가 `None` 값인 경우, `Some(x)` 패턴과 일치하지 않아 패턴이 반박 가능하게 됩니다. 그러나 `let` 문은 반박 불가능한 패턴만 허용합니다. 왜냐하면 `None` 값으로 코드가 유효하게 수행할 수 있는 작업이 없기 때문입니다. 컴파일 시점에 Rust 는 반박 불가능한 패턴이 필요한 곳에서 반박 가능한 패턴을 사용하려고 시도했다고 불평할 것입니다.

```bash
error[E0005]: refutable pattern in local binding: `None` not covered
   --> src/main.rs:3:9
    |
3   |     let Some(x) = some_option_value;
    |         ^^^^^^^ pattern `None` not covered
    |
    = note: `let` bindings require an "irrefutable pattern", like a `struct` or
an `enum` with only one variant
    = note: for more information, visit
https://doc.rust-lang.org/book/ch18-02-refutability.html
    = note: the matched value is of type `Option<i32>`
help: you might want to use `if let` to ignore the variant that isn't matched
    |
3   |     let x = if let Some(x) = some_option_value { x } else { todo!() };
    |     ++++++++++                                 ++++++++++++++++++++++
```

`Some(x)` 패턴으로 모든 유효한 값을 다루지 않았기 때문에 (그리고 다룰 수도 없었기 때문에!) Rust 는 정당하게 컴파일러 오류를 생성합니다.

반박 불가능한 패턴이 필요한 곳에 반박 가능한 패턴이 있는 경우, 패턴을 사용하는 코드를 변경하여 수정할 수 있습니다. `let` 대신 `if let`을 사용할 수 있습니다. 그러면 패턴이 일치하지 않으면 코드는 중괄호 안의 코드를 건너뛰어 유효하게 계속 진행할 수 있습니다. Listing 18-9 는 Listing 18-8 의 코드를 수정하는 방법을 보여줍니다.

    if let Some(x) = some_option_value {
        println!("{x}");
    }

Listing 18-9: `let` 대신 `if let`과 반박 가능한 패턴이 있는 블록 사용

우리는 코드에 탈출구를 제공했습니다! 이 코드는 완벽하게 유효하지만, 오류 없이 반박 불가능한 패턴을 사용할 수 없다는 것을 의미합니다. Listing 18-10 과 같이 `if let`에 `x`와 같이 항상 일치하는 패턴을 제공하면 컴파일러가 경고를 표시합니다.

    if let x = 5 {
        println!("{x}");
    };

Listing 18-10: `if let`과 함께 반박 불가능한 패턴을 사용하려는 시도

Rust 는 `if let`을 반박 불가능한 패턴과 함께 사용하는 것이 말이 안 된다고 불평합니다.

    warning: irrefutable `if let` pattern
     --> src/main.rs:2:8
      |
    2 |     if let x = 5 {
      |        ^^^^^^^^^
      |
      = note: `#[warn(irrefutable_let_patterns)]` on by default
      = note: this pattern will always match, so the `if let` is
    useless
      = help: consider replacing the `if let` with a `let`

이러한 이유로, `match` arm 은 마지막 arm 을 제외하고 반박 가능한 패턴을 사용해야 하며, 마지막 arm 은 반박 불가능한 패턴으로 나머지 모든 값과 일치해야 합니다. Rust 는 단일 arm 만 있는 `match`에서 반박 불가능한 패턴을 사용할 수 있도록 허용하지만, 이 구문은 특히 유용하지 않으며 더 간단한 `let` 문으로 대체될 수 있습니다.

이제 패턴을 어디에 사용해야 하는지, 반박 가능 및 반박 불가능 패턴의 차이점을 알았으므로 패턴을 생성하는 데 사용할 수 있는 모든 구문을 살펴보겠습니다.
