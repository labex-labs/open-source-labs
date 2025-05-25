# Debug (디버그)

`std::fmt` 형식 지정 `trait`를 사용하려는 모든 타입은 출력을 위한 구현이 필요합니다. 자동 구현은 `std` 라이브러리와 같은 타입에 대해서만 제공됩니다. 다른 모든 타입은 _반드시_ 어떤 방식으로든 수동으로 구현되어야 합니다.

`fmt::Debug` `trait`는 이를 매우 간단하게 만들어줍니다. _모든_ 타입은 `fmt::Debug` 구현을 `derive` (자동으로 생성) 할 수 있습니다. 이는 `fmt::Display`에는 해당되지 않으며, `fmt::Display`는 수동으로 구현해야 합니다.

```rust
// This structure cannot be printed either with `fmt::Display` or
// with `fmt::Debug`.
struct UnPrintable(i32);

// The `derive` attribute automatically creates the implementation
// required to make this `struct` printable with `fmt::Debug`.
#[derive(Debug)]
struct DebugPrintable(i32);
```

모든 `std` 라이브러리 타입은 `{:?}`로도 자동으로 출력 가능합니다.

```rust
// Derive the `fmt::Debug` implementation for `Structure`. `Structure`
// is a structure which contains a single `i32`.
#[derive(Debug)]
struct Structure(i32);

// Put a `Structure` inside of the structure `Deep`. Make it printable
// also.
#[derive(Debug)]
struct Deep(Structure);

fn main() {
    // Printing with `{:?}` is similar to with `{}`.
    println!("{:?} months in a year.", 12);
    println!("{1:?} {0:?} is the {actor:?} name.",
             "Slater",
             "Christian",
             actor="actor's");

    // `Structure` is printable!
    println!("Now {:?} will print!", Structure(3));

    // The problem with `derive` is there is no control over how
    // the results look. What if I want this to just show a `7`?
    println!("Now {:?} will print!", Deep(Structure(7)));
}
```

따라서 `fmt::Debug`는 확실히 출력을 가능하게 하지만, 약간의 우아함을 희생합니다. Rust 는 또한 `{:#?}`를 사용한 "pretty printing"을 제공합니다.

```rust
#[derive(Debug)]
struct Person<'a> {
    name: &'a str,
    age: u8
}

fn main() {
    let name = "Peter";
    let age = 27;
    let peter = Person { name, age };

    // Pretty print
    println!("{:#?}", peter);
}
```

`fmt::Display`를 수동으로 구현하여 표시를 제어할 수 있습니다.
