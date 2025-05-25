# 통합 테스트의 서브모듈 (Submodules)

통합 테스트를 더 추가하면서, 테스트를 구성하기 위해 `tests` 디렉토리에 더 많은 파일을 만들고 싶을 수 있습니다. 예를 들어, 테스트하는 기능별로 테스트 함수를 그룹화할 수 있습니다. 앞서 언급했듯이, `tests` 디렉토리의 각 파일은 자체 크레이트로 컴파일되므로, 최종 사용자가 크레이트를 사용하는 방식을 더 가깝게 모방하기 위해 별도의 범위를 만드는 데 유용합니다. 그러나 이는 `tests` 디렉토리의 파일이 코드 분할 방법을 다룬 7 장에서 배운 것처럼 `src`의 파일과 동일한 동작을 공유하지 않음을 의미합니다.

`tests` 디렉토리 파일의 다른 동작은 여러 통합 테스트 파일에서 사용할 헬퍼 함수 집합이 있고, "모듈을 다른 파일로 분리하기"의 단계를 따라 공통 모듈로 추출하려는 경우 가장 두드러집니다. 예를 들어, `tests/common.rs`를 생성하고 `setup`이라는 함수를 배치하면, 여러 테스트 파일의 여러 테스트 함수에서 호출하려는 코드를 `setup`에 추가할 수 있습니다.

파일 이름: `tests/common.rs`

```rust
pub fn setup() {
    // setup code specific to your library's tests would go here
}
```

테스트를 다시 실행하면, 이 파일에 테스트 함수가 없고 `setup` 함수를 어디에서도 호출하지 않았음에도 불구하고 `common.rs` 파일에 대한 새로운 섹션이 테스트 출력에 표시됩니다.

    running 1 test
    test tests::internal ... ok

    test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s

         Running tests/common.rs (target/debug/deps/common-
    92948b65e88960b4)

    running 0 tests

    test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s

         Running tests/integration_test.rs
    (target/debug/deps/integration_test-92948b65e88960b4)

    running 1 test
    test it_adds_two ... ok

    test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s

       Doc-tests adder

    running 0 tests

    test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s

`common`이 테스트 결과에 `running 0 tests`와 함께 나타나는 것은 우리가 원했던 것이 아닙니다. 우리는 단지 다른 통합 테스트 파일과 일부 코드를 공유하고 싶었습니다. `common`이 테스트 출력에 나타나지 않도록 하려면, `tests/common.rs`를 생성하는 대신 `tests/common/mod.rs`를 생성합니다. 이제 프로젝트 디렉토리는 다음과 같습니다.

    ├── Cargo.lock
    ├── Cargo.toml
    ├── src
    │   └── lib.rs
    └── tests
        ├── common
        │   └── mod.rs
        └── integration_test.rs

이것은 "대체 파일 경로"에서 언급한 Rust 가 이해하는 이전 명명 규칙입니다. 파일을 이렇게 명명하면 Rust 가 `common` 모듈을 통합 테스트 파일로 취급하지 않도록 합니다. `setup` 함수 코드를 `tests/common/mod.rs`로 옮기고 `tests/common.rs` 파일을 삭제하면 테스트 출력의 해당 섹션이 더 이상 나타나지 않습니다. `tests` 디렉토리의 하위 디렉토리의 파일은 별도의 크레이트로 컴파일되지 않거나 테스트 출력에 섹션이 없습니다.

`tests/common/mod.rs`를 생성한 후, 모듈로 모든 통합 테스트 파일에서 사용할 수 있습니다. 다음은 `tests/integration_test.rs`의 `it_adds_two` 테스트에서 `setup` 함수를 호출하는 예입니다.

파일 이름: `tests/integration_test.rs`

```rust
use adder;

mod common;

#[test]
fn it_adds_two() {
    common::setup();
    assert_eq!(4, adder::add_two(2));
}
```

`mod common;` 선언은 Listing 7-21 에서 시연한 모듈 선언과 동일합니다. 그런 다음 테스트 함수에서 `common::setup()` 함수를 호출할 수 있습니다.
