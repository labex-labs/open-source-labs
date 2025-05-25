# `pub` 키워드로 경로 노출

Listing 7-4 에서 `hosting` 모듈이 private 이라고 알려준 오류로 돌아가 보겠습니다. 상위 모듈의 `eat_at_restaurant` 함수가 하위 모듈의 `add_to_waitlist` 함수에 접근할 수 있도록 하려면, Listing 7-5 에 표시된 것처럼 `hosting` 모듈을 `pub` 키워드로 표시합니다.

파일 이름: `src/lib.rs`

```rust
mod front_of_house {
    pub mod hosting {
        fn add_to_waitlist() {}
    }
}

--snip--
```

Listing 7-5: `eat_at_restaurant`에서 사용하기 위해 `hosting` 모듈을 `pub`으로 선언

불행히도, Listing 7-5 의 코드는 Listing 7-6 에 표시된 것처럼 여전히 컴파일러 오류를 발생시킵니다.

```bash
$ cargo build
   Compiling restaurant v0.1.0 (file:///projects/restaurant)
error[E0603]: function `add_to_waitlist` is private
 --> src/lib.rs:9:37
  |
9 |     crate::front_of_house::hosting::add_to_waitlist();
  |                                     ^^^^^^^^^^^^^^^ private function
  |
note: the function `add_to_waitlist` is defined here
 --> src/lib.rs:3:9
  |
3 |         fn add_to_waitlist() {}
  |         ^^^^^^^^^^^^^^^^^^^^

error[E0603]: function `add_to_waitlist` is private
  --> src/lib.rs:12:30
   |
12 |     front_of_house::hosting::add_to_waitlist();
   |                              ^^^^^^^^^^^^^^^ private function
   |
note: the function `add_to_waitlist` is defined here
  --> src/lib.rs:3:9
   |
3  |         fn add_to_waitlist() {}
   |         ^^^^^^^^^^^^^^^^^^^^
```

Listing 7-6: Listing 7-5 의 코드를 빌드할 때의 컴파일러 오류

무슨 일이 일어났을까요? `mod hosting` 앞에 `pub` 키워드를 추가하면 모듈이 public 이 됩니다. 이 변경으로 `front_of_house`에 접근할 수 있다면 `hosting`에도 접근할 수 있습니다. 그러나 `hosting`의 *내용*은 여전히 private 입니다. 모듈을 public 으로 만든다고 해서 그 내용이 public 이 되는 것은 아닙니다. 모듈의 `pub` 키워드는 상위 모듈의 코드만 해당 모듈을 참조할 수 있도록 허용하며, 내부 코드에 접근하는 것은 허용하지 않습니다. 모듈은 컨테이너이므로 모듈만 public 으로 만드는 것으로는 할 수 있는 일이 많지 않습니다. 더 나아가 모듈 내의 하나 이상의 항목을 public 으로 만들도록 선택해야 합니다.

Listing 7-6 의 오류는 `add_to_waitlist` 함수가 private 이라고 말합니다. 개인 정보 보호 규칙은 모듈뿐만 아니라 구조체, 열거형, 함수 및 메서드에도 적용됩니다.

Listing 7-7 과 같이 정의 앞에 `pub` 키워드를 추가하여 `add_to_waitlist` 함수도 public 으로 만들어 보겠습니다.

파일 이름: `src/lib.rs`

```rust
mod front_of_house {
    pub mod hosting {
        pub fn add_to_waitlist() {}
    }
}

--snip--
```

Listing 7-7: `mod hosting` 및 `fn add_to_waitlist`에 `pub` 키워드를 추가하면 `eat_at_restaurant`에서 함수를 호출할 수 있습니다.

이제 코드가 컴파일됩니다! `pub` 키워드를 추가하면 개인 정보 보호 규칙에 따라 `add_to_waitlist`에서 이러한 경로를 사용할 수 있는 이유를 확인하기 위해 절대 경로와 상대 경로를 살펴보겠습니다.

절대 경로에서 크레이트 모듈 트리의 루트인 `crate`로 시작합니다. `front_of_house` 모듈은 크레이트 루트에 정의되어 있습니다. `front_of_house`는 public 이 아니지만, `eat_at_restaurant` 함수가 `front_of_house`와 동일한 모듈에 정의되어 있으므로 (`eat_at_restaurant`와 `front_of_house`는 형제 관계임), `eat_at_restaurant`에서 `front_of_house`를 참조할 수 있습니다. 다음은 `pub`으로 표시된 `hosting` 모듈입니다. `hosting`의 상위 모듈에 접근할 수 있으므로 `hosting`에 접근할 수 있습니다. 마지막으로, `add_to_waitlist` 함수는 `pub`으로 표시되어 있으며 해당 상위 모듈에 접근할 수 있으므로 이 함수 호출이 작동합니다!

상대 경로에서 로직은 첫 번째 단계를 제외하고 절대 경로와 동일합니다. 크레이트 루트에서 시작하는 대신 경로가 `front_of_house`에서 시작합니다. `front_of_house` 모듈은 `eat_at_restaurant`과 동일한 모듈 내에 정의되어 있으므로 `eat_at_restaurant`이 정의된 모듈에서 시작하는 상대 경로가 작동합니다. 그런 다음 `hosting`과 `add_to_waitlist`가 `pub`으로 표시되어 있으므로 나머지 경로가 작동하고 이 함수 호출이 유효합니다!

다른 프로젝트에서 코드를 사용할 수 있도록 라이브러리 크레이트를 공유하려는 경우, public API 는 크레이트 사용자가 코드와 상호 작용할 수 있는 방식을 결정하는 계약입니다. 크레이트에 의존하는 사람들을 위해 public API 에 대한 변경 사항을 관리하는 데에는 많은 고려 사항이 있습니다. 이러한 고려 사항은 이 책의 범위를 벗어납니다. 이 주제에 관심이 있다면 *https://rust-lang.github.io/api-guidelines*에서 Rust API 가이드라인을 참조하십시오.

> **바이너리 및 라이브러리가 있는 패키지에 대한 모범 사례**
>
> 패키지에는 `src/main.rs` 바이너리 크레이트 루트와 `src/lib.rs` 라이브러리 크레이트 루트가 모두 포함될 수 있으며, 두 크레이트 모두 기본적으로 패키지 이름을 갖는다고 언급했습니다. 일반적으로 라이브러리와 바이너리 크레이트를 모두 포함하는 이 패턴의 패키지는 라이브러리 크레이트의 코드를 호출하는 실행 파일을 시작하기에 충분한 코드를 바이너리 크레이트에만 갖습니다. 이렇게 하면 다른 프로젝트에서 패키지가 제공하는 대부분의 기능을 활용할 수 있습니다. 라이브러리 크레이트의 코드를 공유할 수 있기 때문입니다.
>
> 모듈 트리는 `src/lib.rs`에 정의되어야 합니다. 그런 다음, 모든 public 항목은 패키지 이름으로 경로를 시작하여 바이너리 크레이트에서 사용할 수 있습니다. 바이너리 크레이트는 완전히 외부 크레이트가 라이브러리 크레이트를 사용하는 것과 마찬가지로 라이브러리 크레이트의 사용자가 됩니다. 즉, public API 만 사용할 수 있습니다. 이렇게 하면 좋은 API 를 설계하는 데 도움이 됩니다. 작성자일 뿐만 아니라 클라이언트이기도 합니다!
>
> 12 장에서 바이너리 크레이트와 라이브러리 크레이트를 모두 포함하는 명령줄 프로그램을 사용하여 이 조직적 관행을 시연합니다.
