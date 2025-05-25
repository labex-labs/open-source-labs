# `pub use`를 사용하여 이름 재수출하기

`use` 키워드를 사용하여 이름을 범위 내로 가져올 때, 새 범위에서 사용 가능한 이름은 private 입니다. 우리 코드를 호출하는 코드가 해당 코드의 범위에서 정의된 것처럼 해당 이름을 참조할 수 있도록 하려면 `pub`와 `use`를 결합할 수 있습니다. 이 기술을 *재수출 (re-exporting)*이라고 합니다. 이는 항목을 범위 내로 가져오는 동시에 다른 사람들이 자신의 범위로 가져올 수 있도록 해당 항목을 사용할 수 있게 하기 때문입니다.

Listing 7-17 은 루트 모듈에서 `use`를 `pub use`로 변경한 Listing 7-11 의 코드를 보여줍니다.

파일 이름: `src/lib.rs`

```rust
mod front_of_house {
    pub mod hosting {
        pub fn add_to_waitlist() {}
    }
}

pub use crate::front_of_house::hosting;

pub fn eat_at_restaurant() {
    hosting::add_to_waitlist();
}
```

Listing 7-17: `pub use`를 사용하여 모든 코드가 새 범위에서 사용할 수 있도록 이름 만들기

이 변경 전에는 외부 코드가 `add_to_waitlist` 함수를 호출하려면 경로 `restaurant::front_of_house::hosting::add_to_waitlist()`를 사용해야 했습니다. 이제 이 `pub use`가 루트 모듈에서 `hosting` 모듈을 재수출했으므로 외부 코드는 대신 경로 `restaurant::hosting::add_to_waitlist()`를 사용할 수 있습니다.

재수출은 코드의 내부 구조가 코드를 호출하는 프로그래머가 도메인에 대해 생각하는 방식과 다를 때 유용합니다. 예를 들어, 이 레스토랑 비유에서 레스토랑을 운영하는 사람들은 "front of house"와 "back of house"에 대해 생각합니다. 그러나 레스토랑을 방문하는 고객은 아마도 레스토랑의 부분을 그러한 용어로 생각하지 않을 것입니다. `pub use`를 사용하면 하나의 구조로 코드를 작성하지만 다른 구조를 노출할 수 있습니다. 이렇게 하면 라이브러리에서 작업하는 프로그래머와 라이브러리를 호출하는 프로그래머 모두에게 라이브러리가 잘 구성됩니다. "pub use 를 사용하여 편리한 공개 API 내보내기"에서 `pub use`의 또 다른 예와 이것이 크레이트의 문서에 미치는 영향을 살펴보겠습니다.
