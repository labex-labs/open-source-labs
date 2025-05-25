# 데이터 타입 (Data Types)

Rust 의 모든 값은 특정 **데이터 타입 (data type)**을 가지며, 이는 Rust 에게 어떤 종류의 데이터가 지정되었는지 알려주어 해당 데이터를 어떻게 처리해야 하는지 알 수 있게 합니다. 우리는 두 가지 데이터 타입 하위 집합, 즉 스칼라 (scalar) 와 컴파운드 (compound) 를 살펴보겠습니다.

Rust 는 **정적으로 타입이 지정된 (statically typed)** 언어라는 점을 기억하십시오. 즉, 컴파일 시간에 모든 변수의 타입을 알아야 합니다. 컴파일러는 일반적으로 값과 사용 방식을 기반으로 우리가 사용하려는 타입을 추론할 수 있습니다. "Comparing the Guess to the Secret Number"에서 `parse`를 사용하여 `String`을 숫자 타입으로 변환하는 경우와 같이 여러 타입이 가능한 경우에는 다음과 같이 타입 어노테이션 (type annotation) 을 추가해야 합니다.

```rust
let guess: u32 = "42".parse().expect("Not a number!");
```

위 코드에 표시된 `: u32` 타입 어노테이션을 추가하지 않으면 Rust 는 다음과 같은 오류를 표시합니다. 이는 컴파일러가 우리가 사용하려는 타입을 알기 위해 우리로부터 더 많은 정보가 필요하다는 의미입니다.

```bash
$ cargo build
   Compiling no_type_annotations v0.1.0 (file:///projects/no_type_annotations)
error[E0282]: type annotations needed
 --> src/main.rs:2:9
  |
2 |     let guess = "42".parse().expect("Not a number!");
  |         ^^^^^ consider giving `guess` a type
```

다른 데이터 타입에 대해서는 다른 타입 어노테이션을 보게 될 것입니다.
