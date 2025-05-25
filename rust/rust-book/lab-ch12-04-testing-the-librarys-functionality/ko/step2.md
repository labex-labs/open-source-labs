# 실패하는 테스트 작성하기

더 이상 필요하지 않으므로 프로그램의 동작을 확인하는 데 사용했던 `src/lib.rs` 및 `src/main.rs`에서 `println!` 문을 제거하겠습니다. 그런 다음, 11 장에서 했던 것처럼 `src/lib.rs`에 테스트 함수가 있는 `tests` 모듈을 추가합니다. 테스트 함수는 `search` 함수가 가져야 할 동작을 지정합니다. 즉, 쿼리와 검색할 텍스트를 가져와 쿼리를 포함하는 텍스트의 줄만 반환합니다. 목록 12-15 는 아직 컴파일되지 않는 이 테스트를 보여줍니다.

파일 이름: `src/lib.rs`

```rust
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn one_result() {
        let query = "duct";
        let contents = "\
Rust:
safe, fast, productive.
Pick three.";

        assert_eq!(
            vec!["safe, fast, productive."],
            search(query, contents)
        );
    }
}
```

목록 12-15: 우리가 원했던 `search` 함수에 대한 실패하는 테스트 생성

이 테스트는 문자열 `"duct"`를 검색합니다. 검색할 텍스트는 세 줄이며, 그 중 하나만 `"duct"`를 포함합니다 (여는 큰따옴표 뒤의 백슬래시는 Rust 에게 이 문자열 리터럴의 내용 시작 부분에 줄 바꿈 문자를 넣지 않도록 지시합니다). `search` 함수에서 반환된 값에 우리가 예상하는 줄만 포함되어 있는지 확인합니다.

테스트가 컴파일되지 않으므로 이 테스트를 실행하고 실패하는 것을 아직 볼 수 없습니다. `search` 함수가 아직 존재하지 않기 때문입니다! TDD 원칙에 따라, 목록 12-16 과 같이 항상 빈 벡터를 반환하는 `search` 함수 정의를 추가하여 테스트가 컴파일되고 실행되도록 충분한 코드를 추가합니다. 그러면 빈 벡터가 `"safe, fast, productive."` 줄을 포함하는 벡터와 일치하지 않으므로 테스트가 컴파일되고 실패해야 합니다.

파일 이름: `src/lib.rs`

```rust
pub fn search<'a>(
    query: &str,
    contents: &'a str,
) -> Vec<&'a str> {
    vec![]
}
```

목록 12-16: 테스트가 컴파일되도록 `search` 함수를 충분히 정의

`search`의 시그니처에서 명시적인 수명 `'a`를 정의하고 해당 수명을 `contents` 인수 및 반환 값과 함께 사용해야 합니다. 10 장에서 수명 매개변수가 어떤 인수 수명이 반환 값의 수명에 연결되는지 지정한다는 것을 기억하십시오. 이 경우 반환된 벡터에 인수 `contents` (인수 `query`가 아님) 의 슬라이스를 참조하는 문자열 슬라이스가 포함되어야 함을 나타냅니다.

다시 말해, `search` 함수에서 반환된 데이터가 `contents` 인수의 `search` 함수에 전달된 데이터만큼 오래 지속되도록 Rust 에 알려줍니다. 이것이 중요합니다! 슬라이스 _에 의해_ 참조된 데이터는 참조가 유효하려면 유효해야 합니다. 컴파일러가 `query`가 아닌 `contents`의 문자열 슬라이스를 만들고 있다고 가정하면 안전성 검사를 잘못 수행합니다.

수명 주석을 잊고 이 함수를 컴파일하려고 하면 다음과 같은 오류가 발생합니다.

```bash
error[E0106]: missing lifetime specifier
  --> src/lib.rs:31:10
   |
29 |     query: &str,
   |            ----
30 |     contents: &str,
   |               ----
31 | ) -> Vec<&str> {
   |          ^ expected named lifetime parameter
   |
   = help: this function's return type contains a borrowed value, but the
signature does not say whether it is borrowed from `query` or `contents`
help: consider introducing a named lifetime parameter
   |
28 ~ pub fn search<'a>(
29 ~     query: &'a str,
30 ~     contents: &'a str,
31 ~ ) -> Vec<&'a str> {
   |
```

Rust 는 두 인수 중 어느 것이 필요한지 알 수 없으므로 명시적으로 알려줘야 합니다. `contents`가 모든 텍스트를 포함하는 인수이고 일치하는 해당 텍스트의 일부를 반환하려는 경우, 수명 구문을 사용하여 반환 값에 연결해야 하는 인수가 `contents`임을 알 수 있습니다.

다른 프로그래밍 언어에서는 시그니처에서 인수를 반환 값에 연결할 필요가 없지만, 이 관행은 시간이 지남에 따라 더 쉬워질 것입니다. "수명으로 참조 유효성 검사"의 예와 이 예를 비교해 볼 수 있습니다.

이제 테스트를 실행해 보겠습니다.

```bash
[object Object]
```

훌륭합니다. 예상대로 테스트가 실패했습니다. 테스트를 통과시켜 봅시다!
