# let-else

Com `let`-`else`, um padrão refutável pode corresponder e vincular variáveis no escopo circundante como um `let` normal, ou divergir (por exemplo, `break`, `return`, `panic!`) quando o padrão não corresponde.

```rust
use std::str::FromStr;

fn get_count_item(s: &str) -> (u64, &str) {
    let mut it = s.split(' ');
    let (Some(count_str), Some(item)) = (it.next(), it.next()) else {
        panic!("Não é possível segmentar o par de itens de contagem: '{s}'");
    };
    let Ok(count) = u64::from_str(count_str) else {
        panic!("Não é possível analisar o inteiro: '{count_str}'");
    };
    (count, item)
}

fn main() {
    assert_eq!(get_count_item("3 chairs"), (3, "chairs"));
}
```

O escopo das ligações de nomes é o principal fator que diferencia isso de expressões `match` ou `if let`-`else`. Anteriormente, esses padrões podiam ser aproximados com uma repetição desnecessária e um `let` externo:

```rust
use std::str::FromStr;

fn get_count_item(s: &str) -> (u64, &str) {
    let mut it = s.split(' ');
    let (count_str, item) = match (it.next(), it.next()) {
        (Some(count_str), Some(item)) => (count_str, item),
        _ => panic!("Não é possível segmentar o par de itens de contagem: '{s}'"),
    };
    let count = if let Ok(count) = u64::from_str(count_str) {
        count
    } else {
        panic!("Não é possível analisar o inteiro: '{count_str}'");
    };
        (count, item)
    }

    assert_eq!(get_count_item("3 chairs"), (3, "chairs"));
}
```
