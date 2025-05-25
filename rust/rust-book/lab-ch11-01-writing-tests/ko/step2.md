# 테스트 함수의 구조

가장 간단하게, Rust 에서 테스트는 `test` 속성 (attribute) 으로 주석 처리된 함수입니다. 속성은 Rust 코드 조각에 대한 메타데이터입니다. 한 가지 예는 5 장에서 구조체 (struct) 와 함께 사용했던 `derive` 속성입니다. 함수를 테스트 함수로 변경하려면 `fn` 앞 줄에 `#[test]`를 추가합니다. `cargo test` 명령으로 테스트를 실행하면 Rust 는 주석 처리된 함수를 실행하고 각 테스트 함수가 통과했는지 실패했는지 보고하는 테스트 러너 (test runner) 바이너리를 빌드합니다.

Cargo 로 새로운 라이브러리 프로젝트를 만들 때마다 테스트 함수가 있는 테스트 모듈이 자동으로 생성됩니다. 이 모듈은 테스트를 작성하기 위한 템플릿을 제공하므로 새로운 프로젝트를 시작할 때마다 정확한 구조와 구문을 찾아볼 필요가 없습니다. 원하는 만큼 많은 추가 테스트 함수와 테스트 모듈을 추가할 수 있습니다!

실제로 코드를 테스트하기 전에 템플릿 테스트를 실험하여 테스트가 작동하는 방식의 몇 가지 측면을 살펴보겠습니다. 그런 다음 작성한 코드를 호출하고 해당 동작이 올바른지 어서션 (assertion) 하는 실제 테스트를 작성합니다.

두 숫자를 더하는 `adder`라는 새로운 라이브러리 프로젝트를 만들어 보겠습니다.

```bash
$ cargo new adder --lib
Created library $(adder) project
$ cd adder
```

`adder` 라이브러리의 `src/lib.rs` 파일의 내용은 Listing 11-1 과 같아야 합니다.

파일 이름: `src/lib.rs`

```rust
#[cfg(test)]
mod tests {
  1 #[test]
    fn it_works() {
        let result = 2 + 2;
      2 assert_eq!(result, 4);
    }
}
```

Listing 11-1: `cargo new`에 의해 자동으로 생성된 테스트 모듈 및 함수

지금은 처음 두 줄을 무시하고 함수에 집중해 보겠습니다. `#[test]` 주석 \[1]에 주목하십시오. 이 속성은 이것이 테스트 함수임을 나타내므로 테스트 러너는 이 함수를 테스트로 처리해야 함을 알고 있습니다. 또한 일반적인 시나리오를 설정하거나 일반적인 작업을 수행하는 데 도움이 되는 비 (非) 테스트 함수를 `tests` 모듈에 가질 수 있으므로 어떤 함수가 테스트인지 항상 표시해야 합니다.

예제 함수 본문은 `assert_eq!` 매크로 \[2]를 사용하여 2 와 2 를 더한 결과가 포함된 `result`가 4 와 같은지 어서션 (assertion) 합니다. 이 어서션은 일반적인 테스트 형식의 예로 사용됩니다. 이 테스트가 통과하는지 확인하기 위해 실행해 보겠습니다.

`cargo test` 명령은 Listing 11-2 와 같이 프로젝트의 모든 테스트를 실행합니다.

```bash
[object Object]
```

Listing 11-2: 자동으로 생성된 테스트를 실행한 결과

Cargo 는 테스트를 컴파일하고 실행했습니다. `running 1 test` \[1] 줄을 볼 수 있습니다. 다음 줄에는 생성된 테스트 함수의 이름인 `it_works`와 해당 테스트 실행 결과가 `ok` \[2]임을 보여줍니다. 전체 요약 `test result: ok.` \[3]는 모든 테스트가 통과했음을 의미하며, `1 passed; 0 failed` 부분은 통과하거나 실패한 테스트의 총 개수를 나타냅니다.

특정 인스턴스에서 실행되지 않도록 테스트를 무시하도록 표시할 수 있습니다. "특정 요청이 없는 한 일부 테스트 무시"에서 다룰 것입니다. 여기서는 그렇게 하지 않았으므로 요약에 `0 ignored`가 표시됩니다. 또한 `cargo test` 명령에 인수를 전달하여 이름이 문자열과 일치하는 테스트만 실행할 수 있습니다. 이를 _필터링_(filtering) 이라고 하며 "이름으로 테스트의 하위 집합 실행"에서 다룰 것입니다. 여기서는 실행되는 테스트를 필터링하지 않았으므로 요약의 끝에 `0 filtered out`이 표시됩니다.

