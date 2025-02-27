# `Option`

Иногда желательно поймать неудачу некоторых частей программы вместо вызова `panic!`; это можно сделать с использованием перечисления `Option`.

Перечисление `Option<T>` имеет два варианта:

- `None`, чтобы указать на неудачу или отсутствие значения, и
- `Some(value)`, структура-тупл, которая оборачивает `value` с типом `T`.

```rust
// Целочисленное деление, которое не вызывает `panic!`
fn checked_division(dividend: i32, divisor: i32) -> Option<i32> {
    if divisor == 0 {
        // Неудача представляется в виде варианта `None`
        None
    } else {
        // Результат оборачивается в вариант `Some`
        Some(dividend / divisor)
    }
}

// Эта функция обрабатывает деление, которое может не пройти успешно
fn try_division(dividend: i32, divisor: i32) {
    // Значения `Option` можно сопоставить по шаблону, как и другие перечисления
    match checked_division(dividend, divisor) {
        None => println!("{} / {} неудачно!", dividend, divisor),
        Some(quotient) => {
            println!("{} / {} = {}", dividend, divisor, quotient)
        },
    }
}

fn main() {
    try_division(4, 2);
    try_division(1, 0);

    // Привязывание `None` к переменной требует указания типа
    let none: Option<i32> = None;
    let _equivalent_none = None::<i32>;

    let optional_float = Some(0f32);

    // Раскрытие варианта `Some` извлечет обернутое значение.
    println!("{:?} раскрывается в {:?}", optional_float, optional_float.unwrap());

    // Раскрытие варианта `None` вызовет `panic!`
    println!("{:?} раскрывается в {:?}", none, none.unwrap());
}
```
