# let-else

Con `let`-`else`, un patrón refutable puede coincidir y enlazar variables en el ámbito circundante como un `let` normal, o en su defecto diverger (por ejemplo, `break`, `return`, `panic!`) cuando el patrón no coincide.

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

El ámbito de enlaces de nombres es lo principal que los distingue de las expresiones `match` o `if let`-`else`. Anteriormente, se podía aproximar estos patrones con una desagradable cantidad de repetición y un `let` externo:

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
