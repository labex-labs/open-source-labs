# 인덱싱 대신 반복자 트레이트 메서드 사용하기

다음으로, `Config::build`의 본문을 수정하겠습니다. `args`가 `Iterator` 트레이트를 구현하므로, `next` 메서드를 호출할 수 있다는 것을 알고 있습니다! Listing 13-20 은 Listing 12-23 의 코드를 업데이트하여 `next` 메서드를 사용합니다.

파일 이름: `src/lib.rs`

```rust
impl Config {
    pub fn build(
        mut args: impl Iterator<Item = String>,
    ) -> Result<Config, &'static str> {
        args.next();

        let query = match args.next() {
            Some(arg) => arg,
            None => return Err("Didn't get a query string"),
        };

        let file_path = match args.next() {
            Some(arg) => arg,
            None => return Err("Didn't get a file path"),
        };

        let ignore_case = env::var("IGNORE_CASE").is_ok();

        Ok(Config {
            query,
            file_path,
            ignore_case,
        })
    }
}
```

Listing 13-20: 반복자 메서드를 사용하도록 `Config::build`의 본문 변경

`env::args`의 반환 값에서 첫 번째 값은 프로그램의 이름이라는 것을 기억하세요. 우리는 그것을 무시하고 다음 값을 얻고 싶으므로, 먼저 `next`를 호출하고 반환 값으로 아무것도 하지 않습니다. 그런 다음 `next`를 호출하여 `Config`의 `query` 필드에 넣을 값을 얻습니다. `next`가 `Some`을 반환하면, `match`를 사용하여 값을 추출합니다. `None`을 반환하면, 인수가 충분하지 않다는 의미이므로 `Err` 값으로 조기에 반환합니다. `filename` 값에 대해서도 동일한 작업을 수행합니다.
