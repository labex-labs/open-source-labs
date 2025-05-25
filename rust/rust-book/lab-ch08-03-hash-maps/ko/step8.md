# 이전 값을 기반으로 값 업데이트하기

해시 맵의 또 다른 일반적인 사용 사례는 키의 값을 조회한 다음 이전 값을 기반으로 업데이트하는 것입니다. 예를 들어, Listing 8-25 는 텍스트에서 각 단어가 몇 번 나타나는지 계산하는 코드를 보여줍니다. 단어를 키로 사용하고 값을 증가시켜 해당 단어를 몇 번 보았는지 추적하는 해시 맵을 사용합니다. 단어를 처음 보는 경우 먼저 값 `0`을 삽입합니다.

```rust
use std::collections::HashMap;

let text = "hello world wonderful world";

let mut map = HashMap::new();

for word in text.split_whitespace() {
    let count = map.entry(word).or_insert(0);
    *count += 1;
}

println!("{:?}", map);
```

Listing 8-25: 단어와 개수를 저장하는 해시 맵을 사용하여 단어의 발생 횟수 계산

이 코드는 `{"world": 2, "hello": 1, "wonderful": 1}`을 출력합니다. 동일한 키 - 값 쌍이 다른 순서로 출력될 수 있습니다. "해시 맵에서 값에 접근하기"에서 해시 맵을 반복하는 것은 임의의 순서로 발생한다는 것을 기억하십시오.

`split_whitespace` 메서드는 `text`의 값에서 공백으로 구분된 하위 슬라이스에 대한 반복자를 반환합니다. `or_insert` 메서드는 지정된 키에 대한 값에 대한 가변 참조 (`&mut V`) 를 반환합니다. 여기서 해당 가변 참조를 `count` 변수에 저장하므로 해당 값에 할당하려면 먼저 별표 (`*`) 를 사용하여 `count`를 역참조해야 합니다. 가변 참조는 `for` 루프의 끝에서 범위를 벗어나므로 이러한 모든 변경 사항은 안전하며 borrow checker 에 의해 허용됩니다.
