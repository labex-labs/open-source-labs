# 모듈을 다른 파일로 분리하기

지금까지 이 장의 모든 예제는 하나의 파일에서 여러 모듈을 정의했습니다. 모듈이 커지면 코드를 더 쉽게 탐색할 수 있도록 정의를 별도의 파일로 옮기고 싶을 수 있습니다.

예를 들어, 여러 레스토랑 모듈이 있는 Listing 7-17 의 코드부터 시작해 보겠습니다. 모든 모듈을 크레이트 루트 파일에 정의하는 대신 모듈을 파일로 추출할 것입니다. 이 경우 크레이트 루트 파일은 `src/lib.rs`이지만, 이 절차는 크레이트 루트 파일이 `src/main.rs`인 바이너리 크레이트에서도 작동합니다.

먼저 `front_of_house` 모듈을 자체 파일로 추출합니다. `front_of_house` 모듈의 중괄호 안의 코드를 제거하고 `mod front_of_house;` 선언만 남겨두면 `src/lib.rs`는 Listing 7-21 에 표시된 코드를 포함하게 됩니다. Listing 7-22 에서 `src/front_of_house.rs` 파일을 생성하기 전까지는 컴파일되지 않습니다.

파일 이름: `src/lib.rs`

```rust
mod front_of_house;

pub use crate::front_of_house::hosting;

pub fn eat_at_restaurant() {
    hosting::add_to_waitlist();
}
```

Listing 7-21: `src/front_of_house.rs`에 본문이 있는 `front_of_house` 모듈 선언

다음으로, 중괄호 안의 코드를 `src/front_of_house.rs`라는 새 파일에 넣습니다 (Listing 7-22 참조). 컴파일러는 크레이트 루트에서 `front_of_house`라는 이름의 모듈 선언을 발견했기 때문에 이 파일을 찾아야 한다는 것을 알고 있습니다.

파일 이름: `src/front_of_house.rs`

```rust
pub mod hosting {
    pub fn add_to_waitlist() {}
}
```

Listing 7-22: `src/front_of_house.rs`의 `front_of_house` 모듈 내부 정의

모듈 트리에서 *한 번*만 `mod` 선언을 사용하여 파일을 로드해야 합니다. 컴파일러가 파일이 프로젝트의 일부임을 알고 (그리고 `mod` 문을 배치한 위치 때문에 코드가 모듈 트리의 어디에 있는지 알고) 나면 프로젝트의 다른 파일은 "모듈 트리에서 항목을 참조하기 위한 경로"에서 다룬 것처럼 선언된 위치에 대한 경로를 사용하여 로드된 파일의 코드를 참조해야 합니다. 즉, `mod`는 다른 프로그래밍 언어에서 보았을 수 있는 "include" 연산이 _아닙니다_.

다음으로, `hosting` 모듈을 자체 파일로 추출합니다. `hosting`은 루트 모듈이 아닌 `front_of_house`의 자식 모듈이므로 프로세스가 약간 다릅니다. `hosting`에 대한 파일을 모듈 트리에서 해당 조상의 이름을 따서 명명된 새 디렉토리 (이 경우 _src/front_of_house_)에 배치합니다.

`hosting`을 이동하기 시작하려면 `src/front_of_house.rs`를 변경하여 `hosting` 모듈의 선언만 포함하도록 합니다.

파일 이름: `src/front_of_house.rs`

```rust
pub mod hosting;
```

그런 다음 `src/front_of_house` 디렉토리와 `hosting` 모듈에서 만든 정의를 포함하는 `hosting.rs` 파일을 만듭니다.

파일 이름: `src/front_of_house/hosting.rs`

```rust
pub fn add_to_waitlist() {}
```

대신 `hosting.rs`를 `src` 디렉토리에 넣으면 컴파일러는 `hosting.rs` 코드가 크레이트 루트에 선언된 `hosting` 모듈에 있어야 하고 `front_of_house` 모듈의 자식으로 선언되지 않아야 한다고 예상합니다. 어떤 모듈의 코드를 위해 어떤 파일을 확인할지에 대한 컴파일러의 규칙은 디렉토리와 파일이 모듈 트리에 더 가깝게 일치하도록 합니다.

> **대체 파일 경로**
>
> 지금까지 Rust 컴파일러가 사용하는 가장 관용적인 파일 경로를 다루었지만, Rust 는 이전 스타일의 파일 경로도 지원합니다. 크레이트 루트에 선언된 `front_of_house`라는 모듈의 경우 컴파일러는 모듈의 코드를 다음에서 찾습니다.
>
> - `src/front_of_house.rs` (우리가 다룬 내용)
> - `src/front_of_house/mod.rs` (이전 스타일, 여전히 지원되는 경로)
>
> `front_of_house`의 하위 모듈인 `hosting`이라는 모듈의 경우 컴파일러는 모듈의 코드를 다음에서 찾습니다.
>
> - `src/front_of_house/hosting.rs` (우리가 다룬 내용)
> - `src/front_of_house/hosting/mod.rs` (이전 스타일, 여전히 지원되는 경로)
>
> 동일한 모듈에 대해 두 스타일을 모두 사용하는 경우 컴파일러 오류가 발생합니다. 동일한 프로젝트의 다른 모듈에 대해 두 스타일을 혼합하여 사용하는 것은 허용되지만 프로젝트를 탐색하는 사람들에게 혼란을 줄 수 있습니다.
>
> `mod.rs`라는 파일을 사용하는 스타일의 주요 단점은 프로젝트에 `mod.rs`라는 파일이 많이 생길 수 있으며, 편집기에서 동시에 열어두면 혼란스러울 수 있다는 것입니다.

각 모듈의 코드를 별도의 파일로 옮겼으며 모듈 트리는 동일하게 유지됩니다. `eat_at_restaurant`의 함수 호출은 정의가 다른 파일에 있어도 수정 없이 작동합니다. 이 기술을 사용하면 모듈이 커짐에 따라 새 파일로 이동할 수 있습니다.

`src/lib.rs`의 `pub use crate::front_of_house::hosting` 문도 변경되지 않았으며, `use`는 크레이트의 일부로 컴파일되는 파일에 영향을 미치지 않습니다. `mod` 키워드는 모듈을 선언하고, Rust 는 해당 모듈에 들어갈 코드를 위해 모듈과 동일한 이름의 파일을 찾습니다.
