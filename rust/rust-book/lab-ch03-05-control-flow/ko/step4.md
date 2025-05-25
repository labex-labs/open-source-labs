# let 문에서 if 사용하기

`if`는 표현식이므로, Listing 3-2 와 같이 결과를 변수에 할당하기 위해 `let` 문의 오른쪽에 사용할 수 있습니다.

파일 이름: `src/main.rs`

```rust
fn main() {
    let condition = true;
    let number = if condition { 5 } else { 6 };

    println!("The value of number is: {number}");
}
```

Listing 3-2: `if` 표현식의 결과를 변수에 할당하기

`number` 변수는 `if` 표현식의 결과에 따라 값에 바인딩됩니다. 이 코드를 실행하여 어떤 일이 발생하는지 확인하십시오.

```bash
$ cargo run
   Compiling branches v0.1.0 (file:///projects/branches)
    Finished dev [unoptimized + debuginfo] target(s) in 0.30s
     Running `target/debug/branches`
The value of number is: 5
```

코드 블록은 마지막 표현식으로 평가되고, 숫자 자체도 표현식이라는 것을 기억하십시오. 이 경우 전체 `if` 표현식의 값은 어떤 코드 블록이 실행되는지에 따라 달라집니다. 즉, `if`의 각 arm 에서 결과가 될 수 있는 값은 동일한 유형이어야 합니다. Listing 3-2 에서 `if` arm 과 `else` arm 의 결과는 모두 `i32` 정수였습니다. 다음 예와 같이 유형이 일치하지 않으면 오류가 발생합니다.

파일 이름: `src/main.rs`

```rust
fn main() {
    let condition = true;

    let number = if condition { 5 } else { "six" };

    println!("The value of number is: {number}");
}
```

이 코드를 컴파일하려고 하면 오류가 발생합니다. `if`와 `else` arm 은 호환되지 않는 값 유형을 가지며, Rust 는 프로그램에서 문제가 있는 정확한 위치를 나타냅니다.

```bash
$ cargo run
   Compiling branches v0.1.0 (file:///projects/branches)
error[E0308]: `if` and `else` have incompatible types
 --> src/main.rs:4:44
  |
4 |     let number = if condition { 5 } else { "six" };
  |                                 -          ^^^^^ expected integer, found
`&str`
  |                                 |
  |                                 expected because of this
```

`if` 블록의 표현식은 정수로 평가되고, `else` 블록의 표현식은 문자열로 평가됩니다. 변수는 단일 유형을 가져야 하고, Rust 는 컴파일 시간에 `number` 변수의 유형을 확실하게 알아야 하므로 이 방법은 작동하지 않습니다. `number`의 유형을 알면 컴파일러가 `number`를 사용하는 모든 곳에서 유형이 유효한지 확인할 수 있습니다. `number`의 유형이 런타임에만 결정된다면 Rust 는 그렇게 할 수 없을 것입니다. 컴파일러는 더 복잡해지고, 모든 변수에 대해 여러 가상 유형을 추적해야 하는 경우 코드에 대한 보장을 줄일 것입니다.
