# 반환된 반복자 직접 사용하기

I/O 프로젝트의 `src/main.rs` 파일을 엽니다. 다음과 같이 보일 것입니다.

파일 이름: `src/main.rs`

```rust
fn main() {
    let args: Vec<String> = env::args().collect();

    let config = Config::build(&args).unwrap_or_else(|err| {
        eprintln!("Problem parsing arguments: {err}");
        process::exit(1);
    });

    --snip--
}
```

먼저 Listing 12-24 에 있던 `main` 함수의 시작 부분을 Listing 13-18 의 코드로 변경합니다. 이번에는 반복자를 사용합니다. `Config::build`도 업데이트해야 컴파일됩니다.

파일 이름: `src/main.rs`

```rust
fn main() {
    let config =
        Config::build(env::args()).unwrap_or_else(|err| {
            eprintln!("Problem parsing arguments: {err}");
            process::exit(1);
        });

    --snip--
}
```

Listing 13-18: `env::args`의 반환 값을 `Config::build`에 전달

`env::args` 함수는 반복자를 반환합니다! 반복자 값을 벡터로 수집한 다음 슬라이스를 `Config::build`에 전달하는 대신, 이제 `env::args`에서 반환된 반복자의 소유권을 직접 `Config::build`에 전달합니다.

다음으로, `Config::build`의 정의를 업데이트해야 합니다. I/O 프로젝트의 `src/lib.rs` 파일에서 `Config::build`의 시그니처를 Listing 13-19 와 같이 변경해 보겠습니다. 함수 본문을 업데이트해야 하므로, 이것 역시 아직 컴파일되지 않습니다.

파일 이름: `src/lib.rs`

```rust
impl Config {
    pub fn build(
        mut args: impl Iterator<Item = String>,
    ) -> Result<Config, &'static str> {
        --snip--
```

Listing 13-19: 반복자를 예상하도록 `Config::build`의 시그니처 업데이트

`env::args` 함수에 대한 표준 라이브러리 문서는 반환하는 반복자의 유형이 `std::env::Args`이며, 해당 유형이 `Iterator` 트레이트를 구현하고 `String` 값을 반환한다는 것을 보여줍니다.

`Config::build` 함수의 시그니처를 업데이트하여 매개변수 `args`가 `&[String]` 대신 `impl Iterator<Item = String>` 트레이트 바운드를 가진 제네릭 타입을 갖도록 했습니다. "매개변수로서의 트레이트"에서 논의한 `impl Trait` 구문을 사용하면 `args`가 `Iterator` 트레이트를 구현하고 `String` 항목을 반환하는 모든 유형이 될 수 있습니다.

`args`의 소유권을 가져가고 반복하여 `args`를 변경할 것이므로, 가변으로 만들기 위해 `args` 매개변수 사양에 `mut` 키워드를 추가할 수 있습니다.
