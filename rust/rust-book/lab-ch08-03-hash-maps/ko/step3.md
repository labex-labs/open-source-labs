# 해시 맵에서 값에 접근하기

Listing 8-21 에 표시된 것처럼, `get` 메서드에 키를 제공하여 해시 맵에서 값을 가져올 수 있습니다.

```rust
use std::collections::HashMap;

let mut scores = HashMap::new();

scores.insert(String::from("Blue"), 10);
scores.insert(String::from("Yellow"), 50);

let team_name = String::from("Blue");
let score = scores.get(&team_name).copied().unwrap_or(0);
```

Listing 8-21: 해시 맵에 저장된 Blue 팀의 점수에 접근하기

여기서 `score`는 Blue 팀과 관련된 값을 가지며, 결과는 `10`이 됩니다. `get` 메서드는 `Option<&V>`를 반환합니다. 해시 맵에 해당 키에 대한 값이 없으면 `get`은 `None`을 반환합니다. 이 프로그램은 `Option`을 처리하기 위해 `copied`를 호출하여 `Option<&i32>` 대신 `Option<i32>`를 얻은 다음, `unwrap_or`를 사용하여 `scores`에 해당 키에 대한 항목이 없는 경우 `score`를 0 으로 설정합니다.

벡터에서와 유사한 방식으로 `for` 루프를 사용하여 해시 맵의 각 키 - 값 쌍을 반복할 수 있습니다.

```rust
use std::collections::HashMap;

let mut scores = HashMap::new();

scores.insert(String::from("Blue"), 10);
scores.insert(String::from("Yellow"), 50);

for (key, value) in &scores {
    println!("{key}: {value}");
}
```

이 코드는 각 쌍을 임의의 순서로 출력합니다.

```rust
Yellow: 50
Blue: 10
```
