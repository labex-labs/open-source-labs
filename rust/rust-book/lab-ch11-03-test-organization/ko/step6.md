# tests 디렉토리

프로젝트 디렉토리의 최상위 레벨에 `src` 옆에 `tests` 디렉토리를 생성합니다. Cargo 는 이 디렉토리에서 통합 테스트 파일을 찾도록 되어 있습니다. 그런 다음 원하는 만큼 많은 테스트 파일을 만들 수 있으며, Cargo 는 각 파일을 개별 크레이트 (crate) 로 컴파일합니다.

통합 테스트를 만들어 보겠습니다. Listing 11-12 의 코드가 여전히 `src/lib.rs` 파일에 있는 상태에서 `tests` 디렉토리를 만들고 `tests/integration_test.rs`라는 새 파일을 만듭니다. 디렉토리 구조는 다음과 같아야 합니다.

    adder
    ├── Cargo.lock
    ├── Cargo.toml
    ├── src
    │   └── lib.rs
    └── tests
        └── integration_test.rs

Listing 11-13 의 코드를 `tests/integration_test.rs` 파일에 입력합니다.

파일 이름: `tests/integration_test.rs`

```rust
use adder;

#[test]
fn it_adds_two() {
    assert_eq!(4, adder::add_two(2));
}
```

Listing 11-13: `adder` 크레이트의 함수에 대한 통합 테스트

`tests` 디렉토리의 각 파일은 별도의 크레이트이므로, 각 테스트 크레이트의 범위로 라이브러리를 가져와야 합니다. 이러한 이유로 코드 상단에 `use adder;`를 추가했는데, 이는 단위 테스트에서는 필요하지 않았습니다.

`tests/integration_test.rs`의 어떤 코드에도 `#[cfg(test)]`를 주석 처리할 필요가 없습니다. Cargo 는 `tests` 디렉토리를 특별하게 취급하며, `cargo test`를 실행할 때만 이 디렉토리의 파일을 컴파일합니다. 지금 `cargo test`를 실행하십시오.

```bash
[object Object]
```

출력의 세 섹션에는 단위 테스트, 통합 테스트 및 문서 테스트가 포함됩니다. 섹션의 테스트가 실패하면 다음 섹션은 실행되지 않습니다. 예를 들어, 단위 테스트가 실패하면 모든 단위 테스트가 통과하는 경우에만 해당 테스트가 실행되므로 통합 및 문서 테스트에 대한 출력이 없습니다.

단위 테스트에 대한 첫 번째 섹션 \[1]은 우리가 보아온 것과 동일합니다. 각 단위 테스트에 대한 한 줄 (Listing 11-12 에서 추가한 `internal`이라는 하나) 과 단위 테스트에 대한 요약 줄입니다.

통합 테스트 섹션은 `Running tests/integration_test.rs` \[2]로 시작합니다. 다음으로, 해당 통합 테스트의 각 테스트 함수에 대한 한 줄 \[3]과 `Doc-tests adder` 섹션이 시작되기 직전의 통합 테스트 결과에 대한 요약 줄 \[4]이 있습니다.

각 통합 테스트 파일에는 자체 섹션이 있으므로, `tests` 디렉토리에 더 많은 파일을 추가하면 더 많은 통합 테스트 섹션이 있을 것입니다.

`cargo test`에 테스트 함수의 이름을 인수로 지정하여 특정 통합 테스트 함수를 계속 실행할 수 있습니다. 특정 통합 테스트 파일의 모든 테스트를 실행하려면 `cargo test`의 `--test` 인수를 파일 이름과 함께 사용하십시오.

```bash
[object Object]
```

이 명령은 `tests/integration_test.rs` 파일의 테스트만 실행합니다.
