# 값 덮어쓰기

해시 맵에 키와 값을 삽입한 다음, 동일한 키를 다른 값으로 삽입하면 해당 키와 관련된 값이 대체됩니다. Listing 8-23 의 코드가 `insert`를 두 번 호출하더라도, 해시 맵은 하나의 키 - 값 쌍만 포함합니다. 이는 Blue 팀의 키에 대한 값을 두 번 모두 삽입하기 때문입니다.

```rust
use std::collections::HashMap;

let mut scores = HashMap::new();

scores.insert(String::from("Blue"), 10);
scores.insert(String::from("Blue"), 25);

println!("{:?}", scores);
```

Listing 8-23: 특정 키에 저장된 값을 대체하기

이 코드는 `{"Blue": 25}`를 출력합니다. 원래 값인 `10`이 덮어쓰여졌습니다.
