# Result 를 사용하여 잠재적 실패 처리하기

우리는 여전히 이 코드 줄을 작업하고 있습니다. 이제 세 번째 텍스트 줄에 대해 논의하고 있지만, 여전히 단일 논리적 코드 줄의 일부임을 기억하십시오. 다음 부분은 이 메서드입니다.

```rust
.expect("Failed to read line");
```

이 코드를 다음과 같이 작성할 수도 있습니다.

```rust
io::stdin().read_line(&mut guess).expect("Failed to read line");
```

그러나 한 줄로 길게 작성하면 읽기 어려우므로 나누는 것이 좋습니다. `.method_name()` 구문을 사용하여 메서드를 호출할 때 긴 줄을 나누기 위해 줄 바꿈 및 기타 공백을 도입하는 것이 좋습니다. 이제 이 줄이 무엇을 하는지 논의해 보겠습니다.

앞서 언급했듯이, `read_line`은 사용자가 입력한 모든 내용을 우리가 전달한 문자열에 넣지만, 또한 `Result` 값을 반환합니다. `Result`는 _열거형_(enumeration) 이며, 종종 *enum*이라고 불리며, 여러 가능한 상태 중 하나일 수 있는 타입입니다. 각 가능한 상태를 _변형_(variant) 이라고 부릅니다.

6 장에서는 열거형에 대해 자세히 다룰 것입니다. 이러한 `Result` 타입의 목적은 오류 처리 정보를 인코딩하는 것입니다.

`Result`의 변형은 `Ok`와 `Err`입니다. `Ok` 변형은 작업이 성공했음을 나타내며, `Ok` 내부에는 성공적으로 생성된 값이 있습니다. `Err` 변형은 작업이 실패했음을 의미하며, `Err`에는 작업이 실패한 방법 또는 이유에 대한 정보가 포함되어 있습니다.

모든 타입의 값과 마찬가지로 `Result` 타입의 값에는 메서드가 정의되어 있습니다. `Result`의 인스턴스에는 호출할 수 있는 `expect` 메서드가 있습니다. 이 `Result`의 인스턴스가 `Err` 값인 경우, `expect`는 프로그램을 충돌시키고 `expect`에 인수로 전달한 메시지를 표시합니다. `read_line` 메서드가 `Err`를 반환하는 경우, 이는 기본 운영 체제에서 발생한 오류의 결과일 가능성이 큽니다. 이 `Result`의 인스턴스가 `Ok` 값인 경우, `expect`는 `Ok`가 가지고 있는 반환 값을 가져와서 해당 값만 반환하므로 사용할 수 있습니다. 이 경우, 해당 값은 사용자의 입력에 있는 바이트 수입니다.

`expect`를 호출하지 않으면 프로그램이 컴파일되지만 경고가 표시됩니다.

```bash
$ cargo build
   Compiling guessing_game v0.1.0 (file:///projects/guessing_game)
warning: unused `Result` that must be used
  --> src/main.rs:10:5
   |
10 |     io::stdin().read_line(&mut guess);
   |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
   |
   = note: `#[warn(unused_must_use)]` on by default
   = note: this `Result` may be an `Err` variant, which should be handled

warning: `guessing_game` (bin "guessing_game") generated 1 warning
    Finished dev [unoptimized + debuginfo] target(s) in 0.59s
```

Rust 는 `read_line`에서 반환된 `Result` 값을 사용하지 않았으며, 이는 프로그램이 가능한 오류를 처리하지 않았음을 나타냅니다.

경고를 억제하는 올바른 방법은 실제로 오류 처리 코드를 작성하는 것이지만, 이 경우 문제가 발생하면 프로그램을 충돌시키고 싶으므로 `expect`를 사용할 수 있습니다. 9 장에서 오류로부터 복구하는 방법에 대해 배우게 됩니다.
