# 개발 종속성

때로는 테스트 (또는 예제 또는 벤치마크) 에만 필요한 종속성이 있습니다. 이러한 종속성은 `Cargo.toml` 파일의 `[dev-dependencies]` 섹션에 추가됩니다. 이러한 종속성은 이 패키지에 의존하는 다른 패키지로 전파되지 않습니다.

예시 중 하나는 [`pretty_assertions`](https://docs.rs/pretty_assertions/1.0.0/pretty_assertions/index.html)입니다. 이 라이브러리는 표준 `assert_eq!` 및 `assert_ne!` 매크로를 확장하여 다채로운 차이점을 제공합니다.
`Cargo.toml` 파일:

```toml
# 표준 크레이트 데이터는 생략
[dev-dependencies]
pretty_assertions = "1"
```

`src/lib.rs` 파일:

```rust
pub fn add(a: i32, b: i32) -> i32 {
    a + b
}

#[cfg(test)]
mod tests {
    use super::*;
    use pretty_assertions::assert_eq; // 테스트 전용 크레이트. 일반 코드에서는 사용할 수 없습니다.

    #[test]
    fn test_add() {
        assert_eq!(add(2, 3), 5);
    }
}
```
