# 숫자 연산 (Numeric Operations)

Rust 는 모든 숫자 타입에 대해 예상할 수 있는 기본적인 수학 연산을 지원합니다: 덧셈, 뺄셈, 곱셈, 나눗셈 및 나머지 연산입니다. 정수 나눗셈은 가장 가까운 정수로 0 방향으로 잘립니다. 다음 코드는 각 숫자 연산을 `let` 문에서 사용하는 방법을 보여줍니다.

파일 이름: `src/main.rs`

```rust
fn main() {
    // 덧셈 (addition)
    let sum = 5 + 10;

    // 뺄셈 (subtraction)
    let difference = 95.5 - 4.3;

    // 곱셈 (multiplication)
    let product = 4 * 30;

    // 나눗셈 (division)
    let quotient = 56.7 / 32.2;
    let truncated = -5 / 3; // 결과는 -1

    // 나머지 (remainder)
    let remainder = 43 % 5;
}
```

이러한 문장의 각 표현식은 수학 연산자를 사용하고 단일 값으로 평가되며, 이 값은 변수에 바인딩됩니다. 부록 B 에는 Rust 가 제공하는 모든 연산자 목록이 있습니다.
