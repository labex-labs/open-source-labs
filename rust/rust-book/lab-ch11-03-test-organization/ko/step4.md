# 비공개 함수 테스트 (Testing Private Functions)

테스팅 커뮤니티 내에서는 비공개 함수를 직접 테스트해야 하는지에 대한 논쟁이 있으며, 다른 언어에서는 비공개 함수를 테스트하기 어렵거나 불가능하게 만듭니다. 어떤 테스팅 이념을 따르든, Rust 의 개인 정보 보호 규칙을 통해 비공개 함수를 테스트할 수 있습니다. 비공개 함수 `internal_adder`가 있는 Listing 11-12 의 코드를 고려하십시오.

파일 이름: `src/lib.rs`

```rust
pub fn add_two(a: i32) -> i32 {
    internal_adder(a, 2)
}

fn internal_adder(a: i32, b: i32) -> i32 {
    a + b
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn internal() {
        assert_eq!(4, internal_adder(2, 2));
    }
}
```

Listing 11-12: 비공개 함수 테스트

`internal_adder` 함수는 `pub`로 표시되지 않았습니다. 테스트는 단지 Rust 코드일 뿐이며, `tests` 모듈은 또 다른 모듈일 뿐입니다. "모듈 트리에서 항목을 참조하는 경로"에서 논의했듯이, 자식 모듈의 항목은 상위 모듈의 항목을 사용할 수 있습니다. 이 테스트에서는 `use super::*`를 사용하여 `test` 모듈의 모든 부모 항목을 범위 내로 가져온 다음, 테스트에서 `internal_adder`를 호출할 수 있습니다. 비공개 함수를 테스트해서는 안 된다고 생각한다면, Rust 에는 그렇게 하도록 강요하는 것은 없습니다.
