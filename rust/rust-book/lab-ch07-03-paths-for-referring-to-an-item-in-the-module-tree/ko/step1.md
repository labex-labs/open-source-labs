# 모듈 트리 내 항목 참조 경로

Rust 가 모듈 트리 내에서 항목을 찾을 위치를 표시하기 위해, 파일 시스템을 탐색할 때 경로를 사용하는 방식과 동일한 방식으로 경로를 사용합니다. 함수를 호출하려면 해당 경로를 알아야 합니다.

경로는 두 가지 형식을 가질 수 있습니다.

- *절대 경로*는 크레이트 루트에서 시작하는 전체 경로입니다. 외부 크레이트의 코드의 경우 절대 경로는 크레이트 이름으로 시작하고, 현재 크레이트의 코드의 경우 리터럴 `crate`로 시작합니다.
- *상대 경로*는 현재 모듈에서 시작하며 `self`, `super` 또는 현재 모듈의 식별자를 사용합니다.

절대 경로와 상대 경로는 모두 이중 콜론 (`::`) 으로 구분된 하나 이상의 식별자를 따릅니다.

Listing 7-1 로 돌아가서, `add_to_waitlist` 함수를 호출하려는 경우를 가정해 봅시다. 이는 다음과 같은 질문과 같습니다: `add_to_waitlist` 함수의 경로는 무엇입니까? Listing 7-3 에는 Listing 7-1 에서 일부 모듈과 함수가 제거된 내용이 포함되어 있습니다.

크레이트 루트에서 정의된 새로운 함수 `eat_at_restaurant`에서 `add_to_waitlist` 함수를 호출하는 두 가지 방법을 보여드리겠습니다. 이 경로는 올바르지만, 이 예제가 현재 상태로 컴파일되지 않도록 하는 또 다른 문제가 남아 있습니다. 잠시 후에 그 이유를 설명하겠습니다.

`eat_at_restaurant` 함수는 라이브러리 크레이트의 공개 API 의 일부이므로 `pub` 키워드로 표시합니다. "pub 키워드로 경로 노출"에서 `pub`에 대해 자세히 알아보겠습니다.

파일 이름: `src/lib.rs`

```rust
mod front_of_house {
    mod hosting {
        fn add_to_waitlist() {}
    }
}

pub fn eat_at_restaurant() {
    // Absolute path
    crate::front_of_house::hosting::add_to_waitlist();

    // Relative path
    front_of_house::hosting::add_to_waitlist();
}
```

Listing 7-3: 절대 및 상대 경로를 사용하여 `add_to_waitlist` 함수 호출

`eat_at_restaurant`에서 `add_to_waitlist` 함수를 처음 호출할 때 절대 경로를 사용합니다. `add_to_waitlist` 함수는 `eat_at_restaurant`과 동일한 크레이트에서 정의되므로 `crate` 키워드를 사용하여 절대 경로를 시작할 수 있습니다. 그런 다음 `add_to_waitlist`에 도달할 때까지 연속적인 각 모듈을 포함합니다. 동일한 구조의 파일 시스템을 상상할 수 있습니다: `add_to_waitlist` 프로그램을 실행하기 위해 `/front_of_house/hosting/add_to_waitlist` 경로를 지정합니다. `crate` 이름을 사용하여 크레이트 루트에서 시작하는 것은 셸에서 `/`를 사용하여 파일 시스템 루트에서 시작하는 것과 같습니다.

`eat_at_restaurant`에서 `add_to_waitlist`를 두 번째로 호출할 때 상대 경로를 사용합니다. 경로는 `eat_at_restaurant`과 동일한 모듈 트리에 정의된 모듈의 이름인 `front_of_house`로 시작합니다. 여기서 파일 시스템에 해당하는 것은 `front_of_house/hosting/add_to_waitlist` 경로를 사용하는 것입니다. 모듈 이름으로 시작하는 것은 경로가 상대적임을 의미합니다.

상대 경로 또는 절대 경로를 사용할지 여부를 선택하는 것은 프로젝트에 따라 결정되며, 항목 정의 코드를 항목을 사용하는 코드와 별도로 이동할지 또는 함께 이동할지에 따라 달라집니다. 예를 들어, `front_of_house` 모듈과 `eat_at_restaurant` 함수를 `customer_experience`라는 모듈로 이동하면 `add_to_waitlist`에 대한 절대 경로를 업데이트해야 하지만 상대 경로는 여전히 유효합니다. 그러나 `eat_at_restaurant` 함수를 별도로 `dining`이라는 모듈로 이동하면 `add_to_waitlist` 호출에 대한 절대 경로는 동일하게 유지되지만 상대 경로는 업데이트해야 합니다. 일반적으로 코드 정의와 항목 호출을 서로 독립적으로 이동하려는 경우가 많으므로 절대 경로를 지정하는 것을 선호합니다.

Listing 7-3 을 컴파일하고 아직 컴파일되지 않는 이유를 알아보겠습니다! 얻는 오류는 Listing 7-4 에 표시됩니다.

```bash
$ cargo build
   Compiling restaurant v0.1.0 (file:///projects/restaurant)
error[E0603]: module `hosting` is private
 --> src/lib.rs:9:28
  |
9 |     crate::front_of_house::hosting::add_to_waitlist();
  |                            ^^^^^^^ private module
  |
note: the module `hosting` is defined here
 --> src/lib.rs:2:5
  |
2 |     mod hosting {
  |     ^^^^^^^^^^^

error[E0603]: module `hosting` is private
  --> src/lib.rs:12:21
   |
12 |     front_of_house::hosting::add_to_waitlist();
   |                     ^^^^^^^ private module
   |
note: the module `hosting` is defined here
  --> src/lib.rs:2:5
   |
2  |     mod hosting {
   |     ^^^^^^^^^^^
```

Listing 7-4: Listing 7-3 의 코드를 빌드할 때의 컴파일러 오류

오류 메시지는 `hosting` 모듈이 private 이라고 말합니다. 즉, `hosting` 모듈과 `add_to_waitlist` 함수에 대한 올바른 경로가 있지만 Rust 는 private 섹션에 액세스할 수 없으므로 해당 경로를 사용할 수 없습니다. Rust 에서 모든 항목 (함수, 메서드, 구조체, 열거형, 모듈 및 상수) 은 기본적으로 상위 모듈에 대해 private 입니다. 함수 또는 구조체와 같은 항목을 private 으로 만들려면 모듈에 넣습니다.

상위 모듈의 항목은 하위 모듈 내부의 private 항목을 사용할 수 없지만 하위 모듈의 항목은 상위 모듈의 항목을 사용할 수 있습니다. 이는 하위 모듈이 구현 세부 정보를 래핑하고 숨기지만 하위 모듈은 정의된 컨텍스트를 볼 수 있기 때문입니다. 비유를 계속하자면, 개인 정보 보호 규칙을 레스토랑의 뒷방과 같다고 생각하십시오: 그곳에서 일어나는 일은 레스토랑 고객에게는 private 이지만, 사무실 관리자는 운영하는 레스토랑의 모든 것을 보고 할 수 있습니다.

Rust 는 내부 구현 세부 정보를 숨기는 것이 기본값이 되도록 모듈 시스템이 이러한 방식으로 작동하도록 선택했습니다. 그렇게 하면 외부 코드를 손상시키지 않고 내부 코드의 어떤 부분을 변경할 수 있는지 알 수 있습니다. 그러나 Rust 는 `pub` 키워드를 사용하여 항목을 public 으로 만들어 하위 모듈 코드의 내부 부분을 외부 상위 모듈에 노출하는 옵션을 제공합니다.
