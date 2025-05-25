# let-else

`let`-`else`를 사용하면 반증 가능한 패턴 (refutable pattern) 이 일반적인 `let`처럼 주변 범위의 변수와 일치하고 바인딩할 수 있습니다. 패턴과 일치하지 않으면 (예: `break`, `return`, `panic!`) 분기 (diverge) 합니다.

```rust
use std::str::FromStr;

fn get_count_item(s: &str) -> (u64, &str) {
    let mut it = s.split(' ');
    let (Some(count_str), Some(item)) = (it.next(), it.next()) else {
        panic!("Can't segment count item pair: '{s}'");
    };
    let Ok(count) = u64::from_str(count_str) else {
        panic!("Can't parse integer: '{count_str}'");
    };
    (count, item)
}

fn main() {
    assert_eq!(get_count_item("3 chairs"), (3, "chairs"));
}
```

이 구문의 주요 차이점은 이름 바인딩의 범위입니다. 이전에는 `match` 또는 `if let`-`else` 표현식으로 이와 유사한 패턴을 구현하려면 불필요한 반복과 외부 `let` 문을 사용해야 했습니다.

```rust
use std::str::FromStr;

fn get_count_item(s: &str) -> (u64, &str) {
    let mut it = s.split(' ');
    let (count_str, item) = match (it.next(), it.next()) {
        (Some(count_str), Some(item)) => (count_str, item),
        _ => panic!("Can't segment count item pair: '{s}'"),
    };
    let count = if let Ok(count) = u64::from_str(count_str) {
        count
    } else {
        panic!("Can't parse integer: '{count_str}'");
    };
        (count, item)
    }

    assert_eq!(get_count_item("3 chairs"), (3, "chairs"));
}
```
