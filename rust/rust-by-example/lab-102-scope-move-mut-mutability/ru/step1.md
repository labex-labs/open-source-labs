# Изменяемость

Изменяемость данных может изменяться при передаче владения.

```rust
fn main() {
    let immutable_box = Box::new(5u32);

    println!("immutable_box содержит {}", immutable_box);

    // Ошибка изменения
    //*immutable_box = 4;

    // *Перемещаем* коробку, меняя владение (и изменяемость)
    let mut mutable_box = immutable_box;

    println!("mutable_box содержит {}", mutable_box);

    // Изменяем содержимое коробки
    *mutable_box = 4;

    println!("mutable_box теперь содержит {}", mutable_box);
}
```
