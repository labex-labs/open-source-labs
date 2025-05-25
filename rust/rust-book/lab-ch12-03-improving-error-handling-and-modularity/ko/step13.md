# 코드를 라이브러리 크레이트 (Library Crate) 로 분할

지금까지 `minigrep` 프로젝트가 잘 진행되고 있습니다! 이제 `src/main.rs` 파일을 분할하고 일부 코드를 `src/lib.rs` 파일에 넣을 것입니다. 이렇게 하면 코드를 테스트하고 책임이 적은 `src/main.rs` 파일을 가질 수 있습니다.

`main` 함수에 없는 모든 코드를 `src/main.rs`에서 `src/lib.rs`로 이동해 보겠습니다.

- `run` 함수 정의
- 관련 `use` 문
- `Config`의 정의
- `Config::build` 함수 정의

`src/lib.rs`의 내용은 목록 12-13 에 표시된 시그니처를 가져야 합니다 (간결성을 위해 함수의 본문은 생략했습니다). 목록 12-14 에서 `src/main.rs`를 수정할 때까지는 컴파일되지 않습니다.

파일 이름: `src/lib.rs`

```rust
use std::error::Error;
use std::fs;

pub struct Config {
    pub query: String,
    pub file_path: String,
}

impl Config {
    pub fn build(
        args: &[String],
    ) -> Result<Config, &'static str> {
        --snip--
    }
}

pub fn run(config: Config) -> Result<(), Box<dyn Error>> {
    --snip--
}
```

목록 12-13: `Config` 및 `run`을 `src/lib.rs`로 이동

`pub` 키워드를 광범위하게 사용했습니다. `Config`에서, 해당 필드와 `build` 메서드에서, 그리고 `run` 함수에서 사용했습니다. 이제 테스트할 수 있는 공개 API 가 있는 라이브러리 크레이트가 있습니다!

이제 목록 12-14 에 표시된 것처럼 `src/lib.rs`로 이동한 코드를 `src/main.rs`의 바이너리 크레이트의 범위로 가져와야 합니다.

파일 이름: `src/main.rs`

```rust
use std::env;
use std::process;

use minigrep::Config;

fn main() {
    --snip--
    if let Err(e) = minigrep::run(config) {
        --snip--
    }
}
```

목록 12-14: `src/main.rs`에서 `minigrep` 라이브러리 크레이트 사용

`use minigrep::Config` 줄을 추가하여 라이브러리 크레이트에서 `Config` 타입을 바이너리 크레이트의 범위로 가져오고, `run` 함수 앞에 크레이트 이름을 붙입니다. 이제 모든 기능이 연결되어 작동해야 합니다. `cargo run`으로 프로그램을 실행하고 모든 것이 제대로 작동하는지 확인합니다.

휴! 많은 작업이었지만, 앞으로 성공할 수 있도록 준비했습니다. 이제 오류를 처리하는 것이 훨씬 쉬워졌고 코드를 더 모듈화했습니다. 앞으로는 거의 모든 작업이 `src/lib.rs`에서 수행될 것입니다.

이 새로운 모듈성을 활용하여 이전 코드에서는 어려웠지만 새로운 코드에서는 쉬운 작업을 수행해 보겠습니다. 즉, 몇 가지 테스트를 작성할 것입니다!
