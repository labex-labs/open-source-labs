# 더 많은 기능을 얻기 위해 크레이트 사용하기

크레이트는 Rust 소스 코드 파일의 모음이라는 것을 기억하세요. 우리가 구축해 온 프로젝트는 실행 파일인 *바이너리 크레이트*입니다. `rand` 크레이트는 다른 프로그램에서 사용하도록 설계된 코드를 포함하고 자체적으로 실행될 수 없는 *라이브러리 크레이트*입니다.

Cargo 가 외부 크레이트를 조정하는 방식은 Cargo 가 진정으로 빛을 발하는 부분입니다. `rand`를 사용하는 코드를 작성하기 전에, `Cargo.toml` 파일을 수정하여 `rand` 크레이트를 종속성으로 포함해야 합니다. 지금 해당 파일을 열고 Cargo 가 생성한 `[dependencies]` 섹션 헤더 아래에 다음 줄을 추가합니다. 여기에 표시된 대로 정확하게 `rand`를 지정하고, 이 버전 번호를 사용해야 합니다. 그렇지 않으면 이 튜토리얼의 코드 예제가 작동하지 않을 수 있습니다.

파일 이름: `Cargo.toml`

```tomlrust
[dependencies]
rand = "0.8.5"
```

`Cargo.toml` 파일에서 헤더 뒤에 오는 모든 것은 다른 섹션이 시작될 때까지 해당 섹션의 일부입니다. `[dependencies]`에서 Cargo 에게 프로젝트가 의존하는 외부 크레이트와 해당 크레이트의 어떤 버전을 요구하는지 알려줍니다. 이 경우, 시맨틱 버전 지정자 `0.8.5`를 사용하여 `rand` 크레이트를 지정합니다. Cargo 는 버전 번호를 작성하기 위한 표준인 시맨틱 버전 관리 (때로는 *SemVer*라고도 함) 를 이해합니다. 지정자 `0.8.5`는 실제로 `^0.8.5`의 약어이며, 이는 최소 0.8.5 이상이지만 0.9.0 미만인 모든 버전을 의미합니다.

Cargo 는 이러한 버전을 버전 0.8.5 와 호환되는 공용 API 를 갖는 것으로 간주하며, 이 사양은 이 장의 코드와 함께 컴파일될 최신 패치 릴리스를 얻도록 보장합니다. 버전 0.9.0 이상은 다음 예제에서 사용하는 것과 동일한 API 를 갖는다고 보장할 수 없습니다.

이제 코드를 변경하지 않고 Listing 2-2 에 표시된 대로 프로젝트를 빌드해 보겠습니다.

```bash
$ cargo build
    Updating crates.io index
  Downloaded rand v0.8.5
  Downloaded libc v0.2.127
  Downloaded getrandom v0.2.7
  Downloaded cfg-if v1.0.0
  Downloaded ppv-lite86 v0.2.16
  Downloaded rand_chacha v0.3.1
  Downloaded rand_core v0.6.3
   Compiling rand_core v0.6.3
   Compiling libc v0.2.127
   Compiling getrandom v0.2.7
   Compiling cfg-if v1.0.0
   Compiling ppv-lite86 v0.2.16
   Compiling rand_chacha v0.3.1
   Compiling rand v0.8.5
   Compiling guessing_game v0.1.0 (file:///projects/guessing_game)
    Finished dev [unoptimized + debuginfo] target(s) in 2.53s
```

Listing 2-2: `rand` 크레이트를 종속성으로 추가한 후 `cargo build`를 실행한 결과

다른 버전 번호 (하지만 SemVer 덕분에 모두 코드와 호환됨) 와 다른 줄 (운영 체제에 따라 다름) 이 표시될 수 있으며, 줄의 순서가 다를 수 있습니다.

외부 종속성을 포함하면 Cargo 는 종속성이 필요로 하는 모든 것의 최신 버전을 *레지스트리*에서 가져옵니다. 레지스트리는 Crates.io 의 데이터 사본이며 *https://crates.io*에 있습니다. Crates.io 는 Rust 생태계의 사람들이 다른 사람들이 사용할 수 있도록 오픈 소스 Rust 프로젝트를 게시하는 곳입니다.

레지스트리를 업데이트한 후 Cargo 는 `[dependencies]` 섹션을 확인하고 아직 다운로드되지 않은 나열된 모든 크레이트를 다운로드합니다. 이 경우, `rand`만 종속성으로 나열했지만 Cargo 는 `rand`가 작동하기 위해 의존하는 다른 크레이트도 가져왔습니다. 크레이트를 다운로드한 후 Rust 는 이를 컴파일한 다음 종속성을 사용할 수 있는 상태로 프로젝트를 컴파일합니다.

변경 사항 없이 즉시 `cargo build`를 다시 실행하면 `Finished` 줄을 제외하고는 아무런 출력도 얻지 못합니다. Cargo 는 이미 종속성을 다운로드하고 컴파일했음을 알고 있으며, `Cargo.toml` 파일에서 이에 대해 아무것도 변경하지 않았습니다. Cargo 는 또한 코드에 대해 아무것도 변경하지 않았다는 것을 알고 있으므로 다시 컴파일하지도 않습니다. 할 일이 없으면 단순히 종료됩니다.

`src/main.rs` 파일을 열고 사소한 변경을 한 다음 저장하고 다시 빌드하면 두 줄의 출력만 표시됩니다.

```bash
$ cargo build
   Compiling guessing_game v0.1.0 (file:///projects/guessing_game)
    Finished dev [unoptimized + debuginfo] target(s) in 2.53 secs
```

이 줄은 Cargo 가 `src/main.rs` 파일에 대한 작은 변경 사항으로 빌드를 업데이트했음을 보여줍니다. 종속성이 변경되지 않았으므로 Cargo 는 이미 다운로드하고 컴파일한 것을 재사용할 수 있음을 알고 있습니다.
