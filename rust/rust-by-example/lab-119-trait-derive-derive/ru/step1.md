# Derive

Компилятор способен предоставлять базовые реализации для некоторых трейтов с помощью атрибута `#[derive]`. Эти трейты по-прежнему можно реализовать вручную, если требуется более сложная поведенческая логика.

Ниже приведен список производимых трейтов:

- Трейты сравнения: `Eq`, `PartialEq`, `Ord`, `PartialOrd`.
- `Clone`, чтобы создавать `T` из `&T` путем копирования.
- `Copy`, чтобы дать типу "семантику копирования" вместо "семантики перемещения".
- `Hash`, чтобы вычислить хэш из `&T`.
- `Default`, чтобы создать пустой экземпляр данных типа.
- `Debug`, чтобы форматировать значение с использованием форматтера `{:?}`.

```rust
// `Centimeters`, кортежная структура, которая может быть сравнена
#[derive(PartialEq, PartialOrd)]
struct Centimeters(f64);

// `Inches`, кортежная структура, которая может быть напечатана
#[derive(Debug)]
struct Inches(i32);

impl Inches {
    fn to_centimeters(&self) -> Centimeters {
        let &Inches(inches) = self;

        Centimeters(inches as f64 * 2.54)
    }
}

// `Seconds`, кортежная структура без дополнительных атрибутов
struct Seconds(i32);

fn main() {
    let _one_second = Seconds(1);

    // Ошибка: `Seconds` не может быть напечатана; она не реализует трейт `Debug`
    //println!("One second looks like: {:?}", _one_second);
    // TODO ^ Попробуйте раскомментировать эту строку

    // Ошибка: `Seconds` не может быть сравнена; она не реализует трейт `PartialEq`
    //let _this_is_true = (_one_second == _one_second);
    // TODO ^ Попробуйте раскомментировать эту строку

    let foot = Inches(12);

    println!("One foot equals {:?}", foot);

    let meter = Centimeters(100.0);

    let cmp =
        if foot.to_centimeters() < meter {
            "smaller"
        } else {
            "bigger"
        };

    println!("One foot is {} than one meter.", cmp);
}
```
