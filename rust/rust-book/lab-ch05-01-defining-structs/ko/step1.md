# 구조체 정의 및 인스턴스화

구조체는 "튜플 타입"에서 논의된 튜플과 유사하며, 둘 다 여러 관련 값을 보유합니다. 튜플과 마찬가지로 구조체의 구성 요소는 서로 다른 타입일 수 있습니다. 튜플과 달리 구조체에서는 각 데이터 조각의 이름을 지정하여 값의 의미를 명확하게 알 수 있습니다. 이러한 이름을 추가하면 구조체가 튜플보다 더 유연해집니다. 인스턴스의 값을 지정하거나 액세스하기 위해 데이터의 순서에 의존할 필요가 없습니다.

구조체를 정의하려면 `struct` 키워드를 입력하고 전체 구조체의 이름을 지정합니다. 구조체의 이름은 함께 그룹화되는 데이터 조각의 중요성을 설명해야 합니다. 그런 다음 중괄호 안에 데이터 조각의 이름과 타입을 정의하는데, 이를 *필드 (fields)*라고 합니다. 예를 들어, Listing 5-1 은 사용자 계정에 대한 정보를 저장하는 구조체를 보여줍니다.

파일 이름: `src/main.rs`

```rust
struct User {
    active: bool,
    username: String,
    email: String,
    sign_in_count: u64,
}
```

Listing 5-1: `User` 구조체 정의

구조체를 정의한 후 사용하려면 각 필드에 대한 구체적인 값을 지정하여 해당 구조체의 *인스턴스 (instance)*를 생성합니다. 구조체의 이름을 지정한 다음 중괄호 안에 키:값 쌍을 포함하여 인스턴스를 생성합니다. 여기서 키는 필드의 이름이고 값은 해당 필드에 저장하려는 데이터입니다. 구조체에서 선언한 것과 동일한 순서로 필드를 지정할 필요는 없습니다. 즉, 구조체 정의는 타입에 대한 일반적인 템플릿과 같으며, 인스턴스는 해당 템플릿을 특정 데이터로 채워 해당 타입의 값을 생성합니다. 예를 들어, Listing 5-2 와 같이 특정 사용자를 선언할 수 있습니다.

파일 이름: `src/main.rs`

```rust
fn main() {
    let user1 = User {
        active: true,
        username: String::from("someusername123"),
        email: String::from("someone@example.com"),
        sign_in_count: 1,
    };
}
```

Listing 5-2: `User` 구조체의 인스턴스 생성

구조체에서 특정 값을 가져오려면 점 표기법을 사용합니다. 예를 들어, 이 사용자의 이메일 주소에 액세스하려면 `user1.email`을 사용합니다. 인스턴스가 가변적이면 점 표기법을 사용하고 특정 필드에 할당하여 값을 변경할 수 있습니다. Listing 5-3 은 가변 `User` 인스턴스의 `email` 필드에서 값을 변경하는 방법을 보여줍니다.

파일 이름: `src/main.rs`

```rust
fn main() {
    let mut user1 = User {
        active: true,
        username: String::from("someusername123"),
        email: String::from("someone@example.com"),
        sign_in_count: 1,
    };

    user1.email = String::from("anotheremail@example.com");
}
```

Listing 5-3: `User` 인스턴스의 `email` 필드에서 값 변경

전체 인스턴스가 가변적이어야 합니다. Rust 는 특정 필드만 가변으로 표시하는 것을 허용하지 않습니다. 모든 표현식과 마찬가지로 함수 본문의 마지막 표현식으로 구조체의 새 인스턴스를 생성하여 해당 새 인스턴스를 암시적으로 반환할 수 있습니다.

Listing 5-4 는 주어진 이메일과 사용자 이름으로 `User` 인스턴스를 반환하는 `build_user` 함수를 보여줍니다. `active` 필드는 `true` 값을 얻고, `sign_in_count`는 `1` 값을 얻습니다.

```rust
fn build_user(email: String, username: String) -> User {
    User {
        active: true,
        username: username,
        email: email,
        sign_in_count: 1,
    }
}
```

Listing 5-4: 이메일과 사용자 이름을 받아 `User` 인스턴스를 반환하는 `build_user` 함수

함수 매개변수의 이름을 구조체 필드와 동일한 이름으로 지정하는 것이 합리적이지만, `email` 및 `username` 필드 이름과 변수를 반복해야 하는 것은 약간 지루합니다. 구조체에 더 많은 필드가 있는 경우 각 이름을 반복하는 것이 더욱 짜증날 것입니다. 다행히 편리한 약어가 있습니다!
