# 런타임에 RefCell`<T>`로 차용 추적하기

불변 및 가변 참조를 생성할 때 각각 `&` 및 `&mut` 구문을 사용합니다. `RefCell<T>`를 사용하면 `RefCell<T>`에 속하는 안전한 API 의 일부인 `borrow` 및 `borrow_mut` 메서드를 사용합니다. `borrow` 메서드는 스마트 포인터 타입 `Ref<T>`를 반환하고, `borrow_mut`는 스마트 포인터 타입 `RefMut<T>`를 반환합니다. 두 타입 모두 `Deref`를 구현하므로 일반 참조처럼 처리할 수 있습니다.

`RefCell<T>`는 현재 활성 상태인 `Ref<T>` 및 `RefMut<T>` 스마트 포인터의 수를 추적합니다. `borrow`를 호출할 때마다 `RefCell<T>`는 활성 상태인 불변 차용의 수를 증가시킵니다. `Ref<T>` 값이 범위를 벗어날 때 불변 차용의 수는 1 감소합니다. 컴파일 타임 차용 규칙과 마찬가지로 `RefCell<T>`를 사용하면 언제든지 여러 개의 불변 차용 또는 하나의 가변 차용을 가질 수 있습니다.

이러한 규칙을 위반하려고 하면, 참조를 사용할 때와 같이 컴파일러 오류가 발생하는 대신, `RefCell<T>`의 구현은 런타임에 패닉 (panic) 을 발생시킵니다. Listing 15-23 은 Listing 15-22 에서 `send`의 구현을 수정한 것을 보여줍니다. `RefCell<T>`가 런타임에 이를 방지한다는 것을 설명하기 위해 동일한 범위에서 두 개의 가변 차용을 의도적으로 생성하려고 합니다.

파일 이름: `src/lib.rs`

```rust
impl Messenger for MockMessenger {
    fn send(&self, message: &str) {
        let mut one_borrow = self.sent_messages.borrow_mut();
        let mut two_borrow = self.sent_messages.borrow_mut();

        one_borrow.push(String::from(message));
        two_borrow.push(String::from(message));
    }
}
```

Listing 15-23: `RefCell<T>`가 패닉을 발생시키는 것을 확인하기 위해 동일한 범위에서 두 개의 가변 참조 생성

`borrow_mut`에서 반환된 `RefMut<T>` 스마트 포인터에 대한 변수 `one_borrow`를 생성합니다. 그런 다음 변수 `two_borrow`에서 동일한 방식으로 다른 가변 차용을 생성합니다. 이렇게 하면 동일한 범위에서 두 개의 가변 참조가 생성되는데, 이는 허용되지 않습니다. 라이브러리에 대한 테스트를 실행하면 Listing 15-23 의 코드는 오류 없이 컴파일되지만 테스트는 실패합니다.

    ---- tests::it_sends_an_over_75_percent_warning_message stdout ----
    thread 'main' panicked at 'already borrowed: BorrowMutError', src/lib.rs:60:53
    note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace

`already borrowed: BorrowMutError` 메시지와 함께 코드가 패닉된 것을 확인하세요. 이것이 `RefCell<T>`가 런타임에 차용 규칙 위반을 처리하는 방식입니다.

여기서와 같이 컴파일 타임 대신 런타임에 차용 오류를 잡도록 선택하면 개발 프로세스 후반에 코드에서 실수를 찾을 수 있습니다. 즉, 코드가 프로덕션에 배포될 때까지 찾지 못할 수도 있습니다. 또한 코드는 런타임에 차용을 추적하는 결과로 컴파일 타임 대신 약간의 런타임 성능 저하를 겪게 됩니다. 그러나 `RefCell<T>`를 사용하면 불변 값만 허용되는 컨텍스트에서 사용하는 동안 본 메시지를 추적하기 위해 자체적으로 수정할 수 있는 모의 객체를 작성할 수 있습니다. 일반 참조가 제공하는 것보다 더 많은 기능을 얻기 위해 트레이드 오프에도 불구하고 `RefCell<T>`를 사용할 수 있습니다.
