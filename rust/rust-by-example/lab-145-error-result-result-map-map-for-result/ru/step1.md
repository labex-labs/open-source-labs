# `map` для `Result`

Паника в `multiply` в предыдущем примере не делает код надежным. Как правило, мы хотим вернуть ошибку вызывающему коду, чтобы он мог решить, как правильно реагировать на ошибки.

Сначала нам нужно знать, с каким типом ошибок мы имеем дело. Чтобы определить тип `Err`, мы смотрим на `parse()`, который реализован с помощью трейта `FromStr` для `i32`. В результате тип `Err` задан как `ParseIntError`.

В следующем примере простой оператор `match` приводит к более громоздкому коду в целом.

```rust
use std::num::ParseIntError;

// После переписывания возвращаемого типа мы используем сопоставление с образцом без `unwrap()`.
fn multiply(first_number_str: &str, second_number_str: &str) -> Result<i32, ParseIntError> {
    match first_number_str.parse::<i32>() {
        Ok(first_number)  => {
            match second_number_str.parse::<i32>() {
                Ok(second_number)  => {
                    Ok(first_number * second_number)
                },
                Err(e) => Err(e),
            }
        },
        Err(e) => Err(e),
    }
}

fn print(result: Result<i32, ParseIntError>) {
    match result {
        Ok(n)  => println!("n is {}", n),
        Err(e) => println!("Error: {}", e),
    }
}

fn main() {
    // Это по-прежнему дает разумный ответ.
    let twenty = multiply("10", "2");
    print(twenty);

    // Следующий пример теперь дает гораздо более информативное сообщение об ошибке.
    let tt = multiply("t", "2");
    print(tt);
}
```

К счастью, `map`, `and_then` и многие другие комбинаторы для `Option` также реализованы для `Result`. Полный список доступен в `Result`.

```rust
use std::num::ParseIntError;

// Как и для `Option`, мы можем использовать комбинаторы, такие как `map()`.
// Эта функция идентична предыдущей, но читается так:
// Умножьте, если оба значения могут быть разобраны из str, в противном случае передайте ошибку дальше.
fn multiply(first_number_str: &str, second_number_str: &str) -> Result<i32, ParseIntError> {
    first_number_str.parse::<i32>().and_then(|first_number| {
        second_number_str.parse::<i32>().map(|second_number| first_number * second_number)
    })
}

fn print(result: Result<i32, ParseIntError>) {
    match result {
        Ok(n)  => println!("n is {}", n),
        Err(e) => println!("Error: {}", e),
    }
}

fn main() {
    // Это по-прежнему дает разумный ответ.
    let twenty = multiply("10", "2");
    print(twenty);

    // Следующий пример теперь дает гораздо более информативное сообщение об ошибке.
    let tt = multiply("t", "2");
    print(tt);
}
```
