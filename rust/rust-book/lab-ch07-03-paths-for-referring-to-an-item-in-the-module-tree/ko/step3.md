# `super`로 상대 경로 시작하기

경로의 시작 부분에 `super`를 사용하여 현재 모듈 또는 크레이트 루트가 아닌 상위 모듈에서 시작하는 상대 경로를 구성할 수 있습니다. 이는 파일 시스템 경로를 `..` 구문으로 시작하는 것과 같습니다. `super`를 사용하면 상위 모듈에 있는 항목을 참조할 수 있으므로, 모듈이 상위 모듈과 밀접하게 관련되어 있지만 상위 모듈이 언젠가 모듈 트리의 다른 곳으로 이동할 수 있는 경우 모듈 트리를 더 쉽게 재정렬할 수 있습니다.

Listing 7-8 의 코드를 살펴보겠습니다. 이 코드는 요리사가 잘못된 주문을 수정하고 직접 고객에게 가져다주는 상황을 모델링합니다. `back_of_house` 모듈에 정의된 `fix_incorrect_order` 함수는 `super`로 시작하는 `deliver_order`에 대한 경로를 지정하여 상위 모듈에 정의된 `deliver_order` 함수를 호출합니다.

파일 이름: `src/lib.rs`

```rust
fn deliver_order() {}

mod back_of_house {
    fn fix_incorrect_order() {
        cook_order();
        super::deliver_order();
    }

    fn cook_order() {}
}
```

Listing 7-8: `super`로 시작하는 상대 경로를 사용하여 함수 호출

`fix_incorrect_order` 함수는 `back_of_house` 모듈에 있으므로 `super`를 사용하여 `back_of_house`의 상위 모듈로 이동할 수 있습니다. 이 경우 루트인 `crate`입니다. 거기에서 `deliver_order`를 찾고 찾습니다. 성공! `back_of_house` 모듈과 `deliver_order` 함수는 서로 동일한 관계를 유지하고 크레이트의 모듈 트리를 재구성하기로 결정하면 함께 이동할 가능성이 높다고 생각합니다. 따라서 이 코드가 다른 모듈로 이동하는 경우 향후 코드 업데이트할 위치를 줄이기 위해 `super`를 사용했습니다.
