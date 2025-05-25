# Interfaces Variádicas

Uma interface _variádica_ recebe um número arbitrário de argumentos. Por exemplo, `println!` pode receber um número arbitrário de argumentos, conforme determinado pela string de formatação.

Podemos estender nossa macro `calculate!` da seção anterior para ser variádica:

```rust
macro_rules! calculate {
    // The pattern for a single `eval`
    (eval $e:expr) => {
        {
            let val: usize = $e; // Force types to be integers
            println!("{} = {}", stringify!{$e}, val);
        }
    };

    // Decompose multiple `eval`s recursively
    (eval $e:expr, $(eval $es:expr),+) => {{
        calculate! { eval $e }
        calculate! { $(eval $es),+ }
    }};
}

fn main() {
    calculate! { // Look ma! Variadic `calculate!`!
        eval 1 + 2,
        eval 3 + 4,
        eval (2 * 3) + 1
    }
}
```

Saída:

```txt
1 + 2 = 3
3 + 4 = 7
(2 * 3) + 1 = 7
```
