# let-else

Avec `let`-`else`, un motif réfutable peut correspondre et lier des variables dans la portée environnante comme un `let` normal, ou sinon diverger (par exemple `break`, `return`, `panic!`) lorsque le motif ne correspond pas.

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

La portée des liaisons de nom est la principale chose qui le différencie des expressions `match` ou `if let`-`else`. Précédemment, vous pourriez approcher ces motifs avec un peu de répétition malheureuse et un `let` externe :

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
