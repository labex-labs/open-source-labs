# 필드 초기화 단축 구문 사용

Listing 5-4 에서 매개변수 이름과 구조체 필드 이름이 정확히 동일하므로 _필드 초기화 단축 구문 (field init shorthand)_ 구문을 사용하여 `build_user`를 다시 작성할 수 있습니다. 이렇게 하면 동일하게 작동하지만 Listing 5-5 에 표시된 것처럼 `username`과 `email`이 반복되지 않습니다.

```rust
fn build_user(email: String, username: String) -> User {
    User {
        active: true,
        username,
        email,
        sign_in_count: 1,
    }
}
```

Listing 5-5: `username` 및 `email` 매개변수가 구조체 필드와 동일한 이름을 갖기 때문에 필드 초기화 단축 구문을 사용하는 `build_user` 함수

여기서는 `email`이라는 필드가 있는 `User` 구조체의 새 인스턴스를 생성하고 있습니다. `email` 필드의 값을 `build_user` 함수의 `email` 매개변수의 값으로 설정하려고 합니다. `email` 필드와 `email` 매개변수가 동일한 이름을 가지므로 `email: email` 대신 `email`만 작성하면 됩니다.
