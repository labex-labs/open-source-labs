# else if 를 사용하여 여러 조건 처리하기

`else if` 표현식에서 `if`와 `else`를 결합하여 여러 조건을 사용할 수 있습니다. 예를 들어:

파일 이름: `src/main.rs`

```rust
fn main() {
    let number = 6;

    if number % 4 == 0 {
        println!("number is divisible by 4");
    } else if number % 3 == 0 {
        println!("number is divisible by 3");
    } else if number % 2 == 0 {
        println!("number is divisible by 2");
    } else {
        println!("number is not divisible by 4, 3, or 2");
    }
}
```

이 프로그램에는 실행할 수 있는 네 가지 경로가 있습니다. 실행 후 다음 출력을 볼 수 있습니다.

```bash
$ cargo run
   Compiling branches v0.1.0 (file:///projects/branches)
    Finished dev [unoptimized + debuginfo] target(s) in 0.31s
     Running `target/debug/branches`
number is divisible by 3
```

이 프로그램이 실행되면 각 `if` 표현식을 차례로 확인하고 조건이 `true`로 평가되는 첫 번째 본문을 실행합니다. 6 이 2 로 나누어 떨어지더라도 `number is divisible by 2` 출력이 표시되지 않으며, `else` 블록의 `number is not divisible by 4, 3, or 2` 텍스트도 표시되지 않습니다. 이는 Rust 가 첫 번째 `true` 조건에 대한 블록만 실행하고, 하나를 찾으면 나머지는 확인하지 않기 때문입니다.

`else if` 표현식을 너무 많이 사용하면 코드가 복잡해질 수 있으므로, 여러 개가 있는 경우 코드를 리팩터링하는 것이 좋습니다. 6 장에서는 이러한 경우에 사용할 수 있는 강력한 Rust 분기 구조인 `match`에 대해 설명합니다.
