# 관용적인 `use` 경로 생성

Listing 7-11 에서 `use crate::front_of_house::hosting`을 지정한 다음 `eat_at_restaurant`에서 `hosting::add_to_waitlist`를 호출한 이유가 궁금했을 수 있습니다. Listing 7-13 과 같이 `add_to_waitlist` 함수까지 모든 경로를 지정하여 동일한 결과를 얻는 대신 말입니다.

파일 이름: `src/lib.rs`

```rust
mod front_of_house {
    pub mod hosting {
        pub fn add_to_waitlist() {}
    }
}

use crate::front_of_house::hosting::add_to_waitlist;

pub fn eat_at_restaurant() {
    add_to_waitlist();
}
```

Listing 7-13: 관용적이지 않은 방식으로 `use`를 사용하여 `add_to_waitlist` 함수를 범위 내로 가져오기

Listing 7-11 과 Listing 7-13 모두 동일한 작업을 수행하지만, Listing 7-11 은 `use`를 사용하여 함수를 범위 내로 가져오는 관용적인 방법입니다. 함수의 상위 모듈을 `use`로 범위 내로 가져오면 함수를 호출할 때 상위 모듈을 지정해야 합니다. 함수를 호출할 때 상위 모듈을 지정하면 함수가 로컬에서 정의되지 않았음을 명확하게 하면서 전체 경로의 반복을 최소화합니다. Listing 7-13 의 코드는 `add_to_waitlist`가 어디에 정의되어 있는지 불분명합니다.

반면에, 구조체, 열거형 및 기타 항목을 `use`로 가져올 때는 전체 경로를 지정하는 것이 관용적입니다. Listing 7-14 는 표준 라이브러리의 `HashMap` 구조체를 바이너리 크레이트의 범위 내로 가져오는 관용적인 방법을 보여줍니다.

파일 이름: `src/main.rs`

```rust
use std::collections::HashMap;

fn main() {
    let mut map = HashMap::new();
    map.insert(1, 2);
}
```

Listing 7-14: 관용적인 방식으로 `HashMap`을 범위 내로 가져오기

이 관용구 뒤에는 강력한 이유가 없습니다. 이는 단지 나타난 관례이며, 사람들은 이러한 방식으로 Rust 코드를 읽고 쓰는 데 익숙해졌습니다.

이 관용구의 예외는 `use` 문을 사용하여 동일한 이름을 가진 두 개의 항목을 범위 내로 가져오는 경우입니다. Rust 는 이를 허용하지 않기 때문입니다. Listing 7-15 는 동일한 이름을 갖지만 다른 상위 모듈을 가진 두 개의 `Result` 타입을 범위 내로 가져오고, 이를 참조하는 방법을 보여줍니다.

파일 이름: `src/lib.rs`

```rust
use std::fmt;
use std::io;

fn function1() -> fmt::Result {
    --snip--
}

fn function2() -> io::Result<()> {
    --snip--
}
```

Listing 7-15: 동일한 이름을 가진 두 개의 타입을 동일한 범위로 가져오려면 상위 모듈을 사용해야 합니다.

보시다시피, 상위 모듈을 사용하면 두 개의 `Result` 타입을 구별할 수 있습니다. 대신 `use std::fmt::Result` 및 `use std::io::Result`를 지정하면 동일한 범위에 두 개의 `Result` 타입이 있게 되며, Rust 는 `Result`를 사용할 때 어느 것을 의미하는지 알 수 없습니다.
