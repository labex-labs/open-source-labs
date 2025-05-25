# Playground

[Rust Playground](https://play.rust-lang.org/)는 웹 인터페이스를 통해 Rust 코드를 실험하는 방법입니다.

## `mdbook`과 함께 사용하기

`mdbook`에서는 코드 예제를 실행 가능하고 편집 가능하게 만들 수 있습니다.

```rust
fn main() {
    println!("Hello World!");
}
```

이렇게 하면 독자는 코드 샘플을 실행할 뿐만 아니라 수정하고 조정할 수 있습니다. 여기서 핵심은 코드 블록에 "editable"이라는 단어를 쉼표로 구분하여 추가하는 것입니다.

````markdown
```rust
//...여기에 코드를 입력하세요
```
````

````

또한 `mdbook`이 빌드 및 테스트 시 코드를 건너뛰도록 하려면 `ignore`를 추가할 수 있습니다.

```markdown
```rust
//...여기에 코드를 입력하세요
````

```

## 문서와 함께 사용하기

일부 공식 Rust 문서에서 "실행" 버튼을 클릭하면 새 탭에서 Rust Playground 에서 코드 샘플을 열 수 있다는 것을 알 수 있습니다. 이 기능은 `html_playground_url`이라는 `#[doc]` 속성을 사용하면 활성화됩니다.
```