`0 measured` 통계는 성능을 측정하는 벤치마크 테스트에 대한 것입니다. 이 글을 쓰는 시점에서 벤치마크 테스트는 nightly Rust 에서만 사용할 수 있습니다. 자세한 내용은 *https://doc.rust-lang.org/unstable-book/library-features/test.html*에서 벤치마크 테스트에 대한 문서를 참조하십시오.

`Doc-tests adder` \[4]로 시작하는 테스트 출력의 다음 부분은 모든 문서 테스트의 결과입니다. 아직 문서 테스트가 없지만 Rust 는 API 문서에 나타나는 모든 코드 예제를 컴파일할 수 있습니다. 이 기능은 문서와 코드를 동기화하는 데 도움이 됩니다! "테스트로서의 문서 주석"에서 문서 테스트를 작성하는 방법에 대해 논의할 것입니다. 지금은 `Doc-tests` 출력을 무시하겠습니다.

테스트를 사용자 정의 요구 사항에 맞게 시작해 보겠습니다. 먼저 `it_works` 함수의 이름을 `exploration`과 같이 다른 이름으로 변경합니다.

파일 이름: `src/lib.rs`

```rust
#[cfg(test)]
mod tests {
    #[test]
    fn exploration() {
        let result = 2 + 2;
        assert_eq!(result, 4);
    }
}
```

그런 다음 `cargo test`를 다시 실행합니다. 이제 출력에 `it_works` 대신 `exploration`이 표시됩니다.

    running 1 test
    test tests::exploration ... ok

    test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s

이제 다른 테스트를 추가하겠지만 이번에는 실패하는 테스트를 만들겠습니다! 테스트 함수의 무언가가 패닉 (panic) 하면 테스트가 실패합니다. 각 테스트는 새로운 스레드에서 실행되며, 메인 스레드가 테스트 스레드가 종료된 것을 감지하면 테스트는 실패로 표시됩니다. 9 장에서 `panic!` 매크로를 호출하는 것이 패닉하는 가장 간단한 방법이라고 이야기했습니다. `another`라는 함수로 새 테스트를 입력하면 `src/lib.rs` 파일이 Listing 11-3 과 같습니다.

파일 이름: `src/lib.rs`

```rust
#[cfg(test)]
mod tests {
    #[test]
    fn exploration() {
        assert_eq!(2 + 2, 4);
    }

    #[test]
    fn another() {
        panic!("Make this test fail");
    }
}
```

Listing 11-3: `panic!` 매크로를 호출하므로 실패할 두 번째 테스트 추가

`cargo test`를 사용하여 테스트를 다시 실행합니다. 출력은 Listing 11-4 와 같아야 하며, `exploration` 테스트가 통과하고 `another`가 실패했음을 보여줍니다.

    running 2 tests
    test tests::exploration ... ok
    1 test tests::another ... FAILED

    2 failures:

    ---- tests::another stdout ----
    thread 'main' panicked at 'Make this test fail', src/lib.rs:10:9
    note: run with `RUST_BACKTRACE=1` environment variable to display
    a backtrace

    3 failures:
        tests::another

    4 test result: FAILED. 1 passed; 1 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s

    error: test failed, to rerun pass '--lib'

Listing 11-4: 하나의 테스트가 통과하고 하나의 테스트가 실패했을 때의 테스트 결과

`ok` 대신 `test tests::another` 줄에 `FAILED` \[1]가 표시됩니다. 개별 결과와 요약 사이에 두 개의 새로운 섹션이 나타납니다. 첫 번째 \[2]는 각 테스트 실패에 대한 자세한 이유를 표시합니다. 이 경우 `another`가 `src/lib.rs` 파일의 10 번째 줄에서 `panic at 'Make this test fail'`로 인해 실패했다는 세부 정보를 얻습니다. 다음 섹션 \[3]은 실패한 모든 테스트의 이름만 나열하며, 테스트가 많고 자세한 실패 테스트 출력이 많은 경우 유용합니다. 실패한 테스트의 이름을 사용하여 해당 테스트만 실행하여 더 쉽게 디버깅할 수 있습니다. "테스트 실행 방법 제어"에서 테스트를 실행하는 방법에 대해 자세히 설명합니다.

요약 줄이 마지막에 표시됩니다 \[4]: 전반적으로 테스트 결과는 `FAILED`입니다. 하나의 테스트가 통과하고 하나의 테스트가 실패했습니다.

이제 다양한 시나리오에서 테스트 결과가 어떻게 보이는지 확인했으므로 `panic!` 외에 테스트에 유용한 다른 매크로를 살펴보겠습니다.
