# let-else

Mit `let`-`else` kann ein widerlegbares Muster wie ein normales `let` Variablen im umgebenden Gültigkeitsbereich abgleichen und binden, oder andernfalls divergieren (z.B. `break`, `return`, `panic!`), wenn das Muster nicht übereinstimmt.

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

Der Gültigkeitsbereich der Namensbindungen ist das Wesentliche, was dieses von `match`- oder `if let`-`else`-Ausdrücken unterscheidet. Früher konnten Sie diese Muster mit einem unglücklichen Wiederholungsanteil und einem äußeren `let` annähern:

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
```
