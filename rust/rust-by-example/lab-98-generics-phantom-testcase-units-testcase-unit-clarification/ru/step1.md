# Тестовый случай: уточнение единиц

Полезный метод преобразования единиц можно рассмотреть, реализовав `Add` с параметром типа-призраком. Трейт `Add` рассмотрен ниже:

```rust
// Эта конструкция предполагает: `Self + RHS = Output`
// где RHS по умолчанию равен Self, если не указано в реализации.
pub trait Add<RHS = Self> {
    type Output;

    fn add(self, rhs: RHS) -> Self::Output;
}

// `Output` должен быть `T<U>`, чтобы `T<U> + T<U> = T<U>`.
impl<U> Add for T<U> {
    type Output = T<U>;
  ...
}
```

Полная реализация:

```rust
use std::ops::Add;
use std::marker::PhantomData;

/// Создаем пустые перечисления для определения типов единиц.
#[derive(Debug, Clone, Copy)]
enum Inch {}
#[derive(Debug, Clone, Copy)]
enum Mm {}

/// `Length` - это тип с параметром типа-призраком `Unit`,
/// и не является обобщенным по типу длины (то есть `f64`).
///
/// `f64` уже реализует трейты `Clone` и `Copy`.
#[derive(Debug, Clone, Copy)]
struct Length<Unit>(f64, PhantomData<Unit>);

/// Трейт `Add` определяет поведение оператора `+`.
impl<Unit> Add for Length<Unit> {
    type Output = Length<Unit>;

    // add() возвращает новую структуру `Length`, содержащую сумму.
    fn add(self, rhs: Length<Unit>) -> Length<Unit> {
        // `+` вызывает реализацию `Add` для `f64`.
        Length(self.0 + rhs.0, PhantomData)
    }
}

fn main() {
    // Указываем, что `one_foot` имеет параметр типа-призраком `Inch`.
    let one_foot:  Length<Inch> = Length(12.0, PhantomData);
    // `one_meter` имеет параметр типа-призраком `Mm`.
    let one_meter: Length<Mm>   = Length(1000.0, PhantomData);

    // `+` вызывает метод `add()`, который мы реализовали для `Length<Unit>`.
    //
    // Поскольку `Length` реализует `Copy`, `add()` не потребляет
    // `one_foot` и `one_meter`, а копирует их в `self` и `rhs`.
    let two_feet = one_foot + one_foot;
    let two_meters = one_meter + one_meter;

    // Сложение работает.
    println!("one foot + one_foot = {:?} in", two_feet.0);
    println!("one meter + one_meter = {:?} mm", two_meters.0);

    // Несмысленные операции не проходят, как и должно быть:
    // Ошибка компиляции: несоответствие типов.
    //let one_feter = one_foot + one_meter;
}
```
