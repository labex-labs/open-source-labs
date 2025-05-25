# 통합 테스트

단위 테스트는 한 번에 하나의 모듈을 격리하여 테스트합니다. 작고 개인 코드를 테스트할 수 있습니다. 통합 테스트는 크레이트 외부에 있으며, 다른 코드와 동일한 방식으로 라이브러리의 공개 인터페이스만 사용합니다. 그 목적은 라이브러리의 여러 부분이 함께 올바르게 작동하는지 테스트하는 것입니다.

Cargo 는 `src` 디렉토리 옆의 `tests` 디렉토리에서 통합 테스트를 찾습니다.

파일 `src/lib.rs`:

```rust
// `adder` 라는 크레이트에 이것을 정의합니다.
pub fn add(a: i32, b: i32) -> i32 {
    a + b
}
```

테스트 파일: `tests/integration_test.rs`:

```rust
#[test]
fn test_add() {
    assert_eq!(adder::add(3, 2), 5);
}
```

`cargo test` 명령으로 테스트 실행:

```shell
$ cargo test
running 0 tests

test result: ok. 0 passed
0 failed
0 ignored
0 measured
0 filtered out

Running target/debug/deps/integration_test-bcd60824f5fbfe19

running 1 test
test test_add ... ok

test result: ok. 1 passed
0 failed
0 ignored
0 measured
0 filtered out

Doc-tests adder

running 0 tests

test result: ok. 0 passed
0 failed
0 ignored
0 measured
0 filtered out
```

`tests` 디렉토리의 각 Rust 소스 파일은 별도의 크레이트로 컴파일됩니다. 통합 테스트 간에 코드를 공유하려면 공개 함수가 있는 모듈을 만들고 테스트 내에서 가져와 사용할 수 있습니다.

파일 `tests/common/mod.rs`:

```rust
pub fn setup() {
    // 필요한 파일/디렉토리 생성, 서버 시작 등의 설정 코드.
}
```

테스트 파일: `tests/integration_test.rs`

```rust
// 공통 모듈 가져오기.
mod common;

#[test]
fn test_add() {
    // 공통 코드 사용.
    common::setup();
    assert_eq!(adder::add(3, 2), 5);
}
```

`tests/common.rs`로 모듈을 만드는 것도 가능하지만, 테스트 러너가 해당 파일을 테스트 크레이트로 간주하고 그 안의 테스트를 실행하려고 하기 때문에 권장하지 않습니다.
