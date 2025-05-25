# main 에서 로직 추출

이제 구성 구문 분석 리팩토링을 완료했으므로 프로그램의 로직으로 넘어가겠습니다. "이진 프로젝트의 관심사 분리"에서 언급했듯이, 구성 설정 또는 오류 처리에 관여하지 않는 `main` 함수에 현재 있는 모든 로직을 포함하는 `run`이라는 함수를 추출할 것입니다. 완료되면 `main`은 간결하고 검사하기 쉬우며, 다른 모든 로직에 대한 테스트를 작성할 수 있습니다.

목록 12-11 은 추출된 `run` 함수를 보여줍니다. 지금은 함수를 추출하는 작은 점진적인 개선만 하고 있습니다. 여전히 `src/main.rs`에서 함수를 정의하고 있습니다.

파일 이름: `src/main.rs`

```rust
fn main() {
    --snip--

    println!("Searching for {}", config.query);
    println!("In file {}", config.file_path);

    run(config);
}

fn run(config: Config) {
    let contents = fs::read_to_string(config.file_path)
        .expect("Should have been able to read the file");

    println!("With text:\n{contents}");
}

--snip--
```

목록 12-11: 나머지 프로그램 로직을 포함하는 `run` 함수 추출

`run` 함수는 이제 파일을 읽는 것부터 시작하여 `main`의 나머지 모든 로직을 포함합니다. `run` 함수는 `Config` 인스턴스를 인수로 사용합니다.
