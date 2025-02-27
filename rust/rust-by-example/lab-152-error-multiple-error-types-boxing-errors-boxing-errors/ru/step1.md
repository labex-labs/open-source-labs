# Boxing ошибок

Одним из способов написания простого кода с сохранением исходных ошибок является их "упаковка" в `Box`. Недостаток заключается в том, что тип исходной ошибки известен только во время выполнения и не определяется статически.

Библиотека стандартной библиотеки помогает упаковывать наши ошибки, реализовав для `Box` преобразование из любого типа, реализующего трейт `Error`, в объект трейта `Box<Error>` с помощью `From`.

```rust
use std::error;
use std::fmt;

// Измените псевдоним на `Box<error::Error>`.
type Result<T> = std::result::Result<T, Box<dyn error::Error>>;

#[derive(Debug, Clone)]
struct EmptyVec;

impl fmt::Display for EmptyVec {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "invalid first item to double")
    }
}

impl error::Error for EmptyVec {}

fn double_first(vec: Vec<&str>) -> Result<i32> {
    vec.first()
     .ok_or_else(|| EmptyVec.into()) // Преобразует в Box
     .and_then(|s| {
            s.parse::<i32>()
             .map_err(|e| e.into()) // Преобразует в Box
             .map(|i| 2 * i)
        })
}

fn print(result: Result<i32>) {
    match result {
        Ok(n) => println!("The first doubled is {}", n),
        Err(e) => println!("Error: {}", e),
    }
}

fn main() {
    let numbers = vec!["42", "93", "18"];
    let empty = vec![];
    let strings = vec!["tofu", "93", "18"];

    print(double_first(numbers));
    print(double_first(empty));
    print(double_first(strings));
}
```
