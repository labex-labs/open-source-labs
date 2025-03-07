# Повторение

Макросы могут использовать `+` в списке аргументов, чтобы указать, что аргумент может повторяться по крайней мере один раз, или `*`, чтобы указать, что аргумент может повторяться ноль или более раз.

В следующем примере обрамление сопоставителя `$(...),+` будет соответствовать одному или более выражениям, разделенным запятыми. Также обратите внимание, что точка с запятой необязательна в последнем случае.

```rust
// `find_min!` будет вычислять минимум любого количества аргументов.
macro_rules! find_min {
    // Базовый случай:
    ($x:expr) => ($x);
    // `$x`, за которым следует по крайней мере один `$y,`
    ($x:expr, $($y:expr),+) => (
        // Вызов `find_min!` для хвоста `$y`
        std::cmp::min($x, find_min!($($y),+))
    )
}

fn main() {
    println!("{}", find_min!(1));
    println!("{}", find_min!(1 + 2, 2));
    println!("{}", find_min!(5, 2 * 3, 4));
}
```
