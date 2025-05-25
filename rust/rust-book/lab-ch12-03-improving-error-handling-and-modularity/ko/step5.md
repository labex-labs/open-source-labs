# Config 에 대한 생성자 생성

지금까지 명령줄 인수를 구문 분석하는 책임을 `main`에서 추출하여 `parse_config` 함수에 넣었습니다. 이렇게 하면 `query` 및 `file_path` 값이 관련되어 있으며 해당 관계가 코드에 전달되어야 함을 알 수 있었습니다. 그런 다음 `query` 및 `file_path`의 관련 목적을 지정하고 `parse_config` 함수에서 구조체 필드 이름으로 값의 이름을 반환할 수 있도록 `Config` 구조체를 추가했습니다.

이제 `parse_config` 함수의 목적이 `Config` 인스턴스를 생성하는 것이므로, `parse_config`를 일반 함수에서 `Config` 구조체와 연결된 `new`라는 함수로 변경할 수 있습니다. 이렇게 변경하면 코드가 더 관용적으로 됩니다. `String::new`을 호출하여 `String`과 같은 표준 라이브러리의 유형 인스턴스를 생성할 수 있습니다. 마찬가지로 `parse_config`를 `Config`와 연결된 `new` 함수로 변경하면 `Config::new`를 호출하여 `Config`의 인스턴스를 생성할 수 있습니다. 목록 12-7 은 필요한 변경 사항을 보여줍니다.

파일 이름: `src/main.rs`

```rust
fn main() {
    let args: Vec<String> = env::args().collect();

  1 let config = Config::new(&args);

    --snip--
}

--snip--

2 impl Config {
  3 fn new(args: &[String]) -> Config {
        let query = args[1].clone();
        let file_path = args[2].clone();

        Config { query, file_path }
    }
}
```

목록 12-7: `parse_config`를 `Config::new`로 변경

`parse_config`를 호출하던 `main`을 업데이트하여 대신 `Config::new`를 호출하도록 했습니다 \[1]. `parse_config`의 이름을 `new`로 변경하고 \[3] `impl` 블록 내로 이동하여 \[2] `new` 함수를 `Config`와 연결했습니다. 이 코드를 다시 컴파일하여 작동하는지 확인하십시오.
