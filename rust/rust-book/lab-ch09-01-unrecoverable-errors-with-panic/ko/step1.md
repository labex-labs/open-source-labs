# panic 을 사용한 복구 불가능한 오류

때로는 코드에서 좋지 않은 일이 발생하며, 이에 대해 할 수 있는 일이 아무것도 없습니다. 이러한 경우, Rust 에는 `panic!` 매크로가 있습니다. 실제로 패닉을 발생시키는 두 가지 방법이 있습니다. 코드에서 패닉을 유발하는 동작을 취하는 경우 (예: 배열의 끝을 넘어 접근하는 경우) 또는 `panic!` 매크로를 명시적으로 호출하는 경우입니다. 두 경우 모두 프로그램에서 패닉을 발생시킵니다. 기본적으로 이러한 패닉은 실패 메시지를 출력하고, 스택을 언와인드 (unwind) 하고, 정리한 다음 종료합니다. 환경 변수를 통해 패닉이 발생할 때 Rust 가 호출 스택을 표시하여 패닉의 원인을 더 쉽게 추적할 수 있습니다.

> **패닉에 대한 응답으로 스택 언와인딩 또는 중단**
>
> 기본적으로 패닉이 발생하면 프로그램은 *언와인딩*을 시작합니다. 즉, Rust 는 스택을 거슬러 올라가면서 만나는 각 함수의 데이터를 정리합니다. 그러나 되돌아가서 정리하는 것은 많은 작업입니다. 따라서 Rust 는 정리하지 않고 프로그램을 즉시 *중단*하는 대안을 선택할 수 있도록 합니다.
>
> 그런 다음 프로그램이 사용하던 메모리는 운영 체제에서 정리해야 합니다. 프로젝트에서 결과 바이너리를 가능한 한 작게 만들어야 하는 경우, `Cargo.toml` 파일의 적절한 `[profile]` 섹션에 `panic = 'abort'`를 추가하여 패닉 발생 시 언와인딩에서 중단으로 전환할 수 있습니다. 예를 들어, 릴리스 모드에서 패닉 시 중단하려면 다음을 추가합니다.
>
> ```toml
> [profile.release]
> panic = 'abort'
> ```

간단한 프로그램에서 `panic!`을 호출해 보겠습니다.

파일 이름: `src/main.rs`

```rust
fn main() {
    panic!("crash and burn");
}
```

프로그램을 실행하면 다음과 같은 내용이 표시됩니다.

    thread 'main' panicked at 'crash and burn', src/main.rs:2:5
    note: run with `RUST_BACKTRACE=1` environment variable to display
    a backtrace

`panic!` 호출은 마지막 두 줄에 포함된 오류 메시지를 발생시킵니다. 첫 번째 줄은 패닉 메시지와 패닉이 발생한 소스 코드의 위치를 ​​나타냅니다. *src/main.rs:2:5*는 `src/main.rs` 파일의 두 번째 줄, 다섯 번째 문자를 나타냅니다.

이 경우, 표시된 줄은 코드의 일부이며 해당 줄로 이동하면 `panic!` 매크로 호출을 볼 수 있습니다. 다른 경우에는 `panic!` 호출이 코드가 호출하는 코드에 있을 수 있으며, 오류 메시지에서 보고하는 파일 이름과 줄 번호는 `panic!` 매크로가 호출되는 다른 사람의 코드일 수 있으며, 결국 `panic!` 호출로 이어진 코드 줄이 아닐 수 있습니다.

`panic!` 호출이 발생한 함수의 백트레이스 (backtrace) 를 사용하여 문제의 원인이 되는 코드 부분을 파악할 수 있습니다. `panic!` 백트레이스를 사용하는 방법을 이해하기 위해 다른 예를 살펴보고, `panic!` 호출이 매크로를 직접 호출하는 코드 대신 코드의 버그로 인해 라이브러리에서 발생하는 경우 어떤 모습인지 살펴보겠습니다. 목록 9-1 에는 유효한 인덱스 범위를 벗어난 벡터의 인덱스에 접근하려는 코드가 있습니다.

파일 이름: `src/main.rs`

```rust
fn main() {
    let v = vec![1, 2, 3];

    v[99];
}
```

목록 9-1: 벡터의 끝을 넘어 요소에 접근하려는 시도, 이로 인해 `panic!` 호출이 발생합니다.

여기서는 벡터의 100 번째 요소 (인덱싱이 0 부터 시작하므로 인덱스 99) 에 접근하려고 하지만, 벡터에는 세 개의 요소만 있습니다. 이 상황에서 Rust 는 패닉을 발생시킵니다. `[]`를 사용하면 요소를 반환해야 하지만, 잘못된 인덱스를 전달하면 Rust 가 여기서 반환할 수 있는 올바른 요소가 없습니다.

C 에서 데이터 구조의 끝을 넘어 읽으려는 시도는 정의되지 않은 동작입니다. 데이터 구조의 해당 요소에 해당하는 메모리 위치에 있는 내용을 얻을 수 있으며, 해당 메모리가 해당 구조에 속하지 않더라도 마찬가지입니다. 이를 *버퍼 오버리드 (buffer overread)*라고 하며, 공격자가 데이터 구조 뒤에 저장된 데이터를 읽을 수 있도록 인덱스를 조작할 수 있는 경우 보안 취약점으로 이어질 수 있습니다.

