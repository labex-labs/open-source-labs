# Оборачивание ошибок

Вместо boxing ошибок можно обернуть их в собственный тип ошибок.

```rust
use std::error;
use std::error::Error;
use std::num::ParseIntError;
use std::fmt;

type Result<T> = std::result::Result<T, DoubleError>;

#[derive(Debug)]
enum DoubleError {
    EmptyVec,
    // Мы передадим обработку ошибки в реализацию ошибки разбора.
    // Предоставление дополнительной информации требует добавления
    // дополнительных данных в тип.
    Parse(ParseIntError),
}

impl fmt::Display for DoubleError {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        match *self {
            DoubleError::EmptyVec =>
                write!(f, "пожалуйста, используйте вектор с хотя бы одним элементом"),
            // Обернутая ошибка содержит дополнительную информацию и доступна
            // через метод source().
            DoubleError::Parse(..) =>
                write!(f, "предоставленная строка не может быть распознана как целое число"),
        }
    }
}

impl error::Error for DoubleError {
    fn source(&self) -> Option<&(dyn error::Error + 'static)> {
        match *self {
            DoubleError::EmptyVec => None,
            // Причина - это тип ошибки нижележащей реализации. Неявно
            // приводится к объекту трейта `&error::Error`. Это работает,
            // потому что нижележащий тип уже реализует трейт `Error`.
            DoubleError::Parse(ref e) => Some(e),
        }
    }
}

// Реализуем преобразование из `ParseIntError` в `DoubleError`.
// Это будет автоматически вызвано `?`, если `ParseIntError`
// нужно преобразовать в `DoubleError`.
impl From<ParseIntError> for DoubleError {
    fn from(err: ParseIntError) -> DoubleError {
        DoubleError::Parse(err)
    }
}

fn double_first(vec: Vec<&str>) -> Result<i32> {
    let first = vec.first().ok_or(DoubleError::EmptyVec)?;
    // Здесь мы неявно используем реализацию `From` для `ParseIntError` (которую
    // мы определили выше), чтобы создать `DoubleError`.
    let parsed = first.parse::<i32>()?;

    Ok(2 * parsed)
}

fn print(result: Result<i32>) {
    match result {
        Ok(n)  => println!("Первое число, умноженное на два, равно {}", n),
        Err(e) => {
            println!("Ошибка: {}", e);
            if let Some(source) = e.source() {
                println!("  Причина: {}", source);
            }
        },
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

Это добавляет немного больше boilerplate для обработки ошибок и может не потребоваться в всех приложениях. Существуют некоторые библиотеки, которые могут позаботиться о boilerplate за вас.
