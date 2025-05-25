# `use` 키워드를 사용하여 경로를 범위 내로 가져오기

함수를 호출하기 위해 경로를 일일이 작성하는 것은 불편하고 반복적으로 느껴질 수 있습니다. Listing 7-7 에서 `add_to_waitlist` 함수에 대한 절대 경로 또는 상대 경로를 선택했든, `add_to_waitlist`를 호출할 때마다 `front_of_house`와 `hosting`도 지정해야 했습니다. 다행히 이 과정을 단순화하는 방법이 있습니다. `use` 키워드를 사용하여 경로에 대한 단축키를 한 번 만들고, 해당 범위의 다른 모든 곳에서 더 짧은 이름을 사용할 수 있습니다.

Listing 7-11 에서 `crate::front_of_house::hosting` 모듈을 `eat_at_restaurant` 함수의 범위 내로 가져와서 `eat_at_restaurant`에서 `add_to_waitlist` 함수를 호출하기 위해 `hosting::add_to_waitlist`만 지정하면 됩니다.

파일 이름: `src/lib.rs`

```rust
mod front_of_house {
    pub mod hosting {
        pub fn add_to_waitlist() {}
    }
}

use crate::front_of_house::hosting;

pub fn eat_at_restaurant() {
    hosting::add_to_waitlist();
}
```

Listing 7-11: `use`를 사용하여 모듈을 범위 내로 가져오기

범위에 `use`와 경로를 추가하는 것은 파일 시스템에서 심볼릭 링크를 만드는 것과 유사합니다. 크레이트 루트에 `use crate::front_of_house::hosting`을 추가하면 `hosting`은 해당 범위에서 유효한 이름이 됩니다. 마치 `hosting` 모듈이 크레이트 루트에 정의된 것처럼 말입니다. `use`를 사용하여 범위 내로 가져온 경로는 다른 경로와 마찬가지로 개인 정보 보호도 확인합니다.

`use`는 `use`가 발생하는 특정 범위에 대해서만 단축키를 생성합니다. Listing 7-12 는 `eat_at_restaurant` 함수를 `customer`라는 새로운 자식 모듈로 이동합니다. 이는 `use` 문과는 다른 범위이므로 함수 본문은 컴파일되지 않습니다.

파일 이름: `src/lib.rs`

```rust
mod front_of_house {
    pub mod hosting {
        pub fn add_to_waitlist() {}
    }
}

use crate::front_of_house::hosting;

mod customer {
    pub fn eat_at_restaurant() {
        hosting::add_to_waitlist();
    }
}
```

Listing 7-12: `use` 문은 해당 범위에서만 적용됩니다.

컴파일러 오류는 단축키가 더 이상 `customer` 모듈 내에서 적용되지 않음을 보여줍니다.

```bash
error[E0433]: failed to resolve: use of undeclared crate or module `hosting`
  --> src/lib.rs:11:9
   |
11 |         hosting::add_to_waitlist();
   |         ^^^^^^^ use of undeclared crate or module `hosting`

warning: unused import: `crate::front_of_house::hosting`
 --> src/lib.rs:7:5
  |
7 | use crate::front_of_house::hosting;
  |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  |
  = note: `#[warn(unused_imports)]` on by default
```

`use`가 더 이상 해당 범위에서 사용되지 않는다는 경고도 있습니다! 이 문제를 해결하려면 `use`를 `customer` 모듈 내로 이동하거나, 자식 `customer` 모듈 내에서 `super::hosting`을 사용하여 상위 모듈의 단축키를 참조하십시오.
