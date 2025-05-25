# 값에 바인딩되는 패턴

match arm 의 또 다른 유용한 기능은 패턴과 일치하는 값의 부분에 바인딩될 수 있다는 것입니다. 이것이 enum 변형에서 값을 추출하는 방법입니다.

예를 들어, enum 변형 중 하나를 변경하여 내부에 데이터를 저장해 보겠습니다. 1999 년부터 2008 년까지 미국은 한 면에 50 개 주 각각에 대해 다른 디자인을 가진 쿼터를 주조했습니다. 다른 동전은 주 디자인을 갖지 않았으므로 쿼터만 이 추가 값을 갖습니다. Listing 6-4 에서와 같이 `Quarter` 변형을 변경하여 내부에 저장된 `UsState` 값을 포함하도록 하여 이 정보를 `enum`에 추가할 수 있습니다.

```rust
#[derive(Debug)] // so we can inspect the state in a minute
enum UsState {
    Alabama,
    Alaska,
    --snip--
}

enum Coin {
    Penny,
    Nickel,
    Dime,
    Quarter(UsState),
}
```

Listing 6-4: `Quarter` 변형이 `UsState` 값도 포함하는 `Coin` enum

친구가 50 개 주 쿼터를 모두 수집하려고 한다고 가정해 보겠습니다. 동전 종류별로 느슨한 변화를 정렬하는 동안 각 쿼터와 관련된 주의 이름을 외쳐서 친구가 가지고 있지 않은 경우 컬렉션에 추가할 수 있도록 합니다.

이 코드의 match 표현식에서 `Coin::Quarter` 변형의 값과 일치하는 패턴에 `state`라는 변수를 추가합니다. `Coin::Quarter`가 일치하면 `state` 변수는 해당 쿼터의 주 값에 바인딩됩니다. 그런 다음 다음과 같이 해당 arm 의 코드에서 `state`를 사용할 수 있습니다.

```rust
fn value_in_cents(coin: Coin) -> u8 {
    match coin {
        Coin::Penny => 1,
        Coin::Nickel => 5,
        Coin::Dime => 10,
        Coin::Quarter(state) => {
            println!("State quarter from {:?}!", state);
            25
        }
    }
}
```

`value_in_cents(Coin::Quarter(UsState::Alaska))`를 호출하면 `coin`은 `Coin::Quarter(UsState::Alaska)`가 됩니다. 해당 값을 각 match arm 과 비교할 때 `Coin::Quarter(state)`에 도달할 때까지 일치하는 항목이 없습니다. 그 시점에서 `state`에 대한 바인딩은 값 `UsState::Alaska`가 됩니다. 그런 다음 `println!` 표현식에서 해당 바인딩을 사용하여 `Quarter`에 대한 `Coin` enum 변형에서 내부 주 값을 얻을 수 있습니다.
