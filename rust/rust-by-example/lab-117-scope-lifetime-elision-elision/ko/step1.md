# 생략 (Elision)

일부 lifetime 패턴은 압도적으로 흔하며, 따라서 borrow checker 는 타이핑을 줄이고 가독성을 향상시키기 위해 이를 생략하도록 허용합니다. 이것을 생략 (elision) 이라고 합니다. Rust 에서 생략은 이러한 패턴이 흔하기 때문에 존재합니다.

다음 코드는 생략의 몇 가지 예를 보여줍니다. 생략에 대한 더 포괄적인 설명은 책의 lifetime 생략 부분을 참조하십시오.

```rust
// `elided_input` 과 `annotated_input` 은 본질적으로 동일한 시그니처를 갖습니다.
// `elided_input` 의 lifetime 이 컴파일러에 의해 추론되기 때문입니다.
fn elided_input(x: &i32) {
    println!("`elided_input`: {}", x);
}

fn annotated_input<'a>(x: &'a i32) {
    println!("`annotated_input`: {}", x);
}

// 마찬가지로, `elided_pass` 와 `annotated_pass` 는 동일한 시그니처를 갖습니다.
// lifetime 이 `elided_pass` 에 암시적으로 추가되기 때문입니다.
fn elided_pass(x: &i32) -> &i32 { x }

fn annotated_pass<'a>(x: &'a i32) -> &'a i32 { x }

fn main() {
    let x = 3;

    elided_input(&x);
    annotated_input(&x);

    println!("`elided_pass`: {}", elided_pass(&x));
    println!("`annotated_pass`: {}", annotated_pass(&x));
}
```
