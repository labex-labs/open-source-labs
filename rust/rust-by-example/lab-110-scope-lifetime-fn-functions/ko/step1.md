# 함수 (Functions)

\[elision]을 제외하고, 생명주기를 가진 함수 시그니처 (function signature) 에는 몇 가지 제약 조건이 있습니다.

- 모든 참조 (reference) 는 _반드시_ 주석 처리된 생명주기를 가져야 합니다.
- 반환되는 모든 참조는 _반드시_ 입력과 동일한 생명주기를 가지거나 `static`이어야 합니다.

또한, 입력 없이 참조를 반환하는 것은 유효하지 않은 데이터에 대한 참조를 반환하는 결과를 초래할 경우 금지된다는 점에 유의하십시오. 다음 예제는 생명주기를 가진 함수의 몇 가지 유효한 형태를 보여줍니다.

```rust
// 생명주기 `'a` 를 가진 하나의 입력 참조.
// 이 참조는 함수만큼 오래 유지되어야 합니다.
fn print_one<'a>(x: &'a i32) {
    println!("`print_one`: x is {}", x);
}

// 가변 참조 (mutable reference) 도 생명주기와 함께 사용할 수 있습니다.
fn add_one<'a>(x: &'a mut i32) {
    *x += 1;
}

// 서로 다른 생명주기를 가진 여러 요소. 이 경우,
// 둘 다 동일한 생명주기 `'a` 를 갖는 것이 괜찮지만,
// 더 복잡한 경우에는 서로 다른 생명주기가 필요할 수 있습니다.
fn print_multi<'a, 'b>(x: &'a i32, y: &'b i32) {
    println!("`print_multi`: x is {}, y is {}", x, y);
}

// 전달된 참조를 반환하는 것은 허용됩니다.
// 그러나 올바른 생명주기가 반환되어야 합니다.
fn pass_x<'a, 'b>(x: &'a i32, _: &'b i32) -> &'a i32 { x }

//fn invalid_output<'a>() -> &'a String { &String::from("foo") }
// 위는 유효하지 않습니다: `'a` 는 함수보다 오래 유지되어야 합니다.
// 여기서 `&String::from("foo")` 는 `String` 을 생성한 다음
// 참조를 생성합니다. 그런 다음 범위가 종료될 때 데이터가 삭제되어
// 유효하지 않은 데이터에 대한 참조가 반환됩니다.

fn main() {
    let x = 7;
    let y = 9;

    print_one(&x);
    print_multi(&x, &y);

    let z = pass_x(&x, &y);
    print_one(z);

    let mut t = 3;
    add_one(&mut t);
    print_one(&t);
}
```
