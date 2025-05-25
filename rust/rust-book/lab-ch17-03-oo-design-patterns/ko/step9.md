# 전환을 다른 타입으로 변환하여 구현

그렇다면 게시된 게시물을 어떻게 얻을 수 있을까요? 초안 게시물은 게시되기 전에 검토 및 승인되어야 한다는 규칙을 적용하려고 합니다. 검토 대기 중인 게시물은 여전히 콘텐츠를 표시해서는 안 됩니다. Listing 17-20 에 표시된 대로 `DraftPost`에서 `PendingReviewPost`를 반환하는 `request_review` 메서드를 정의하고 `PendingReviewPost`에서 `Post`를 반환하는 `approve` 메서드를 정의하여 이러한 제약 조건을 구현해 보겠습니다.

파일 이름: `src/lib.rs`

```rust
impl DraftPost {
    --snip--
    pub fn request_review(self) -> PendingReviewPost {
        PendingReviewPost {
            content: self.content,
        }
    }
}

pub struct PendingReviewPost {
    content: String,
}

impl PendingReviewPost {
    pub fn approve(self) -> Post {
        Post {
            content: self.content,
        }
    }
}
```

Listing 17-20: `DraftPost`에서 `request_review`를 호출하여 생성된 `PendingReviewPost`와 `PendingReviewPost`를 게시된 `Post`로 변환하는 `approve` 메서드

`request_review` 및 `approve` 메서드는 `self`의 소유권을 가져와 `DraftPost` 및 `PendingReviewPost` 인스턴스를 소비하고 각각 `PendingReviewPost` 및 게시된 `Post`로 변환합니다. 이렇게 하면 `request_review`를 호출한 후에도 `DraftPost` 인스턴스가 남아 있지 않게 됩니다. `PendingReviewPost` 구조체에는 정의된 `content` 메서드가 없으므로 해당 콘텐츠를 읽으려고 하면 `DraftPost`와 마찬가지로 컴파일러 오류가 발생합니다. `content` 메서드가 정의된 게시된 `Post` 인스턴스를 얻는 유일한 방법은 `PendingReviewPost`에서 `approve` 메서드를 호출하는 것이고, `PendingReviewPost`를 얻는 유일한 방법은 `DraftPost`에서 `request_review` 메서드를 호출하는 것이므로, 이제 블로그 게시물 워크플로우를 타입 시스템에 인코딩했습니다.

하지만 `main`에도 몇 가지 작은 변경 사항을 적용해야 합니다. `request_review` 및 `approve` 메서드는 호출되는 구조체를 수정하는 대신 새 인스턴스를 반환하므로 반환된 인스턴스를 저장하기 위해 더 많은 `let post =` 섀도잉 할당을 추가해야 합니다. 또한 초안 및 검토 대기 중인 게시물의 내용에 대한 어설션이 빈 문자열일 수 없으며 필요하지도 않습니다. 더 이상 해당 상태의 게시물 내용을 사용하려는 코드를 컴파일할 수 없습니다. `main`의 업데이트된 코드는 Listing 17-21 에 나와 있습니다.

파일 이름: `src/main.rs`

```rust
use blog::Post;

fn main() {
    let mut post = Post::new();

    post.add_text("I ate a salad for lunch today");

    let post = post.request_review();

    let post = post.approve();

    assert_eq!("I ate a salad for lunch today", post.content());
}
```

Listing 17-21: 블로그 게시물 워크플로우의 새로운 구현을 사용하도록 `main`을 수정

`post`를 다시 할당하기 위해 `main`에 적용해야 하는 변경 사항은 이 구현이 더 이상 객체 지향 상태 패턴을 완전히 따르지 않는다는 것을 의미합니다. 상태 간의 변환은 더 이상 `Post` 구현 내에 완전히 캡슐화되지 않습니다. 그러나 우리가 얻는 것은 타입 시스템과 컴파일 시간에 발생하는 타입 검사로 인해 잘못된 상태가 이제 불가능하다는 것입니다! 이렇게 하면 게시되지 않은 게시물의 내용 표시와 같은 특정 버그가 프로덕션에 들어가기 전에 발견됩니다.

Listing 17-21 이후의 `blog` 크레이트에서 이 섹션의 시작 부분에서 제안된 작업을 시도하여 이 버전의 코드 디자인에 대해 어떻게 생각하는지 확인하십시오. 일부 작업은 이 디자인에서 이미 완료되었을 수 있습니다.

Rust 가 객체 지향 디자인 패턴을 구현할 수 있지만, 상태를 타입 시스템에 인코딩하는 것과 같은 다른 패턴도 Rust 에서 사용할 수 있음을 확인했습니다. 이러한 패턴은 서로 다른 장단점을 가지고 있습니다. 객체 지향 패턴에 매우 익숙할 수 있지만, Rust 의 기능을 활용하기 위해 문제를 다시 생각하면 컴파일 시간에 일부 버그를 방지하는 것과 같은 이점을 얻을 수 있습니다. 객체 지향 언어에는 없는 소유권과 같은 특정 기능으로 인해 객체 지향 패턴이 Rust 에서 항상 최선의 해결책이 아닐 것입니다.
