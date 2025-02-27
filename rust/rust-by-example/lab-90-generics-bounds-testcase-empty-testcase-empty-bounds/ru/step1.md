# Тестовый случай: пустые ограничения

Вследствие того, как работают ограничения, даже если `trait` не содержит никакой функциональности, вы по-прежнему можете использовать его в качестве ограничения. `Eq` и `Copy` - это примеры таких `trait` из стандартной библиотеки `std`.

```rust
struct Cardinal;
struct BlueJay;
struct Turkey;

trait Red {}
trait Blue {}

impl Red for Cardinal {}
impl Blue for BlueJay {}

// Эти функции действительны только для типов, которые реализуют эти
// трейты. Факт того, что трейты пустые, не имеет значения.
fn red<T: Red>(_: &T)   -> &'static str { "red" }
fn blue<T: Blue>(_: &T) -> &'static str { "blue" }

fn main() {
    let cardinal = Cardinal;
    let blue_jay = BlueJay;
    let _turkey   = Turkey;

    // `red()` не будет работать с голубым воробьем, и наоборот
    // из-за ограничений.
    println!("A cardinal is {}", red(&cardinal));
    println!("A blue jay is {}", blue(&blue_jay));
    //println!("A turkey is {}", red(&_turkey));
    // ^ TODO: Попробуйте раскомментировать эту строку.
}
```
