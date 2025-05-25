# 구조체

마찬가지로, `struct`는 다음과 같이 분해될 수 있습니다.

```rust
fn main() {
    struct Foo {
        x: (u32, u32),
        y: u32,
    }

    // 구조체 내 값을 변경하여 결과를 확인해 보세요
    let foo = Foo { x: (1, 2), y: 3 };

    match foo {
        Foo { x: (1, b), y } => println!("x 의 첫 번째 값은 1, b = {}, y = {} ", b, y),

        // 구조체를 분해하고 변수 이름을 바꿀 수도 있습니다.
        // 순서는 중요하지 않습니다.
        Foo { y: 2, x: i } => println!("y 는 2, i = {:?}", i),

        // 일부 변수를 무시할 수도 있습니다.
        Foo { y, .. } => println!("y = {}, x 는 신경 쓰지 않습니다", y),
        // 이것은 오류를 발생시킵니다: 패턴이 필드 `x` 를 언급하지 않습니다
        //Foo { y } => println!("y = {}", y),
    }

    let faa = Foo { x: (1, 2), y: 3 };

    // 구조체를 분해하기 위해 match 블록이 필요하지 않습니다.
    let Foo { x: x0, y: y0 } = faa;
    println!("외부: x0 = {x0:?}, y0 = {y0}");
}
```
