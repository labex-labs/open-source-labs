# let-else

`let`-`else` を使用すると、検証可能なパターンは通常の `let` と同じように周囲のスコープ内の変数をマッチングして束縛することができ、そうでなければ、パターンが一致しない場合には制御を抜けます（たとえば、`break`、`return`、`panic!`）。

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

名前の束縛のスコープが、これを `match` や `if let`-`else` 式と区別する主な点です。以前は、不運なことに繰り返しと外部の `let` を使ってこれらのパターンを近似することができました。

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
