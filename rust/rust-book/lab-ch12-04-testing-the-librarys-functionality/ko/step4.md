# `lines` 메서드를 사용하여 줄 반복하기

Rust 에는 문자열의 줄별 반복을 처리하는 데 유용한 메서드인 `lines`가 있습니다. 이는 목록 12-17 과 같이 작동합니다. 아직 컴파일되지 않는다는 점에 유의하십시오.

파일 이름: `src/lib.rs`

```rust
pub fn search<'a>(
    query: &str,
    contents: &'a str,
) -> Vec<&'a str> {
    for line in contents.lines() {
        // do something with line
    }
}
```

목록 12-17: `contents`의 각 줄을 반복

`lines` 메서드는 이터레이터 (iterator) 를 반환합니다. 13 장에서 이터레이터에 대해 자세히 이야기하겠지만, 목록 3-5 에서 이터레이터를 사용하는 방식을 보았다는 것을 기억하십시오. 여기서는 이터레이터가 있는 `for` 루프를 사용하여 컬렉션의 각 항목에 대해 일부 코드를 실행했습니다.
