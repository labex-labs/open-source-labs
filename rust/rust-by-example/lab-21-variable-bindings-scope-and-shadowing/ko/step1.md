# 범위와 그림자화

변수 바인딩은 범위를 가지며, _블록_ 내에서만 존재합니다. 블록은 중괄호 `{}`로 묶인 문장들의 집합입니다.

```rust
fn main() {
    // 이 바인딩은 main 함수 내에서 존재합니다.
    let long_lived_binding = 1;

    // 이것은 블록이며, main 함수보다 범위가 더 작습니다.
    {
        // 이 바인딩은 이 블록 내에서만 존재합니다.
        let short_lived_binding = 2;

        println!("내부 짧은: {}", short_lived_binding);
    }
    // 블록 끝

    // 오류! `short_lived_binding` 은 이 범위에 존재하지 않습니다.
    println!("외부 짧은: {}", short_lived_binding);
    // FIXME ^ 이 줄을 주석 처리하세요.

    println!("외부 긴: {}", long_lived_binding);
}
```

또한, 변수 그림자화가 허용됩니다.

```rust
fn main() {
    let shadowed_binding = 1;

    {
        println!("그림자 지정되기 전: {}", shadowed_binding);

        // 이 바인딩은 외부 바인딩을 *그림자화*합니다.
        let shadowed_binding = "abc";

        println!("내부 블록에서 그림자화됨: {}", shadowed_binding);
    }
    println!("내부 블록 외부: {}", shadowed_binding);

    // 이 바인딩은 이전 바인딩을 *그림자화*합니다.
    let shadowed_binding = 2;
    println!("외부 블록에서 그림자화됨: {}", shadowed_binding);
}
```
