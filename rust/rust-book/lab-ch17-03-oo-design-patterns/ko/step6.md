# content 의 동작을 변경하기 위해 승인 추가

`approve` 메서드는 `request_review` 메서드와 유사합니다. Listing 17-16 에 표시된 것처럼, 현재 상태가 승인되었을 때 현재 상태가 가져야 한다고 말하는 값으로 `state`를 설정합니다.

파일 이름: `src/lib.rs`

```rust
impl Post {
    --snip--
    pub fn approve(&mut self) {
        if let Some(s) = self.state.take() {
            self.state = Some(s.approve())
        }
    }
}

trait State {
    fn request_review(self: Box<Self>) -> Box<dyn State>;
    fn approve(self: Box<Self>) -> Box<dyn State>;
}

struct Draft {}

impl State for Draft {
    --snip--
    fn approve(self: Box<Self>) -> Box<dyn State> {
      1 self
    }
}

struct PendingReview {}

impl State for PendingReview {
    --snip--
    fn approve(self: Box<Self>) -> Box<dyn State> {
      2 Box::new(Published {})
    }
}

struct Published {}

impl State for Published {
    fn request_review(self: Box<Self>) -> Box<dyn State> {
        self
    }

    fn approve(self: Box<Self>) -> Box<dyn State> {
        self
    }
}
```

Listing 17-16: `Post` 및 `State` 트레이트에 `approve` 메서드 구현

`State` 트레이트에 `approve` 메서드를 추가하고 `State`를 구현하는 새 구조체인 `Published` 상태를 추가합니다.

`PendingReview`에서 `request_review`가 작동하는 방식과 유사하게, `Draft`에서 `approve` 메서드를 호출하면 `approve`가 `self`를 반환하므로 아무런 효과가 없습니다 \[1]. `PendingReview`에서 `approve`를 호출하면 `Published` 구조체의 새, boxed 인스턴스를 반환합니다 \[2]. `Published` 구조체는 `State` 트레이트를 구현하며, `request_review` 메서드와 `approve` 메서드 모두에 대해 자체를 반환합니다. 게시물이 해당 경우에 `Published` 상태로 유지되어야 하기 때문입니다.

이제 `Post`에서 `content` 메서드를 업데이트해야 합니다. `content`에서 반환되는 값이 `Post`의 현재 상태에 따라 달라지도록 하므로, Listing 17-17 에 표시된 것처럼 `Post`가 `state`에서 정의된 `content` 메서드에 위임하도록 할 것입니다.

파일 이름: `src/lib.rs`

```rust
impl Post {
    --snip--
    pub fn content(&self) -> &str {
        self.state.as_ref().unwrap().content(self)
    }
    --snip--
}
```

Listing 17-17: `Post`에서 `content` 메서드를 업데이트하여 `State`의 `content` 메서드로 위임

목표는 이러한 모든 규칙을 `State`를 구현하는 구조체 내에 유지하는 것이므로, `state`의 값에서 `content` 메서드를 호출하고 게시물 인스턴스 (즉, `self`) 를 인수로 전달합니다. 그런 다음 `state` 값에서 `content` 메서드를 사용하여 반환된 값을 반환합니다.

`Option` 내의 값에 대한 참조를 원하고 값의 소유권을 원하지 않으므로 `Option`에서 `as_ref` 메서드를 호출합니다. `state`가 `Option<Box<dyn State>>`이므로 `as_ref`를 호출하면 `Option<&Box<dyn State>>`가 반환됩니다. `as_ref`를 호출하지 않으면 함수 매개변수의 빌린 `&self`에서 `state`를 이동할 수 없으므로 오류가 발생합니다.

그런 다음 `unwrap` 메서드를 호출합니다. `Post`의 메서드가 해당 메서드가 완료될 때 `state`가 항상 `Some` 값을 포함하도록 보장하므로 이 메서드가 절대 패닉하지 않는다는 것을 알고 있습니다. 이것은 컴파일러가 이해할 수 없더라도 `None` 값이 불가능하다는 것을 알고 있는 "컴파일러보다 더 많은 정보를 가지고 있는 경우"에서 이야기했던 경우 중 하나입니다.

이 시점에서 `&Box<dyn State>`에서 `content`를 호출하면 역참조 강제 변환이 `&` 및 `Box`에 적용되므로 `content` 메서드는 궁극적으로 `State` 트레이트를 구현하는 타입에서 호출됩니다. 즉, `State` 트레이트 정의에 `content`를 추가해야 하며, Listing 17-18 에 표시된 것처럼 어떤 콘텐츠를 반환할지 로직을 넣을 것입니다.

파일 이름: `src/lib.rs`

```rust
trait State {
    --snip--
    fn content<'a>(&self, post: &'a Post) -> &'a str {
      1 ""
    }
}

--snip--
struct Published {}

impl State for Published {
    --snip--
    fn content<'a>(&self, post: &'a Post) -> &'a str {
      2 &post.content
    }
}
```

Listing 17-18: `State` 트레이트에 `content` 메서드 추가

빈 문자열 슬라이스를 반환하는 `content` 메서드에 대한 기본 구현을 추가합니다 \[1]. 즉, `Draft` 및 `PendingReview` 구조체에서 `content`를 구현할 필요가 없습니다. `Published` 구조체는 `content` 메서드를 재정의하고 `post.content`의 값을 반환합니다 \[2].

10 장에서 논의했듯이 이 메서드에는 수명 주기 주석이 필요합니다. `post`에 대한 참조를 인수로 사용하고 해당 `post`의 일부에 대한 참조를 반환하므로 반환된 참조의 수명은 `post` 인수의 수명과 관련이 있습니다.

이제 완료되었습니다. Listing 17-11 의 모든 것이 이제 작동합니다! 블로그 게시물 워크플로우의 규칙으로 상태 패턴을 구현했습니다. 규칙과 관련된 로직은 `Post` 전체에 분산되지 않고 상태 객체에 있습니다.

> **Enum 을 사용하지 않는 이유는 무엇입니까?**
>
> 다양한 가능한 게시물 상태를 변형으로 사용하는 `enum`을 사용하지 않은 이유가 궁금했을 것입니다. 물론 가능한 해결책입니다. 시도해 보고 최종 결과를 비교하여 어떤 것을 선호하는지 확인하십시오! `enum`을 사용하는 한 가지 단점은 `enum`의 값을 확인하는 모든 위치에서 가능한 모든 변형을 처리하기 위해 `match` 표현식 또는 유사한 표현식이 필요하다는 것입니다. 이것은 이 트레이트 객체 솔루션보다 더 반복적일 수 있습니다.
