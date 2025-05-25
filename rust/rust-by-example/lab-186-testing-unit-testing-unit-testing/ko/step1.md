# 단위 테스트

테스트는 Rust 함수로서 테스트 대상이 아닌 코드가 예상대로 작동하는지 확인합니다. 테스트 함수의 본문은 일반적으로 일부 설정을 수행하고, 테스트하려는 코드를 실행한 다음, 결과가 예상대로인지 확인합니다.

대부분의 단위 테스트는 `tests` 모듈에 `#[cfg(test)]` 특성과 함께 들어갑니다. 테스트 함수는 `#[test]` 특성으로 표시됩니다.

테스트 함수에서 예외가 발생하면 테스트가 실패합니다. 몇 가지 도움말 매크로가 있습니다.

- `assert!(expression)` - expression 이 `false`로 평가되면 예외를 발생시킵니다.
- `assert_eq!(left, right)` 및 `assert_ne!(left, right)` - 각각 left 와 right 표현식이 같거나 다름을 테스트합니다.

```rust
pub fn add(a: i32, b: i32) -> i32 {
    a + b
}

// 이것은 실제로 좋지 않은 더하기 함수이며, 이 예제에서 실패하는 것이 목적입니다.
#[allow(dead_code)]
fn bad_add(a: i32, b: i32) -> i32 {
    a - b
}

#[cfg(test)]
mod tests {
    // 이 유용한 구문을 참고하세요: 외부 범위 (mod 테스트용) 에서 이름 가져오기.
    use super::*;

    #[test]
    fn test_add() {
        assert_eq!(add(1, 2), 3);
    }

    #[test]
    fn test_bad_add() {
        // 이 assert 는 실행되고 테스트가 실패합니다.
        // 개인 함수도 테스트할 수 있음을 참고하세요!
        assert_eq!(bad_add(1, 2), 3);
    }
}
```

테스트는 `cargo test`를 사용하여 실행할 수 있습니다.

```shell
$ cargo test

running 2 tests
test tests::test_bad_add ... 실패
test tests::test_add ... ok

실패 사항:

---- tests::test_bad_add stdout ----
스레드 'tests::test_bad_add'에서 'assertion failed: `(left == right)`
  left: `-1`,
 right: `3`'라는 메시지로 패닉 발생, src/lib.rs:21:8
참고: 백트레이스를 위해 $(RUST_BACKTRACE=1)로 실행하세요.

실패 사항:
tests::test_bad_add

테스트 결과: 실패. 1 통과
1 실패
0 무시
0 측정
0 필터링됨
```

## 테스트 및 `?`

이전 단위 테스트 예제 중 어느 것도 반환 형식이 없었습니다. 하지만 Rust 2018 에서는 단위 테스트가 `Result<()>`를 반환할 수 있으므로 `?`를 사용할 수 있습니다! 이렇게 하면 훨씬 간결해집니다.

```rust
fn sqrt(number: f64) -> Result<f64, String> {
    if number >= 0.0 {
        Ok(number.powf(0.5))
    } else {
        Err("음수 부동소수점은 제곱근이 없습니다".to_owned())
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_sqrt() -> Result<(), String> {
        let x = 4.0;
        assert_eq!(sqrt(x)?.powf(2.0), x);
        Ok(())
    }
}
```

자세한 내용은 "The Edition Guide"를 참조하세요.

## 패닉 테스트

특정 상황에서 패닉이 발생해야 하는 함수를 확인하려면 `#[should_panic]` 특성을 사용합니다. 이 특성은 패닉 메시지의 텍스트를 가진 선택적 매개변수 `expected =`를 받습니다. 함수가 여러 가지 방법으로 패닉이 발생할 수 있는 경우, 테스트가 올바른 패닉을 테스트하는지 확인하는 데 도움이 됩니다.

```rust
pub fn divide_non_zero_result(a: u32, b: u32) -> u32 {
    if b == 0 {
        panic!("Divide-by-zero error");
    } else if a < b {
        panic!("Divide result is zero");
    }
    a / b
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_divide() {
        assert_eq!(divide_non_zero_result(10, 2), 5);
    }

    #[test]
    #[should_panic]
    fn test_any_panic() {
        divide_non_zero_result(1, 0);
    }

    #[test]
    #[should_panic(expected = "Divide result is zero")]
    fn test_specific_panic() {
        divide_non_zero_result(1, 10);
    }
}
```

이러한 테스트를 실행하면 다음과 같습니다.

```shell
$ cargo test

running 3 tests
test tests::test_any_panic ... ok
test tests::test_divide ... ok
test tests::test_specific_panic ... ok

테스트 결과: ok. 3 통과
0 실패
0 무시
0 측정
0 필터링됨
```

## 특정 테스트 실행

특정 테스트를 실행하려면 `cargo test` 명령에 테스트 이름을 지정할 수 있습니다.

```shell
$ cargo test test_any_panic
running 1 test
test tests::test_any_panic ... ok

테스트 결과: ok. 1 통과
0 실패
0 무시
0 측정
2 필터링됨
```

여러 테스트를 실행하려면 실행할 테스트와 일치하는 테스트 이름의 일부를 지정할 수 있습니다.

```shell
$ cargo test panic
running 2 tests
test tests::test_any_panic ... ok
test tests::test_specific_panic ... ok

테스트 결과: ok. 2 통과
0 실패
0 무시
0 측정
1 필터링됨
```

## 테스트 무시

테스트는 `#[ignore]` 특성으로 표시하여 일부 테스트를 제외할 수 있습니다. 또는 `cargo test -- --ignored` 명령으로 실행할 수 있습니다.

```rust
pub fn add(a: i32, b: i32) -> i32 {
    a + b
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_add() {
        assert_eq!(add(2, 2), 4);
    }

    #[test]
    fn test_add_hundred() {
        assert_eq!(add(100, 2), 102);
        assert_eq!(add(2, 100), 102);
    }

    #[test]
    #[ignore]
    fn ignored_test() {
        assert_eq!(add(0, 0), 0);
    }
}
```

```shell
$ cargo test
running 3 tests
test tests::ignored_test ... 무시됨
test tests::test_add ... ok
test tests::test_add_hundred ... ok

테스트 결과: ok. 2 통과
0 실패
1 무시
0 측정
0 필터링됨

$ cargo test -- --ignored
running 1 test
test tests::ignored_test ... ok

테스트 결과: ok. 1 통과
0 실패
0 무시
0 측정
0 필터링됨
```
