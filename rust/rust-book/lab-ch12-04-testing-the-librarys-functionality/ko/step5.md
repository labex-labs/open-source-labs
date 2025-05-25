# 각 줄에서 쿼리 검색하기

다음으로, 현재 줄에 쿼리 문자열이 포함되어 있는지 확인합니다. 다행히 문자열에는 이를 수행하는 데 도움이 되는 `contains`라는 메서드가 있습니다! 목록 12-18 과 같이 `search` 함수에 `contains` 메서드 호출을 추가합니다. 이것 역시 아직 컴파일되지 않는다는 점에 유의하십시오.

파일 이름: `src/lib.rs`

```rust
pub fn search<'a>(
    query: &str,
    contents: &'a str,
) -> Vec<&'a str> {
    for line in contents.lines() {
        if line.contains(query) {
            // do something with line
        }
    }
}
```

목록 12-18: 줄에 `query` 문자열이 포함되어 있는지 확인하는 기능 추가

현재 기능을 구축하고 있습니다. 코드가 컴파일되도록 하려면 함수 시그니처에서 표시했듯이 본문에서 값을 반환해야 합니다.
