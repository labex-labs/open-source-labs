# if let 을 사용한 간결한 제어 흐름

`if let` 구문을 사용하면 `if`와 `let`을 결합하여 나머지 값은 무시하고 하나의 패턴과 일치하는 값을 처리하는 덜 장황한 방식으로 구현할 수 있습니다. `config_max` 변수에서 `Option<u8>` 값에 대해 일치하지만 값이 `Some` 변형인 경우에만 코드를 실행하려는 Listing 6-6 의 프로그램을 생각해 보십시오.

```rust
let config_max = Some(3u8);
match config_max {
    Some(max) => println!("The maximum is configured to be {max}"),
    _ => (),
}
```

Listing 6-6: 값이 `Some`일 때만 코드를 실행하는 `match`

값이 `Some`인 경우, 값을 패턴의 변수 `max`에 바인딩하여 `Some` 변형의 값을 출력합니다. `None` 값으로는 아무것도 하고 싶지 않습니다. `match` 표현식을 충족하기 위해 하나의 변형만 처리한 후 `_ => ()`를 추가해야 하는데, 이는 추가하기 귀찮은 상용구 코드입니다.

대신, `if let`을 사용하여 더 짧은 방식으로 작성할 수 있습니다. 다음 코드는 Listing 6-6 의 `match`와 동일하게 동작합니다.

```rust
let config_max = Some(3u8);
if let Some(max) = config_max {
    println!("The maximum is configured to be {max}");
}
```

`if let` 구문은 등호로 구분된 패턴과 표현식을 사용합니다. `match`와 동일한 방식으로 작동하며, 표현식은 `match`에 제공되고 패턴은 첫 번째 arm 입니다. 이 경우 패턴은 `Some(max)`이고 `max`는 `Some` 내부의 값에 바인딩됩니다. 그런 다음 해당 `match` arm 에서 `max`를 사용한 것과 동일한 방식으로 `if let` 블록의 본문에서 `max`를 사용할 수 있습니다. 값이 패턴과 일치하지 않으면 `if let` 블록의 코드는 실행되지 않습니다.

`if let`을 사용하면 타이핑, 들여쓰기 및 상용구 코드가 줄어듭니다. 그러나 `match`가 강제하는 완전한 검사를 잃게 됩니다. `match`와 `if let` 중에서 선택하는 것은 특정 상황에서 수행하는 작업과 완전한 검사를 잃는 것이 간결성을 얻는 데 적절한 절충안인지 여부에 따라 달라집니다.

다시 말해, `if let`을 값과 일치하는 패턴이 있을 때 코드를 실행하고 다른 모든 값은 무시하는 `match`에 대한 구문 설탕 (syntax sugar) 으로 생각할 수 있습니다.

`if let`과 함께 `else`를 포함할 수 있습니다. `else`와 함께 제공되는 코드 블록은 `if let` 및 `else`와 동일한 `match` 표현식에서 `_` case 와 함께 제공되는 코드 블록과 동일합니다. `Quarter` 변형이 `UsState` 값도 포함하는 Listing 6-4 의 `Coin` 열거형 정의를 기억하십시오. 분기별 동전의 상태를 알리는 동시에 분기별이 아닌 모든 동전을 세고 싶다면 다음과 같이 `match` 표현식을 사용할 수 있습니다.

```rust
let mut count = 0;
match coin {
    Coin::Quarter(state) => println!("State quarter from {:?}!", state),
    _ => count += 1,
}
```

또는 다음과 같이 `if let` 및 `else` 표현식을 사용할 수 있습니다.

```rust
let mut count = 0;
if let Coin::Quarter(state) = coin {
    println!("State quarter from {:?}!", state);
} else {
    count += 1;
}
```

프로그램에 `match`를 사용하여 표현하기에는 너무 장황한 로직이 있는 상황이 있다면, `if let`도 Rust 도구 상자에 있다는 것을 기억하십시오.
