# 구조체 업데이트 구문을 사용하여 다른 인스턴스에서 인스턴스 생성

다른 인스턴스의 대부분의 값을 포함하지만 일부 값을 변경하는 구조체의 새 인스턴스를 생성하는 것이 유용한 경우가 많습니다. *구조체 업데이트 구문 (struct update syntax)*을 사용하여 이를 수행할 수 있습니다.

먼저, Listing 5-6 에서는 업데이트 구문 없이 `user2`에서 새 `User` 인스턴스를 일반적인 방식으로 생성하는 방법을 보여줍니다. `email`에 대한 새 값을 설정하지만, 그 외에는 Listing 5-2 에서 생성한 `user1`의 동일한 값을 사용합니다.

파일 이름: `src/main.rs`

```rust
fn main() {
    --snip--

    let user2 = User {
        active: user1.active,
        username: user1.username,
        email: String::from("another@example.com"),
        sign_in_count: user1.sign_in_count,
    };
}
```

Listing 5-6: `user1`의 값 중 하나를 사용하여 새 `User` 인스턴스 생성

구조체 업데이트 구문을 사용하면 Listing 5-7 에 표시된 것처럼 더 적은 코드로 동일한 효과를 얻을 수 있습니다. 구문 `..`은 명시적으로 설정되지 않은 나머지 필드가 지정된 인스턴스의 필드와 동일한 값을 가져야 함을 지정합니다.

파일 이름: `src/main.rs`

```rust
fn main() {
    --snip--


    let user2 = User {
        email: String::from("another@example.com"),
        ..user1
    };
}
```

Listing 5-7: 구조체 업데이트 구문을 사용하여 `User` 인스턴스에 대한 새 `email` 값을 설정하지만 `user1`의 나머지 값을 사용

Listing 5-7 의 코드는 또한 `email`에 대해 다른 값을 갖지만 `user1`의 `username`, `active`, 및 `sign_in_count` 필드에 대해 동일한 값을 갖는 `user2`의 인스턴스를 생성합니다. `..user1`은 나머지 필드가 `user1`의 해당 필드에서 값을 가져야 함을 지정하기 위해 마지막에 와야 하지만, 구조체의 정의에서 필드의 순서에 관계없이 원하는 만큼의 필드에 대한 값을 원하는 순서로 지정할 수 있습니다.

구조체 업데이트 구문은 할당과 마찬가지로 `=`를 사용합니다. 이는 "변수와 데이터의 상호 작용: 이동 (Move)"에서 살펴본 것처럼 데이터를 이동하기 때문입니다. 이 예제에서는 `user1`의 `username` 필드에 있는 `String`이 `user2`로 이동되었으므로 `user2`를 생성한 후에는 더 이상 `user1`을 사용할 수 없습니다. `user2`에 `email`과 `username` 모두에 대한 새 `String` 값을 제공하여 `user1`에서 `active` 및 `sign_in_count` 값만 사용했다면, `user2`를 생성한 후에도 `user1`은 여전히 유효합니다. `active`와 `sign_in_count`는 모두 `Copy` 트레이트를 구현하는 타입이므로 "스택 전용 데이터: 복사 (Copy)"에서 논의한 동작이 적용됩니다.
