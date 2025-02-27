# Трейты

Аннотация сроков жизни в методах трейтов в основном аналогична функциям. Обратите внимание, что `impl` также может иметь аннотацию сроков жизни.

```rust
// Структура с аннотацией срока жизни.
#[derive(Debug)]
struct Borrowed<'a> {
    x: &'a i32,
}

// Аннотируем сроки жизни для impl.
impl<'a> Default for Borrowed<'a> {
    fn default() -> Self {
        Self {
            x: &10,
        }
    }
}

fn main() {
    let b: Borrowed = Default::default();
    println!("b is {:?}", b);
}
```
