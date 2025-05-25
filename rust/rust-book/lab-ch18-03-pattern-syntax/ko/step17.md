# @ 바인딩 (Bindings)

_at_ 연산자 `@`를 사용하면 패턴 일치를 위해 값을 테스트하는 동시에 값을 보유하는 변수를 생성할 수 있습니다. Listing 18-29 에서 `Message::Hello` `id` 필드가 범위 `3..=7` 내에 있는지 테스트하려고 합니다. 또한 값을 `id_variable` 변수에 바인딩하여 arm 과 관련된 코드에서 사용할 수 있도록 하려고 합니다. 이 변수의 이름을 필드와 동일하게 `id`로 지정할 수도 있지만, 이 예제에서는 다른 이름을 사용합니다.

파일 이름: `src/main.rs`

```rust
enum Message {
    Hello { id: i32 },
}

let msg = Message::Hello { id: 5 };

match msg {
    Message::Hello {
        id: id_variable @ 3..=7,
    } => println!("Found an id in range: {id_variable}"),
    Message::Hello { id: 10..=12 } => {
        println!("Found an id in another range")
    }
    Message::Hello { id } => println!("Some other id: {id}"),
}
```

Listing 18-29: `@`를 사용하여 패턴에서 값을 테스트하는 동시에 바인딩하기

이 예제는 `Found an id in range: 5`를 출력합니다. 범위 `3..=7` 앞에 `id_variable @`를 지정하여, 범위 패턴과 일치하는 값을 테스트하는 동시에 범위와 일치하는 모든 값을 캡처합니다.

두 번째 arm 에서는 패턴에 범위만 지정되어 있으며, arm 과 관련된 코드에는 `id` 필드의 실제 값을 포함하는 변수가 없습니다. `id` 필드의 값은 10, 11 또는 12 일 수 있지만, 해당 패턴과 함께 제공되는 코드는 어떤 값인지 알지 못합니다. `id` 값을 변수에 저장하지 않았기 때문에 패턴 코드는 `id` 필드의 값을 사용할 수 없습니다.

마지막 arm 에서는 범위를 지정하지 않고 변수를 지정했으므로, `id`라는 변수에서 arm 의 코드에서 사용할 수 있는 값이 있습니다. 그 이유는 구조체 필드 축약 구문을 사용했기 때문입니다. 그러나 이 arm 에서는 처음 두 arm 에서와 같이 `id` 필드의 값에 대한 테스트를 적용하지 않았습니다. 모든 값이 이 패턴과 일치합니다.

`@`를 사용하면 값을 테스트하고 하나의 패턴 내에서 변수에 저장할 수 있습니다.
