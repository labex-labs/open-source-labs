# 변수와 가변성 (Mutability)

"변수로 값 저장하기"에서 언급했듯이, 기본적으로 변수는 불변 (immutable) 입니다. 이는 Rust 가 안전성과 Rust 가 제공하는 쉬운 동시성을 활용할 수 있도록 코드를 작성하도록 유도하는 많은 방법 중 하나입니다. 하지만, 여전히 변수를 가변 (mutable) 하게 만들 수 있는 옵션이 있습니다. Rust 가 왜 불변성을 선호하도록 권장하는지, 그리고 때로는 왜 이를 벗어나고 싶을 수 있는지 살펴보겠습니다.

변수가 불변일 때, 값이 이름에 바인딩되면 해당 값을 변경할 수 없습니다. 이를 설명하기 위해, `cargo new variables`를 사용하여 `project` 디렉토리에 *variables*라는 새 프로젝트를 생성합니다.

그런 다음, 새 `variables` 디렉토리에서 `src/main.rs`를 열고 코드를 다음 코드로 바꿉니다. 아직 컴파일되지 않습니다.

파일 이름: `src/main.rs`

```rust
fn main() {
    let x = 5;
    println!("The value of x is: {x}");
    x = 6;
    println!("The value of x is: {x}");
}
```

`cargo run`을 사용하여 프로그램을 저장하고 실행합니다. 다음 출력과 같이 불변성 오류와 관련된 오류 메시지를 받게 됩니다.

```bash
$ cargo run
   Compiling variables v0.1.0 (file:///projects/variables)
error[E0384]: cannot assign twice to immutable variable `x`
 --> src/main.rs:4:5
  |
2 |     let x = 5;
  |         -
  |         |
  |         first assignment to `x`
  |         help: consider making this binding mutable: `mut x`
3 |     println!("The value of x is: {x}");
4 |     x = 6;
  |     ^^^^^ cannot assign twice to immutable variable
```

이 예제는 컴파일러가 프로그램에서 오류를 찾는 데 어떻게 도움이 되는지 보여줍니다. 컴파일러 오류는 좌절감을 줄 수 있지만, 실제로 이는 프로그램이 원하는 대로 안전하게 작동하지 않는다는 의미일 뿐입니다. 이는 여러분이 훌륭한 프로그래머가 아니라는 의미가 _아닙니다_! 숙련된 Rust 개발자 (Rustacean) 도 여전히 컴파일러 오류를 겪습니다.

`x` 불변 변수에 두 번째 값을 할당하려고 시도했기 때문에 `cannot assign twice to immutable variable`x`` 오류 메시지를 받았습니다.

불변으로 지정된 값을 변경하려고 시도할 때 컴파일 시간 오류가 발생하는 것은 중요합니다. 이러한 상황이 버그로 이어질 수 있기 때문입니다. 코드의 한 부분이 값이 절대 변경되지 않는다는 가정하에 작동하고, 코드의 다른 부분이 해당 값을 변경하는 경우, 코드의 첫 번째 부분이 설계된 대로 작동하지 않을 수 있습니다. 이러한 종류의 버그의 원인은, 특히 두 번째 코드 조각이 값을 _때때로_ 변경하는 경우, 사후에 추적하기 어려울 수 있습니다. Rust 컴파일러는 값이 변경되지 않는다고 선언하면 실제로 변경되지 않도록 보장하므로, 직접 추적할 필요가 없습니다. 따라서 코드를 더 쉽게 추론할 수 있습니다.

하지만 가변성은 매우 유용할 수 있으며, 코드를 더 편리하게 작성할 수 있게 해줍니다. 변수는 기본적으로 불변이지만, 2 장에서 했던 것처럼 변수 이름 앞에 `mut`를 추가하여 가변하게 만들 수 있습니다. `mut`를 추가하면 코드의 미래 독자에게 이 변수의 값을 변경할 것임을 나타내어 의도를 전달합니다.

예를 들어, `src/main.rs`를 다음과 같이 변경해 보겠습니다.

파일 이름: `src/main.rs`

```rust
fn main() {
    let mut x = 5;
    println!("The value of x is: {x}");
    x = 6;
    println!("The value of x is: {x}");
}
```

이제 프로그램을 실행하면 다음과 같은 결과를 얻습니다.

```bash
$ cargo run
   Compiling variables v0.1.0 (file:///projects/variables)
    Finished dev [unoptimized + debuginfo] target(s) in 0.30s
     Running `target/debug/variables`
The value of x is: 5
The value of x is: 6
```

`mut`를 사용하면 `x`에 바인딩된 값을 `5`에서 `6`으로 변경할 수 있습니다. 궁극적으로, 가변성을 사용할지 여부를 결정하는 것은 여러분에게 달려 있으며, 특정 상황에서 무엇이 가장 명확하다고 생각하는지에 따라 달라집니다.
