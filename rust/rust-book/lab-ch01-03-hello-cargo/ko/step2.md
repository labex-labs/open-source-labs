# Cargo 로 프로젝트 생성하기

Cargo 를 사용하여 새 프로젝트를 생성하고, 원래의 "Hello, world!" 프로젝트와 어떻게 다른지 살펴보겠습니다. `project` 디렉토리 (또는 코드를 저장하기로 결정한 곳) 로 다시 이동합니다. 그런 다음, 모든 운영 체제에서 다음을 실행합니다.

```bash
cd ~/project
cargo new hello_cargo
cd hello_cargo
```

첫 번째 명령은 *hello_cargo*라는 새 디렉토리와 프로젝트를 생성합니다. 프로젝트 이름을 *hello_cargo*로 지정했으며, Cargo 는 동일한 이름의 디렉토리에 파일을 생성합니다.

`hello_cargo` 디렉토리로 이동하여 파일을 나열합니다. Cargo 가 두 개의 파일과 하나의 디렉토리를 생성했음을 알 수 있습니다: `Cargo.toml` 파일과 그 안에 `main.rs` 파일이 있는 `src` 디렉토리입니다.

또한 새로운 Git 저장소를 _.gitignore_ 파일과 함께 초기화했습니다. 기존 Git 저장소 내에서 `cargo new`를 실행하면 Git 파일이 생성되지 않습니다. `cargo new --vcs=git`을 사용하여 이 동작을 재정의할 수 있습니다.

> 참고: Git 은 일반적인 버전 관리 시스템입니다. `--vcs` 플래그를 사용하여 `cargo new`를 다른 버전 관리 시스템이나 버전 관리 시스템 없이 사용하도록 변경할 수 있습니다. 사용 가능한 옵션을 보려면 `cargo new --help`를 실행하십시오.

선택한 텍스트 편집기에서 `Cargo.toml`을 엽니다. Listing 1-2 의 코드와 유사하게 표시됩니다.

파일 이름: `Cargo.toml`

```toml
[package]
name = "hello_cargo"
version = "0.1.0"
edition = "2021"

[dependencies]
```

Listing 1-2: `cargo new`로 생성된 `Cargo.toml`의 내용

이 파일은 Cargo 의 구성 형식인 _TOML_ (_Tom's Obvious, Minimal Language_) 형식입니다.

첫 번째 줄인 `[package]`는 다음 문이 패키지를 구성하고 있음을 나타내는 섹션 제목입니다. 이 파일에 더 많은 정보를 추가하면 다른 섹션을 추가할 것입니다.

다음 세 줄은 Cargo 가 프로그램을 컴파일하는 데 필요한 구성 정보를 설정합니다: 이름, 버전 및 사용할 Rust 의 에디션 (edition). 부록 E 에서 `edition` 키에 대해 이야기하겠습니다.

마지막 줄인 `[dependencies]`는 프로젝트의 의존성을 나열하기 위한 섹션의 시작 부분입니다. Rust 에서 코드 패키지는 *crate*라고 합니다. 이 프로젝트에는 다른 crate 가 필요하지 않지만, 2 장에서 첫 번째 프로젝트에서 필요하므로 이 의존성 섹션을 사용합니다.

이제 `src/main.rs`를 열어보세요:

파일 이름: `src/main.rs`

```rust
fn main() {
    println!("Hello, world!");
}
```

Cargo 는 Listing 1-1 에서 작성한 것과 똑같은 "Hello, world!" 프로그램을 생성했습니다! 지금까지 우리 프로젝트와 Cargo 가 생성한 프로젝트의 차이점은 Cargo 가 코드를 `src` 디렉토리에 넣었고, 최상위 디렉토리에 `Cargo.toml` 구성 파일이 있다는 것입니다.

Cargo 는 소스 파일이 `src` 디렉토리 내에 있을 것으로 예상합니다. 최상위 프로젝트 디렉토리는 README 파일, 라이선스 정보, 구성 파일 및 코드와 관련 없는 모든 항목에만 사용됩니다. Cargo 를 사용하면 프로젝트를 구성하는 데 도움이 됩니다. 모든 것에 자리가 있고, 모든 것이 제자리에 있습니다.

"Hello, world!" 프로젝트에서 했던 것처럼 Cargo 를 사용하지 않는 프로젝트를 시작한 경우, Cargo 를 사용하는 프로젝트로 변환할 수 있습니다. 프로젝트 코드를 `src` 디렉토리로 이동하고 적절한 `Cargo.toml` 파일을 생성합니다.
