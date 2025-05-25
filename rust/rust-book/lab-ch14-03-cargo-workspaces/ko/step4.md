# Workspace 에서 외부 패키지에 의존하기

workspace 에는 각 크레이트의 디렉토리에 *Cargo.lock*이 있는 대신 최상위 레벨에 하나의 _Cargo.lock_ 파일만 있다는 점에 유의하십시오. 이렇게 하면 모든 크레이트가 모든 종속성의 동일한 버전을 사용하도록 보장됩니다. `rand` 패키지를 _adder/Cargo.toml_ 및 _add_one/Cargo.toml_ 파일에 추가하면 Cargo 는 둘 다 `rand`의 한 버전으로 확인하고 해당 내용을 하나의 *Cargo.lock*에 기록합니다. workspace 의 모든 크레이트가 동일한 종속성을 사용하도록 하면 크레이트가 항상 서로 호환됩니다. `add_one` 크레이트에서 `rand` 크레이트를 사용할 수 있도록 `rand` 크레이트를 _add_one/Cargo.toml_ 파일의 `[dependencies]` 섹션에 추가해 보겠습니다.

파일 이름: `add_one/Cargo.toml`

```tomlrust
[dependencies]
rand = "0.8.5"
```

이제 `add_one/src/lib.rs` 파일에 `use rand;`를 추가할 수 있으며, `add` 디렉토리에서 `cargo build`를 실행하여 전체 workspace 를 빌드하면 `rand` 크레이트가 가져와 컴파일됩니다. 범위 내로 가져온 `rand`를 참조하지 않기 때문에 경고가 하나 표시됩니다.

```bash
$ cargo build
    Updating crates.io index
  Downloaded rand v0.8.5
   --snip--
   Compiling rand v0.8.5
   Compiling add_one v0.1.0 (file:///projects/add/add_one)
   Compiling adder v0.1.0 (file:///projects/add/adder)
    Finished dev [unoptimized + debuginfo] target(s) in 10.18s
```

최상위 *Cargo.lock*에는 이제 `rand`에 대한 `add_one`의 종속성에 대한 정보가 포함되어 있습니다. 그러나 `rand`가 workspace 어딘가에서 사용되더라도 `rand`를 해당 `Cargo.toml` 파일에도 추가하지 않으면 workspace 의 다른 크레이트에서 사용할 수 없습니다. 예를 들어, `adder` 패키지의 `adder/src/main.rs` 파일에 `use rand;`를 추가하면 오류가 발생합니다.

```bash
$ cargo build
   --snip--
   Compiling adder v0.1.0 (file:///projects/add/adder)
error[E0432]: unresolved import `rand`
 --> adder/src/main.rs:2:5
  |
2 | use rand;
  |     ^^^^ no external crate `rand`
```

이 문제를 해결하려면 `adder` 패키지의 `Cargo.toml` 파일을 편집하고 `rand`가 해당 패키지의 종속성임을 나타냅니다. `adder` 패키지를 빌드하면 *Cargo.lock*에서 `adder`의 종속성 목록에 `rand`가 추가되지만, `rand`의 추가 복사본은 다운로드되지 않습니다. Cargo 는 `rand` 패키지를 사용하는 workspace 의 모든 패키지의 모든 크레이트가 동일한 버전을 사용하도록 보장하여 공간을 절약하고 workspace 의 크레이트가 서로 호환되도록 합니다.
