# 반복자 어댑터로 코드 명확하게 만들기

I/O 프로젝트의 `search` 함수에서도 반복자를 활용할 수 있습니다. Listing 13-21 에 Listing 12-19 와 동일하게 재현되어 있습니다.

파일 이름: `src/lib.rs`

```rust
pub fn search<'a>(
    query: &str,
    contents: &'a str,
) -> Vec<&'a str> {
    let mut results = Vec::new();

    for line in contents.lines() {
        if line.contains(query) {
            results.push(line);
        }
    }

    results
}
```

Listing 13-21: Listing 12-19 의 `search` 함수 구현

반복자 어댑터 메서드를 사용하여 이 코드를 더 간결하게 작성할 수 있습니다. 그렇게 하면 가변 중간 `results` 벡터를 사용하지 않아도 됩니다. 함수형 프로그래밍 스타일은 코드를 더 명확하게 만들기 위해 가변 상태의 양을 최소화하는 것을 선호합니다. 가변 상태를 제거하면 `results` 벡터에 대한 동시 접근을 관리할 필요가 없으므로, 향후 검색을 병렬로 수행할 수 있는 기능 향상을 가능하게 할 수 있습니다. Listing 13-22 는 이러한 변경 사항을 보여줍니다.

파일 이름: `src/lib.rs`

```rust
pub fn search<'a>(
    query: &str,
    contents: &'a str,
) -> Vec<&'a str> {
    contents
        .lines()
        .filter(|line| line.contains(query))
        .collect()
}
```

Listing 13-22: `search` 함수 구현에서 반복자 어댑터 메서드 사용

`search` 함수의 목적은 `query`를 포함하는 `contents`의 모든 줄을 반환하는 것임을 기억하세요. Listing 13-16 의 `filter` 예제와 유사하게, 이 코드는 `line.contains(query)`가 `true`를 반환하는 줄만 유지하기 위해 `filter` 어댑터를 사용합니다. 그런 다음 `collect`를 사용하여 일치하는 줄을 다른 벡터로 수집합니다. 훨씬 간단합니다! `search_case_insensitive` 함수에서도 동일한 변경을 수행하여 반복자 메서드를 사용해 보세요.
