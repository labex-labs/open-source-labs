# 연산자 오버로딩 (Operator Overloading)

Rust 에서는 많은 연산자를 트레이트를 통해 오버로딩할 수 있습니다. 즉, 일부 연산자는 입력 인수에 따라 다른 작업을 수행하는 데 사용될 수 있습니다. 이는 연산자가 메서드 호출에 대한 구문적 설탕이기 때문에 가능합니다. 예를 들어, `a + b`에서 `+` 연산자는 `add` 메서드 (예: `a.add(b)`) 를 호출합니다. 이 `add` 메서드는 `Add` 트레이트의 일부입니다. 따라서 `+` 연산자는 `Add` 트레이트를 구현하는 모든 객체에서 사용할 수 있습니다.

`Add`와 같이 연산자를 오버로딩하는 트레이트 목록은 `core::ops`에서 찾을 수 있습니다.

```rust
use std::ops;

struct Foo;
struct Bar;

#[derive(Debug)]
struct FooBar;

#[derive(Debug)]
struct BarFoo;

// `std::ops::Add` 트레이트는 `+` 의 기능을 지정하는 데 사용됩니다.
// 여기서는 `Add<Bar>` 를 만듭니다. 즉, 타입 `Bar` 의 RHS(Right-Hand Side) 와의 덧셈을 위한 트레이트입니다.
// 다음 블록은 연산: Foo + Bar = FooBar 를 구현합니다.
impl ops::Add<Bar> for Foo {
    type Output = FooBar;

    fn add(self, _rhs: Bar) -> FooBar {
        println!("> Foo.add(Bar) was called");

        FooBar
    }
}

// 타입을 반전시켜 비가환 덧셈을 구현합니다.
// 여기서는 `Add<Foo>` 를 만듭니다. 즉, 타입 `Foo` 의 RHS 와의 덧셈을 위한 트레이트입니다.
// 이 블록은 연산: Bar + Foo = BarFoo 를 구현합니다.
impl ops::Add<Foo> for Bar {
    type Output = BarFoo;

    fn add(self, _rhs: Foo) -> BarFoo {
        println!("> Bar.add(Foo) was called");

        BarFoo
    }
}

fn main() {
    println!("Foo + Bar = {:?}", Foo + Bar);
    println!("Bar + Foo = {:?}", Bar + Foo);
}
```
