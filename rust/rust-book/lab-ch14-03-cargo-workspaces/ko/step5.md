# Workspace 에 테스트 추가하기

또 다른 개선 사항으로, `add_one` 크레이트 내에서 `add_one::add_one` 함수의 테스트를 추가해 보겠습니다.

파일 이름: `add_one/src/lib.rs`

```rust
pub fn add_one(x: i32) -> i32 {
    x + 1
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_works() {
        assert_eq!(3, add_one(2));
    }
}
```

이제 최상위 `add` 디렉토리에서 `cargo test`를 실행합니다. 이와 같이 구조화된 workspace 에서 `cargo test`를 실행하면 workspace 의 모든 크레이트에 대한 테스트가 실행됩니다.

```bash
[object Object]
```

출력의 첫 번째 섹션은 `add_one` 크레이트의 `it_works` 테스트가 통과했음을 보여줍니다. 다음 섹션은 `adder` 크레이트에서 테스트가 0 개 발견되었음을 보여주고, 마지막 섹션은 `add_one` 크레이트에서 문서 테스트가 0 개 발견되었음을 보여줍니다.

또한 `-p` 플래그를 사용하고 테스트하려는 크레이트의 이름을 지정하여 최상위 디렉토리에서 workspace 의 특정 크레이트에 대한 테스트를 실행할 수도 있습니다.

```bash
[object Object]
```

이 출력은 `cargo test`가 `add_one` 크레이트에 대한 테스트만 실행하고 `adder` 크레이트 테스트는 실행하지 않았음을 보여줍니다.

workspace 의 크레이트를 *https://crates.io*에 게시하는 경우 workspace 의 각 크레이트를 별도로 게시해야 합니다. `cargo test`와 마찬가지로 `-p` 플래그를 사용하고 게시하려는 크레이트의 이름을 지정하여 workspace 의 특정 크레이트를 게시할 수 있습니다.

추가 연습을 위해 `add_one` 크레이트와 유사한 방식으로 이 workspace 에 `add_two` 크레이트를 추가하십시오!

프로젝트가 커짐에 따라 workspace 를 사용하는 것을 고려하십시오. workspace 는 하나의 큰 코드 덩어리보다 이해하기 쉽고 작은 개별 구성 요소를 제공합니다. 또한 크레이트를 workspace 에 유지하면 크레이트가 동시에 자주 변경되는 경우 크레이트 간의 조정을 더 쉽게 할 수 있습니다.
