# `should_panic`을 사용한 패닉 확인

반환 값을 확인하는 것 외에도 코드가 예상대로 오류 조건을 처리하는지 확인하는 것이 중요합니다. 예를 들어, Listing 9-13 에서 생성한 `Guess` 유형을 생각해 보십시오. `Guess`를 사용하는 다른 코드는 `Guess` 인스턴스가 1 에서 100 사이의 값만 포함한다는 보장에 의존합니다. 해당 범위를 벗어난 값으로 `Guess` 인스턴스를 생성하려고 하면 패닉이 발생하는지 확인하는 테스트를 작성할 수 있습니다.

이 작업은 테스트 함수에 `should_panic` 속성을 추가하여 수행합니다. 함수 내부의 코드가 패닉하면 테스트가 통과하고, 함수 내부의 코드가 패닉하지 않으면 테스트가 실패합니다.

Listing 11-8 은 `Guess::new`의 오류 조건이 예상대로 발생하는지 확인하는 테스트를 보여줍니다.

    // src/lib.rs
    pub struct Guess {
        value: i32,
    }

    impl Guess {
        pub fn new(value: i32) -> Guess {
            if value < 1 || value > 100 {
                panic!(
                    "Guess value must be between 1 and 100, got {}.",
                    value
                );
            }

            Guess { value }
        }
    }

    #[cfg(test)]
    mod tests {
        use super::*;

        #[test]
        #[should_panic]
        fn greater_than_100() {
            Guess::new(200);
        }
    }

Listing 11-8: 조건이 패닉을 유발하는지 테스트!

`#[test]` 속성 뒤와 적용되는 테스트 함수 앞에 `#[should_panic]` 속성을 배치합니다. 이 테스트가 통과할 때의 결과를 살펴보겠습니다.

    running 1 test
    test tests::greater_than_100 - should panic ... ok

    test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s

좋아 보입니다! 이제 `new` 함수가 값이 100 보다 큰 경우 패닉하는 조건을 제거하여 코드에 버그를 도입해 보겠습니다.

    // src/lib.rs
    --snip--

    impl Guess {
        pub fn new(value: i32) -> Guess {
            if value < 1 {
                panic!(
                    "Guess value must be between 1 and 100, got {}.",
                    value
                );
            }

            Guess { value }
        }
    }

Listing 11-8 에서 테스트를 실행하면 실패합니다.

    running 1 test
    test tests::greater_than_100 - should panic ... FAILED

    failures:

    ---- tests::greater_than_100 stdout ----
    note: test did not panic as expected

    failures:
        tests::greater_than_100

    test result: FAILED. 0 passed; 1 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s

이 경우 매우 유용한 메시지를 얻지 못하지만, 테스트 함수를 살펴보면 `#[should_panic]`으로 주석 처리되어 있음을 알 수 있습니다. 우리가 얻은 실패는 테스트 함수의 코드가 패닉을 유발하지 않았음을 의미합니다.

`should_panic`을 사용하는 테스트는 부정확할 수 있습니다. `should_panic` 테스트는 예상했던 것과 다른 이유로 테스트가 패닉하는 경우에도 통과합니다. `should_panic` 테스트를 더 정확하게 만들려면 `should_panic` 속성에 선택적 `expected` 매개변수를 추가할 수 있습니다. 테스트 하네스는 실패 메시지에 제공된 텍스트가 포함되어 있는지 확인합니다. 예를 들어, Listing 11-9 에서 `new` 함수가 값이 너무 작거나 너무 큰지에 따라 다른 메시지로 패닉하는 `Guess`에 대한 수정된 코드를 고려하십시오.

    // src/lib.rs
    --snip--

    impl Guess {
        pub fn new(value: i32) -> Guess {
            if value < 1 {
                panic!(
                    "Guess value must be greater than or equal to 1, got {}.",
                    value
                );
            } else if value > 100 {
                panic!(
                    "Guess value must be less than or equal to 100, got {}.",
                    value
                );
            }

            Guess { value }
        }
    }

    #[cfg(test)]
    mod tests {
        use super::*;

        #[test]
        #[should_panic(expected = "less than or equal to 100")]
        fn greater_than_100() {
            Guess::new(200);
        }
    }

Listing 11-9: 지정된 부분 문자열을 포함하는 패닉 메시지로 `panic!` 테스트

이 테스트는 `should_panic` 속성의 `expected` 매개변수에 넣은 값이 `Guess::new` 함수가 패닉하는 메시지의 부분 문자열이기 때문에 통과합니다. 예상하는 전체 패닉 메시지를 지정할 수 있었는데, 이 경우 `Guess value must be less than or equal to 100, got 200`이 됩니다. 무엇을 지정할지는 패닉 메시지의 고유하거나 동적인 부분과 테스트의 정확성에 따라 다릅니다. 이 경우 패닉 메시지의 부분 문자열만으로 테스트 함수의 코드가 `else if value > 100` 케이스를 실행하도록 하는 데 충분합니다.

`expected` 메시지가 있는 `should_panic` 테스트가 실패하는 경우를 보려면 `if value < 1` 및 `else if value > 100` 블록의 본문을 바꿔서 코드에 다시 버그를 도입해 보겠습니다.

    // src/lib.rs
    --snip--
    if value < 1 {
        panic!(
            "Guess value must be less than or equal to 100, got {}.",
            value
        );
    } else if value > 100 {
        panic!(
            "Guess value must be greater than or equal to 1, got {}.",
            value
        );
    }
    --snip--

이번에는 `should_panic` 테스트를 실행하면 실패합니다.

    running 1 test
    test tests::greater_than_100 - should panic ... FAILED

    failures:

    ---- tests::greater_than_100 stdout ----
    thread 'main' panicked at 'Guess value must be greater than or equal to 1, got
    200.', src/lib.rs:13:13
    note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace
    note: panic did not contain expected string
          panic message: `"Guess value must be greater than or equal to 1, got
    200."`,
     expected substring: `"less than or equal to 100"`

    failures:
        tests::greater_than_100

    test result: FAILED. 0 passed; 1 failed; 0 ignored; 0 measured; 0 filtered out;
    finished in 0.00s

실패 메시지는 이 테스트가 실제로 예상대로 패닉했지만 패닉 메시지에 예상 문자열 `'Guess value must be less than or equal to 100'`이 포함되지 않았음을 나타냅니다. 이 경우 실제로 얻은 패닉 메시지는 `Guess value must be greater than or equal to 1, got 200`이었습니다. 이제 버그가 있는 위치를 파악하기 시작할 수 있습니다!
