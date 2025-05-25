# Post 정의 및 초안 상태에서 새 인스턴스 생성

라이브러리 구현을 시작해 봅시다! 우리는 일부 콘텐츠를 보유하는 공개 `Post` 구조체가 필요하다는 것을 알고 있으므로, Listing 17-12 에 표시된 대로 구조체 정의와 `Post`의 인스턴스를 생성하는 관련 공개 `new` 함수로 시작합니다. 또한 모든 `Post`에 대한 모든 상태 객체가 가져야 하는 동작을 정의하는 비공개 `State` 트레이트도 만들 것입니다.

그런 다음 `Post`는 상태 객체를 보유하기 위해 `state`라는 비공개 필드에서 `Option<T>` 내부에 `Box<dyn State>`의 트레이트 객체를 보유합니다. 잠시 후에 `Option<T>`가 필요한 이유를 알게 될 것입니다.

파일 이름: `src/lib.rs`

```rust
pub struct Post {
    state: Option<Box<dyn State>>,
    content: String,
}

impl Post {
    pub fn new() -> Post {
        Post {
          1 state: Some(Box::new(Draft {})),
          2 content: String::new(),
        }
    }
}

trait State {}

struct Draft {}

impl State for Draft {}
```

Listing 17-12: `Post` 구조체 정의 및 새 `Post` 인스턴스를 생성하는 `new` 함수, `State` 트레이트 및 `Draft` 구조체

`State` 트레이트는 서로 다른 게시물 상태에서 공유되는 동작을 정의합니다. 상태 객체는 `Draft`, `PendingReview` 및 `Published`이며, 모두 `State` 트레이트를 구현합니다. 현재 트레이트에는 메서드가 없으며, 게시물이 시작되기를 원하는 상태인 `Draft` 상태를 먼저 정의하는 것으로 시작합니다.

새 `Post`를 만들 때 `state` 필드를 `Box`를 보유하는 `Some` 값으로 설정합니다 \[1]. 이 `Box`는 `Draft` 구조체의 새 인스턴스를 가리킵니다. 이렇게 하면 새 `Post` 인스턴스를 만들 때마다 초안으로 시작됩니다. `Post`의 `state` 필드는 비공개이므로 다른 상태에서 `Post`를 만들 방법이 없습니다! `Post::new` 함수에서 `content` 필드를 새롭고 빈 `String`으로 설정합니다 \[2].
