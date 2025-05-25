# `assert_eq!` 및 `assert_ne!` 매크로를 사용한 동등성 테스트

기능을 확인하는 일반적인 방법은 테스트 중인 코드의 결과와 코드가 반환할 것으로 예상하는 값 간의 동등성을 테스트하는 것입니다. `assert!` 매크로를 사용하고 `==` 연산자를 사용하는 표현식을 전달하여 이 작업을 수행할 수 있습니다. 그러나 이것은 매우 일반적인 테스트이므로 표준 라이브러리는 이 테스트를 보다 편리하게 수행하기 위해 `assert_eq!` 및 `assert_ne!`라는 한 쌍의 매크로를 제공합니다. 이러한 매크로는 각각 두 인수를 동등성 또는 비동등성에 대해 비교합니다. 또한 어서션 (assertion) 이 실패하면 두 값을 인쇄하여 테스트가 _왜_ 실패했는지 더 쉽게 확인할 수 있습니다. 반대로, `assert!` 매크로는 `==` 표현식에 대해 `false` 값을 얻었다는 것만 나타내며, `false` 값을 초래한 값을 인쇄하지 않습니다.

Listing 11-7 에서 매개변수에 `2`를 더하는 `add_two`라는 함수를 작성한 다음 `assert_eq!` 매크로를 사용하여 이 함수를 테스트합니다.

파일 이름: `src/lib.rs`

```rust
pub fn add_two(a: i32) -> i32 {
    a + 2
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_adds_two() {
        assert_eq!(4, add_two(2));
    }
}
```

Listing 11-7: `assert_eq!` 매크로를 사용하여 `add_two` 함수 테스트

통과하는지 확인해 봅시다!

    running 1 test
    test tests::it_adds_two ... ok

    test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s

`assert_eq!`에 `4`를 인수로 전달했는데, 이는 `add_two(2)`를 호출한 결과와 같습니다. 이 테스트에 대한 줄은 `test tests::it_adds_two ... ok`이고, `ok` 텍스트는 테스트가 통과했음을 나타냅니다!

`assert_eq!`가 실패할 때 어떻게 보이는지 확인하기 위해 코드에 버그를 도입해 보겠습니다. `add_two` 함수의 구현을 변경하여 대신 `3`을 더하도록 합니다.

```rust
pub fn add_two(a: i32) -> i32 {
    a + 3
}
```

테스트를 다시 실행합니다.

    running 1 test
    test tests::it_adds_two ... FAILED

    failures:

    ---- tests::it_adds_two stdout ----
    1 thread 'main' panicked at 'assertion failed: `(left == right)`
    2   left: `4`,
    3  right: `5`', src/lib.rs:11:9
    note: run with `RUST_BACKTRACE=1` environment variable to display
    a backtrace

    failures:
        tests::it_adds_two

    test result: FAILED. 0 passed; 1 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s

테스트가 버그를 잡았습니다! `it_adds_two` 테스트가 실패했고, 메시지는 실패한 어서션이 `assertion failed:`(left == right)\``[1]이고`left`[2] 및`right`[3] 값이 무엇인지 알려줍니다. 이 메시지는 디버깅을 시작하는 데 도움이 됩니다. `left`인수는`4`였지만 `add_two(2)`가 있는 `right`인수는`5`였습니다. 테스트가 많이 진행될 때 특히 도움이 될 것이라고 상상할 수 있습니다.

일부 언어 및 테스트 프레임워크에서 동등성 어서션 (assertion) 함수의 매개변수를 `expected` 및 `actual`이라고 부르며, 인수를 지정하는 순서가 중요합니다. 그러나 Rust 에서는 `left` 및 `right`라고 부르며, 예상하는 값과 코드가 생성하는 값을 지정하는 순서는 중요하지 않습니다. 이 테스트에서 어서션을 `assert_eq!(add_two(2), 4)`로 작성할 수 있으며, 이는 `assertion failed:`(left == right)\``을 표시하는 동일한 실패 메시지를 생성합니다.

`assert_ne!` 매크로는 제공된 두 값이 같지 않으면 통과하고 같으면 실패합니다. 이 매크로는 값이 무엇인지 확실하지 않지만 값이 확실히 _아니어야_ 하는 경우에 가장 유용합니다. 예를 들어, 입력을 어떤 방식으로 변경하는 것이 보장되지만 입력이 변경되는 방식이 테스트를 실행하는 요일에 따라 달라지는 함수를 테스트하는 경우, 어서션하는 가장 좋은 방법은 함수의 출력이 입력과 같지 않다는 것입니다.

내부적으로 `assert_eq!` 및 `assert_ne!` 매크로는 각각 `==` 및 `!=` 연산자를 사용합니다. 어서션이 실패하면 이러한 매크로는 디버그 형식 지정을 사용하여 인수를 인쇄합니다. 즉, 비교되는 값은 `PartialEq` 및 `Debug` 트레이트를 구현해야 합니다. 모든 기본 유형과 대부분의 표준 라이브러리 유형은 이러한 트레이트를 구현합니다. 직접 정의하는 구조체 (struct) 및 열거형 (enum) 의 경우 해당 유형의 동등성을 어서션 (assertion) 하려면 `PartialEq`를 구현해야 합니다. 또한 어서션이 실패할 때 값을 인쇄하려면 `Debug`를 구현해야 합니다. 두 트레이트 모두 Listing 5-12 에서 언급했듯이 파생 가능한 트레이트이므로 일반적으로 `#[derive(PartialEq, Debug)]` 주석을 구조체 또는 열거형 정의에 추가하는 것만큼 간단합니다. 이러한 파생 가능한 트레이트에 대한 자세한 내용은 부록 C 를 참조하십시오.
