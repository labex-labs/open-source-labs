# 해시 맵과 소유권

`i32`와 같이 `Copy` 트레이트를 구현하는 타입의 경우, 값은 해시 맵으로 복사됩니다. `String`과 같은 소유된 값의 경우, 값은 이동되고 해시 맵이 해당 값의 소유자가 됩니다. 이는 Listing 8-22 에서 보여줍니다.

```rust
use std::collections::HashMap;

let field_name = String::from("Favorite color");
let field_value = String::from("Blue");

let mut map = HashMap::new();
map.insert(field_name, field_value);
// field_name and field_value are invalid at this point, try
// using them and see what compiler error you get!
```

Listing 8-22: 삽입된 후 키와 값이 해시 맵에 의해 소유됨을 보여줍니다.

`insert` 호출을 통해 변수 `field_name`과 `field_value`가 해시 맵으로 이동된 후에는 사용할 수 없습니다.

값에 대한 참조를 해시 맵에 삽입하는 경우, 값은 해시 맵으로 이동되지 않습니다. 참조가 가리키는 값은 해시 맵이 유효한 기간 이상 동안 유효해야 합니다. 이러한 문제에 대해서는 "생명주기를 사용하여 참조 유효성 검사"에서 자세히 설명합니다.
