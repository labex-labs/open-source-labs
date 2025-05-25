# 섀도잉 (Shadowing)

2 장의 추측 게임 튜토리얼에서 보았듯이, 이전 변수와 동일한 이름으로 새 변수를 선언할 수 있습니다. Rust 개발자들은 첫 번째 변수가 두 번째 변수에 의해 *섀도잉 (shadowed)*된다고 말합니다. 이는 변수의 이름을 사용할 때 컴파일러가 두 번째 변수를 보게 된다는 의미입니다. 실제로, 두 번째 변수는 첫 번째 변수를 가리고, 해당 변수 이름의 모든 사용을 자체적으로 가져가며, 자체적으로 섀도잉되거나 범위가 종료될 때까지 유지됩니다. 다음과 같이 동일한 변수 이름을 사용하고 `let` 키워드를 반복하여 변수를 섀도잉할 수 있습니다.

파일 이름: `src/main.rs`

```rust
fn main() {
    let x = 5;

    let x = x + 1;

    {
        let x = x * 2;
        println!("The value of x in the inner scope is: {x}");
    }

    println!("The value of x is: {x}");
}
```

이 프로그램은 먼저 `x`를 값 `5`에 바인딩합니다. 그런 다음 `let x =`를 반복하여 새 변수 `x`를 생성하고, 원래 값을 가져와 `1`을 더하여 `x`의 값이 `6`이 됩니다. 그런 다음 중괄호로 생성된 내부 범위 내에서 세 번째 `let` 문도 `x`를 섀도잉하고 새 변수를 생성하여 이전 값에 `2`를 곱하여 `x`의 값을 `12`로 만듭니다. 해당 범위가 끝나면 내부 섀도잉이 종료되고 `x`는 다시 `6`이 됩니다. 이 프로그램을 실행하면 다음과 같은 출력이 표시됩니다.

```bash
$ cargo run
   Compiling variables v0.1.0 (file:///projects/variables)
    Finished dev [unoptimized + debuginfo] target(s) in 0.31s
     Running `target/debug/variables`
The value of x in the inner scope is: 12
The value of x is: 6
```

섀도잉은 변수를 `mut`로 표시하는 것과 다릅니다. `let` 키워드를 사용하지 않고 이 변수에 실수로 다시 할당하려고 하면 컴파일 시간 오류가 발생하기 때문입니다. `let`을 사용하면 값에 대해 몇 가지 변환을 수행할 수 있지만, 해당 변환이 완료된 후에는 변수가 불변으로 유지됩니다.

`mut`와 섀도잉의 또 다른 차이점은 `let` 키워드를 다시 사용할 때 효과적으로 새 변수를 생성하기 때문에 값의 타입을 변경할 수 있지만 동일한 이름을 재사용할 수 있다는 것입니다. 예를 들어, 프로그램이 사용자에게 텍스트 사이에 원하는 공백 수를 공백 문자를 입력하여 표시하도록 요청한 다음 해당 입력을 숫자로 저장하려는 경우를 생각해 보겠습니다.

```rust
let spaces = "   ";
let spaces = spaces.len();
```

첫 번째 `spaces` 변수는 문자열 타입이고, 두 번째 `spaces` 변수는 숫자 타입입니다. 따라서 섀도잉은 `spaces_str` 및 `spaces_num`과 같은 다른 이름을 생각해내야 하는 수고를 덜어줍니다. 대신, 더 간단한 `spaces` 이름을 재사용할 수 있습니다. 그러나 여기에 표시된 것처럼 이 작업을 위해 `mut`를 사용하려고 하면 컴파일 시간 오류가 발생합니다.

```rust
let mut spaces = "   ";
spaces = spaces.len();
```

오류는 변수의 타입을 변경할 수 없다고 말합니다.

```bash
$ cargo run
   Compiling variables v0.1.0 (file:///projects/variables)
error[E0308]: mismatched types
 --> src/main.rs:3:14
  |
2 |     let mut spaces = "   ";
  |                      ----- expected due to this value
3 |     spaces = spaces.len();
  |              ^^^^^^^^^^^^ expected `&str`, found `usize`
```

이제 변수가 작동하는 방식을 살펴보았으므로, 변수가 가질 수 있는 더 많은 데이터 타입을 살펴보겠습니다.
