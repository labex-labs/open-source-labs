# run 함수에서 오류 반환

나머지 프로그램 로직이 `run` 함수로 분리되었으므로 목록 12-9 에서 `Config::build`에서 했던 것처럼 오류 처리를 개선할 수 있습니다. `expect`를 호출하여 프로그램이 패닉 상태가 되도록 하는 대신, `run` 함수는 문제가 발생하면 `Result<T, E>`를 반환합니다. 이렇게 하면 오류 처리를 둘러싼 로직을 사용자 친화적인 방식으로 `main`으로 더욱 통합할 수 있습니다. 목록 12-12 는 `run`의 시그니처와 본문에 필요한 변경 사항을 보여줍니다.

파일 이름: `src/main.rs`

```rust
1 use std::error::Error;

--snip--

2 fn run(config: Config) -> Result<(), Box<dyn Error>> {
    let contents = fs::read_to_string(config.file_path)3 ?;

    println!("With text:\n{contents}");

  4 Ok(())
}
```

목록 12-12: `Result`를 반환하도록 `run` 함수 변경

여기서 세 가지 중요한 변경을 했습니다. 먼저, `run` 함수의 반환 유형을 `Result<(), Box<dyn Error>>`로 변경했습니다 \[2]. 이 함수는 이전에 유닛 타입 `()`을 반환했으며, `Ok`의 경우 반환되는 값으로 유지합니다.

오류 유형의 경우 _트레이트 객체_(trait object) `Box<dyn Error>`를 사용했습니다 (그리고 맨 위에 `use` 문을 사용하여 `std::error::Error`를 범위 내로 가져왔습니다 \[1]). 트레이트 객체는 17 장에서 다룰 것입니다. 지금은 `Box<dyn Error>`가 함수가 `Error` 트레이트를 구현하는 유형을 반환한다는 것을 의미하지만, 반환 값이 어떤 특정 유형이 될지는 지정할 필요가 없다는 것만 알아두세요. 이렇게 하면 서로 다른 오류 사례에서 서로 다른 유형일 수 있는 오류 값을 반환할 수 있는 유연성이 제공됩니다. `dyn` 키워드는 _동적_(dynamic) 의 줄임말입니다.

둘째, 9 장에서 이야기했듯이 `expect` 호출을 `?` 연산자 \[3]로 대체했습니다. 오류가 발생하면 `panic!`하는 대신, `?`는 현재 함수에서 오류 값을 호출자에게 반환하여 처리하도록 합니다.

셋째, `run` 함수는 이제 성공적인 경우 `Ok` 값을 반환합니다 \[4]. `run` 함수의 성공 유형을 시그니처에서 `()`로 선언했으므로 유닛 타입 값을 `Ok` 값으로 래핑해야 합니다. 이 `Ok(())` 구문은 처음에는 약간 이상하게 보일 수 있지만, 이처럼 `()`를 사용하는 것은 부작용만을 위해 `run`을 호출하고 있다는 것을 나타내는 관용적인 방법입니다. 즉, 필요한 값을 반환하지 않습니다.

이 코드를 실행하면 컴파일되지만 경고가 표시됩니다.

    warning: unused `Result` that must be used
      --> src/main.rs:19:5
       |
    19 |     run(config);
       |     ^^^^^^^^^^^^
       |
       = note: `#[warn(unused_must_use)]` on by default
       = note: this `Result` may be an `Err` variant, which should be
    handled

Rust 는 우리 코드가 `Result` 값을 무시했으며 `Result` 값은 오류가 발생했음을 나타낼 수 있다고 알려줍니다. 하지만 오류가 있었는지 여부를 확인하지 않고 있으며, 컴파일러는 아마도 여기에 일부 오류 처리 코드를 넣으려고 했을 것이라고 상기시켜 줍니다! 이제 그 문제를 해결해 보겠습니다.
