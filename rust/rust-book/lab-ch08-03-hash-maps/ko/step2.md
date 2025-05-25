# 새로운 해시 맵 생성하기

빈 해시 맵을 생성하는 한 가지 방법은 `new`를 사용하고 `insert`로 요소를 추가하는 것입니다. Listing 8-20 에서는 *Blue*와 *Yellow*라는 이름을 가진 두 팀의 점수를 추적하고 있습니다. Blue 팀은 10 점으로 시작하고 Yellow 팀은 50 점으로 시작합니다.

```rust
use std::collections::HashMap;

let mut scores = HashMap::new();

scores.insert(String::from("Blue"), 10);
scores.insert(String::from("Yellow"), 50);
```

Listing 8-20: 새로운 해시 맵을 생성하고 일부 키와 값을 삽입하기

먼저 표준 라이브러리의 collections 부분에서 `HashMap`을 `use`해야 합니다. 세 가지 일반적인 컬렉션 중에서 이 해시 맵은 가장 덜 사용되므로, prelude 에서 자동으로 범위 내로 가져오는 기능에 포함되지 않습니다. 해시 맵은 또한 표준 라이브러리에서 지원이 적습니다. 예를 들어, 해시 맵을 생성하기 위한 내장 매크로가 없습니다.

벡터와 마찬가지로 해시 맵은 데이터를 힙 (heap) 에 저장합니다. 이 `HashMap`은 `String` 타입의 키와 `i32` 타입의 값을 갖습니다. 벡터와 마찬가지로 해시 맵은 동질적 (homogeneous) 입니다. 즉, 모든 키는 동일한 타입을 가져야 하고, 모든 값은 동일한 타입을 가져야 합니다.
