# main 에서 run 에서 반환된 오류 처리

목록 12-10 에서 `Config::build`에서 사용했던 것과 유사한 기술을 사용하여 오류를 확인하고 처리할 것입니다. 하지만 약간의 차이점이 있습니다.

파일 이름: `src/main.rs`

```rust
fn main() {
    --snip--

    println!("Searching for {}", config.query);
    println!("In file {}", config.file_path);

    if let Err(e) = run(config) {
        println!("Application error: {e}");
        process::exit(1);
    }
}
```

`run`이 `Err` 값을 반환하는지 확인하고, 반환하는 경우 `process::exit(1)`을 호출하기 위해 `unwrap_or_else` 대신 `if let`을 사용합니다. `run` 함수는 `Config::build`가 `Config` 인스턴스를 반환하는 것과 같은 방식으로 `unwrap`하려는 값을 반환하지 않습니다. `run`은 성공적인 경우 `()`를 반환하므로 오류 감지에만 관심이 있으며, `unwrap_or_else`가 언래핑된 값 (단지 `()`) 을 반환할 필요가 없습니다.

`if let` 및 `unwrap_or_else` 함수의 본문은 두 경우 모두 동일합니다. 즉, 오류를 출력하고 종료합니다.
