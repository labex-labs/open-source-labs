# 게시물 콘텐츠 텍스트 저장

Listing 17-11 에서 `add_text`라는 메서드를 호출하고 `&str`을 전달하여 블로그 게시물의 텍스트 콘텐츠로 추가할 수 있기를 원한다는 것을 확인했습니다. 나중에 `content` 필드의 데이터를 읽는 방법을 제어하는 메서드를 구현할 수 있도록 `content` 필드를 `pub`로 노출하는 대신 이 메서드를 구현합니다. `add_text` 메서드는 매우 간단하므로 Listing 17-13 의 구현을 `impl Post` 블록에 추가해 보겠습니다.

파일 이름: `src/lib.rs`

```rust
impl Post {
    --snip--
    pub fn add_text(&mut self, text: &str) {
        self.content.push_str(text);
    }
}
```

Listing 17-13: 게시물의 `content`에 텍스트를 추가하는 `add_text` 메서드 구현

`add_text` 메서드는 `add_text`를 호출하는 `Post` 인스턴스를 변경하므로 `self`에 대한 가변 참조를 사용합니다. 그런 다음 `content`의 `String`에서 `push_str`을 호출하고 저장된 `content`에 추가할 `text` 인수를 전달합니다. 이 동작은 게시물의 상태에 의존하지 않으므로 상태 패턴의 일부가 아닙니다. `add_text` 메서드는 `state` 필드와 전혀 상호 작용하지 않지만 지원하려는 동작의 일부입니다.
