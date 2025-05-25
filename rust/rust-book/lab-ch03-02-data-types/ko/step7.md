# 문자 타입 (The Character Type)

Rust 의 `char` 타입은 언어의 가장 기본적인 알파벳 타입입니다. 다음은 `char` 값을 선언하는 몇 가지 예입니다.

파일 이름: `src/main.rs`

```rust
fn main() {
    let c = 'z';
    let z: char = 'ℤ'; // 명시적 타입 어노테이션 (explicit type annotation)
    let heart_eyed_cat = '😻';
}
```

문자열 리터럴이 큰따옴표를 사용하는 것과 달리, `char` 리터럴은 작은따옴표로 지정합니다. Rust 의 `char` 타입은 크기가 4 바이트이며 유니코드 스칼라 값 (Unicode Scalar Value) 을 나타내며, 이는 ASCII 보다 훨씬 더 많은 것을 나타낼 수 있음을 의미합니다. 악센트가 있는 문자, 중국어, 일본어 및 한국어 문자, 이모지, 그리고 너비가 0 인 공백 모두 Rust 에서 유효한 `char` 값입니다. 유니코드 스칼라 값은 `U+0000`에서 `U+D7FF`까지, 그리고 `U+E000`에서 `U+10FFFF`까지 (포함) 의 범위를 가집니다. 그러나 "문자"는 실제로 유니코드의 개념이 아니므로, "문자"에 대한 인간적인 직관은 Rust 의 `char`와 일치하지 않을 수 있습니다. 이 주제는 "문자열로 UTF-8 인코딩된 텍스트 저장 (Storing UTF-8 Encoded Text with Strings)"에서 자세히 논의할 것입니다.
