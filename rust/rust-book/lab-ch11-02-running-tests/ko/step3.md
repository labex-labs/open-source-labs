# 함수 출력 표시

기본적으로, 테스트가 통과하면 Rust 의 테스트 라이브러리는 표준 출력에 인쇄된 모든 것을 캡처합니다. 예를 들어, 테스트에서 `println!`을 호출하고 테스트가 통과하면 터미널에서 `println!` 출력을 볼 수 없습니다. 테스트가 통과했음을 나타내는 줄만 보게 됩니다. 테스트가 실패하면 실패 메시지의 나머지 부분과 함께 표준 출력에 인쇄된 모든 것을 보게 됩니다.

예를 들어, Listing 11-10 에는 매개변수 값을 인쇄하고 10 을 반환하는 어리석은 함수와 통과하는 테스트 및 실패하는 테스트가 있습니다.

Filename: `src/lib.rs`

```rust
fn prints_and_returns_10(a: i32) -> i32 {
    println!("I got the value {a}");
    10
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn this_test_will_pass() {
        let value = prints_and_returns_10(4);
        assert_eq!(10, value);
    }

    #[test]
    fn this_test_will_fail() {
        let value = prints_and_returns_10(8);
        assert_eq!(5, value);
    }
}
```

Listing 11-10: `println!`을 호출하는 함수에 대한 테스트

`cargo test`로 이러한 테스트를 실행하면 다음과 같은 출력이 표시됩니다.

    running 2 tests
    test tests::this_test_will_pass ... ok
    test tests::this_test_will_fail ... FAILED

    failures:

    ---- tests::this_test_will_fail stdout ----
    1 I got the value 8
    thread 'main' panicked at 'assertion failed: `(left == right)`
      left: `5`,
     right: `10`', src/lib.rs:19:9
    note: run with `RUST_BACKTRACE=1` environment variable to display
    a backtrace

    failures:
        tests::this_test_will_fail

    test result: FAILED. 1 passed; 1 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s

이 출력 어디에서도 테스트가 통과할 때 인쇄되는 `I got the value 4`를 볼 수 없습니다. 해당 출력은 캡처되었습니다. 실패한 테스트의 출력인 `I got the value 8` \[1]은 테스트 요약 출력 섹션에 나타나며, 테스트 실패의 원인도 표시합니다.

통과하는 테스트의 인쇄된 값도 보려면 `--show-output`을 사용하여 성공적인 테스트의 출력도 표시하도록 Rust 에 지시할 수 있습니다.

```bash
cargo test -- --show-output
```

Listing 11-10 의 테스트를 `--show-output` 플래그로 다시 실행하면 다음과 같은 출력이 표시됩니다.

    running 2 tests
    test tests::this_test_will_pass ... ok
    test tests::this_test_will_fail ... FAILED

    successes:

    ---- tests::this_test_will_pass stdout ----
    I got the value 4


    successes:
        tests::this_test_will_pass

    failures:

    ---- tests::this_test_will_fail stdout ----
    I got the value 8
    thread 'main' panicked at 'assertion failed: `(left == right)`
      left: `5`,
     right: `10`', src/lib.rs:19:9
    note: run with `RUST_BACKTRACE=1` environment variable to display
    a backtrace

    failures:
        tests::this_test_will_fail

    test result: FAILED. 1 passed; 1 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s
