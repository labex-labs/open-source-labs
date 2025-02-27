# let-else

С использованием `let`-`else` разрешающий шаблон может сопоставить и связать переменные в окружающей области видимости, как и обычное `let`, или же расходиться (например, `break`, `return`, `panic!`), если шаблон не соответствует.

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

Область видимости именованных связей - это то, что главным образом делает это различным от `match` или `if let`-`else` выражений. Раньше вы могли приблизить эти шаблоны с помощью несчастливой повторяющейся части и внешнего `let`:

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