이러한 종류의 취약성으로부터 프로그램을 보호하기 위해, 존재하지 않는 인덱스의 요소에 접근하려고 하면 Rust 는 실행을 중단하고 계속 진행하는 것을 거부합니다. 시도해 보겠습니다.

    thread 'main' panicked at 'index out of bounds: the len is 3 but the index is
    99', src/main.rs:4:5
    note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace

이 오류는 `main.rs`의 4 번째 줄에서 `index`에 접근하려는 시도를 가리킵니다.

`note:` 줄은 `RUST_BACKTRACE` 환경 변수를 설정하여 오류를 발생시킨 정확한 내용을 백트레이스할 수 있음을 알려줍니다. *백트레이스*는 이 지점에 도달하기 위해 호출된 모든 함수의 목록입니다. Rust 의 백트레이스는 다른 언어와 마찬가지로 작동합니다. 백트레이스를 읽는 핵심은 맨 위에서 시작하여 작성한 파일이 보일 때까지 읽는 것입니다. 이것이 문제가 시작된 지점입니다. 해당 지점 위의 줄은 코드가 호출한 코드이고, 아래 줄은 코드가 호출한 코드입니다. 이러한 전후 줄에는 핵심 Rust 코드, 표준 라이브러리 코드 또는 사용 중인 크레이트가 포함될 수 있습니다. `RUST_BACKTRACE` 환경 변수를 `0`을 제외한 모든 값으로 설정하여 백트레이스를 얻어 보겠습니다. 목록 9-2 는 표시될 내용과 유사한 출력을 보여줍니다.

```bash
$ RUST_BACKTRACE=1 cargo run
thread 'main' panicked at 'index out of bounds: the len is 3 but the index is
99', src/main.rs:4:5
stack backtrace:
0: rust_begin_unwind
at /rustc/e092d0b6b43f2de967af0887873151bb1c0b18d3/library/std
/src/panicking.rs:584:5
1: core::panicking::panic_fmt
at /rustc/e092d0b6b43f2de967af0887873151bb1c0b18d3/library/core
/src/panicking.rs:142:14
2: core::panicking::panic_bounds_check
at /rustc/e092d0b6b43f2de967af0887873151bb1c0b18d3/library/core
/src/panicking.rs:84:5
3: < usize as core::slice::index::SliceIndex < [T] >> ::index
at /rustc/e092d0b6b43f2de967af0887873151bb1c0b18d3/library/core
/src/slice/index.rs:242:10
4: core::slice::index:: core::ops::index::Index [T] < impl < I > for > ::index
at /rustc/e092d0b6b43f2de967af0887873151bb1c0b18d3/library/core
/src/slice/index.rs:18:9
5: < alloc::vec::Vec < T,A > as core::ops::index::Index < I >> ::index
at /rustc/e092d0b6b43f2de967af0887873151bb1c0b18d3/library/alloc
/src/vec/mod.rs:2591:9
6: panic::main
at ./src/main.rs:4:5
7: core::ops::function::FnOnce::call_once
at /rustc/e092d0b6b43f2de967af0887873151bb1c0b18d3/library/core
/src/ops/function.rs:248:5
note: Some details are omitted, run with $(RUST_BACKTRACE=full) for a verbose
backtrace.
```

목록 9-2: `panic!` 호출로 생성된 백트레이스 (환경 변수 `RUST_BACKTRACE`가 설정된 경우 표시됨)

출력이 많습니다! 표시되는 정확한 출력은 운영 체제 및 Rust 버전에 따라 다를 수 있습니다. 이 정보로 백트레이스를 얻으려면 디버그 기호가 활성화되어 있어야 합니다. 디버그 기호는 여기에서와 같이 `--release` 플래그 없이 `cargo build` 또는 `cargo run`을 사용할 때 기본적으로 활성화됩니다.

목록 9-2 의 출력에서 백트레이스의 6 번째 줄은 문제의 원인이 되는 프로젝트의 줄을 가리킵니다. 즉, `src/main.rs`의 4 번째 줄입니다. 프로그램이 패닉을 발생시키지 않도록 하려면 작성한 파일을 언급하는 첫 번째 줄에서 조사를 시작해야 합니다. 목록 9-1 에서 패닉을 발생시키는 코드를 의도적으로 작성한 경우, 패닉을 수정하는 방법은 벡터 인덱스 범위를 벗어난 요소를 요청하지 않는 것입니다. 앞으로 코드에서 패닉이 발생하면 패닉을 유발하기 위해 코드가 어떤 값으로 어떤 동작을 취하고 있는지, 그리고 대신 코드가 수행해야 하는 작업을 파악해야 합니다.

"To panic! or Not to panic!"에서 오류 조건을 처리하기 위해 `panic!`을 사용해야 하는 경우와 사용하지 않아야 하는 경우에 대해 다시 살펴보겠습니다. 다음으로, `Result`를 사용하여 오류로부터 복구하는 방법을 살펴보겠습니다.
