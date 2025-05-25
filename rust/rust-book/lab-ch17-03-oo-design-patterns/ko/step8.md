# 상태 및 동작을 타입으로 인코딩

상태 패턴을 재고하여 다른 일련의 장단점을 얻는 방법을 보여드리겠습니다. 외부 코드가 상태와 전환에 대해 전혀 알 수 없도록 상태와 전환을 완전히 캡슐화하는 대신, 상태를 다른 타입으로 인코딩합니다. 결과적으로 Rust 의 타입 검사 시스템은 컴파일러 오류를 발생시켜 게시된 게시물만 허용되는 곳에서 초안 게시물을 사용하려는 시도를 방지합니다.

Listing 17-11 의 `main`의 첫 번째 부분을 살펴보겠습니다.

파일 이름: `src/main.rs`

```rust
fn main() {
    let mut post = Post::new();

    post.add_text("I ate a salad for lunch today");
    assert_eq!("", post.content());
}
```

`Post::new`를 사용하여 초안 상태에서 새 게시물을 생성하고 게시물의 내용에 텍스트를 추가하는 기능을 계속 사용할 수 있습니다. 그러나 빈 문자열을 반환하는 초안 게시물에 `content` 메서드를 갖는 대신, 초안 게시물에 `content` 메서드가 전혀 없도록 만들 것입니다. 그렇게 하면 초안 게시물의 내용을 얻으려고 하면 메서드가 존재하지 않는다는 컴파일러 오류가 발생합니다. 결과적으로 해당 코드가 컴파일되지 않으므로 프로덕션에서 초안 게시물 내용을 실수로 표시하는 것은 불가능합니다. Listing 17-19 는 `Post` 구조체와 `DraftPost` 구조체의 정의와 각 구조체의 메서드를 보여줍니다.

파일 이름: `src/lib.rs`

```rust
pub struct Post {
    content: String,
}

pub struct DraftPost {
    content: String,
}

impl Post {
  1 pub fn new() -> DraftPost {
        DraftPost {
            content: String::new(),
        }
    }

  2 pub fn content(&self) -> &str {
        &self.content
    }
}

impl DraftPost {
  3 pub fn add_text(&mut self, text: &str) {
        self.content.push_str(text);
    }
}
```

Listing 17-19: `content` 메서드가 있는 `Post`와 `content` 메서드가 없는 `DraftPost`

`Post` 및 `DraftPost` 구조체 모두 블로그 게시물 텍스트를 저장하는 private `content` 필드를 가지고 있습니다. 구조체는 상태를 구조체의 타입으로 인코딩하므로 더 이상 `state` 필드를 갖지 않습니다. `Post` 구조체는 게시된 게시물을 나타내며 `content`를 반환하는 `content` 메서드를 갖습니다 \[2].

여전히 `Post::new` 함수가 있지만, `Post`의 인스턴스를 반환하는 대신 `DraftPost`의 인스턴스를 반환합니다 \[1]. `content`가 private 이고 `Post`를 반환하는 함수가 없으므로 지금은 `Post`의 인스턴스를 생성할 수 없습니다.

`DraftPost` 구조체에는 `add_text` 메서드가 있으므로 이전과 같이 `content`에 텍스트를 추가할 수 있지만 \[3], `DraftPost`에는 `content` 메서드가 정의되어 있지 않습니다! 따라서 이제 프로그램은 모든 게시물이 초안 게시물로 시작되도록 보장하며, 초안 게시물은 표시할 수 있는 콘텐츠를 갖지 않습니다. 이러한 제약 조건을 우회하려는 모든 시도는 컴파일러 오류를 발생시킵니다.
