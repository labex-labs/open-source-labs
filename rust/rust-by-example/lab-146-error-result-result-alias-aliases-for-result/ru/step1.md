# псевдонимы для `Result`

Что делать, если мы хотим многократно использовать определенный тип `Result`? Помните, что Rust позволяет создавать псевдонимы. К счастью, мы можем определить один для конкретного `Result`.

На уровне модуля создание псевдонимов может быть особенно полезным. Ошибки, обнаруженные в определенном модуле, часто имеют один и тот же тип `Err`, поэтому один псевдоним может кратко определить _все_ связанные `Result`. Это настолько полезно, что стандартная библиотека `std` даже предоставляет один: `io::Result`!

Вот простой пример, демонстрирующий синтаксис:

```rust
use std::num::ParseIntError;

// Определите общий псевдоним для `Result` с типом ошибки `ParseIntError`.
type AliasedResult<T> = Result<T, ParseIntError>;

// Используйте вышеуказанный псевдоним, чтобы сослаться на наш конкретный тип `Result`.
fn multiply(first_number_str: &str, second_number_str: &str) -> AliasedResult<i32> {
    first_number_str.parse::<i32>().and_then(|first_number| {
        second_number_str.parse::<i32>().map(|second_number| first_number * second_number)
    })
}

// Здесь псевдоним снова позволяет нам节省ить некоторое пространство.
fn print(result: AliasedResult<i32>) {
    match result {
        Ok(n)  => println!("n is {}", n),
        Err(e) => println!("Error: {}", e),
    }
}

fn main() {
    print(multiply("10", "2"));
    print(multiply("t", "2"));
}
```
