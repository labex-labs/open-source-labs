# Трейты

`Трейт` - это коллекция методов, определенных для неизвестного типа: `Self`. Они могут обращаться к другим методам, объявленным в том же трейте.

Трейты могут быть реализованы для любого типа данных. В следующем примере мы определяем `Animal`, группу методов. Затем трейт `Animal` реализуется для типа данных `Sheep`, что позволяет использовать методы из `Animal` с экземпляром `Sheep`.

```rust
struct Sheep { naked: bool, name: &'static str }

trait Animal {
    // Сигнатура ассоциированной функции; `Self` ссылается на тип, реализующий трейт.
    fn new(name: &'static str) -> Self;

    // Сигнатуры методов; они будут возвращать строку.
    fn name(&self) -> &'static str;
    fn noise(&self) -> &'static str;

    // Трейты могут предоставлять определения по умолчанию для методов.
    fn talk(&self) {
        println!("{} says {}", self.name(), self.noise());
    }
}

impl Sheep {
    fn is_naked(&self) -> bool {
        self.naked
    }

    fn shear(&mut self) {
        if self.is_naked() {
            // Методы, реализующие трейт, могут использовать методы трейта для реализующего типа.
            println!("{} is already naked...", self.name());
        } else {
            println!("{} gets a haircut!", self.name);

            self.naked = true;
        }
    }
}

// Реализуем трейт `Animal` для `Sheep`.
impl Animal for Sheep {
    // `Self` - это тип, реализующий трейт: `Sheep`.
    fn new(name: &'static str) -> Sheep {
        Sheep { name: name, naked: false }
    }

    fn name(&self) -> &'static str {
        self.name
    }

    fn noise(&self) -> &'static str {
        if self.is_naked() {
            "baaaaah?"
        } else {
            "baaaaah!"
        }
    }

    // Определения методов по умолчанию трейта можно переопределить.
    fn talk(&self) {
        // Например, мы можем добавить некоторое замолчание для размышления.
        println!("{} pauses briefly... {}", self.name, self.noise());
    }
}

fn main() {
    // В этом случае необходим тип-аннотация.
    let mut dolly: Sheep = Animal::new("Dolly");
    // TODO ^ Попробуйте удалить тип-аннотации.

    dolly.talk();
    dolly.shear();
    dolly.talk();
}
```
