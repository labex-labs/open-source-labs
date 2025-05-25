# panic! 호출 대신 Result 반환

대신 성공적인 경우 `Config` 인스턴스를 포함하고 오류의 경우 문제를 설명하는 `Result` 값을 반환할 수 있습니다. 또한 많은 프로그래머가 `new` 함수가 절대 실패하지 않기를 기대하기 때문에 함수 이름을 `new`에서 `build`로 변경할 것입니다. `Config::build`가 `main`과 통신할 때 `Result` 타입을 사용하여 문제가 있음을 알릴 수 있습니다. 그런 다음 `main`을 변경하여 `Err` 변형을 `panic!` 호출이 발생하는 `thread 'main'` 및 `RUST_BACKTRACE`에 대한 주변 텍스트 없이 사용자에게 더 실용적인 오류로 변환할 수 있습니다.

목록 12-9 는 이제 `Config::build`라고 부르는 함수의 반환 값과 `Result`를 반환하는 데 필요한 함수 본문에 필요한 변경 사항을 보여줍니다. 다음 목록에서 수행할 `main`도 업데이트할 때까지 이 코드는 컴파일되지 않습니다.

파일 이름: `src/main.rs`

```rust
impl Config {
    fn build(args: &[String]) -> Result<Config, &'static str> {
        if args.len() < 3 {
            return Err("not enough arguments");
        }

        let query = args[1].clone();
        let file_path = args[2].clone();

        Ok(Config { query, file_path })
    }
}
```

목록 12-9: `Config::build`에서 `Result` 반환

`build` 함수는 성공적인 경우 `Config` 인스턴스와 오류의 경우 `&'static str`을 사용하여 `Result`를 반환합니다. 오류 값은 항상 `'static` 수명을 가진 문자열 리터럴이 됩니다.

함수 본문에서 두 가지 변경 사항을 적용했습니다. 사용자가 충분한 인수를 전달하지 않을 때 `panic!`을 호출하는 대신 이제 `Err` 값을 반환하고 `Config` 반환 값을 `Ok`로 래핑했습니다. 이러한 변경 사항은 함수가 새로운 타입 시그니처를 준수하도록 합니다.

`Config::build`에서 `Err` 값을 반환하면 `main` 함수가 `build` 함수에서 반환된 `Result` 값을 처리하고 오류의 경우 프로세스를 더 깔끔하게 종료할 수 있습니다.
