# 검토 요청은 게시물의 상태를 변경합니다

다음으로, 게시물 검토를 요청하는 기능을 추가해야 합니다. 이 기능은 게시물의 상태를 `Draft`에서 `PendingReview`로 변경해야 합니다. Listing 17-15 는 이 코드를 보여줍니다.

파일 이름: `src/lib.rs`

```rust
impl Post {
    --snip--
  1 pub fn request_review(&mut self) {
      2 if let Some(s) = self.state.take() {
          3 self.state = Some(s.request_review())
        }
    }
}

trait State {
  4 fn request_review(self: Box<Self>) -> Box<dyn State>;
}

struct Draft {}

impl State for Draft {
    fn request_review(self: Box<Self>) -> Box<dyn State> {
      5 Box::new(PendingReview {})
    }
}

struct PendingReview {}

impl State for PendingReview {
    fn request_review(self: Box<Self>) -> Box<dyn State> {
      6 self
    }
}
```

Listing 17-15: `Post` 및 `State` 트레이트에 `request_review` 메서드 구현

`Post`에 `self`에 대한 가변 참조를 사용하는 `request_review`라는 public 메서드를 제공합니다 \[1]. 그런 다음 `Post`의 현재 상태에서 내부 `request_review` 메서드를 호출합니다 \[3]. 이 두 번째 `request_review` 메서드는 현재 상태를 소비하고 새 상태를 반환합니다.

`State` 트레이트에 `request_review` 메서드를 추가합니다 \[4]. 트레이트를 구현하는 모든 타입은 이제 `request_review` 메서드를 구현해야 합니다. 메서드의 첫 번째 매개변수로 `self`, `&self`, 또는 `&mut self` 대신 `self: Box<Self>`를 사용합니다. 이 구문은 해당 타입이 포함된 `Box`에서 호출될 때만 메서드가 유효함을 의미합니다. 이 구문은 `Box<Self>`의 소유권을 가져와 이전 상태를 무효화하므로 `Post`의 상태 값을 새 상태로 변환할 수 있습니다.

이전 상태를 소비하기 위해 `request_review` 메서드는 상태 값의 소유권을 가져야 합니다. 이것이 `Post`의 `state` 필드에 있는 `Option`이 사용되는 곳입니다. `take` 메서드를 호출하여 `state` 필드에서 `Some` 값을 가져오고 그 자리에 `None`을 남겨둡니다. Rust 는 구조체에 채워지지 않은 필드를 허용하지 않기 때문입니다 \[2]. 이렇게 하면 `state` 값을 빌리는 대신 `Post`에서 이동할 수 있습니다. 그런 다음 게시물의 `state` 값을 이 작업의 결과로 설정합니다.

`state` 값을 소유하려면 `self.state = self.state.request_review();`와 같은 코드로 직접 설정하는 대신 임시로 `state`를 `None`으로 설정해야 합니다. 이렇게 하면 `Post`가 이전 `state` 값을 새 상태로 변환한 후 사용할 수 없게 됩니다.

`Draft`의 `request_review` 메서드는 새 `PendingReview` 구조체의 새, boxed 인스턴스를 반환합니다 \[5]. 이 구조체는 게시물이 검토를 기다리는 상태를 나타냅니다. `PendingReview` 구조체도 `request_review` 메서드를 구현하지만 변환을 수행하지 않습니다. 대신 자체를 반환합니다 \[6]. `PendingReview` 상태인 게시물에 대해 검토를 요청하면 `PendingReview` 상태로 유지되어야 하기 때문입니다.

이제 상태 패턴의 장점을 보기 시작할 수 있습니다. `Post`의 `request_review` 메서드는 `state` 값에 관계없이 동일합니다. 각 상태는 자체 규칙을 담당합니다.

`Post`의 `content` 메서드는 빈 문자열 슬라이스를 반환하는 그대로 둡니다. 이제 `PendingReview` 상태와 `Draft` 상태의 `Post`를 가질 수 있지만, `PendingReview` 상태에서도 동일한 동작을 원합니다. Listing 17-11 은 이제 \[5] 줄까지 작동합니다!
