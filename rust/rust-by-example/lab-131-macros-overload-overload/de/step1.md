# Überladen

Makros können überladen werden, um verschiedene Argumentkombinationen zu akzeptieren. In Bezug auf das können `macro_rules!` ähnlich wie ein `match`-Block funktionieren:

```rust
// `test!` wird `$left` und `$right`
// auf verschiedene Weise vergleichen, je nachdem, wie du es aufrufst:
macro_rules! test {
    // Die Argumente müssen nicht durch ein Komma getrennt werden.
    // Jede Vorlage kann verwendet werden!
    ($left:expr; and $right:expr) => {
        println!("{:?} and {:?} is {:?}",
                 stringify!($left),
                 stringify!($right),
                 $left && $right)
    };
    // ^ jedes Armende muss mit einem Semikolon enden.
    ($left:expr; or $right:expr) => {
        println!("{:?} or {:?} is {:?}",
                 stringify!($left),
                 stringify!($right),
                 $left || $right)
    };
}

fn main() {
    test!(1i32 + 1 == 2i32; and 2i32 * 2 == 4i32);
    test!(true; or false);
}
```
