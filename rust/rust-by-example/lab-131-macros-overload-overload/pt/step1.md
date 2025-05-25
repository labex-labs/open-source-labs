# Sobrecarga (Overload)

Macros podem ser sobrecarregadas para aceitar diferentes combinações de argumentos. Nesse sentido, `macro_rules!` pode funcionar de forma semelhante a um bloco `match`:

```rust
// `test!` irá comparar `$left` e `$right`
// de diferentes maneiras, dependendo de como você o invoca:
macro_rules! test {
    // Os argumentos não precisam ser separados por vírgula.
    // Qualquer template pode ser usado!
    ($left:expr; and $right:expr) => {
        println!("{:?} and {:?} is {:?}",
                 stringify!($left),
                 stringify!($right),
                 $left && $right)
    };
    // ^ cada braço deve terminar com um ponto e vírgula.
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
