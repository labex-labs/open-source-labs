# 내부 가변성: 불변 값에 대한 가변 차용

차용 규칙의 결과는 불변 값을 가지고 있을 때 가변적으로 차용할 수 없다는 것입니다. 예를 들어, 이 코드는 컴파일되지 않습니다.

파일 이름: `src/main.rs`

```rust
fn main() {
    let x = 5;
    let y = &mut x;
}
```

이 코드를 컴파일하려고 하면 다음과 같은 오류가 발생합니다.

```bash
error[E0596]: cannot borrow `x` as mutable, as it is not declared
as mutable
 --> src/main.rs:3:13
  |
2 |     let x = 5;
  |         - help: consider changing this to be mutable: `mut x`
3 |     let y = &mut x;
  |             ^^^^^^ cannot borrow as mutable
```

그러나 값의 메서드에서 자체적으로 변경되지만 다른 코드에는 불변으로 보이는 상황이 있습니다. 값의 메서드 외부의 코드는 값을 변경할 수 없습니다. `RefCell<T>`를 사용하는 것은 내부 가변성을 갖는 한 가지 방법이지만, `RefCell<T>`는 차용 규칙을 완전히 우회하지 않습니다. 컴파일러의 차용 검사기 (borrow checker) 는 이 내부 가변성을 허용하며, 차용 규칙은 대신 런타임에 확인됩니다. 규칙을 위반하면 컴파일러 오류 대신 `panic!`이 발생합니다.

`RefCell<T>`를 사용하여 불변 값을 변경하고 그 이유가 무엇인지 알 수 있는 실용적인 예제를 살펴보겠습니다.
