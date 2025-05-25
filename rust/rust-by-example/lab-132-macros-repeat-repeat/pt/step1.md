# Repetição

Macros podem usar `+` na lista de argumentos para indicar que um argumento pode se repetir pelo menos uma vez, ou `*`, para indicar que o argumento pode se repetir zero ou mais vezes.

No exemplo a seguir, envolver o matcher com `$(...),+` corresponderá a uma ou mais expressões, separadas por vírgulas. Observe também que o ponto e vírgula é opcional no último caso.

```rust
// `find_min!` calculará o mínimo de qualquer número de argumentos.
macro_rules! find_min {
    // Caso base:
    ($x:expr) => ($x);
    // `$x` seguido por pelo menos um `$y,`
    ($x:expr, $($y:expr),+) => (
        // Chama `find_min!` na cauda `$y`
        std::cmp::min($x, find_min!($($y),+))
    )
}

fn main() {
    println!("{}", find_min!(1));
    println!("{}", find_min!(1 + 2, 2));
    println!("{}", find_min!(5, 2 * 3, 4));
}
```
