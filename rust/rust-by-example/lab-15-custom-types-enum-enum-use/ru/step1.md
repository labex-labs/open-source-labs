# use

Объявление `use` можно использовать, чтобы не было необходимости вручную определять области видимости:

```rust
// Аттрибут для скрытия предупреждений о неиспользуемом коде.
#![allow(dead_code)]

enum Status {
    Rich,
    Poor,
}

enum Work {
    Civilian,
    Soldier,
}

fn main() {
    // Явно `use` каждый из имен, чтобы они были доступны без
    // ручной области видимости.
    use crate::Status::{Poor, Rich};
    // Автоматически `use` каждый из имен внутри `Work`.
    use crate::Work::*;

    // Эквивалентно `Status::Poor`.
    let status = Poor;
    // Эквивалентно `Work::Civilian`.
    let work = Civilian;

    match status {
        // Обратите внимание на отсутствие области видимости из-за явного `use` выше.
        Rich => println!("Богатые имеют много денег!"),
        Poor => println!("Бедные не имеют денег..."),
    }

    match work {
        // Обратите внимание еще раз на отсутствие области видимости.
        Civilian => println!("Граждане работают!"),
        Soldier  => println!("Солдаты боятся!"),
    }
}
```
