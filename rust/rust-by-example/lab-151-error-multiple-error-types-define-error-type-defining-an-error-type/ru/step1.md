# Определение типа ошибок

Иногда упрощает код скрыть все разные ошибки одним типом ошибок. Мы покажем это на примере пользовательской ошибки.

Rust позволяет определять собственные типы ошибок. В общем, "хороший" тип ошибок:

- Представляет разные ошибки одним типом
- Предоставляет удобные сообщения об ошибках для пользователя
- Легко сравнивается с другими типами
  - Хорошо: `Err(EmptyVec)`
  - Плохо: `Err("Please use a vector with at least one element".to_owned())`
- Может хранить информацию об ошибке
  - Хорошо: `Err(BadChar(c, position))`
  - Плохо: `Err("+ cannot be used here".to_owned())`
- Хорошо сочетается с другими ошибками

```rust
use std::fmt;

type Result<T> = std::result::Result<T, DoubleError>;

// Определяем наши типы ошибок. Они могут быть настроены для наших случаев обработки ошибок.
// Теперь мы сможем писать собственные ошибки, отдавать управление ошибке нижележащему
// реализации или что-то между ними.
#[derive(Debug, Clone)]
struct DoubleError;

// Генерация ошибки полностью отделена от того, как она отображается.
// Не нужно беспокоиться, что сложная логика будет мешаться стилем отображения.
//
// Обратите внимание, что мы не храним никакой дополнительной информации о ошибках.
// Это означает, что мы не можем указать, какая строка не прошла разбор, не изменив наши типы,
// чтобы они хранили эту информацию.
impl fmt::Display for DoubleError {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "invalid first item to double")
    }
}

fn double_first(vec: Vec<&str>) -> Result<i32> {
    vec.first()
        // Меняем ошибку на наш новый тип.
     .ok_or(DoubleError)
     .and_then(|s| {
            s.parse::<i32>()
                // Также обновляем на новый тип ошибки здесь.
             .map_err(|_| DoubleError)
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
