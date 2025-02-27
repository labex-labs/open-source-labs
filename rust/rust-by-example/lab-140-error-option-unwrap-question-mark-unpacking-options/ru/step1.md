# Распаковка вариантов с помощью `?`

Вы можете распаковывать варианты `Option` с использованием инструкций `match`, но часто проще использовать оператор `?`. Если `x` имеет тип `Option`, то вычисление `x?` вернет внутреннее значение, если `x` равно `Some`, в противном случае оно завершит выполнение любой функции, в которой оно используется, и вернет `None`.

```rust
fn next_birthday(current_age: Option<u8>) -> Option<String> {
    // Если `current_age` равно `None`, то возвращается `None`.
    // Если `current_age` равно `Some`, то внутреннее значение типа `u8` присваивается переменной `next_age`
    let next_age: u8 = current_age? + 1;
    Some(format!("Next year I will be {}", next_age))
}
```

Вы можете связать несколько операторов `?` вместе, чтобы сделать ваш код гораздо более читаемым.

```rust
struct Person {
    job: Option<Job>,
}

#[derive(Clone, Copy)]
struct Job {
    phone_number: Option<PhoneNumber>,
}

#[derive(Clone, Copy)]
struct PhoneNumber {
    area_code: Option<u8>,
    number: u32,
}

impl Person {

    // Возвращает код города телефонного номера места работы человека, если он существует.
    fn work_phone_area_code(&self) -> Option<u8> {
        // Без оператора `?` для этого пришлось бы использовать много вложенных инструкций `match`.
        // Это потребовало бы гораздо больше кода - попробуйте написать его сами и сравните, какой вариант легче.
        self.job?.phone_number?.area_code
    }
}

fn main() {
    let p = Person {
        job: Some(Job {
            phone_number: Some(PhoneNumber {
                area_code: Some(61),
                number: 439222222,
            }),
        }),
    };

    assert_eq!(p.work_phone_area_code(), Some(61));
}
```
