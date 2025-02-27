# Variadische Schnittstellen

Eine _variadische_ Schnittstelle nimmt beliebig viele Argumente an. Beispielsweise kann `println!` beliebig viele Argumente entgegennehmen, wie durch die Formatzeichenfolge bestimmt.

Wir können unsere `calculate!`-Makro aus dem vorherigen Abschnitt erweitern, um es variadisch zu machen:

```rust
macro_rules! calculate {
    // Das Muster für einen einzelnen `eval`
    (eval $e:expr) => {
        {
            let val: usize = $e; // Zwinge die Typen zu Ganzzahlen
            println!("{} = {}", stringify!{$e}, val);
        }
    };

    // Zerlege mehrere `eval`s rekursiv
    (eval $e:expr, $(eval $es:expr),+) => {{
        calculate! { eval $e }
        calculate! { $(eval $es),+ }
    }};
}

fn main() {
    calculate! { // Sieh mal, Mama! Variadisches `calculate!`!
        eval 1 + 2,
        eval 3 + 4,
        eval (2 * 3) + 1
    }
}
```

Ausgabe:

```txt
1 + 2 = 3
3 + 4 = 7
(2 * 3) + 1 = 7
```
