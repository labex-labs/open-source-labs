# 인수 파서 추출

명령줄 구문 분석 로직을 src/lib.rs*로 이동하기 전에 `main`이 호출할 함수로 인수를 구문 분석하는 기능을 추출합니다. 목록 12-5 는 `parse_config`라는 새로운 함수를 호출하는 `main`의 새로운 시작 부분을 보여줍니다. 이 함수는 현재 *src/main.rs\*에서 정의할 것입니다.

파일 이름: `src/main.rs`

```rust
fn main() {
    let args: Vec<String> = env::args().collect();

    let (query, file_path) = parse_config(&args);

    --snip--
}

fn parse_config(args: &[String]) -> (&str, &str) {
    let query = &args[1];
    let file_path = &args[2];

    (query, file_path)
}
```

목록 12-5: `main`에서 `parse_config` 함수 추출

여전히 명령줄 인수를 벡터로 수집하지만, `main` 함수 내에서 인덱스 1 의 인수 값을 변수 `query`에 할당하고 인덱스 2 의 인수 값을 변수 `file_path`에 할당하는 대신 전체 벡터를 `parse_config` 함수에 전달합니다. 그런 다음 `parse_config` 함수는 어떤 인수가 어떤 변수에 들어가는지 결정하는 로직을 가지고 값을 `main`으로 다시 전달합니다. 여전히 `main`에서 `query` 및 `file_path` 변수를 생성하지만, `main`은 더 이상 명령줄 인수와 변수가 어떻게 대응하는지 결정하는 책임을 지지 않습니다.

이러한 재작업은 작은 프로그램에 과도한 것처럼 보일 수 있지만, 작고 점진적인 단계로 리팩토링하고 있습니다. 이 변경을 수행한 후 프로그램을 다시 실행하여 인수 구문 분석이 여전히 작동하는지 확인합니다. 문제가 발생했을 때 문제의 원인을 식별하는 데 도움이 되도록 진행 상황을 자주 확인하는 것이 좋습니다.
