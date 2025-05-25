# 이름으로 테스트 하위 집합 실행

때로는 전체 테스트 스위트를 실행하는 데 시간이 오래 걸릴 수 있습니다. 특정 영역의 코드를 작업하는 경우 해당 코드와 관련된 테스트만 실행할 수 있습니다. 실행하려는 테스트의 이름 (들) 을 인수로 `cargo test`에 전달하여 실행할 테스트를 선택할 수 있습니다.

테스트 하위 집합을 실행하는 방법을 보여주기 위해 먼저 Listing 11-11 에 표시된 대로 `add_two` 함수에 대한 세 개의 테스트를 생성하고 실행할 테스트를 선택합니다.

Filename: `src/lib.rs`

```rust
pub fn add_two(a: i32) -> i32 {
    a + 2
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn add_two_and_two() {
        assert_eq!(4, add_two(2));
    }

    #[test]
    fn add_three_and_two() {
        assert_eq!(5, add_two(3));
    }

    #[test]
    fn one_hundred() {
        assert_eq!(102, add_two(100));
    }
}
```

Listing 11-11: 세 개의 서로 다른 이름을 가진 세 개의 테스트

앞서 보았듯이 인수를 전달하지 않고 테스트를 실행하면 모든 테스트가 병렬로 실행됩니다.

    running 3 tests
    test tests::add_three_and_two ... ok
    test tests::add_two_and_two ... ok
    test tests::one_hundred ... ok

    test result: ok. 3 passed; 0 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s
