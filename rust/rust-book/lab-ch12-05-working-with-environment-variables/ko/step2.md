# 대소문자 구분 없는 검색 함수에 대한 실패하는 테스트 작성하기

먼저 환경 변수에 값이 있을 때 호출될 새로운 `search_case_insensitive` 함수를 추가합니다. TDD 프로세스를 계속 따를 것이므로 첫 번째 단계는 다시 실패하는 테스트를 작성하는 것입니다. 새로운 `search_case_insensitive` 함수에 대한 새로운 테스트를 추가하고, 두 테스트 간의 차이점을 명확히 하기 위해 이전 테스트 이름을 `one_result`에서 `case_sensitive`로 변경합니다. 이는 Listing 12-20 에 나와 있습니다.

파일 이름: `src/lib.rs`

```rust
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn case_sensitive() {
        let query = "duct";
        let contents = "\
Rust:
safe, fast, productive.
Pick three.
Duct tape.";

        assert_eq!(
            vec!["safe, fast, productive."],
            search(query, contents)
        );
    }

    #[test]
    fn case_insensitive() {
        let query = "rUsT";
        let contents = "\
Rust:
safe, fast, productive.
Pick three.
Trust me.";

        assert_eq!(
            vec!["Rust:", "Trust me."],
            search_case_insensitive(query, contents)
        );
    }
}
```

Listing 12-20: 곧 추가할 대소문자 구분 없는 함수에 대한 새로운 실패하는 테스트 추가

이전 테스트의 `contents`도 편집했습니다. 대문자 *D*를 사용하여 텍스트 `"Duct tape."`가 포함된 새 줄을 추가했는데, 이는 대소문자를 구분하는 방식으로 검색할 때 쿼리 `"duct"`와 일치하지 않아야 합니다. 이러한 방식으로 이전 테스트를 변경하면 이미 구현한 대소문자 구분 검색 기능을 실수로 손상시키지 않도록 하는 데 도움이 됩니다. 이 테스트는 이제 통과해야 하며, 대소문자 구분 없는 검색 작업을 하는 동안 계속 통과해야 합니다.

대소문자 _구분 없는_ 검색에 대한 새 테스트는 `"rUsT"`를 쿼리로 사용합니다. 곧 추가할 `search_case_insensitive` 함수에서 쿼리 `"rUsT"`는 대문자 *R*이 있는 `"Rust:"`가 포함된 줄과 쿼리와 다른 대소문자를 가지고 있음에도 불구하고 `"Trust me."` 줄과 일치해야 합니다. 이것이 실패하는 테스트이며, `search_case_insensitive` 함수를 아직 정의하지 않았기 때문에 컴파일에 실패합니다. Listing 12-16 에서 `search` 함수에 대해 했던 방식과 유사하게 항상 빈 벡터를 반환하는 스켈레톤 구현을 추가하여 테스트가 컴파일되고 실패하는 것을 확인할 수 있습니다.
