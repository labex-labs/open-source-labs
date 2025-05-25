# Release Profile 로 빌드 사용자 정의하기

Rust 에서 *release profile*은 프로그래머가 코드를 컴파일하기 위한 다양한 옵션을 더 잘 제어할 수 있도록 하는, 미리 정의되고 사용자 정의 가능한 서로 다른 구성을 가진 프로파일입니다. 각 프로파일은 다른 프로파일과 독립적으로 구성됩니다.

Cargo 는 두 가지 주요 프로파일을 가지고 있습니다: `cargo build`를 실행할 때 Cargo 가 사용하는 `dev` 프로파일과 `cargo build --release`를 실행할 때 Cargo 가 사용하는 `release` 프로파일입니다. `dev` 프로파일은 개발에 적합한 기본값으로 정의되어 있으며, `release` 프로파일은 release 빌드에 적합한 기본값을 가지고 있습니다.

이러한 프로파일 이름은 빌드 출력에서 익숙할 수 있습니다:

```bash
$ cargo build
    Finished dev [unoptimized + debuginfo] target(s) in 0.0s
$ cargo build --release
    Finished release [optimized] target(s) in 0.0s
```

`dev`와 `release`는 컴파일러가 사용하는 이러한 서로 다른 프로파일입니다.

Cargo 는 프로젝트의 `Cargo.toml` 파일에 `[profile.*]` 섹션을 명시적으로 추가하지 않은 경우 적용되는 각 프로파일에 대한 기본 설정을 가지고 있습니다. 사용자 정의하려는 모든 프로파일에 대해 `[profile.*]` 섹션을 추가하여 기본 설정의 하위 집합을 재정의할 수 있습니다. 예를 들어, `dev` 및 `release` 프로파일에 대한 `opt-level` 설정의 기본값은 다음과 같습니다:

파일 이름: `Cargo.toml`

```tomltoml
[profile.dev]
opt-level = 0

[profile.release]
opt-level = 3
```

`opt-level` 설정은 Rust 가 코드에 적용할 최적화 수준을 제어하며, 범위는 0 에서 3 까지입니다. 더 많은 최적화를 적용하면 컴파일 시간이 늘어나므로, 개발 중이고 코드를 자주 컴파일하는 경우, 결과 코드가 느리게 실행되더라도 더 빠르게 컴파일하기 위해 최적화를 덜 적용하려고 할 것입니다. 따라서 `dev`의 기본 `opt-level`은 `0`입니다. 코드를 릴리스할 준비가 되면 컴파일에 더 많은 시간을 할애하는 것이 좋습니다. release 모드에서는 한 번만 컴파일하지만, 컴파일된 프로그램을 여러 번 실행하므로 release 모드는 더 긴 컴파일 시간과 더 빠르게 실행되는 코드를 교환합니다. 이것이 `release` 프로파일의 기본 `opt-level`이 `3`인 이유입니다.

`Cargo.toml`에 다른 값을 추가하여 기본 설정을 재정의할 수 있습니다. 예를 들어, 개발 프로파일에서 최적화 레벨 1 을 사용하려면 프로젝트의 `Cargo.toml` 파일에 다음 두 줄을 추가할 수 있습니다:

파일 이름: `Cargo.toml`

```tomltoml
[profile.dev]
opt-level = 1
```

이 코드는 기본 설정인 `0`을 재정의합니다. 이제 `cargo build`를 실행하면 Cargo 는 `dev` 프로파일의 기본값과 `opt-level`에 대한 사용자 정의를 사용합니다. `opt-level`을 `1`로 설정했으므로 Cargo 는 기본값보다 더 많은 최적화를 적용하지만, release 빌드만큼 많지는 않습니다.

각 프로파일에 대한 구성 옵션 및 기본값의 전체 목록은 *https://doc.rust-lang.org/cargo/reference/profiles.html*에서 Cargo 의 문서를 참조하십시오.
