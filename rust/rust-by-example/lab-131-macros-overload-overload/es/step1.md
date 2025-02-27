# Sobrecarga

Las macros pueden ser sobrecargadas para aceptar diferentes combinaciones de argumentos. Al respecto, `macro_rules!` puede funcionar de manera similar a un bloque `match`:

```rust
// `test!` comparará `$left` y `$right`
// de diferentes maneras dependiendo de cómo se invoque:
macro_rules! test {
    // Los argumentos no necesitan estar separados por una coma.
    // ¡Se puede utilizar cualquier plantilla!
    ($left:expr; and $right:expr) => {
        println!("{:?} and {:?} is {:?}",
                 stringify!($left),
                 stringify!($right),
                 $left && $right)
    };
    // ^ cada brazo debe terminar con un punto y coma.
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
