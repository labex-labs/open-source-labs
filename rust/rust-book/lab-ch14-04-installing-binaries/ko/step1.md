# cargo install 로 바이너리 설치하기

`cargo install` 명령을 사용하면 바이너리 크레이트 (binary crate) 를 로컬에 설치하고 사용할 수 있습니다. 이는 시스템 패키지를 대체하기 위한 것이 아니라, Rust 개발자가 *https://crates.io*에서 공유된 도구를 편리하게 설치할 수 있도록 하기 위한 것입니다. 바이너리 타겟 (binary target) 이 있는 패키지만 설치할 수 있다는 점에 유의하십시오. *바이너리 타겟*은 크레이트에 `src/main.rs` 파일 또는 바이너리로 지정된 다른 파일이 있는 경우 생성되는 실행 가능한 프로그램입니다. 이는 자체적으로 실행할 수 없지만 다른 프로그램 내에 포함하기에 적합한 라이브러리 타겟 (library target) 과는 대조적입니다. 일반적으로 크레이트는 _README_ 파일에 크레이트가 라이브러리인지, 바이너리 타겟을 가지고 있는지, 또는 둘 다인지에 대한 정보가 있습니다.

`cargo install`로 설치된 모든 바이너리는 설치 루트의 `bin` 폴더에 저장됩니다. `rustup.rs`를 사용하여 Rust 를 설치했고 사용자 지정 구성이 없는 경우, 이 디렉토리는 \_$HOME/.cargo/bin_이 됩니다. `cargo install\`로 설치한 프로그램을 실행하려면 해당 디렉토리가 `$PATH`에 포함되어 있는지 확인하십시오.

예를 들어, 12 장에서 파일 검색을 위한 `ripgrep`이라는 `grep` 도구의 Rust 구현에 대해 언급했습니다. `ripgrep`을 설치하려면 다음을 실행할 수 있습니다.

```bash
$ cargo install ripgrep
    Updating crates.io index
  Downloaded ripgrep v13.0.0
  Downloaded 1 crate (243.3 KB) in 0.88s
  Installing ripgrep v13.0.0
   --snip--
   Compiling ripgrep v13.0.0
    Finished release [optimized + debuginfo] target(s) in 3m 10s
  Installing ~/.cargo/bin/rg
   Installed package `ripgrep v13.0.0` (executable `rg`)
```

출력의 두 번째 줄에서 설치된 바이너리의 위치와 이름을 보여줍니다. `ripgrep`의 경우 `rg`입니다. 앞서 언급했듯이 설치 디렉토리가 `$PATH`에 포함되어 있다면 `rg --help`를 실행하고 더 빠르고 Rust 스러운 파일 검색 도구를 사용할 수 있습니다!
