# Workspace 생성하기

*workspace*는 동일한 _Cargo.lock_ 및 출력 디렉토리를 공유하는 패키지 집합입니다. workspace 를 사용하여 프로젝트를 만들어 보겠습니다. workspace 의 구조에 집중할 수 있도록 간단한 코드를 사용하겠습니다. workspace 를 구성하는 방법에는 여러 가지가 있으므로 일반적인 방법 중 하나만 보여드리겠습니다. 바이너리 하나와 라이브러리 두 개를 포함하는 workspace 를 만들 것입니다. 주요 기능을 제공하는 바이너리는 두 라이브러리에 의존합니다. 한 라이브러리는 `add_one` 함수를 제공하고 다른 라이브러리는 `add_two` 함수를 제공합니다. 이 세 개의 크레이트는 동일한 workspace 의 일부가 됩니다. 먼저 workspace 를 위한 새 디렉토리를 만듭니다.

```bash
mkdir add
cd add
```

다음으로, `add` 디렉토리에서 전체 workspace 를 구성할 `Cargo.toml` 파일을 만듭니다. 이 파일에는 `[package]` 섹션이 없습니다. 대신, 바이너리 크레이트가 있는 패키지의 경로를 지정하여 workspace 에 멤버를 추가할 수 있도록 하는 `[workspace]` 섹션으로 시작합니다. 이 경우 해당 경로는 *adder*입니다.

파일 이름: `Cargo.toml`

```toml
[workspace]

members = [
    "adder",
]
```

다음으로, `add` 디렉토리 내에서 `cargo new`를 실행하여 `adder` 바이너리 크레이트를 만듭니다.

```bash
$ cargo new adder
     Created binary (application) `adder` package
```

이 시점에서 `cargo build`를 실행하여 workspace 를 빌드할 수 있습니다. `add` 디렉토리의 파일은 다음과 같아야 합니다.

    ├── Cargo.lock
    ├── Cargo.toml
    ├── adder
    │   ├── Cargo.toml
    │   └── src
    │       └── main.rs
    └── target

workspace 는 컴파일된 아티팩트가 배치될 최상위 레벨에 하나의 `target` 디렉토리를 갖습니다. `adder` 패키지 자체에는 `target` 디렉토리가 없습니다. `adder` 디렉토리 내부에서 `cargo build`를 실행하더라도 컴파일된 아티팩트는 `add/adder/target`이 아닌 *add/target*에 배치됩니다. Cargo 는 workspace 에서 크레이트가 서로 의존하도록 설계되었기 때문에 workspace 에서 `target` 디렉토리를 이렇게 구성합니다. 각 크레이트가 자체 `target` 디렉토리를 갖는다면, 각 크레이트는 아티팩트를 자체 `target` 디렉토리에 배치하기 위해 workspace 의 다른 각 크레이트를 다시 컴파일해야 합니다. 하나의 `target` 디렉토리를 공유함으로써 크레이트는 불필요한 재빌드를 피할 수 있습니다.
