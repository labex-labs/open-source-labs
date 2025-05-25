# 클로저 반환

클로저는 트레이트로 표현되므로 클로저를 직접 반환할 수 없습니다. 트레이트를 반환하려는 대부분의 경우, 대신 트레이트를 구현하는 구체적인 타입을 함수의 반환 값으로 사용할 수 있습니다. 그러나 클로저는 반환 가능한 구체적인 타입을 갖지 않으므로 그렇게 할 수 없습니다. 예를 들어 함수 포인터 `fn`을 반환 타입으로 사용할 수 없습니다.

다음 코드는 클로저를 직접 반환하려고 시도하지만 컴파일되지 않습니다.

```rust
fn returns_closure() -> dyn Fn(i32) -> i32 {
    |x| x + 1
}
```

컴파일러 오류는 다음과 같습니다.

```bash
error[E0746]: return type cannot have an unboxed trait object
 --> src/lib.rs:1:25
  |
1 | fn returns_closure() -> dyn Fn(i32) -> i32 {
  |                         ^^^^^^^^^^^^^^^^^^ doesn't have a size known at
compile-time
  |
  = note: for information on `impl Trait`, see
<https://doc.rust-lang.org/book/ch10-02-traits.html#returning-types-that-
implement-traits>
help: use `impl Fn(i32) -> i32` as the return type, as all return paths are of
type `[closure@src/lib.rs:2:5: 2:14]`, which implements `Fn(i32) -> i32`
  |
1 | fn returns_closure() -> impl Fn(i32) -> i32 {
  |                         ~~~~~~~~~~~~~~~~~~~
```

오류는 다시 `Sized` 트레이트를 참조합니다! Rust 는 클로저를 저장하는 데 얼마나 많은 공간이 필요한지 알지 못합니다. 이 문제에 대한 해결책을 앞서 보았습니다. 트레이트 객체 (trait object) 를 사용할 수 있습니다.

```rust
fn returns_closure() -> Box<dyn Fn(i32) -> i32> {
    Box::new(|x| x + 1)
}
```

이 코드는 문제없이 컴파일됩니다. 트레이트 객체에 대한 자세한 내용은 "다양한 타입의 값을 허용하는 트레이트 객체 사용"을 참조하십시오.

다음으로, 매크로를 살펴보겠습니다!
