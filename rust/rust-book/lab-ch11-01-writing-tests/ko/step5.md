# 사용자 지정 실패 메시지 추가

`assert!`, `assert_eq!`, 및 `assert_ne!` 매크로에 선택적 인수로 실패 메시지와 함께 인쇄할 사용자 지정 메시지를 추가할 수도 있습니다. 필수 인수 뒤에 지정된 모든 인수는 "더하기 연산자 또는 format! 매크로를 사용한 연결"에서 논의된 `format!` 매크로로 전달되므로, `{}` 자리 표시자와 해당 자리 표시자에 들어갈 값을 포함하는 형식 문자열을 전달할 수 있습니다. 사용자 지정 메시지는 어서션 (assertion) 의 의미를 문서화하는 데 유용합니다. 테스트가 실패하면 코드에 어떤 문제가 있는지 더 잘 알 수 있습니다.

예를 들어, 사람들에게 이름을 사용하여 인사를 하는 함수가 있고 함수에 전달하는 이름이 출력에 나타나는지 테스트하려는 경우를 가정해 보겠습니다.

파일 이름: `src/lib.rs`

```rust
pub fn greeting(name: &str) -> String {
    format!("Hello {name}!")
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn greeting_contains_name() {
        let result = greeting("Carol");
        assert!(result.contains("Carol"));
    }
}
```

이 프로그램에 대한 요구 사항은 아직 합의되지 않았으며, 인사말 시작 부분의 `Hello` 텍스트가 변경될 것이라고 확신합니다. 요구 사항이 변경될 때 테스트를 업데이트할 필요가 없도록 결정했으므로, `greeting` 함수에서 반환된 값과 정확한 동등성을 확인하는 대신 출력에 입력 매개변수의 텍스트가 포함되어 있는지 어서션 (assertion) 합니다.

이제 `greeting`을 변경하여 `name`을 제외하여 이 코드에 버그를 도입하여 기본 테스트 실패가 어떻게 보이는지 살펴보겠습니다.

```rust
pub fn greeting(name: &str) -> String {
    String::from("Hello!")
}
```

이 테스트를 실행하면 다음이 생성됩니다.

    running 1 test
    test tests::greeting_contains_name ... FAILED

    failures:

    ---- tests::greeting_contains_name stdout ----
    thread 'main' panicked at 'assertion failed:
    result.contains(\"Carol\")', src/lib.rs:12:9
    note: run with `RUST_BACKTRACE=1` environment variable to display
    a backtrace


    failures:
        tests::greeting_contains_name

이 결과는 어서션이 실패했고 어서션이 있는 줄을 나타냅니다. 더 유용한 실패 메시지는 `greeting` 함수에서 값을 인쇄합니다. `greeting` 함수에서 얻은 실제 값으로 채워진 자리 표시자가 있는 형식 문자열로 구성된 사용자 지정 실패 메시지를 추가해 보겠습니다.

    #[test]
    fn greeting_contains_name() {
        let result = greeting("Carol");
        assert!(
            result.contains("Carol"),
            "Greeting did not contain name, value was `{result}`"
        );
    }

이제 테스트를 실행하면 더 많은 정보를 제공하는 오류 메시지가 표시됩니다.

    ---- tests::greeting_contains_name stdout ----
    thread 'main' panicked at 'Greeting did not contain name, value
    was `Hello!`', src/lib.rs:12:9
    note: run with `RUST_BACKTRACE=1` environment variable to display
    a backtrace

테스트 출력에서 실제로 얻은 값을 볼 수 있으며, 이는 예상되는 것이 아니라 발생한 문제를 디버깅하는 데 도움이 됩니다.
