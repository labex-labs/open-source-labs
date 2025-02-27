# Другие用途 оператора `?`

Заметим, что в предыдущем примере наше первое действие при вызове `parse` - это `map` ошибку из ошибки библиотеки в заboxed ошибку:

```rust
.and_then(|s| s.parse::<i32>())
 .map_err(|e| e.into())
```

Поскольку это простая и распространенная операция, было бы удобно, если бы ее можно было опустить. К сожалению, поскольку `and_then` недостаточно гибкий, это невозможно. Однако, мы можем вместо этого использовать `?`.

`?` ранее объяснялось как `unwrap` или `return Err(err)`. Это лишь в основном верно. На самом деле это означает `unwrap` или `return Err(From::from(err))`. Поскольку `From::from` - это утилита преобразования между разными типами, это означает, что если вы используете `?`, где ошибка может быть преобразована в тип возврата, она будет автоматически преобразована.

Здесь мы переписываем предыдущий пример с использованием `?`. В результате `map_err` исчезнет, когда для нашего типа ошибки будет реализован `From::from`:

```rust
use std::error;
use std::fmt;

// Изменим псевдоним на `Box<dyn error::Error>`.
type Result<T> = std::result::Result<T, Box<dyn error::Error>>;

#[derive(Debug)]
struct EmptyVec;

impl fmt::Display for EmptyVec {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "invalid first item to double")
    }
}

impl error::Error for EmptyVec {}

// Та же структура, что и раньше, но вместо того, чтобы цеплять все `Result`
// и `Option` последовательно, мы используем `?`, чтобы сразу получить внутреннее значение.
fn double_first(vec: Vec<&str>) -> Result<i32> {
    let first = vec.first().ok_or(EmptyVec)?;
    let parsed = first.parse::<i32>()?;
    Ok(2 * parsed)
}

fn print(result: Result<i32>) {
    match result {
        Ok(n)  => println!("The first doubled is {}", n),
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

Теперь это на самом деле довольно чисто. Сравнивая с исходным `panic`, это очень похоже на замену вызовов `unwrap` на `?`, за исключением того, что типы возврата - это `Result`. В результате они должны быть деструктурированы на верхнем уровне.
