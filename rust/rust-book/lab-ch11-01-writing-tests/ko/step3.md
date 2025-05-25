# `assert!` 매크로로 결과 확인하기

표준 라이브러리에서 제공하는 `assert!` 매크로는 테스트에서 어떤 조건이 `true`로 평가되는지 확인하려는 경우에 유용합니다. `assert!` 매크로에 부울 (Boolean) 로 평가되는 인수를 제공합니다. 값이 `true`이면 아무 일도 일어나지 않고 테스트가 통과합니다. 값이 `false`이면 `assert!` 매크로는 `panic!`을 호출하여 테스트가 실패하도록 합니다. `assert!` 매크로를 사용하면 코드가 의도한 방식으로 작동하는지 확인할 수 있습니다.

Listing 5-15 에서 `Rectangle` 구조체와 `can_hold` 메서드를 사용했는데, 이는 Listing 11-5 에 다시 반복됩니다. 이 코드를 `src/lib.rs` 파일에 넣은 다음 `assert!` 매크로를 사용하여 몇 가지 테스트를 작성해 보겠습니다.

파일 이름: `src/lib.rs`

```rust
#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
}

impl Rectangle {
    fn can_hold(&self, other: &Rectangle) -> bool {
        self.width > other.width && self.height > other.height
    }
}
```

Listing 11-5: 5 장에서 `Rectangle` 구조체와 해당 `can_hold` 메서드 사용

`can_hold` 메서드는 부울을 반환하므로 `assert!` 매크로에 완벽한 사용 사례입니다. Listing 11-6 에서 너비가 8 이고 높이가 7 인 `Rectangle` 인스턴스를 생성하고 너비가 5 이고 높이가 1 인 다른 `Rectangle` 인스턴스를 포함할 수 있는지 어서션 (assertion) 하여 `can_hold` 메서드를 실행하는 테스트를 작성합니다.

파일 이름: `src/lib.rs`

```rust
#[cfg(test)]
mod tests {
  1 use super::*;

    #[test]
  2 fn larger_can_hold_smaller() {
      3 let larger = Rectangle {
            width: 8,
            height: 7,
        };
        let smaller = Rectangle {
            width: 5,
            height: 1,
        };

      4 assert!(larger.can_hold(&smaller));
    }
}
```

Listing 11-6: 더 큰 사각형이 실제로 더 작은 사각형을 포함할 수 있는지 확인하는 `can_hold`에 대한 테스트

`tests` 모듈 내에 새로운 줄 `use super::*;` \[1]을 추가했음에 유의하십시오. `tests` 모듈은 "모듈 트리에서 항목을 참조하기 위한 경로"에서 다룬 일반적인 가시성 규칙을 따르는 일반 모듈입니다. `tests` 모듈은 내부 모듈이므로 외부 모듈에서 테스트 중인 코드를 내부 모듈의 범위로 가져와야 합니다. 여기서는 glob 을 사용하므로 외부 모듈에서 정의한 모든 항목을 이 `tests` 모듈에서 사용할 수 있습니다.

테스트 이름을 `larger_can_hold_smaller` \[2]로 지정하고 필요한 두 개의 `Rectangle` 인스턴스를 생성했습니다 \[3]. 그런 다음 `assert!` 매크로를 호출하고 `larger.can_hold(&smaller)` \[4]를 호출한 결과를 전달했습니다. 이 표현식은 `true`를 반환해야 하므로 테스트가 통과해야 합니다. 확인해 봅시다!

    running 1 test
    test tests::larger_can_hold_smaller ... ok

    test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s

통과했습니다! 이번에는 더 작은 사각형이 더 큰 사각형을 포함할 수 없음을 어서션 (assertion) 하는 다른 테스트를 추가해 보겠습니다.

파일 이름: `src/lib.rs`

```rust
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn larger_can_hold_smaller() {
        --snip--
    }

    #[test]
    fn smaller_cannot_hold_larger() {
        let larger = Rectangle {
            width: 8,
            height: 7,
        };
        let smaller = Rectangle {
            width: 5,
            height: 1,
        };

        assert!(!smaller.can_hold(&larger));
    }
}
```

이 경우 `can_hold` 함수의 올바른 결과는 `false`이므로 `assert!` 매크로에 전달하기 전에 해당 결과를 부정해야 합니다. 결과적으로 `can_hold`가 `false`를 반환하면 테스트가 통과합니다.

    running 2 tests
    test tests::larger_can_hold_smaller ... ok
    test tests::smaller_cannot_hold_larger ... ok

    test result: ok. 2 passed; 0 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s

두 개의 테스트가 통과했습니다! 이제 코드에 버그를 도입했을 때 테스트 결과가 어떻게 되는지 살펴보겠습니다. 너비 비교 시 부등호를 `<`로 바꿔서 `can_hold` 메서드의 구현을 변경합니다.

    --snip--

    impl Rectangle {
        fn can_hold(&self, other: &Rectangle) -> bool {
            self.width < other.width && self.height > other.height
        }
    }

이제 테스트를 실행하면 다음과 같은 결과가 생성됩니다.

    running 2 tests
    test tests::smaller_cannot_hold_larger ... ok
    test tests::larger_can_hold_smaller ... FAILED

    failures:

    ---- tests::larger_can_hold_smaller stdout ----
    thread 'main' panicked at 'assertion failed:
    larger.can_hold(&smaller)', src/lib.rs:28:9
    note: run with `RUST_BACKTRACE=1` environment variable to display
    a backtrace


    failures:
        tests::larger_can_hold_smaller

    test result: FAILED. 1 passed; 1 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s

테스트가 버그를 잡았습니다! `larger.width`는 `8`이고 `smaller.width`는 `5`이므로 `can_hold`에서 너비 비교는 이제 `false`를 반환합니다. 8 은 5 보다 작지 않기 때문입니다.
