# 키가 존재하지 않는 경우에만 키와 값 추가하기

특정 키가 해시 맵에 이미 값과 함께 존재하는지 확인한 다음 다음 작업을 수행하는 것이 일반적입니다. 키가 해시 맵에 존재하면 기존 값은 그대로 유지되어야 합니다. 키가 존재하지 않으면 키와 해당 값을 삽입합니다.

해시 맵에는 이를 위한 특별한 API 인 `entry`가 있으며, 확인하려는 키를 매개변수로 사용합니다. `entry` 메서드의 반환 값은 `Entry`라는 열거형 (enum) 으로, 존재할 수도 있고 존재하지 않을 수도 있는 값을 나타냅니다. Yellow 팀의 키에 연결된 값이 있는지 확인하려는 경우를 가정해 보겠습니다. 값이 없으면 값 `50`을 삽입하고, Blue 팀에 대해서도 동일하게 수행하려고 합니다. `entry` API 를 사용하면 코드는 Listing 8-24 와 같습니다.

```rust
use std::collections::HashMap;

let mut scores = HashMap::new();
scores.insert(String::from("Blue"), 10);

scores.entry(String::from("Yellow")).or_insert(50);
scores.entry(String::from("Blue")).or_insert(50);

println!("{:?}", scores);
```

Listing 8-24: 키에 이미 값이 없는 경우에만 삽입하기 위해 `entry` 메서드 사용

`Entry`의 `or_insert` 메서드는 해당 키가 존재하면 해당 `Entry` 키에 대한 값에 대한 가변 참조를 반환하도록 정의되어 있으며, 그렇지 않으면 매개변수를 이 키에 대한 새 값으로 삽입하고 새 값에 대한 가변 참조를 반환합니다. 이 기술은 자체적으로 로직을 작성하는 것보다 훨씬 깔끔하며, 또한 borrow checker 와 더 잘 작동합니다.

Listing 8-24 의 코드를 실행하면 `{"Yellow": 50, "Blue": 10}`이 출력됩니다. `entry`에 대한 첫 번째 호출은 Yellow 팀에 대한 키를 값 `50`과 함께 삽입합니다. Yellow 팀에는 이미 값이 없기 때문입니다. `entry`에 대한 두 번째 호출은 Blue 팀에 이미 값 `10`이 있기 때문에 해시 맵을 변경하지 않습니다.
